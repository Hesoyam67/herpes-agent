# Herpes Agent Brain Workflow

Herpes Agent is allowed to be a ridiculous open-source rash. The operating model is not ridiculous:

- **Hermes is the brain.** It chooses strategy, reads state, writes acceptance criteria, protects safety boundaries, keeps upstream credit visible, and verifies the final artifact.
- **OpenClaw is the muscle.** It does tool-heavy execution: repo edits, local scripts, browser/OAuth chores when approved, scans, repetitive checks, commits, pushes, and issue operations.
- **Verification is the immune system.** Every mutation needs evidence before anyone does a victory lap in a biohazard hoodie.

The reusable in-repo skill lives at [`skills/herpes-agent/brain/SKILL.md`](../../skills/herpes-agent/brain/SKILL.md).

## What the Brain Owns

Hermes owns the strategy layer:

1. Read active state, roadmap, content queue, open issues, and repo status.
2. Pick the next small mutation that leaves a durable artifact.
3. Define acceptance criteria and approval gates.
4. Keep the project name exact: **Herpes Agent**, not Agent Herpes.
5. Keep upstream credit loud: this fork is built on [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) and keeps the MIT/open-source posture intact.
6. Review and verify OpenClaw output before reporting success.
7. Update roadmap, issue state, and memory/state files when the information is durable.

## What the Muscle Owns

OpenClaw handles execution-heavy work:

- repo edits and generated artifacts
- local scripts and verification runs
- file scans, metrics scans, and issue scans
- screenshots/browser work only when the scope is approved
- commits, pushes, and issue closure when scoped to the owned repo

OpenClaw should return verifiable evidence:

- files changed
- commands run and important output
- commit SHA when committed
- issue state/URL when changed
- final `git status --short --branch`

If OpenClaw says “done” without a handle, that is not done; that is vibes wearing a fake mustache.

## Free-First / Open-Source Defaults

Default to:

- GitHub issues, labels, repo docs, and Actions where useful
- Markdown docs under `docs/herpes-agent/`
- built-in skills under `skills/herpes-agent/`
- Python standard library scripts in `scripts/`
- generated reports committed or ignored intentionally
- free local tools before paid SaaS
- open-source dependencies only when justified and documented

Avoid paid services, private lock-in, and SaaS goo until a local/free approach has clearly failed.

## Approval Gates

Safe to do autonomously inside the Herpes Agent repo:

- read files and inspect public repo metadata
- edit docs, skills, scripts, plans, and draft content
- run local tests/checks/generators
- commit and push verified owned-repo changes
- close the issue being worked after acceptance passes
- open one or two scoped follow-up issues when the backlog needs it

Ask Papu first for:

- public posts, replies, DMs, emails, Discord/forum messages, or launch announcements
- account/profile changes, OAuth permission grants, or browser identity actions
- paid services, purchases, subscriptions, or new secrets
- destructive Git/filesystem operations, force-pushes, or data deletion
- legal/license/ownership changes
- medical, malware, harassment, spam, or credential-theft-adjacent claims that are not obviously safe metaphor

## Standard Mutation Loop

1. **Orient:** read `state/active-task.json`, roadmap, content queue, open issues, and git status.
2. **Select:** choose one small, useful, funny, verifiable mutation.
3. **Specify:** define acceptance criteria, approval gates, target files, and checks.
4. **Execute:** implement locally or delegate tool-heavy work to OpenClaw.
5. **Verify:** run the checks that prove the artifact works.
6. **Commit/push/close:** only after verification.
7. **Record:** update durable docs/state/memory, not stale trivia.
8. **Continue:** if Papu requested nonstop/focused loop mode, pick the next mutation without waiting.

## Verification Checklist

For brain-workflow/docs mutations, check:

```bash
git diff --check
python3 - <<'PY'
from pathlib import Path
links = [
    Path('README.md'),
    Path('README_HERPES_AGENT.md'),
    Path('docs/herpes-agent/brain-workflow.md'),
    Path('skills/herpes-agent/brain/SKILL.md'),
]
missing = [str(p) for p in links if not p.exists()]
if missing:
    raise SystemExit(f'missing paths: {missing}')
for text_path in links:
    text = text_path.read_text(encoding='utf-8')
    if 'NousResearch/hermes-agent' not in text and text_path.name != 'SKILL.md':
        raise SystemExit(f'upstream credit missing in {text_path}')
print('brain workflow docs paths and upstream credit OK')
PY
python3 - <<'PY'
import re
from pathlib import Path
import yaml
content = Path('skills/herpes-agent/brain/SKILL.md').read_text(encoding='utf-8')
assert content.startswith('---')
match = re.search(r'\n---\s*\n', content[3:])
assert match
frontmatter = yaml.safe_load(content[3:match.start()+3])
assert frontmatter['name'] == 'herpes-agent-brain'
assert frontmatter['description']
print('brain skill frontmatter OK')
PY
```

## Related Docs

- [`contagion-protocol.md`](contagion-protocol.md) — safe autonomous operating rules.
- [`autonomy-loop-demo.md`](autonomy-loop-demo.md) — harmless local loop demo.
- [`autonomous-scans.md`](autonomous-scans.md) — zero-cost daily scan workflow.
- [`weekly-summaries.md`](weekly-summaries.md) — weekly digest generator.
- [`../../skills/herpes-agent/autonomous-growth/SKILL.md`](../../skills/herpes-agent/autonomous-growth/SKILL.md) — growth-loop skill.
