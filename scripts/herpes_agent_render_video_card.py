#!/usr/bin/env python3
"""Render a local Herpes Agent YouTube-short title card and video.

The renderer is intentionally boring: Python stdlib writes an SVG with an
embedded local image; local tools (Quick Look/qlmanage, sips, and ffmpeg
when present) turn that into a thumbnail PNG and a simple MP4 with either a
supplied audio track or a generated silent track.
"""
from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
import pathlib
import shutil
import subprocess
import sys
import textwrap
from typing import Any

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_AVATAR = REPO_ROOT / "assets" / "herpes-agent" / "herpes-agent-avatar-x-400.png"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "content" / "herpes-agent" / "youtube" / "rendered"

DEFAULT_SPEC: dict[str, Any] = {
    "title": "HERPES AGENT",
    "subtitle": "LOCAL SHORT RENDERER",
    "big_text": "SPREAD WORKFLOWS\nNOT MALWARE",
    "bottom_line": "viral metaphor. safe behavior.",
    "cta": "github.com/Hesoyam67/herpes-agent",
    "avatar": str(DEFAULT_AVATAR),
    "audio": None,
    "output_dir": str(DEFAULT_OUTPUT_DIR),
    "basename": "herpes_agent_short",
    "duration": 35.0,
    "width": 1080,
    "height": 1920,
    "fps": 30,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a repeatable local Herpes Agent YouTube short card.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--spec",
        type=pathlib.Path,
        help="Optional JSON render spec. CLI flags override JSON values.",
    )
    parser.add_argument("--title", help="Top title text.")
    parser.add_argument("--subtitle", help="Subtitle under the title.")
    parser.add_argument(
        "--big-text",
        "--hook",
        "--top-hook",
        dest="big_text",
        help="Large thumbnail hook text; use literal newlines in JSON for line breaks.",
    )
    parser.add_argument("--bottom-line", help="Small bottom line above the CTA.")
    parser.add_argument("--cta", help="Call-to-action text at the bottom.")
    parser.add_argument("--avatar", help="Local avatar/image path to embed in the SVG.")
    parser.add_argument(
        "--audio",
        help="Optional local audio path. If omitted, ffmpeg creates a silent track.",
    )
    parser.add_argument("--output-dir", help="Directory for title_card.svg, thumbnail.png, and MP4.")
    parser.add_argument(
        "--basename",
        "--video-basename",
        dest="basename",
        help="MP4 basename without extension.",
    )
    parser.add_argument(
        "--duration",
        type=float,
        help="Silent-track duration in seconds when --audio is omitted.",
    )
    parser.add_argument("--width", type=int, help="Canvas/video width in pixels.")
    parser.add_argument("--height", type=int, help="Canvas/video height in pixels.")
    parser.add_argument("--fps", type=int, help="Output video frame rate.")
    parser.add_argument(
        "--no-mp4",
        action="store_true",
        help="Only write SVG and thumbnail PNG; skip ffmpeg MP4 rendering.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print local command output when external tools run.",
    )
    return parser


