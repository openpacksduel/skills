# Product reference

## Core model

- A duel has one creator and one opponent.
- A direct challenge commits the opponent wallet at creation.
- An open match accepts the first eligible non-creator wallet that funds it.
- Both players commit equal payment stakes and one authenticated pack per side.
- Off-chain providers supply pack inventory, opening results, and card delivery.
- On-chain settlement must verify the committed provider result and custody accounts.

## Status language

| Status | Explain as |
| --- | --- |
| `waiting` | Created but not fully funded; an opponent may still join |
| `funded` | Both payment deposits confirmed; opening may begin |
| `opening` | Provider opening is in progress; no winner is final |
| `awaiting_assets` | Results exist but card custody or delivery is incomplete |
| `settled` | Winner and transfers are finalized on-chain |
| `cancelled` | Unmatched duel cancelled under protocol rules |
| `refunded` | Deposits returned after cancellation or timeout |
| `failed` | Flow stopped; inspect refund and chain state before advising |

## Data hierarchy

1. Finalized Solana program state and transaction signatures.
2. Provider-signed result bound to the duel and valuation policy.
3. OpenPacks Duel API/indexer state.
4. Social card or user-provided screenshot.

Lower levels help discovery but do not override higher levels.
