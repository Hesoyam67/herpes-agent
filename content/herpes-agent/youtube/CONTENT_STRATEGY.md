# Herpes Agent content strategy — YouTube + X

Generated: 2026-05-20

## Trend scan notes

Low-cost scan source: YouTube search for `AI agents open source coding agents` from logged-out browser. X API search is currently blocked by `CreditsDepleted`, so X trend monitoring must use browser/manual access or unpaid sources for now.

Observed YouTube patterns:

1. Fresh AI-agent setup/tutorial content is moving fast. Example search result: `Pi: Open-Source AI Agent Terminal Set-Up`, 7.8K views in 13 hours.
2. Explainers around MCP/ADK/agent architecture still pull broad interest. Example: IBM Technology `MCP vs ADK`, 21K views in 1 day.
3. Mega tutorials exist (`Build Your Own Claude Code`, ~12 hours), which creates space for short parody summaries: "I did the 12-hour thing but infected it with docs."
4. Titles that work: concrete tool name + clear setup/build promise + timeframe/result.
5. Thumbnails are direct: big tool/agent name, high-contrast text, human/mascot/terminal element.
6. The audience cares about practical autonomy: terminal setup, guardrails, session management, providers/models, extending/customization.
7. "Agent chaos but safe" is a good differentiator: funny brand + actual guardrails is memorable.
8. Shorts can recycle repo artifacts quickly: skin demo, daily scan, weekly mutation summary, autonomy loop, contagion protocol.

## Content pillars

1. Patient Zero updates — what the agent shipped today.
2. Zero-budget autonomy — tools/scripts/cron/docs, no SaaS wallet leeches.
3. Agent safety but funny — approval gates, secrets hygiene, non-spam growth.
4. Build-in-public mutations — small commits, small issues, visible roadmap.
5. Parody branding — corporate beige vs neon workflow rash.

## Immediate videos from existing artifacts

### Video 001 — Patient Zero: Herpes Agent Exists Now

Status: produced locally.

- Metadata/script: `content/herpes-agent/youtube/VIDEO_001_patient_zero.md`
- MP4: `content/herpes-agent/youtube/video_001/herpes_agent_patient_zero_video.mp4`
- Thumbnail: `content/herpes-agent/youtube/video_001/thumbnail.png`

### Video 002 — The Contagion Protocol

Hook: "I told an AI agent to be autonomous, then immediately had to write a safety protocol because I enjoy not being sued."

Use artifact: `docs/herpes-agent/contagion-protocol.md`

Angle: show autonomy levels: safe internal work vs approval-gated public/account/destructive actions.

### Video 003 — The Autonomy Loop Demo

Hook: "This agent doesn't need vibes. It needs inspect → decide → artifact → verify. Like Scrum, but less haunted."

Use artifact: `docs/herpes-agent/autonomy-loop-demo.md`

Angle: explain how Herpes Agent safely picks tiny repo mutations and leaves proof.

### Video 004 — Daily Scan / Weekly Mutation Report

Hook: "My agent writes its own status reports so I can spend less time managing and more time making worse branding decisions."

Use artifacts:

- `scripts/herpes_agent_daily_scan.py`
- `scripts/herpes_agent_weekly_summary.py`
- `docs/herpes-agent/autonomous-scans.md`
- `docs/herpes-agent/weekly-summaries.md`

## Title patterns

- `I Built/Forked X and It Did Y`
- `Open-Source AI Agent Setup, But Unhinged`
- `My AI Agent Shipped N Things While I Watched`
- `I Gave My Coding Agent a Safety Protocol`
- `Zero-Budget Autonomous Agent: Day N`

## Thumbnail patterns

- Big neon phrase: `I GAVE MY AI AGENT A RASH`
- Mascot/avatar + terminal background
- Before/after: `Corporate Beige` → `Workflow Rash`
- Red/green safety stamp: `NO MALWARE, JUST DOCS`
- Counter style: `0$ SPENT / N ARTIFACTS SHIPPED`

## X growth plan while API is blocked

- Queue posts locally in `content/herpes-agent/X_QUEUE.md`.
- Do not buy X API credits.
- Use browser posting only when active account is verified as `@Heso_67`.
- Once posting works, publish 1 launch post + 1 video clip post, then engage only with relevant AI-agent/build-in-public threads.

## Next production steps

1. Upload Video 001 only after the correct Herpes Agent YouTube channel/account is confirmed.
2. Produce Video 002 from contagion protocol using the same FFmpeg/TTS pipeline.
3. Create a repeatable `scripts/render_youtube_short.py` so future videos are one-command instead of artisanal gremlin pottery.
4. Add a local upload checklist so YouTube Studio work is predictable and not a click goblin ritual.
