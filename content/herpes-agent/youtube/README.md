# Herpes Agent YouTube local production

This directory stores local-only YouTube/X video drafts and rendered artifacts for Herpes Agent.

## Renderer

Use the repeatable local renderer:

```bash
python3 scripts/herpes_agent_render_video_card.py --help
```

The script uses:

- Python stdlib to generate `title_card.svg` with the chosen local avatar/image embedded as a data URI.
- `qlmanage` on macOS, when available, to generate a Quick Look thumbnail.
- `sips` on macOS, when available, to preserve exact SVG canvas dimensions for `thumbnail.png`.
- Local fallbacks for PNG if installed: `rsvg-convert`, ImageMagick, or ffmpeg SVG support.
- `ffmpeg` to render an MP4 from the still thumbnail plus either supplied audio or a generated silent audio track.

No paid APIs, SaaS renderers, account logins, uploads, or posting actions are part of this flow.

## JSON spec flow

A render spec can keep video production repeatable:

```json
{
  "title": "HERPES AGENT",
  "subtitle": "THE CONTAGION PROTOCOL",
  "big_text": "VIRAL VIBE.\nSAFE BEHAVIOR.",
  "bottom_line": "no malware • no spam • no credential goblins",
  "cta": "github.com/Hesoyam67/herpes-agent",
  "avatar": "{repo_root}/assets/herpes-agent/herpes-agent-avatar-x-400.png",
  "audio": null,
  "output_dir": "{repo_root}/content/herpes-agent/youtube/video_002",
  "basename": "herpes_agent_contagion_protocol_silent_dry_run",
  "duration": 35,
  "width": 1080,
  "height": 1920,
  "fps": 30
}
```

Path tokens supported by the script:

- `{repo_root}` / `$REPO_ROOT`
- `{cwd}`
- `{spec_dir}` / `$SPEC_DIR` when `--spec` is used

Render from a spec:

```bash
python3 scripts/herpes_agent_render_video_card.py \
  --spec content/herpes-agent/youtube/video_002/render_spec.json
```

Outputs in the configured `output_dir`:

- `title_card.svg`
- `thumbnail.png`
- `<basename>.mp4`

## CLI-only flow

```bash
python3 scripts/herpes_agent_render_video_card.py \
  --title "HERPES AGENT" \
  --subtitle "THE CONTAGION PROTOCOL" \
  --big-text $'VIRAL VIBE.\nSAFE BEHAVIOR.' \
  --bottom-line "no malware • no spam • no credential goblins" \
  --cta "github.com/Hesoyam67/herpes-agent" \
  --avatar assets/herpes-agent/herpes-agent-avatar-x-400.png \
  --output-dir content/herpes-agent/youtube/video_002 \
  --basename herpes_agent_contagion_protocol_silent_dry_run \
  --duration 35
```

Add final voiceover when available:

```bash
python3 scripts/herpes_agent_render_video_card.py \
  --spec content/herpes-agent/youtube/video_002/render_spec.json \
  --audio content/herpes-agent/youtube/video_002_voiceover.mp3 \
  --basename herpes_agent_contagion_protocol_video
```

If `--audio` is omitted, the MP4 contains a silent AAC track of `--duration` seconds. That is useful for local dry-runs only; do not treat it as the final publishable cut unless silence is the bit.

## Current drafts

- `VIDEO_001_patient_zero.md` — produced locally with manual pipeline.
- `VIDEO_002_contagion_protocol.md` — draft from `docs/herpes-agent/contagion-protocol.md`; silent dry-run render lives in `video_002/`.