def load_json_spec(path: pathlib.Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON spec {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"Invalid JSON spec {path}: top-level value must be an object")
    return data


def merged_spec(args: argparse.Namespace) -> tuple[dict[str, Any], pathlib.Path | None]:
    spec = dict(DEFAULT_SPEC)
    spec_path = args.spec.resolve() if args.spec else None
    if spec_path:
        spec.update(load_json_spec(spec_path))

    for key in (
        "title",
        "subtitle",
        "big_text",
        "bottom_line",
        "cta",
        "avatar",
        "audio",
        "output_dir",
        "basename",
        "duration",
        "width",
        "height",
        "fps",
    ):
        value = getattr(args, key)
        if value is not None:
            spec[key] = value
    return spec, spec_path


def resolve_path(value: str | pathlib.Path | None, *, spec_path: pathlib.Path | None) -> pathlib.Path | None:
    if value in (None, ""):
        return None
    raw = str(value)
    replacements = {
        "{repo_root}": str(REPO_ROOT),
        "${repo_root}": str(REPO_ROOT),
        "$REPO_ROOT": str(REPO_ROOT),
        "{cwd}": str(pathlib.Path.cwd()),
    }
    if spec_path:
        replacements["{spec_dir}"] = str(spec_path.parent)
        replacements["${spec_dir}"] = str(spec_path.parent)
        replacements["$SPEC_DIR"] = str(spec_path.parent)
    for token, replacement in replacements.items():
        raw = raw.replace(token, replacement)
    path = pathlib.Path(raw).expanduser()
    if path.is_absolute():
        return path
    return (pathlib.Path.cwd() / path).resolve()


def safe_int(value: Any, key: str, minimum: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError) as exc:
        raise SystemExit(f"{key} must be an integer") from exc
    if number < minimum:
        raise SystemExit(f"{key} must be >= {minimum}")
    return number


def safe_float(value: Any, key: str, minimum: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise SystemExit(f"{key} must be a number") from exc
    if number < minimum:
        raise SystemExit(f"{key} must be >= {minimum}")
    return number


def clean_basename(value: Any) -> str:
    basename = pathlib.Path(str(value or "herpes_agent_short")).name
    stem = pathlib.Path(basename).stem or "herpes_agent_short"
    safe = "".join(char if char.isalnum() or char in "._-" else "_" for char in stem)
    return safe.strip("._-") or "herpes_agent_short"


def data_uri(path: pathlib.Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    if not mime:
        mime = "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def wrap_lines(text: Any, *, max_chars: int, max_lines: int) -> list[str]:
    raw = str(text or "").strip()
    if not raw:
        return []
    lines: list[str] = []
    for chunk in raw.splitlines():
        wrapped = textwrap.wrap(
            chunk.strip(),
            width=max_chars,
            break_long_words=False,
            replace_whitespace=False,
        ) or [""]
        lines.extend(wrapped)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        if len(lines[-1]) >= max_chars - 1:
            lines[-1] = lines[-1][: max(1, max_chars - 2)].rstrip() + "…"
        else:
            lines[-1] = lines[-1].rstrip() + "…"
    return lines


def estimate_chars(width: int, font_size: int, factor: float = 0.56) -> int:
    return max(8, int((width * 0.86) / max(1, font_size * factor)))


def text_block(
    lines: list[str],
    *,
    x: int,
    y: int,
    size: int,
    fill: str,
    family: str,
    line_height: float = 1.14,
    weight: str = "700",
    anchor: str = "middle",
    extra: str = "",
) -> str:
    if not lines:
        return ""
    rendered = []
    dy = int(size * line_height)
    for index, line in enumerate(lines):
        rendered.append(
            f'  <text x="{x}" y="{y + index * dy}" text-anchor="{anchor}" '
            f'font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" {extra}>{html.escape(line)}</text>'
        )
    return "\n".join(rendered)


def render_svg(spec: dict[str, Any], *, avatar_path: pathlib.Path, width: int, height: int) -> str:
    avatar_uri = data_uri(avatar_path)
    title_size = max(44, round(width * 0.070))
    subtitle_size = max(28, round(width * 0.038))
    big_size = max(56, round(width * 0.086))
    bottom_size = max(28, round(width * 0.034))
    cta_size = max(24, round(width * 0.028))

    title_lines = wrap_lines(str(spec["title"]).upper(), max_chars=estimate_chars(width, title_size, 0.58), max_lines=2)
    subtitle_lines = wrap_lines(
        str(spec["subtitle"]).upper(),
        max_chars=estimate_chars(width, subtitle_size, 0.56),
        max_lines=2,
    )
    big_lines = wrap_lines(
        str(spec["big_text"]).upper(),
        max_chars=estimate_chars(width, big_size, 0.58),
        max_lines=4,
    )
    bottom_lines = wrap_lines(
        spec.get("bottom_line", ""),
        max_chars=estimate_chars(width, bottom_size, 0.48),
        max_lines=2,
    )
    cta_lines = wrap_lines(
        spec.get("cta", ""),
        max_chars=estimate_chars(width, cta_size, 0.50),
        max_lines=2,
    )

    cx = width // 2
    title_y = round(height * 0.070)
    subtitle_y = title_y + round(title_size * 1.08 * max(1, len(title_lines)))
    avatar_cy = round(height * 0.390)
    avatar_r = round(min(width * 0.280, height * 0.175))
    avatar_x = cx - avatar_r
    avatar_y = avatar_cy - avatar_r
    avatar_size = avatar_r * 2
    big_y = round(height * 0.625)
    bottom_y = round(height * 0.842)
    cta_y = round(height * 0.925)

    title_text = text_block(
        title_lines,
        x=cx,
        y=title_y,
        size=title_size,
        fill="#39ff88",
        family="Arial Black, Helvetica, sans-serif",
        line_height=1.05,
        weight="900",
        extra='filter="url(#glow)"',
    )
    subtitle_text = text_block(
        subtitle_lines,
        x=cx,
        y=subtitle_y,
        size=subtitle_size,
        fill="#ff33cc",
        family="Arial Black, Helvetica, sans-serif",
        line_height=1.10,
        weight="900",
    )
    big_text = text_block(
        big_lines,
        x=cx,
        y=big_y,
        size=big_size,
        fill="#ffffff",
        family="Arial Black, Helvetica, sans-serif",
        line_height=1.08,
        weight="900",
        extra='filter="url(#shadow)"',
    )
    bottom_text = text_block(
        bottom_lines,
        x=cx,
        y=bottom_y,
        size=bottom_size,
        fill="#d1fff1",
        family="Helvetica, Arial, sans-serif",
        line_height=1.22,
        weight="700",
    )
    cta_text = text_block(
        cta_lines,
        x=cx,
        y=cta_y,
        size=cta_size,
        fill="#90ffff",
        family="Menlo, Consolas, monospace",
        line_height=1.18,
        weight="700",
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <radialGradient id="bg" cx="50%" cy="28%" r="86%">
      <stop offset="0%" stop-color="#123f3a"/>
      <stop offset="48%" stop-color="#071022"/>
      <stop offset="100%" stop-color="#02040a"/>
    </radialGradient>
    <linearGradient id="slash" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#39ff88" stop-opacity="0.0"/>
      <stop offset="45%" stop-color="#39ff88" stop-opacity="0.32"/>
      <stop offset="55%" stop-color="#ff33cc" stop-opacity="0.34"/>
      <stop offset="100%" stop-color="#ff33cc" stop-opacity="0.0"/>
    </linearGradient>
    <filter id="glow"><feGaussianBlur stdDeviation="7" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <filter id="shadow"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="#000000" flood-opacity="0.72"/></filter>
    <clipPath id="avatarClip"><circle cx="{cx}" cy="{avatar_cy}" r="{avatar_r}"/></clipPath>
  </defs>
  <rect width="{width}" height="{height}" fill="url(#bg)"/>
  <path d="M {-round(width * 0.12)} {round(height * 0.22)} L {round(width * 1.12)} {round(height * 0.08)} L {round(width * 1.15)} {round(height * 0.18)} L {-round(width * 0.05)} {round(height * 0.34)} Z" fill="url(#slash)" opacity="0.72"/>
  <path d="M {-round(width * 0.08)} {round(height * 0.78)} L {round(width * 1.08)} {round(height * 0.62)} L {round(width * 1.15)} {round(height * 0.76)} L {-round(width * 0.03)} {round(height * 0.92)} Z" fill="url(#slash)" opacity="0.55"/>
  <circle cx="{cx}" cy="{avatar_cy}" r="{round(avatar_r * 1.13)}" fill="none" stroke="#ff33cc" stroke-width="8" stroke-dasharray="26 22" opacity="0.88"/>
  <circle cx="{cx}" cy="{avatar_cy}" r="{round(avatar_r * 1.02)}" fill="none" stroke="#39ff88" stroke-width="14" opacity="0.82" filter="url(#glow)"/>
  <circle cx="{cx}" cy="{avatar_cy}" r="{avatar_r}" fill="#050812" opacity="0.82"/>
  <image href="{avatar_uri}" x="{avatar_x}" y="{avatar_y}" width="{avatar_size}" height="{avatar_size}" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>
  <rect x="{round(width * 0.075)}" y="{round(height * 0.552)}" width="{round(width * 0.85)}" height="{round(height * 0.018)}" rx="{round(height * 0.009)}" fill="#39ff88" opacity="0.78"/>
  <rect x="{round(width * 0.075)}" y="{round(height * 0.807)}" width="{round(width * 0.85)}" height="{round(height * 0.006)}" rx="{round(height * 0.003)}" fill="#ff33cc" opacity="0.82"/>
{title_text}
{subtitle_text}
{big_text}
{bottom_text}
{cta_text}
</svg>
'''


def run_command(command: list[str], *, verbose: bool = False, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if verbose or (check and result.returncode != 0):
        print("$ " + " ".join(command), file=sys.stderr)
        if result.stdout:
            print(result.stdout, file=sys.stderr, end="" if result.stdout.endswith("\n") else "\n")
        if result.stderr:
            print(result.stderr, file=sys.stderr, end="" if result.stderr.endswith("\n") else "\n")
    if check and result.returncode != 0:
        raise RuntimeError(f"command failed with exit code {result.returncode}: {' '.join(command)}")
    return result


def nonempty(path: pathlib.Path) -> bool:
    return path.exists() and path.stat().st_size > 0


def render_thumbnail(
    svg_path: pathlib.Path,
    thumbnail_path: pathlib.Path,
    *,
    width: int,
    height: int,
    verbose: bool,
) -> str:
    thumbnail_path.parent.mkdir(parents=True, exist_ok=True)
    if thumbnail_path.exists():
        thumbnail_path.unlink()

    def render_with_sips(destination: pathlib.Path) -> bool:
        sips = shutil.which("sips")
        if not sips:
            return False
        if destination.exists():
            destination.unlink()
        result = run_command(
            [sips, "-s", "format", "png", str(svg_path), "--out", str(destination)],
            verbose=verbose,
            check=False,
        )
        if nonempty(destination):
            return True
        if verbose and result.returncode != 0:
            print(f"sips failed with exit code {result.returncode}; trying next renderer", file=sys.stderr)
        destination.unlink(missing_ok=True)
        return False

    qlmanage = shutil.which("qlmanage")
    if qlmanage:
        candidates = [svg_path.with_name(svg_path.name + ".png"), svg_path.with_suffix(".png")]
        for candidate in candidates:
            if candidate.exists() and candidate != thumbnail_path:
                candidate.unlink()
        result = run_command(
            [qlmanage, "-t", "-s", str(max(width, height)), "-o", str(svg_path.parent), str(svg_path)],
            verbose=verbose,
            check=False,
        )
        for candidate in candidates:
            if nonempty(candidate):
                shutil.copyfile(candidate, thumbnail_path)
                if candidate != thumbnail_path:
                    candidate.unlink(missing_ok=True)
                sips_path = thumbnail_path.with_name(thumbnail_path.stem + ".sips.png")
                if render_with_sips(sips_path):
                    shutil.move(str(sips_path), str(thumbnail_path))
                    return "qlmanage+sips" if result.returncode == 0 else "qlmanage+sips (qlmanage nonzero, usable PNG)"
                return "qlmanage" if result.returncode == 0 else "qlmanage (nonzero exit, usable PNG)"

    if render_with_sips(thumbnail_path):
        return "sips"

    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        run_command([rsvg, "-w", str(width), "-h", str(height), "-o", str(thumbnail_path), str(svg_path)], verbose=verbose)
        if nonempty(thumbnail_path):
            return "rsvg-convert"

    magick = shutil.which("magick") or shutil.which("convert")
    if magick:
        run_command(
            [magick, "-background", "none", "-density", "144", str(svg_path), "-resize", f"{width}x{height}!", str(thumbnail_path)],
            verbose=verbose,
        )
        if nonempty(thumbnail_path):
            return pathlib.Path(magick).name

    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        run_command(
            [ffmpeg, "-y", "-i", str(svg_path), "-vf", f"scale={width}:{height}", "-frames:v", "1", str(thumbnail_path)],
            verbose=verbose,
        )
        if nonempty(thumbnail_path):
            return "ffmpeg"

    raise RuntimeError(
        "Could not render thumbnail. Install/use one local tool: qlmanage (macOS), rsvg-convert, ImageMagick, or ffmpeg with SVG support."
    )


def render_mp4(
    thumbnail_path: pathlib.Path,
    mp4_path: pathlib.Path,
    *,
    audio_path: pathlib.Path | None,
    duration: float,
    width: int,
    height: int,
    fps: int,
    verbose: bool,
) -> str:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is required to render MP4 output")
    mp4_path.parent.mkdir(parents=True, exist_ok=True)
    if mp4_path.exists():
        mp4_path.unlink()

    vf = (
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p"
    )
    base = [ffmpeg, "-y", "-loop", "1", "-framerate", str(fps), "-i", str(thumbnail_path)]
    if audio_path:
        command = base + [
            "-i",
            str(audio_path),
            "-vf",
            vf,
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-r",
            str(fps),
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(mp4_path),
        ]
        audio_mode = "supplied audio"
    else:
        duration_text = f"{duration:.3f}"
        command = base + [
            "-f",
            "lavfi",
            "-t",
            duration_text,
            "-i",
            "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-vf",
            vf,
            "-t",
            duration_text,
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-r",
            str(fps),
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(mp4_path),
        ]
        audio_mode = f"silent {duration_text}s audio"

    run_command(command, verbose=verbose)
    if not nonempty(mp4_path):
        raise RuntimeError(f"ffmpeg did not create a non-empty MP4 at {mp4_path}")
    return audio_mode


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    spec, spec_path = merged_spec(args)

    width = safe_int(spec.get("width"), "width", 16)
    height = safe_int(spec.get("height"), "height", 16)
    fps = safe_int(spec.get("fps"), "fps", 1)
    duration = safe_float(spec.get("duration"), "duration", 0.1)
    basename = clean_basename(spec.get("basename"))

    avatar_path = resolve_path(spec.get("avatar"), spec_path=spec_path)
    audio_path = resolve_path(spec.get("audio"), spec_path=spec_path)
    output_dir = resolve_path(spec.get("output_dir"), spec_path=spec_path)
    if output_dir is None:
        raise SystemExit("output_dir is required")
    if avatar_path is None or not avatar_path.exists():
        raise SystemExit(f"avatar/image path not found: {avatar_path}")
    if audio_path is not None and not audio_path.exists():
        raise SystemExit(f"audio path not found: {audio_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    svg_path = output_dir / "title_card.svg"
    thumbnail_path = output_dir / "thumbnail.png"
    mp4_path = output_dir / f"{basename}.mp4"

    svg_path.write_text(render_svg(spec, avatar_path=avatar_path, width=width, height=height), encoding="utf-8")
    thumbnail_tool = render_thumbnail(svg_path, thumbnail_path, width=width, height=height, verbose=args.verbose)

    audio_mode = "skipped"
    if not args.no_mp4:
        audio_mode = render_mp4(
            thumbnail_path,
            mp4_path,
            audio_path=audio_path,
            duration=duration,
            width=width,
            height=height,
            fps=fps,
            verbose=args.verbose,
        )

    print(f"SVG: {svg_path}")
    print(f"Thumbnail: {thumbnail_path} ({thumbnail_tool})")
    if args.no_mp4:
        print("MP4: skipped (--no-mp4)")
    else:
        print(f"MP4: {mp4_path} ({audio_mode})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
