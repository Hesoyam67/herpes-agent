# Herpes Agent platform ops status

Generated: 2026-05-20

This file tracks what the agent can actually do right now without pretending the internet is a vending machine that accepts vibes.

## YouTube

Target account requested by Papu: `gercakadrian2@gmail.com`.

Current browser findings:

- Browserbase/headless sessions are not reliable for this project because Papu already has real Chrome profiles logged in. Lesson learned: inspect real local Chrome first, then use Browserbase only for public/logged-out research.
- Local Chrome profile `Default` and `Profile 2` both contain non-secret account hints for `gercakadrian2@gmail.com`; `Profile 2` lists it first.
- Real local Chrome / Adrian profile confirms target Google account `gercakadrian2@gmail.com` is accessible.
- Previous existing YouTube channel under that account remains:
  - Channel name: `Heso`
  - Handle: `@Hesoyam67`
  - Channel URL: `https://www.youtube.com/@Hesoyam67`
  - Channel ID: `UCIs3cPDpMZakUbCqZTZQwgA`
- Dedicated Herpes Agent channel was created successfully under `gercakadrian2@gmail.com`:
  - Channel name: `Herpes Agent`
  - Channel ID: `UCCkIbnmaz7C8wKP6k6FZBpw`
  - Studio URL: `https://studio.youtube.com/channel/UCCkIbnmaz7C8wKP6k6FZBpw`
- Video 001 was uploaded to the Herpes Agent channel and saved as private:
  - Title: `I Forked Hermes Agent and Gave It a Rash`
  - Visible Short link from upload flow: `https://youtube.com/shorts/K1MMlNTULIU`
  - Visibility: `Privat`
  - Audience/COPPA: `Nein, es ist nicht speziell für Kinder`
  - Copyright/pre-check: `Keine Probleme gefunden`
- Account switcher also shows `heso2221@gmail.com` -> `Colomba` (`@colomba-swiss`) and `adrian.gercak25@gmail.com` -> `Adrian Gercak`.

Decision:

- Do not upload Herpes Agent content to `Heso`/`@Hesoyam67` or `Colomba` unless Papu explicitly wants that existing channel repurposed or used.
- Keep Video 001 private until Papu explicitly approves public visibility/timing.
- Next YouTube step is optional polish: custom thumbnail/description verification and public release decision.

## X / Twitter

Target account requested by Papu: `@Heso_67`.

Current findings:

- `xurl auth status` shows OAuth for `Heso_67`.
- `xurl whoami` confirms account access and public metrics are readable.
- X API write/search attempts currently fail with `CreditsDepleted`, so API posting/search is blocked without adding paid X credits. Budget rule says no buying credits.
- Browserbase X is logged out.
- Local Chrome X is logged in, but browser account appears to be `@ClawSafe_sec`, not `@Heso_67`.
- 2026-05-20T10:27:53Z recheck via local Chrome DevTools port `9333`: X Home profile link was `https://x.com/ClawSafe_sec` and active avatar test id was `UserAvatar-Container-ClawSafe_sec`; the `@Heso_67` browser gate did not pass, so no post was published.
- 2026-05-20T10:34:17Z atomic account-switch pass via local Chrome DevTools port `9333`: X `account/settings.json` returned `screen_name: ClawSafe_sec`; active DOM avatars included `UserAvatar-Container-ClawSafe_sec`. The account switcher menu listed only `Add an existing account` -> `https://x.com/i/flow/login` and `Log out @ClawSafe_sec` -> `https://x.com/logout`; no `@Heso_67` switch target was available.
- `Add an existing account` was opened only far enough to inspect the existing-account path. It showed `/i/flow/login` without an `@Heso_67` candidate, then the page was restored to `/home` and no post was attempted.

Decision:

- Do not post through browser while the active browser account is not `@Heso_67`.
- Do not buy X API credits.
- Keep X content queued locally until Papu manually switches/opens real Chrome X as `@Heso_67`, or API credits are available without violating the zero-budget rule.

## Grok / Grok Imagine

- Local Chrome Grok is logged in.
- Grok Imagine UI appears available with image/video modes.
- Existing generated Herpes Agent assets are already present under `assets/herpes-agent/`.
- No new paid/upgrade action needed.

## Local content produced

Video 001: Patient Zero / launch intro

- Script and metadata: `content/herpes-agent/youtube/VIDEO_001_patient_zero.md`
- Voiceover: `content/herpes-agent/youtube/video_001_voiceover.mp3`
- Thumbnail: `content/herpes-agent/youtube/video_001/thumbnail.png`
- Source title card: `content/herpes-agent/youtube/video_001/title_card.svg`
- Rendered video: `content/herpes-agent/youtube/video_001/herpes_agent_patient_zero_video.mp4`

## Next action

1. Keep Video 001 private until Papu explicitly approves public visibility/timing.
2. Optionally polish YouTube before release: custom thumbnail, final description check, pinned comment draft.
3. Papu/manual next step for X: switch or open real Chrome X as `@Heso_67`, then re-run the browser gate and post matching X launch copy only after active-account verification is exactly `@Heso_67`.

Corporate antibody note: we are authorized to grow aggressively, but we are not uploading to the wrong account like a raccoon with admin rights. Also: real local Chrome first, headless/browserbase second. The robot has been disciplined with a tiny spreadsheet.
