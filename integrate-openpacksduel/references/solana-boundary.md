# Solana boundary reference

## Transaction preparation

An integration may request or construct an unsigned transaction. Before wallet approval,
decode and show:

- program ID and instruction action;
- duel and vault PDAs;
- signer and participant roles;
- payment mint, amount, and destination;
- provider signer, fee basis points, fee recipient, and policy hash;
- expiry and refund behavior.

Reject unexpected writable accounts, signers, programs, mints, or instruction data.

## Settlement verification

The chain cannot call an HTTP API. Provider results must be signed, domain-separated, bound
to the program ID and duel PDA, time-bounded, and replay-protected. Asset custody must match
the exact signed asset IDs before winner transfers occur atomically.

Indexed API state and MCP output are discovery surfaces. Finalized Solana program state is
the authority for deposits, refunds, fees, and settlement.
