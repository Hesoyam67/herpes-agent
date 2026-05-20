#!/usr/bin/env python3
"""Free-first daily growth scan for Herpes Agent.

No paid APIs. Uses `gh` when available and falls back gracefully when the
internet goblin is asleep. Emits Markdown so cron, humans, and gremlins can all
read it.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import subprocess
import sys
from typing import Any

REPO = "Hesoyam67/herpes-agent"
UPSTREAM = "NousResearch/hermes-agent"
ROOT = pathlib.Path(__file__).resolve().parents[1]


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
    code, out = run(["gh", *args])
    if code != 0:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def repo_metrics() -> dict[str, Any]:
    data = gh_json([
        "repo",
        "view",
        REPO,
        "--json",
        "nameWithOwner,url,stargazerCount,forkCount,watchers,issues,repositoryTopics,updatedAt",
    ])
    if not data:
        return {"repo": REPO, "error": "gh repo view failed; network goblin probably sneezed"}
    return {
        "repo": data.get("nameWithOwner"),
        "url": data.get("url"),
        "stars": data.get("stargazerCount", 0),
        "forks": data.get("forkCount", 0),
        "watchers": data.get("watchers", {}).get("totalCount", 0),
        "open_issues": data.get("issues", {}).get("totalCount", 0),
        "topics": [t.get("name") for t in data.get("repositoryTopics", [])],
        "updated_at": data.get("updatedAt"),
    }


def open_issues() -> list[dict[str, Any]]:
    data = gh_json([
        "issue",
        "list",
        "--repo",
        REPO,
        "--limit",
        "20",
        "--json",
        "number,title,labels,updatedAt,url",
    ])
    return data or []


def git_state() -> dict[str, str]:
    checks = {
        "branch": ["git", "branch", "--show-current"],
        "status": ["git", "status", "--short", "--branch"],
        "last_commit": ["git", "log", "-1", "--oneline"],
    }
    out: dict[str, str] = {}
    for key, cmd in checks.items():
        _, text = run(cmd)
        out[key] = text
    # Fetch is allowed to fail quietly; scan should not faceplant over Wi-Fi drama.
    run(["git", "fetch", "origin", "main", "--quiet"], timeout=90)
    run(["git", "fetch", "upstream", "main", "--quiet"], timeout=90)
    _, ahead = run(["git", "rev-list", "--left-right", "--count", "origin/main...upstream/main"])
    out["upstream_delta"] = ahead or "unknown"
    return out


def pick_next(issues: list[dict[str, Any]]) -> str:
    titles = {i.get("title", "") for i in issues}
    if any("demo capture" in t.lower() for t in titles):
        return "Issue #1: create a tiny terminal demo/capture for the `herpes-agent` skin. The rash needs screenshots, not vibes."
    if any("daily autonomous growth scan" in t.lower() for t in titles):
        return "Finish wiring this scan into docs/cron instructions, then close the issue before it starts charging rent."
    return "Open one small mutation issue or draft one content item. If nothing hurts, poke the roadmap until it does."


def render() -> str:
    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()
    metrics = repo_metrics()
    issues = open_issues()
    git = git_state()
    lines: list[str] = []
    lines.append(f"# Herpes Agent Daily Growth Scan — {now}")
    lines.append("")
    lines.append("Chaotic but strategic. Free-first. No SaaS wallet leeches detected unless explicitly summoned.")
    lines.append("")
    lines.append("## Repo vitals")
    lines.append(f"- Repo: {metrics.get('url', REPO)}")
    if "error" in metrics:
        lines.append(f"- Warning: {metrics['error']}")
    else:
        lines.append(f"- Stars: {metrics.get('stars', 0)}")
        lines.append(f"- Forks: {metrics.get('forks', 0)}")
        lines.append(f"- Watchers: {metrics.get('watchers', 0)}")
        lines.append(f"- Open issues: {metrics.get('open_issues', 0)}")
        lines.append(f"- Topics: {', '.join(metrics.get('topics') or [])}")
    lines.append("")
    lines.append("## Local git")
    lines.append("```text")
    lines.append(git.get("status", "unknown"))
    lines.append(f"last: {git.get('last_commit', 'unknown')}")
    lines.append(f"origin/main vs upstream/main commits (left/right): {git.get('upstream_delta', 'unknown')}")
    lines.append("```")
    lines.append("")
    lines.append("## Open mutations")
    if not issues:
        lines.append("- No open issues. Either we won or the issue tracker fell into a lake.")
    else:
        for issue in issues:
            labels = ", ".join(label.get("name", "") for label in issue.get("labels", []))
            lines.append(f"- #{issue.get('number')} {issue.get('title')} [{labels}] — {issue.get('url')}")
    lines.append("")
    lines.append("## Recommended next infection vector")
    lines.append(f"- {pick_next(issues)}")
    lines.append("")
    lines.append("## Cost check")
    lines.append("- Dollars burned by this scan: 0.00, unless your electricity bill is sentient.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit a Herpes Agent daily growth scan in Markdown.")
    parser.add_argument("--out", type=pathlib.Path, help="Optional file path to write the report.")
    args = parser.parse_args()
    report = render()
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
    print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
