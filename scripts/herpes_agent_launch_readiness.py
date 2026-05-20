#!/usr/bin/env python3
"""Validate the Herpes Agent local launch approval pack.

No network, no posting, no paid dependencies. This is the tiny immune-system
script that makes sure launch docs still point at real files and keep the
approval gates visible before anyone lets the rash near a public account.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]

PACK = Path("content/herpes-agent/LAUNCH_APPROVAL_PACK.md")
README = Path("README.md")
README_HERPES = Path("README_HERPES_AGENT.md")
MANIFEST = Path("assets/herpes-agent/herpes-agent-grok-imagine-manifest.json")

REQUIRED_PACK_PHRASES = [
    "Do not post",
    "Approval Checklist",
    "@Heso_67",
    "NousResearch/hermes-agent",
    "https://github.com/Hesoyam67/herpes-agent",
    "No checked boxes, no public rash",
]

REQUIRED_README_LINKS = [
    "content/herpes-agent/LAUNCH_APPROVAL_PACK.md",
    "docs/herpes-agent/brain-workflow.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read_text(path: Path) -> str:
    full = REPO_ROOT / path
    if not full.exists():
        fail(f"missing required file: {path}")
    return full.read_text(encoding="utf-8")


def local_markdown_links(markdown: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", markdown)


def check_local_links(path: Path) -> list[str]:
    text = read_text(path)
    missing: list[str] = []
    for target in local_markdown_links(text):
        if "://" in target or target.startswith("#") or target.startswith("mailto:"):
            continue
        clean = unquote(target.split("#", 1)[0])
        if not clean:
            continue
        resolved = (REPO_ROOT / path.parent / clean).resolve()
        try:
            resolved.relative_to(REPO_ROOT.resolve())
        except ValueError:
            missing.append(f"{path}: link escapes repo: {target}")
            continue
        if not resolved.exists():
            missing.append(f"{path}: missing link target {target} -> {resolved}")
    return missing


def check_manifest() -> None:
    full = REPO_ROOT / MANIFEST
    if not full.exists():
        fail(f"missing asset manifest: {MANIFEST}")
    data = json.loads(full.read_text(encoding="utf-8"))
    candidates = data.get("public_launch_candidates") or []
    if len(candidates) < 2:
        fail("asset manifest needs at least avatar/header public_launch_candidates")
    for item in candidates:
        rel = item.get("path")
        if not rel:
            fail("asset candidate missing path")
        asset = REPO_ROOT / rel
        if not asset.exists() or asset.stat().st_size == 0:
            fail(f"asset candidate missing or empty: {rel}")
        note = item.get("review_note", "")
        if "no gore" not in note.lower() or "malware" not in note.lower():
            fail(f"asset candidate review_note missing safety language: {rel}")
    gate = data.get("approval_gate", "")
    if "without explicit Papu approval" not in gate:
        fail("asset manifest approval_gate must require explicit Papu approval")


def run_checks(verbose: bool = False) -> int:
    pack = read_text(PACK)
    readme = read_text(README)
    readme_herpes = read_text(README_HERPES)

    for phrase in REQUIRED_PACK_PHRASES:
        if phrase not in pack:
            fail(f"launch pack missing required phrase: {phrase}")

    for link in REQUIRED_README_LINKS:
        if link not in readme and link not in readme_herpes:
            fail(f"README surfaces missing link: {link}")

    if "NousResearch/hermes-agent" not in readme or "NousResearch/hermes-agent" not in readme_herpes:
        fail("upstream credit missing from README surfaces")

    missing_links: list[str] = []
    for path in [README, README_HERPES, PACK]:
        missing_links.extend(check_local_links(path))
    if missing_links:
        for item in missing_links:
            print(item)
        fail("local markdown link check failed")

    check_manifest()

    if verbose:
        print(f"Checked launch pack: {PACK}")
        print(f"Checked README surfaces: {README}, {README_HERPES}")
        print(f"Checked asset manifest: {MANIFEST}")
    print("Herpes Agent launch readiness OK: approval-gated, linked, credited, and asset-reviewed.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="print checked files")
    args = parser.parse_args(argv)
    return run_checks(verbose=args.verbose)


if __name__ == "__main__":
    sys.exit(main())
