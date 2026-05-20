# Herpes Agent

This fork adds a chaotic, free-first, open-source autonomy layer on top of Hermes Agent.

Start here:

- `HERPES_AGENT.md` — doctrine, tone, safety translation.
- `plans/herpes-agent/ROADMAP.md` — mutation roadmap.
- `content/herpes-agent/CONTENT_QUEUE.md` — drafts and demo ideas.
- `docs/herpes-agent/autonomy-loop-demo.md` — harmless local autonomy loop demo.
- `docs/herpes-agent/autonomous-scans.md` — daily repo scan workflow.
- `docs/herpes-agent/weekly-summaries.md` — weekly mutation digest workflow.

## Activate The Rash

### Fast path for this fork

```bash
# Clone the fork
gh repo clone Hesoyam67/herpes-agent
cd herpes-agent

# Install in editable mode using the existing Hermes dev pattern
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .

# Launch and switch skin inside the CLI
hermes
/skin herpes-agent
```

### If Hermes is already installed from this checkout

```bash
hermes config set display.skin herpes-agent
# restart Hermes, or use /skin herpes-agent inside an interactive session
```

### Development sanity check

```bash
python3 - <<'PY'
from hermes_cli.skin_engine import load_skin
skin = load_skin('herpes-agent')
print(skin.name, skin.branding['agent_name'])
PY
```

Expected output contains:

```text
herpes-agent Herpes Agent
```

## Upstream Credit

Herpes Agent is a fork of NousResearch Hermes Agent. The engine remains MIT-licensed and upstream deserves credit for the serious machinery. This fork is the questionable lab coat, neon gloves, and meme cannon.

## Safety

The viral language is a metaphor for open-source distribution and autonomous workflow replication. No malware, no spam, no credential theft, no creepy nonsense. We spread docs, skills, demos, and useful chaos.
