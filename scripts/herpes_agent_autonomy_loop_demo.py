#!/usr/bin/env python3
"""Harmless local autonomy-loop demo for Herpes Agent.

This is not an agent runner and it does not touch networks, secrets, wallets, or
public timelines. It demonstrates the operating rhythm: inspect local project
state, pick one safe internal mutation, explain why, write a Markdown artifact,
and leave verification breadcrumbs.
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import subprocess
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "docs/herpes-agent/autonomy-loop-demo.md"


@dataclass(frozen=True)
class Candidate:
    name: str
    path: pathlib.Path
    reason: str
    safe_action: str


def run(cmd: list[str], *, timeout: int = 30) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(ROOT),
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


def checked(path: pathlib.Path, needle: str) -> bool:
    if not path.exists():
        return False
    return needle in path.read_text(encoding="utf-8")


def candidates() -> list[Candidate]:
    return [
        Candidate(
            name="contagion protocol docs",
            path=ROOT / "docs/herpes-agent/contagion-protocol.md",
            reason="The project has autonomy scripts, but the antibody manual should be obvious before chaos scales.",
            safe_action="Draft local-only operating rules; do not post externally.",
        ),
        Candidate(
            name="README demo link",
            path=ROOT / "README.md",
            reason="Top-level docs should point humans at reproducible demos before they assume this is just a rash-shaped joke.",
            safe_action="Add or verify links to generated demo artifacts.",
        ),
        Candidate(
            name="content queue refresh",
            path=ROOT / "content/herpes-agent/CONTENT_QUEUE.md",
            reason="Fresh drafts create growth options without spamming the timeline goblins.",
            safe_action="Append drafts locally; require approval before posting.",
        ),
    ]


def pick_candidate() -> Candidate:
    for candidate in candidates():
        if not candidate.path.exists():
            return candidate
    readme = ROOT / "README.md"
    if not checked(readme, "autonomy-loop-demo.md"):
        return candidates()[1]
    return candidates()[2]


def git_status() -> str:
    _, out = run(["git", "status", "--short", "--branch"])
    return out or "unknown"


def open_issues() -> str:
    code, out = run([
        "gh",
        "issue",
        "list",
        "--repo",
        "Hesoyam67/herpes-agent",
        "--limit",
        "10",
        "--json",
        "number,title,state",
        "--jq",
        '.[] | "#\\(.number) \\(.state) \\(.title)"',
    ])
    if code != 0:
        return "gh issue list unavailable; local demo keeps waddling."
    return out or "No open issues. Suspiciously peaceful."


def render() -> str:
    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()
    chosen = pick_candidate()
    lines: list[str] = []
    lines.append(f"# Herpes Agent harmless autonomy loop demo — {now}")
    lines.append("")
    lines.append("This demo shows the Herpes Agent operating loop without touching public channels, secrets, paid APIs, destructive commands, or anything that would make legal wake up and hiss.")
    lines.append("")
    lines.append("## Loop")
    lines.append("")
    lines.append("1. Inspect local repo state.")
    lines.append("2. Review open project mutations.")
    lines.append("3. Pick one safe internal improvement.")
    lines.append("4. Write a Markdown artifact humans can inspect.")
    lines.append("5. Verify before bragging, because unverified bragging is how software gets scabies.")
    lines.append("")
    lines.append("## Local repo state")
    lines.append("")
    lines.append("```text")
    lines.append(git_status())
    lines.append("```")
    lines.append("")
    lines.append("## Open mutations")
    lines.append("")
    lines.append("```text")
    lines.append(open_issues())
    lines.append("```")
    lines.append("")
    lines.append("## Picked safe action")
    lines.append("")
    lines.append(f"- Mutation: {chosen.name}")
    lines.append(f"- Target: `{chosen.path.relative_to(ROOT)}`")
    lines.append(f"- Why: {chosen.reason}")
    lines.append(f"- Safe action: {chosen.safe_action}")
    lines.append("")
    lines.append("## Safety gates")
    lines.append("")
    lines.append("- Network writes: none from this demo except optional `gh issue list` read-only metadata.")
    lines.append("- Paid services: none. Wallet remains unlicked.")
    lines.append("- Secrets: not read, not printed, not invited to the party.")
    lines.append("- Public posting: no. Drafts stay local until Papu approves the infection vector.")
    lines.append("- Destructive commands: no. We mutate docs, not kneecaps.")
    lines.append("")
    lines.append("## Human next step")
    lines.append("")
    lines.append("Let the agent execute the picked safe action if it is still useful, then verify with syntax/docs checks and commit the artifact. Tiny loop, tiny blast radius, maximum gremlin velocity.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a harmless Herpes Agent autonomy-loop demo artifact.")
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT, help="Markdown output path.")
    args = parser.parse_args()
    report = render()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
