# OpenPacks Duel Agent Skills

Installable Agent Skills for explaining, using, and integrating OpenPacks Duel.

```bash
bunx skills add openpacksduel/skills --list
bunx skills add openpacksduel/skills --skill use-openpacksduel --skill integrate-openpacksduel
```

## Skills

- `use-openpacksduel` — explain the product, discover packs and duels, interpret
  status, and produce accurate share copy without implying guaranteed returns.
- `integrate-openpacksduel` — design API, webhook, MCP, and Solana transaction
  integrations against the canonical preview contract.

Both skills enforce the non-custodial boundary: agents must never request wallet
private keys, silently sign transactions, or treat an indexed API response as a
substitute for on-chain verification.

Detailed domain knowledge lives in each skill's `references/` directory so it is
loaded only when relevant.

## Related repositories

- [Developer docs](https://github.com/openpacksduel/docs)
- [MCP server](https://github.com/openpacksduel/mcp)
- [Solana escrow](https://github.com/openpacksduel/escrow)

## License

[MIT](LICENSE)
