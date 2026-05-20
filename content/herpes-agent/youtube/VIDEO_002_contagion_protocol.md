# Video 002 — The Contagion Protocol

## Format

YouTube Short / X video, 30-40 seconds. Vertical card render plus voiceover.

## Source artifact

- `docs/herpes-agent/contagion-protocol.md`

## Working title options

1. I Gave My AI Agent a Safety Protocol
2. My Autonomous Agent Needed a Contagion Protocol
3. Viral AI Agent, Boringly Safe Behavior
4. Herpes Agent: Infect Responsibly
5. No Malware, Just Docs

## Recommended title

I Gave My AI Agent a Safety Protocol

## Description

Herpes Agent uses viral language as a software/workflow metaphor. The contagion protocol defines what is safe to mutate locally, what needs human approval, and what is absolutely not allowed: malware, spam, credential theft, fake engagement, botnets, or other goblin behavior.

Repo: https://github.com/Hesoyam67/herpes-agent
Upstream credit: https://github.com/NousResearch/hermes-agent

#AIagents #OpenSource #BuildInPublic #CodingAgents #AgentSafety

## Voiceover script

I told an AI agent to be autonomous.

Then I immediately wrote a contagion protocol, because I enjoy not being sued.

In this repo, contagion means useful ideas replicate: docs, skills, harmless local scripts, tiny issues, and demos.

It does not mean malware, spam, credential theft, botnets, fake engagement, or any goblin behavior that gets a lawyer's attention.

Herpes Agent can inspect the repo, draft docs, run local checks, and make small verified commits when explicitly tasked.

But public posting, OAuth, money, destructive changes, account stuff, and internet rash cannons are approval-gated.

The vibe is viral. The behavior is boringly safe.

Mutate docs. Ship scripts. Infect responsibly.

## On-screen beats

1. 0:00 — Avatar/mascot appears. Text: "I told an AI agent to be autonomous."
2. 0:04 — Safety stamp. "Then I wrote a protocol."
3. 0:08 — Bullet burst: docs, skills, scripts, issues, demos.
4. 0:14 — Red warning list: no malware, no spam, no credential goblins.
5. 0:22 — Gate graphic: local work OK; public/account/destructive actions need approval.
6. 0:31 — CTA: "Mutate docs. Ship scripts. Infect responsibly."

## Thumbnail text

VIRAL VIBE.
SAFE BEHAVIOR.

Bottom line: `no malware • no spam • no credential goblins`

## Render status

Final local production assets exist:

- Voiceover: `content/herpes-agent/youtube/video_002_voiceover.mp3`
- Thumbnail: `content/herpes-agent/youtube/video_002/thumbnail.png`
- Final MP4: `content/herpes-agent/youtube/video_002/herpes_agent_contagion_protocol_video.mp4`
- Silent renderer dry run: `content/herpes-agent/youtube/video_002/herpes_agent_contagion_protocol_silent_dry_run.mp4`

Re-render command:

```bash
python3 scripts/herpes_agent_render_video_card.py \
  --spec content/herpes-agent/youtube/video_002/render_spec.json \
  --audio content/herpes-agent/youtube/video_002_voiceover.mp3 \
  --basename herpes_agent_contagion_protocol_video
```

No upload/post is implied by this draft. It is a local production artifact only until the correct YouTube/X publishing accounts are active.
