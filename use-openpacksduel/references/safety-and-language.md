# Safety and language reference

## User action checklist

Before a user approves a wallet transaction, surface:

- action (`fund`, `cancel`, `refund`, or future `settle`);
- duel and escrow addresses;
- payment mint and integer amount;
- opponent or open-match semantics;
- fee basis points and recipient;
- expiry and refund path;
- program ID.

If any value is missing, do not tell the user the transaction is safe.

## Promotional copy

Good:

- “Two packs enter. The higher verified pull wins the duel.”
- “Challenge a wallet or join open matchmaking.”
- “Wallet-signed on Solana. Verify the duel before approving.”

Avoid:

- guaranteed, guaranteed profit, investment, yield, passive income;
- risk-free, free money, sure win;
- provably fair unless the exact randomness proof is public and verified;
- on-chain when only an off-chain status or animation exists.

Do not disguise paid randomized packs as a conventional coin flip. Explain both the random
pack outcome and the value-based winner rule.
