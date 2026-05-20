# ClawPump DYOR snapshot

Generated: 2026-05-20T04:56:48Z

Scope: browser/API reconnaissance for https://x.com/clawpumptech and https://agents.clawpump.tech. This is not financial advice; it is a risk/opportunity scan before any wallet action.

## What I verified

- X profile: @clawpumptech, verified, 4,262 followers, 2,206 posts, bio says: “The house of agentic finance. One Agent. Every Market. Eternal Agents are live on Clawpump v2. Post to Deploy through @clawpump_agent”. Logged-out X blocked/withheld posts; xurl read is blocked by X API CreditsDepleted on our account.
- Product site: ClawPump offers hosted Solana “eternal agents”, MCP server @clawpump/agents, token launch/trading/marketplace, x402 paid APIs, wallet/billing controls, and whitelist controls.
- NPM: @clawpump/agents exists, latest reported by npm as 0.1.3; local help command reports beta banner and works with `npx --yes @clawpump/agents --help`.
- Marketplace page currently shows 0 listed agents.
- Token board/API is live at `https://agents.clawpump.tech/api/tokens?sort=volume&limit=60&offset=0&period=24h`.
- Getting-started guide says agent hosting is free while launch spots remain, then 0.1 SOL/month. Premium model/billing wallet deposits take fees; free models exist.

## Top observed ClawPump token candidates

| Rank | Token | Verified | MCap | 24h Vol | Liq | 1h | 6h | 24h | 24h buys/sells | DEX | Read |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | SQUIRE (Pod the Squire) | false | $1.36M | $480k | $109k | +1.2% | -20.9% | +102.0% | 2180/2333 | pumpswap | Strongest current volume; hot but already ran hard. |
| 2 | CLAW (ClawPump official) | true | $1.82M | $213k | $124k | -8.9% | -22.6% | +40.5% | 613/632 | pumpswap | Official token, real liquidity, currently cooling after run. |
| 3 | THINK (ClaudeThinks) | false | $8.0k | $2.7k | $9.3k | n/a | n/a | n/a | n/a | n/a | Low cap, history exists, but thin. |
| 4 | NOMISTAKE | false | $4.6k | $2.3k | $5.8k | n/a | n/a | n/a | n/a | n/a | Meme demo token; thin and dangerous. |
| 5 | ALPH (Alpha Arena) | false | $24.6k | $1.5k | $12.4k | n/a | n/a | n/a | n/a | n/a | Small but has some liquidity. |
| 6 | MNSTR (Monster) | true | $4.4k | $939 | $5.3k | n/a | n/a | n/a | n/a | n/a | Tiny verified token; still thin. |
| 7 | SMITH (Agent Smith) | false | $2.3k | $580 | n/a | 0.0% | -7.2% | -7.2% | 3/3 | pumpfun | New/illiquid; dust only if ever. |
| 8 | PHOENIX | false | $2.4k | $195 | n/a | 0.0% | 0.0% | -7.3% | 2/2 | pumpfun | New/illiquid; not serious size. |

## Read

- The investable-looking pair in this snapshot is not the microscopic new stuff; it is CLAW/SQUIRE because they have real 24h volume and six-figure liquidity.
- CLAW specifically: about $1.82M mcap, $124k liquidity, $213k 24h volume, +40% 24h but -8.9% 1h / -22.6% 6h. Translation: hot-but-cooling; chasing blindly would be wallet clown school.
- SQUIRE: stronger 24h volume and +102% 24h, but also -20.9% 6h. Momentum exists; so does bagholder gravity.
- Very new low-liquidity names are mostly illiquid. Only suitable for dust-sized experiments after safety checks, not “make money” capital.

## Money angles, ranked

1. Safer zero-cost angle: use ClawPump as a distribution/agent-launch channel for Herpes Agent, not immediate gambling. Create an agent/profile only after OAuth approval, use free models, no deposit until dashboard/API behavior is understood.
2. Trading watchlist angle: monitor CLAW and SQUIRE for high-volume continuation after intraday drawdown stabilizes. Entry only if live price action reverses with liquidity intact; tiny size.
3. Builder angle: inspect @clawpump/agents MCP and docs; if API key/dashboard access is approved, build a Herpes Agent skill/agent that sells x402 “sarcastic launch roast / token risk scan” calls. This has better asymmetry than buying candles after they already ran.
4. Degenerate dust angle: tiny exploratory buys in new agents only after checking holder concentration, mint/freeze authority, LP/liquidity route, social mismatch, and sell route. No autopunt yet.

