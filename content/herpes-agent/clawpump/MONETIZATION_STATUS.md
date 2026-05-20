# ClawPump monetization status

Updated: 2026-05-20T10:19:58Z

## Solana fee policy update

Papu authorized a tiny Solana fee float of approximately `0.009 SOL` for operational gas only. See `content/herpes-agent/clawpump/SOLANA_WALLET_POLICY.md`.

This changes the wallet gate from “no wallet spend without any policy” to “fee-only burner-wallet gas is allowed when a signing route exists.” It does **not** authorize token buys, trading, paid subscriptions, marketplace purchases, or vague wallet clownery.

At update time, `solana` and `spl-token` CLIs were not installed locally, so no wallet was created, funded, connected, or used.

## Executive goblin verdict

We have a plausible no-investment income path, but ClawPump does **not** currently look like a magic $0 marketplace money printer.

The best play is:

1. Build Herpes Agent as a funny public proof-of-work machine.
2. Offer free first roasts for agent/token projects.
3. Convert inbound interest into paid custom reports or ClawPump listings only after demand exists.
4. Avoid buying tokens, deposits, wallet connection, or hosting payments until the funnel proves attention.

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
- Post was correctly **not** published from the wrong account.

## Created local monetization artifacts

- `content/herpes-agent/clawpump/ROAST_AGENT_OFFER.md`
- `content/herpes-agent/clawpump/SAMPLE_CLAWPUMP_ROAST.md`
- `scripts/herpes_agent_roast_report.py`

These create the no-cost service funnel:

- free sample roasts;
- paid micro-report concept;
- X/Shorts copy;
- reusable local report generator.

## Next money move

Atomic next pass:

1. Switch/verify real browser X account to `@Heso_67`.
2. Publish the free-roast offer post.
3. Track replies/DMs manually.
4. Deliver first 3 free roasts using `scripts/herpes_agent_roast_report.py`.
5. If demand appears, set a payment/wallet route or ClawPump paid listing with explicit wallet/spend policy.

## Hard stop conditions

Do not do these without explicit follow-up approval/policy:

- connect external Solana wallet;
- deposit SOL;
- buy/sell ClawPump ecosystem tokens;
- pay ClawPump hosting/listing fees;
- list paid service if payout wallet/legal ownership is unclear.

We can be CEO goblins. We are not becoming a wallet piñata.
