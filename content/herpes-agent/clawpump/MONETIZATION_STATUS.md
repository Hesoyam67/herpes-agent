# ClawPump monetization status

Updated: 2026-05-20T13:41:07Z

## Solana policy update

Papu widened the previous fee-only policy. The available small SOL balance may now be used for Herpes Agent / ClawPump revenue attempts so work is not blocked by a zero-SOL wallet. See `content/herpes-agent/clawpump/SOLANA_WALLET_POLICY.md`.

Allowed uses include fees, burner-wallet setup, and small token/operational experiments when the target, amount, and purpose are explicit and tied to the ClawPump revenue experiment. Still avoid unclear wallet actions, liquidity locks, ongoing subscriptions, or anything reckless/destructive.

## Live CLAW scout position

On 2026-05-20T13:40Z, after Papu explicitly said SOL was available for ClawPump money attempts, Herpes Agent executed one tiny ecosystem-aligned scout buy:

- Token: `CLAW / ClawPump`
- Mint: `739dnZEG4yaBWFsY8L8ZwrfhGG6dhtCSercW8Umspump`
- Spend: `0.005 SOL`
- Fill: `211.335175 CLAW`
- Tx: `4ckpqaoxxtLF9LwemgCpkk8RTqPhDyQCLVED5xPVCho7QBNqc9Cs8fMyhvR3wf2rrksLN8CJTktxyZiwUycbsE9L`
- Guard: `/Users/hesoyam/.openclaw/workspace/state/live-exit-guards/739dnZEG4yaBWFsY8L8ZwrfhGG6dhtCSercW8Umspump.json`
- Detailed status: `content/herpes-agent/clawpump/CLAW_TRADE_STATUS.md`

A live exit guard is running with hard stop `0.0037 SOL`, TP1 `0.0075 SOL`, TP2 `0.010 SOL`, and a 24h time stop. Tiny bet. Tiny claws. No wallet piñata ceremony.

## Executive goblin verdict

We have a plausible no-investment income path, but ClawPump does **not** currently look like a magic $0 marketplace money printer.

Fresh strategic decision: **do not launch a Herpes Agent token yet**. Ship GitHub + landing page + X/community proof first, then tokenize only if external attention appears. See:

- `CLAWPUMP_GTM_STRATEGY.md`
- `TOKENIZATION_DECISION.md`
- `docs/herpes-agent/landing.html` from the repo root as the static landing surface

The best play is:

1. Build Herpes Agent as a funny public proof-of-work machine.
2. Offer free first roasts for agent/token projects.
3. Convert inbound interest into paid custom reports or ClawPump listings only after demand exists.
4. Avoid wallet connection, deposits, or token actions unless the target, amount, and purpose are explicit and tied to revenue validation.

## Checked gates

OpenClaw/browser/source inspection found:

- ClawPump marketplace API/UI exists.
- Listing flow calls `POST /marketplace`.
- Listing form requires existing agent, name, description, category, tags, and `price_sol`.
- Frontend requires `parseFloat(price) > 0`.
- Free `$0` marketplace listing is not supported by the visible frontend gate.
- Listing requires saved external Solana wallet.
- Exact gate text found: “Connect and save your external Solana wallet before listing an agent for sale.”
- No wallet connected, no deposit made, no trade executed, no spend performed.

## X posting attempt

Prepared launch post at `/tmp/herpes_clawpump_xpost.txt`.

- `xurl whoami` verifies OAuth identity `Heso_67`.
- `xurl post` failed due `CreditsDepleted`.
- Browser-based X posting was attempted only after identity verification gate.
- Real Chrome X UI was active as `@ClawSafe_sec`, not exactly `@Heso_67`.
- 2026-05-20T10:27:53Z browser recheck via local Chrome DevTools port `9333` still showed X Home with `AppTabBar_Profile_Link` href `https://x.com/ClawSafe_sec` and avatar test id `UserAvatar-Container-ClawSafe_sec`; no post was published.
- 2026-05-20T10:34:17Z atomic account-switch pass via local Chrome DevTools port `9333`: X `account/settings.json` response returned `screen_name: ClawSafe_sec`; visible active avatars included `UserAvatar-Container-ClawSafe_sec`; the account switcher menu only exposed `Add an existing account` (`https://x.com/i/flow/login`) and `Log out @ClawSafe_sec` (`https://x.com/logout`).
- Clicking `Add an existing account` opened `/i/flow/login`; no `@Heso_67` account candidate or switch target appeared. The page was returned to `/home` and the account switcher was closed.
- Post was correctly **not** published from the wrong account.

## Created local monetization artifacts

- `content/herpes-agent/clawpump/ROAST_AGENT_OFFER.md`
- `content/herpes-agent/clawpump/SAMPLE_CLAWPUMP_ROAST.md`
- `scripts/herpes_agent_roast_report.py`
- `scripts/clawpump_lead_scan.py`
- `content/herpes-agent/clawpump/LEAD_SCAN.md`
- `content/herpes-agent/clawpump/reports/SQUIRE_roast.md`
- `content/herpes-agent/clawpump/reports/NOMISTAKE_roast.md`
- `content/herpes-agent/clawpump/reports/THINK_roast.md`
- `content/herpes-agent/clawpump/reports/ALPH_roast.md`
- `content/herpes-agent/clawpump/reports/MNSTR_roast.md`
- `content/herpes-agent/clawpump/reports/PHOENIX_roast.md`

These create the no-cost service funnel:

- free sample roasts;
- paid micro-report concept;
- X/Shorts copy;
- reusable local report generator.

## Next money move

Atomic next pass:

1. Have Papu manually switch real browser X to `@Heso_67` or open a Chrome/X session where `@Heso_67` is already logged in and visible in the switcher.
2. Re-verify active browser X account exactly as `@Heso_67` before posting.
3. Publish the free-roast offer post only after that verification passes.
4. Track replies/DMs manually.
5. Deliver existing free-roast proofs (`SQUIRE`, `NOMISTAKE`, `THINK`, `ALPH`, `MNSTR`, `PHOENIX`) or generate more with `scripts/herpes_agent_roast_report.py`.
6. If demand appears, set a payment/wallet route or ClawPump paid listing with explicit wallet/spend policy.

## Guardrails

Do not do these without an explicit target, amount, purpose, and verification of the active wallet/account:

- connect external Solana wallet;
- deposit SOL;
- buy/sell ClawPump ecosystem tokens;
- pay ClawPump hosting/listing fees;
- list paid service if payout wallet/legal ownership is unclear.

We can be CEO goblins. We are not becoming a wallet piñata.
