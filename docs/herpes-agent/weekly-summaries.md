# Herpes Agent weekly mutation summaries

The weekly summary generator produces a Markdown digest of what the rash did lately: commits, changed files, issue metabolism, roadmap digestion, content spores, and the next safe infection vector.

It is intentionally zero-cost:

- local Git for commit/file history
- `gh` CLI for public repo/issue metadata when available
- Markdown output for humans, cron, GitHub comments, and gremlins
- no paid APIs, no analytics trackers, no SaaS wallet leeches

## Manual run

```bash
python3 scripts/herpes_agent_weekly_summary.py
```

Write a local report:

```bash
python3 scripts/herpes_agent_weekly_summary.py --out reports/weekly/latest.md
```

Use a different window:

```bash
python3 scripts/herpes_agent_weekly_summary.py --days 14 --out reports/weekly/last-14-days.md
```

## Cron-friendly prompt

Use this with Hermes cron if Papu wants a weekly digest delivered into chat:

```text
Run from /Users/hesoyam/.openclaw/workspace/herpes-agent.
Execute: python3 scripts/herpes_agent_weekly_summary.py --out reports/weekly/latest.md
Read the generated Markdown and summarize the most important changes, blockers, and next safe autonomous action. Keep the tone chaotic but useful. Do not post publicly.
```

## Output sections

- Repo vitals
- Mutations shipped
- Files touched
- Issue metabolism
- Roadmap digestion
- Content spores
- Recommended next infection vector
- Safety / budget antibodies

## Rules

- Public posting still requires explicit approval.
- Do not include secrets or private credentials in reports.
- Keep upstream Hermes credit visible.
- If GitHub CLI/network fails, local Git data should still produce a useful report.
