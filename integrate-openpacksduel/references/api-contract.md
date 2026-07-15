# API contract reference

Canonical source: `https://github.com/openpacksduel/docs/blob/main/openapi.yaml`.

## Preview operations

| Operation | Intent |
| --- | --- |
| `listPacks` / `getPack` | Read duel-eligible pack definitions |
| `listDuels` / `getDuel` | Discover and inspect canonical indexed state |
| `createDuel` | Create an off-chain intent; not proof of funding |
| `prepareDuelTransaction` | Return an unsigned base64 Solana transaction |
| `getDuelSocialCard` | Return canonical share and image URLs |

## Invariants

- Mutations authenticate with a server-side bearer key.
- Mutations require `Idempotency-Key`.
- Money is `{ amount: string, currency: "USDC", decimals: 6 }`.
- `escrowAddress` and `transactionSignature` may be null before chain confirmation.
- List endpoints are cursor-paginated and bounded to 100 records.
- Error responses use `application/problem+json` and include `requestId`.

Regenerate clients from the canonical contract when possible. If maintaining handwritten
schemas, fail closed when the API response drifts.
