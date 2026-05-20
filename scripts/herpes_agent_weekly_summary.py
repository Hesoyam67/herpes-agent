#!/usr/bin/env python3
"""Weekly mutation summary generator for Herpes Agent.

Free-first, Markdown-native, and allergic to SaaS wallet leeches. It uses local
Git plus the GitHub CLI when available, then turns the week's mutations into a
human-readable report for maintainers, cron jobs, and mildly cursed launch logs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
from typing import Any

REPO = "Hesoyam67/herpes-agent"
ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_DAYS = 7


def run(cmd: list[str], *, cwd: pathlib.Path = ROOT, timeout: int = 60) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        return proc.returncode, proc.stdout.strip()
    except FileNotFoundError:
        return 127, f"missing command: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return 124, f"timeout after {timeout}s: {' '.join(cmd)}"


def gh_json(args: list[str]) -> Any | None:
    code, out = run(["gh", *args], timeout=90)
    if code != 0:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def iso_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()


def since_date(days: int) -> str:
    return (dt.datetime.now(dt.UTC) - dt.timedelta(days=days)).strftime("%Y-%m-%d")


def mutation_range() -> str:
    # Prefer fork-only changes so upstream's entire ancient fossil bed doesn't
    # get counted as our weekly rash. If upstream is missing, fall back to HEAD.
    code, _ = run(["git", "rev-parse", "--verify", "upstream/main"])
    if code == 0:
        return "upstream/main..HEAD"
    return "HEAD"


def git_commits(days: int) -> list[str]:
    code, out = run([
        "git",
        "log",
        mutation_range(),
        f"--since={days} days ago",
        "--pretty=format:%h%x09%ad%x09%s",
        "--date=short",
    ])
    if code != 0 or not out:
        return []
    return out.splitlines()


def git_changed_files(days: int) -> list[str]:
    code, out = run([
        "git",
        "log",
        mutation_range(),
        f"--since={days} days ago",
        "--name-only",
        "--pretty=format:",
    ])
    if code != 0 or not out:
        return []
    return sorted(set(line.strip() for line in out.splitlines() if line.strip()))


def repo_metrics() -> dict[str, Any]:
    data = gh_json([
        "repo",
        "view",
        REPO,
        "--json",
        "url,stargazerCount,forkCount,watchers,issues,pullRequests,repositoryTopics,updatedAt",
    ])
    if not data:
        return {"url": f"https://github.com/{REPO}", "error": "gh repo view failed; report continues in local-only goblin mode"}
    return {
        "url": data.get("url"),
        "stars": data.get("stargazerCount", 0),
        "forks": data.get("forkCount", 0),
        "watchers": data.get("watchers", {}).get("totalCount", 0),
        "open_issues": data.get("issues", {}).get("totalCount", 0),
        "open_prs": data.get("pullRequests", {}).get("totalCount", 0),
        "topics": [t.get("name") for t in data.get("repositoryTopics", [])],
        "updated_at": data.get("updatedAt"),
    }


def issues(state: str = "all", limit: int = 50) -> list[dict[str, Any]]:
    data = gh_json([
        "issue",
        "list",
        "--repo",
        REPO,
        "--state",
        state,
        "--limit",
        str(limit),
        "--json",
        "number,title,state,labels,updatedAt,closedAt,url",
    ])
    return data or []


def roadmap_counts() -> tuple[int, int]:
    path = ROOT / "plans/herpes-agent/ROADMAP.md"
    if not path.exists():
        return 0, 0
    text = path.read_text(encoding="utf-8")
    done = len(re.findall(r"- \[x\]", text))
    total = len(re.findall(r"- \[[ x]\]", text))
    return done, total


def content_inventory() -> list[str]:
    path = ROOT / "content/herpes-agent/CONTENT_QUEUE.md"
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    interesting: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not (stripped.startswith("- ") or re.match(r"\d+\. ", stripped)):
            continue
        normalized = re.sub(r"^(?:- |\d+\. )", "", stripped)
        if normalized:
            interesting.append(normalized)
    return interesting[:12]


def recommendation(open_issues: list[dict[str, Any]], done: int, total: int) -> str:
    titles = [i.get("title", "").lower() for i in open_issues]
    if any("weekly mutation" in title for title in titles):
        return "Finish and close the weekly mutation generator. The report gremlin is already chewing on the wires."
    if total and done / total < 0.75:
        return "Burn down one roadmap checkbox with a tiny artifact. Small mutations beat grand speeches."
    if not open_issues:
        return "Open one sharply-scoped issue from the roadmap so the autonomy loop has a fresh infection vector."
    return f"Pick the oldest open issue: #{open_issues[-1].get('number')} {open_issues[-1].get('title')}."


def render(days: int) -> str:
    metrics = repo_metrics()
    all_issues = issues("all")
    open_issues = [i for i in all_issues if i.get("state") == "OPEN"]
    closed_issues = [i for i in all_issues if i.get("state") == "CLOSED"]
    commits = git_commits(days)
    changed = git_changed_files(days)
    done, total = roadmap_counts()
    content = content_inventory()

    lines: list[str] = []
    lines.append(f"# Herpes Agent Weekly Mutation Summary — {iso_now()}")
    lines.append("")
    lines.append(f"Window: last {days} days, since {since_date(days)}. Budget: still basically zero. Viral load: strategically annoying.")
    lines.append("")

    lines.append("## Repo vitals")
    lines.append(f"- Repo: {metrics.get('url', f'https://github.com/{REPO}')}")
    if metrics.get("error"):
        lines.append(f"- Warning: {metrics['error']}")
    else:
        lines.append(f"- Stars: {metrics.get('stars', 0)}")
        lines.append(f"- Forks: {metrics.get('forks', 0)}")
        lines.append(f"- Watchers: {metrics.get('watchers', 0)}")
        lines.append(f"- Open issues: {metrics.get('open_issues', 0)}")
        lines.append(f"- Open PRs: {metrics.get('open_prs', 0)}")
        lines.append(f"- Topics: {', '.join(metrics.get('topics') or [])}")
    lines.append("")

    lines.append("## Mutations shipped")
    if commits:
        for commit in commits:
            sha, date, subject = (commit.split("\t", 2) + ["", ""])[:3]
            lines.append(f"- `{sha}` {date} — {subject}")
    else:
        lines.append("- No commits in this window. The rash is dormant; poke it with a roadmap stick.")
    lines.append("")

    lines.append("## Files touched")
    if changed:
        for rel in changed[:30]:
            lines.append(f"- `{rel}`")
        if len(changed) > 30:
            lines.append(f"- ...and {len(changed) - 30} more files. The mutation plume got chunky.")
    else:
        lines.append("- No changed files detected for this window.")
    lines.append("")

    lines.append("## Issue metabolism")
    if open_issues:
        lines.append("Open:")
        for issue in open_issues[:20]:
            labels = ", ".join(label.get("name", "") for label in issue.get("labels", []))
            lines.append(f"- #{issue.get('number')} {issue.get('title')} [{labels}] — {issue.get('url')}")
    else:
        lines.append("Open: none. Suspiciously clean. Probably a trap.")
    if closed_issues:
        lines.append("Closed recently / visible in tracker:")
        for issue in closed_issues[:20]:
            lines.append(f"- #{issue.get('number')} {issue.get('title')} — closed {issue.get('closedAt') or 'unknown'}")
    lines.append("")

    lines.append("## Roadmap digestion")
    if total:
        lines.append(f"- Completed roadmap checkboxes: {done}/{total}")
        lines.append(f"- Remaining checkboxes: {total - done}")
    else:
        lines.append("- Roadmap counts unavailable. Somebody stole the clipboard.")
    lines.append("")

    lines.append("## Content spores")
    if content:
        for item in content:
            lines.append(f"- {item}")
    else:
        lines.append("- No content queue items found. Draft a meme before the beige wins.")
    lines.append("")

    lines.append("## Recommended next infection vector")
    lines.append(f"- {recommendation(open_issues, done, total)}")
    lines.append("")

    lines.append("## Safety / budget antibodies")
    lines.append("- Public posting still requires approval. Drafts can multiply locally like cursed sourdough.")
    lines.append("- Paid services used: 0. If a wallet opened, it was not because of this script.")
    lines.append("- Upstream credit remains mandatory. We parody; we do not plagiarize.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit a Herpes Agent weekly mutation summary in Markdown.")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS, help="Lookback window in days. Default: 7.")
    parser.add_argument("--out", type=pathlib.Path, help="Optional file path to write the report.")
    args = parser.parse_args()
    if args.days < 1:
        raise SystemExit("--days must be >= 1; even chaos needs a calendar.")
    report = render(args.days)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
    print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
