#!/usr/bin/env python3
"""Render a plain-text Herpes Agent skin demo.

This deliberately avoids screenshots and paid tooling. It gives README/docs a
stable capture that can be regenerated anywhere with Python, because our budget
is currently a raccoon holding a coupon.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from hermes_cli.skin_engine import load_skin

RICH_TAG = re.compile(r"\[[^\]]+\]")


def plain_rich(text: str) -> str:
    return RICH_TAG.sub("", text).replace("[/]", "")


def render() -> str:
    skin = load_skin("herpes-agent")
    logo = plain_rich(skin.banner_logo).rstrip()
    hero = plain_rich(skin.banner_hero).rstrip()
    welcome = skin.branding["welcome"]
    response_label = skin.branding["response_label"].strip()
    prompt = skin.branding["prompt_symbol"]
    tool = skin.tool_prefix
    block = f"""{logo}

{hero}

{welcome}

{prompt} make this project less corporate
{tool} shedding virions: loaded autonomous-growth skill
{tool} mutating plans: updated roadmap
{tool} evading corporate antibodies: refused beige status prose

{response_label}
Infection update: docs are alive, repo is public, budget remains zero,
and the roadmap has entered the prodrome phase. Ship small. Mutate fast.
Wash hands. Commit often."""
    return "\n".join([
        "# Herpes Agent skin demo",
        "",
        "```text",
        block,
        "```",
        "",
        "Regenerate:",
        "",
        "```bash",
        "python3 scripts/render_herpes_agent_demo.py > docs/herpes-agent/demo.md",
        "```",
        "",
    ])


def main() -> int:
    print(render(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
