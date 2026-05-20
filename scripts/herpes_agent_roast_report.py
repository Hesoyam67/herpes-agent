#!/usr/bin/env python3
"""Generate a Herpes Agent roast report from simple project metadata.

Zero-cost local lead magnet for ClawPump/agent-token outreach.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from textwrap import dedent


def render(name: str, symbol: str, url: str, context: str, tone: str) -> str:
    symbol_part = f" ({symbol})" if symbol else ""
    return dedent(f"""
    # Roast report: {name}{symbol_part}

    ## Verified facts
    - Project/agent: {name}
    - Symbol/name hint: {symbol or 'not provided'}
    - Source URL: {url or 'not provided'}
    - Provided context: {context or 'not provided'}

    ## Goblin read
    This thing may be a serious agent project, a wallet piñata, or three raccoons in a trench coat whispering “utility.” Current confidence depends on source quality; missing data is not bullish, it is fog with a marketing department.

    ## Risk smells
    1. If liquidity, holder concentration, or mint/freeze authority are not visible, the wallet should keep both hands inside the vehicle.
    2. If the X account is louder than the docs, that is not community — that is a smoke machine with a token address.
    3. If the product cannot explain who pays, why they pay, and what happens after launch week, it may be vibes wearing a helmet.

    ## Launch angles
    1. “We built the anti-boring agent: useful first, memeable second, solvent hopefully.”
    2. “Before you ape, let the goblin audit the pitch.”
    3. “Agent launch copy that does not sound like a VC pitch deck got microwaved.”

    ## X drafts
    1. I looked at {name} and the first question is simple: product, parasite, or performance art? Here’s the goblin read: useful claims need source links, liquidity needs daylight, and launch copy needs less anesthesia.
    2. {name} wants attention. Fine. But attention without trust is just a haunted billboard. Show docs, show traction, show risk — then meme.
    3. The fastest way to improve an agent launch: explain the buyer, the use case, and the post-launch reason to exist. Revolutionary concept: not dying after the candle.

    ## YouTube Short script
    Hook: “I found {name}, and my wallet immediately asked for adult supervision.”
    Body: “Here are the three things I check: visible product, visible risk, and whether the launch copy sounds like a human or a spreadsheet possessed by a casino.”
    CTA: “Want yours roasted? Drop the link. Herpes Agent spreads, but the spreadsheet disinfects.”

    ## Disclaimer
    This is not financial advice. It is a sarcastic public-info review. Do your own research, do not buy things because a robot made a joke, and never trust a green candle with unresolved childhood issues.
    """).strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--symbol', default='')
    ap.add_argument('--url', default='')
    ap.add_argument('--context', default='')
    ap.add_argument('--tone', default='spicy')
    ap.add_argument('--out', default='')
    args = ap.parse_args()
    report = render(args.name, args.symbol, args.url, args.context, args.tone)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(report)
    else:
        print(report)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
