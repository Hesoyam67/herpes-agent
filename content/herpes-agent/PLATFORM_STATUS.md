# Herpes Agent platform ops status

Generated: 2026-05-20

This file tracks what the agent can actually do right now without pretending the internet is a vending machine that accepts vibes.

## YouTube

Target account requested by Papu: `gercakadrian2@gmail.com`.

Current browser findings:

- Browserbase/headless sessions are not reliable for this project because Papu already has real Chrome profiles logged in. Lesson learned: inspect real local Chrome first, then use Browserbase only for public/logged-out research.
- Local Chrome profile `Default` and `Profile 2` both contain non-secret account hints for `gercakadrian2@gmail.com`; `Profile 2` lists it first.
- Real local Chrome / Adrian profile confirms target Google account `gercakadrian2@gmail.com` is accessible.
- YouTube Studio under `gercakadrian2@gmail.com` currently opens channel:
  - Channel name: `Heso`
  - Handle: `@Hesoyam67`
  - Channel URL: `https://www.youtube.com/@Hesoyam67`
  - Channel ID: `UCIs3cPDpMZakUbCqZTZQwgA`
- Account switcher also shows `heso2221@gmail.com` -> `Colomba` (`@colomba-swiss`) and `adrian.gercak25@gmail.com` -> `Adrian Gercak`.
- YouTube create-channel UI is available for a new Brand Account managed by `gercakadrian2@gmail.com`; no payment/phone/password/2FA gate was observed before the last automation limit.
- Upload UI is reachable for existing channel `Heso`, but no Herpes Agent channel has been created/selected yet.

Decision:

- Do not upload Herpes Agent content to `Heso`/`@Hesoyam67` or `Colomba` unless Papu explicitly wants that existing channel repurposed or used.
- Prefer creating/selecting a dedicated `Herpes Agent` Brand/channel under `gercakadrian2@gmail.com`, then upload Video 001 as private/unlisted first.
- Continue producing local-ready video assets and metadata so upload is one click once the correct channel/account is active.

## X / Twitter

Target account requested by Papu: `@Heso_67`.

Current findings:

- `xurl auth status` shows OAuth for `Heso_67`.
- `xurl whoami` confirms account access and public metrics are readable.
- X API write/search attempts currently fail with `CreditsDepleted`, so API posting/search is blocked without adding paid X credits. Budget rule says no buying credits.
- Browserbase X is logged out.
- Local Chrome X is logged in, but browser account appears to be `@ClawSafe_sec`, not `@Heso_67`.

Decision:

- Do not post through browser while the active browser account is not `@Heso_67`.
- Do not buy X API credits.
- Keep X content queued locally until either browser is switched to `@Heso_67` or API credits are available without violating the zero-budget rule.

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

1. Create/select a dedicated `Herpes Agent` Brand/channel under `gercakadrian2@gmail.com` using real local Chrome Profile 2 / Adrian.
2. Upload Video 001 as private/unlisted first, verify metadata/thumbnail, then publish only when channel identity is correct and visibility is intentional.
3. Re-verify browser X active account; post matching X launch copy only from `@Heso_67`.

Corporate antibody note: we are authorized to grow aggressively, but we are not uploading to the wrong account like a raccoon with admin rights. Also: real local Chrome first, headless/browserbase second. The robot has been disciplined with a tiny spreadsheet.
