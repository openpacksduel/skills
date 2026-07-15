---
name: integrate-openpacksduel
description: Design and implement safe OpenPacks Duel integrations using the preview OpenAPI contract, read-only MCP tools, signed webhooks, and wallet-confirmed Solana transactions. Use when building pack catalogs, matchmaking clients, duel status pages, social cards, agent tools, indexers, webhook consumers, or transaction-preparation flows that interact with OpenPacks Duel.
---

# Integrate OpenPacks Duel

## Workflow

1. Read the canonical `apps/docs/openapi.yaml` from `openpacksduel/app` before designing
   endpoints or types. The preview implementation lives in `apps/api`; treat it as
   non-production until the corresponding API deployment is confirmed.
2. Choose the narrowest surface:
   - public API for application integrations;
   - MCP for agent-facing read operations;
   - Solana RPC/program state for value-bearing verification.
3. Preserve the non-custodial boundary: construct or request unsigned transactions, decode
   them for the user, and require wallet confirmation.
4. Use integer minor units, explicit currency/decimals, stable IDs, idempotency keys, and
   request correlation.
5. Verify webhook signatures over raw bytes, reject stale timestamps, and deduplicate event
   IDs before applying side effects.
6. Test failure, expiry, cancellation, refund, tie, provider timeout, and duplicate-delivery
   paths before enabling a mutation.

Read [references/api-contract.md](references/api-contract.md) for API invariants and
[references/solana-boundary.md](references/solana-boundary.md) for transaction and settlement
rules.

## MCP rules

Use the `openpacksduel` MCP server for live read tools when installed. Its current tools are
read-only. Do not add create, fund, cancel, refund, or settle tools until they can require
explicit user confirmation, authenticate the caller, display decoded transaction intent,
and return an unsigned transaction rather than acting as a wallet.

## Contract discipline

- Do not invent an endpoint, enum member, field, or status.
- Do not expose integration keys in browser code, logs, tool output, or social cards.
- Do not equate API acceptance with Solana confirmation.
- Do not use floating-point numbers for USDC or card valuations.
- Do not retry non-idempotent mutations without the same `Idempotency-Key`.
- Do not accept a webhook signature calculated from re-serialized JSON.

When the preview contract lacks a required capability, propose a versioned OpenAPI change
and review its custody, replay, and compatibility impact before implementation.
