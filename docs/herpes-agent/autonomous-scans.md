# Herpes Agent autonomous scans

This is the zero-budget little goblin that checks whether the project is spreading or just sitting there like a cursed houseplant.

## Run manually

```bash
python3 scripts/herpes_agent_daily_scan.py
```

Write a report file:

```bash
python3 scripts/herpes_agent_daily_scan.py --out reports/daily/latest.md
```

## Cron-friendly prompt

Use this with Hermes cron or any regular cron runner:

```text
Run `python3 scripts/herpes_agent_daily_scan.py --out reports/daily/$(date -u +%F).md`, inspect the report, pick one safe free-first mutation from the recommendation/open issues, implement it if it is internal and low-risk, verify it, commit/push, and update the issue. Do not post publicly or spend money without explicit approval.
```

## Design rules

- Uses GitHub CLI and git only.
- No paid APIs.
- No secrets printed.
- Markdown output so it can be pasted anywhere without a SaaS priest blessing it.
- Failure should degrade into warnings, not explode like a VC-funded toaster.
