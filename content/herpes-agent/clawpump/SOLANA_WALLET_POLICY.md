# Solana wallet / fee policy

Updated: 2026-05-20T10:19:58Z

## Current authorization

Papu authorized sending a tiny amount of SOL, approximately `0.009 SOL`, to a dedicated Solana wallet so Herpes Agent can cover operational Solana fees if a ClawPump/Solana action needs gas.

This is **not** a general trading bankroll. It is mosquito gas.

## Allowed use

The `0.009 SOL` fee float may be used only for:

- network transaction fees;
- wallet/account setup transactions required to save or verify an external Solana wallet;
- tiny operational gas for a specific Herpes Agent / ClawPump listing or demo action that has already passed identity and safety gates.

## Not allowed without explicit fresh approval

Do not use this fee float for:

- buying tokens;
- speculative trading;
- liquidity provision;
- paid hosting/monthly subscriptions;
- marketplace purchases;
- tips/donations;
- any irreversible action where the active wallet, destination, or purpose is unclear.

## Wallet custody rule

Preferred setup:

1. Use a dedicated burner Solana wallet.
2. Keep only the small approved fee amount on it.
3. Store signing access locally only if Papu intentionally wants this agent environment to operate that burner wallet.
4. Never paste or commit private keys, seed phrases, `.json` keypairs, or wallet secrets into the repo, chat, memory files, issues, or docs.

## Current machine state

At the time this policy was written, Solana CLI tools were not installed on this machine (`solana` and `spl-token` were not found in PATH), so no wallet was created, connected, funded, or used.

## Practical implication

The previous hard gate “no wallet spend without explicit wallet policy” is now narrowed:

- tiny fee use up to about `0.009 SOL` is allowed if a suitable burner wallet/signing route exists;
- all non-fee spending remains blocked;
- public posts, paid listings, token buys, and real marketplace actions still require their own normal safety/identity gates.