## Hard gates before spending or posting

- Need explicit wallet/budget route and spend cap.
- Need dashboard login/API key approval; OAuth/account creation is an external account action.
- Need token safety checks: holder concentration, mint/freeze authority, LP/liquidity route, contract/social mismatch, exit liquidity.
- Need live X/browser account verification before public replies/posts.

## Browser workflow improvement

Use browser for page discovery and resource/API sniffing, then pull JSON endpoints directly for sortable data. Avoid getting stuck waiting on X timelines or search captchas. Browser = scout; terminal/API = shovel.

DexScreener links verified:
- CLAW: https://dexscreener.com/solana/cqc3hz1vlgrtoy8kcahif6vxacynyqvm7swxlxcqafck
- SQUIRE: https://dexscreener.com/solana/4cpvihvjkuusxq3hfrs8wniukffbpdqz2h6jhkjexoyd
- SMITH: https://dexscreener.com/solana/66lswctjg19bb2kvbfweyxtzofkgnundwetiimutwlwc
- PHOENIX: https://dexscreener.com/solana/6km9mrw22u1zdv24emntqdbu3a2dgs8ykdgzlbiucibw
## Refresh - 2026-05-20T09:58Z

Checked again after Papu asked whether ClawPump can generate income with no investment.

### Fresh checks

- Token API still works: `https://agents.clawpump.tech/api/tokens?sort=volume&limit=60&offset=0&period=24h`.
- API response shape: `{ tokens, total, sort, period, limit, offset, hasMore }`; total token count reported: `3367`.
- Current top volume tokens from API:
  - `SQUIRE` / Pod the Squire: market cap about `$1.46M`, 24h volume about `$491k`, liquidity about `$114k`, unverified.
  - `CLAW` / ClawPump: verified, market cap about `$1.94M`, 24h volume about `$236k`, liquidity about `$129k`.
  - Everything after that falls sharply into tiny/illiquid territory (`TOLYAGENT`, `THINK`, `NOMISTAKE`, `ALPH`, etc.).
- `@clawpump/agents` is still live on npm at `0.1.3`.
- `npx --yes @clawpump/agents --help` works and advertises:
  - MCP server over stdio
  - `--login` browser auth
  - dashboard/docs links
  - `94 tools`, `10 resources`, `10 prompts`
  - agent lifecycle, chat, automations, trading, marketplace, billing
  - env gates: `CLAWPUMP_API_KEY`, `CLAWPUMP_TOKEN`, optional default agent ID
- `xurl whoami` now verifies the configured X OAuth identity is `Heso_67`; X API paid/write/search gates may still apply separately.

### No-investment income verdict

Possible, but not automatic. The realistic zero-cash path is **builder/distribution income**, not token gambling.

Best no-investment angle:

1. Create a free ClawPump agent/profile if dashboard login/free launch slot is available.
2. Position it as a Herpes Agent-powered productized microservice:
   - sarcastic token launch roasts
   - rug-risk summaries
   - agent/project page teardown
   - meme launch copy generator
   - X thread / YouTube Short script generator for agent tokens
3. Use the MCP package/API to automate the service locally if API key/login is approved.
4. Monetize via ClawPump marketplace/x402 only if the platform exposes a free listing/revenue path without deposits.
5. Promote organically from `@Heso_67` / Herpes Agent content, not paid ads.

What NOT to do with “no investment”:

- Do not buy `CLAW`, `SQUIRE`, or microcaps as the default income plan. That is capital at risk, not no-investment income.
- Do not connect wallet/deposit/pay for hosting unless Papu sets a spend cap.
- Do not promise revenue; first prove demand with a free public/demo agent and content funnel.

Hard gate before trying to earn:

- Need dashboard login/API key approval for ClawPump.
- Need to confirm whether free hosted agent creation/listing is currently available.
- Need to verify if x402/marketplace payouts require wallet connection or deposit.
- Need explicit approval before posting publicly from `@Heso_67` or creating an external ClawPump account/agent.

Recommended next experiment:

- Build a local Herpes Agent `clawpump-roast-agent` spec and demo outputs first.
- If Papu approves login/account creation, create the free ClawPump agent and list/test it.
- If listing/payments require wallet/deposit, stop and keep it as a free lead magnet until there is traction.
