# Solana wallet / fee policy

Updated: 2026-05-20T10:31:00Z

## Current authorization

Papu widened the previous mosquito-gas policy: the available small SOL balance may be used for Herpes Agent / ClawPump revenue attempts so work is not blocked by a zero-SOL wallet.

This allows small, bounded actions such as fees, token buys, wallet setup, or other operational ClawPump/Solana moves when they are directly tied to the revenue experiment and the active wallet/action is clear.

## Allowed use

The small SOL balance may be used for:

- network transaction fees;
- wallet/account setup transactions required to save or verify an external Solana wallet;
- tiny operational gas for a specific Herpes Agent / ClawPump listing or demo action that has already passed identity and safety gates;
- token buys or similar small experiments only when the target, amount, and purpose are explicit and the action is not reckless/destructive.

## Still not allowed without explicit fresh approval

Do not use this balance for:

- unclear wallet actions where the active wallet, destination, or purpose is unknown;
- paid hosting/monthly subscriptions unrelated to ClawPump revenue validation;
- liquidity provision or any action that could lock funds;
- tips/donations;
- any spend that exceeds the available small SOL float or creates ongoing obligations.

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
