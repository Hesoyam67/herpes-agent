#!/usr/bin/env python3
"""Scan ClawPump token data for roast-report outreach leads.

This is a zero-cost funnel helper: it does not trade, connect wallets, post, or
claim financial upside. It ranks public ClawPump tokens by whether they look
worth roasting/promoting as sample reports.
"""
from __future__ import annotations

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

API_URL = "https://agents.clawpump.tech/api/tokens"


def money(value: Any) -> str:
    try:
        n = float(value or 0)
    except (TypeError, ValueError):
        return "n/a"
    if abs(n) >= 1_000_000:
        return f"${n / 1_000_000:.2f}M"
    if abs(n) >= 1_000:
        return f"${n / 1_000:.1f}k"
    return f"${n:.2f}"


def handle(twitter: Any) -> str:
    if not twitter:
        return ""
    s = str(twitter).strip()
    if not s:
        return ""
    if "x.com/" in s:
        return "@" + s.rstrip("/").split("/")[-1]
    if "twitter.com/" in s:
        return "@" + s.rstrip("/").split("/")[-1]
    return s if s.startswith("@") else f"@{s}"


def fetch_tokens(limit: int, period: str, sort: str) -> dict[str, Any]:
    url = f"{API_URL}?sort={sort}&limit={limit}&offset=0&period={period}"
    req = Request(url, headers={"User-Agent": "HerpesAgentLeadScan/0.1"})
    with urlopen(req, timeout=25) as response:
        return json.load(response)


def score_token(token: dict[str, Any]) -> tuple[float, list[str]]:
    volume = float(token.get("volume24h") or 0)
    liquidity = float(token.get("liquidity") or 0)
    market_cap = float(token.get("marketCap") or 0)
    reasons: list[str] = []

    score = 0.0
    if volume > 0:
        score += math.log10(volume + 1) * 12
        reasons.append(f"24h volume {money(volume)}")
    if liquidity >= 5_000:
        score += math.log10(liquidity + 1) * 7
        reasons.append(f"liquidity {money(liquidity)}")
    if token.get("twitter"):
        score += 12
        reasons.append(f"has X handle {handle(token.get('twitter'))}")
    if token.get("website"):
        score += 6
        reasons.append("has website")
    if not token.get("verified"):
        score += 8
        reasons.append("unverified = better roast angle")
    else:
        reasons.append("verified")
    if market_cap and liquidity and liquidity / market_cap < 0.03:
        score -= 8
        reasons.append("thin liquidity vs market cap")
    if volume > 50_000 and liquidity < 10_000:
        score -= 10
        reasons.append("volume/liquidity mismatch")
    return round(score, 2), reasons


def render_report(payload: dict[str, Any], limit: int) -> str:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    rows: list[dict[str, Any]] = []
    for token in payload.get("tokens", []):
        score, reasons = score_token(token)
        rows.append({"score": score, "reasons": reasons, "token": token})
    rows.sort(key=lambda r: r["score"], reverse=True)
    rows = rows[:limit]

    lines = [
        "# ClawPump roast lead scan",
        "",
        f"Generated: {now}",
        "",
        "Purpose: find public ClawPump token/agent leads for free roast reports and future paid micro-reports. This is not financial advice and does not execute wallet actions.",
        "",
        f"Source: `{API_URL}?sort={payload.get('sort')}&limit={payload.get('limit')}&offset=0&period={payload.get('period')}`",
        f"Reported total tokens: `{payload.get('total')}`",
        "",
        "## Ranked leads",
        "",
        "| Rank | Score | Token | Agent | X | Verified | MCap | 24h Vol | Liq | Why roast it |",
        "|---:|---:|---|---|---|---:|---:|---:|---:|---|",
    ]
    for i, row in enumerate(rows, start=1):
        token = row["token"]
        reasons = "; ".join(row["reasons"][:4])
        name = f"{token.get('symbol') or '?'} / {token.get('name') or '?'}"
        agent = token.get("agentName") or token.get("agentId") or "n/a"
        lines.append(
            "| {rank} | {score:.2f} | `{name}` | `{agent}` | {x} | {verified} | {mcap} | {vol} | {liq} | {why} |".format(
                rank=i,
                score=float(row["score"]),
                name=str(name).replace("|", " "),
                agent=str(agent).replace("|", " "),
                x=handle(token.get("twitter")) or "n/a",
                verified="yes" if token.get("verified") else "no",
                mcap=money(token.get("marketCap")),
                vol=money(token.get("volume24h")),
                liq=money(token.get("liquidity")),
                why=reasons.replace("|", " "),
            )
        )

    lines.extend([
        "",
        "## Next use",
        "",
        "1. Generate sample reports for the top 3 non-official leads.",
        "2. When @Heso_67 posting is available, use these as proof-of-work replies/posts.",
        "3. If inbound demand appears, offer a paid micro-report before attempting ClawPump paid marketplace listing.",
        "",
        "## Safety",
        "",
        "- No wallet connection, no trading, no token buys, no posts were performed by this scan.",
        "- Treat low liquidity and unverified status as outreach/roast angles, not buy signals.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank ClawPump tokens as roast-report leads")
    parser.add_argument("--limit", type=int, default=12, help="number of ranked rows to print")
    parser.add_argument("--fetch-limit", type=int, default=60, help="number of API rows to fetch")
    parser.add_argument("--period", default="24h")
    parser.add_argument("--sort", default="volume")
    parser.add_argument("--json-out", default="")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    payload = fetch_tokens(args.fetch_limit, args.period, args.sort)
    report = render_report(payload, args.limit)

    if args.json_out:
        path = Path(args.json_out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
