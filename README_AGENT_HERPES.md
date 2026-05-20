# Agent Herpes

This fork adds a chaotic, free-first, open-source autonomy layer on top of Hermes Agent.

Start here:

- `AGENT_HERPES.md` — doctrine, tone, safety translation.
- `plans/agent-herpes/ROADMAP.md` — mutation roadmap.
- `content/agent-herpes/CONTENT_QUEUE.md` — drafts and demo ideas.
- `skills/agent-herpes/autonomous-growth/SKILL.md` — reusable growth loop.

## Activate The Rash

### Fast path for this fork

```bash
# Clone the fork
gh repo clone Hesoyam67/agent-herpes
cd agent-herpes

# Install in editable mode using the existing Hermes dev pattern
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .

# Launch and switch skin inside the CLI
hermes
/skin agent-herpes
```

### If Hermes is already installed from this checkout

```bash
hermes config set display.skin agent-herpes
# restart Hermes, or use /skin agent-herpes inside an interactive session
```

### Development sanity check

```bash
python3 - <<'PY'
from hermes_cli.skin_engine import load_skin
skin = load_skin('agent-herpes')
print(skin.name, skin.branding['agent_name'])
PY
```

Expected output contains:

```text
agent-herpes Agent Herpes
```

## Upstream Credit

Agent Herpes is a fork of NousResearch Hermes Agent. The engine remains MIT-licensed and upstream deserves credit for the serious machinery. This fork is the questionable lab coat, neon gloves, and meme cannon.

## Safety

The viral language is a metaphor for open-source distribution and autonomous workflow replication. No malware, no spam, no credential theft, no creepy nonsense. We spread docs, skills, demos, and useful chaos.
