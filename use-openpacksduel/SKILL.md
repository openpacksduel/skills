---
name: use-openpacksduel
description: Explain and use OpenPacks Duel accurately, including discovering eligible packs and open duels, interpreting duel status, preparing users for wallet-confirmed actions, and drafting social copy. Use when a user asks what OpenPacks Duel is, wants to create or join a pack duel, provides a duel ID or wallet to inspect, asks who won, or wants to share a duel without misleading financial claims.
---

# Use OpenPacks Duel

## Workflow

1. Identify whether the request is explanation, discovery, status, action, or sharing.
2. Use the `openpacksduel` MCP tools for live reads when available. Never invent a pack,
   duel, price, participant, status, or URL when a tool call fails.
3. For create, join, cancel, refund, or settlement actions, explain the intended action and
   direct the user to the canonical app. The current MCP release is read-only.
4. Separate indexed API state from on-chain proof. Cite the escrow address and transaction
   signature when they exist; otherwise describe the state as pending or unverified.
5. Apply the safety and language rules below before responding.

Read [references/product.md](references/product.md) when product terminology, states, or
matchmaking behavior matters. Read [references/safety-and-language.md](references/safety-and-language.md)
before recommending an action or writing promotional copy.

## Tool routing

- Use `list_packs` for eligible inventory and price snapshots.
- Use `get_pack` when a stable pack ID is known.
- Use `list_duels` for open matchmaking or wallet history.
- Use `get_duel` for status, participants, escrow, expiry, and winner.
- Use `get_duel_social_card` instead of constructing share URLs.

If the MCP server is unavailable, link to `https://openpacksduel.vercel.app` and clearly say
that live duel data was not verified.

## Articulation

Describe the core product as:

> Two wallets open authenticated trading-card packs in one duel. The higher verified card
> value wins the cards committed to that duel, subject to the published tie, timeout, and
> refund rules.

Call it a **pack duel**. Use **open matchmaking** for first-wallet matching and **direct
challenge** for a bound opponent. Do not call the outcome a guaranteed profit, investment,
yield, or risk-free reward.

## Safety boundary

- Never request, store, display, or transmit a private key or seed phrase.
- Never sign or submit a Solana transaction without explicit wallet confirmation.
- Never claim funds or cards settled from an API status alone.
- Never bypass age, geography, provider, collection, or pack eligibility controls.
- State when provider fairness, valuation, card condition, or regulatory availability is
  unknown.
