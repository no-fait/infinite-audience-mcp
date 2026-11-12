# Infinite Audience MCP

[Infinite Audience](https://infiniteaudience.ai) brings **Identity Resolution & Enrichment** to your AI workspace. Turn the customer data you already have into a clearer picture of the people behind it: connect records to our identity graph, receive durable, organization-scoped Person IDs for strong matches, and enrich them with the attributes you choose. Resolve identities, refresh customer intelligence, and put richer data to work through your preferred AI assistant. [Explore Identity Resolution & Enrichment →](https://docs.infiniteaudience.ai/product/identity-resolution/)

**Endpoint:** `https://mcp.infiniteaudience.ai/mcp`

**Transport:** Streamable HTTP

**Official MCP Registry identity:** `io.github.no-fait/infinite-audience`

[Full documentation](https://docs.infiniteaudience.ai/agents/mcp/) · [Support](https://infiniteaudience.ai/contact) · [Privacy](https://nofait.ai/privacy) · [Service terms](https://nofait.ai/terms)

## Authentication and usage

The server publishes its tool definitions through tokenless MCP discovery (`initialize`, `tools/list`, `ping`, and `notifications/initialized`). Every tool call requires authentication, including read-only operations. Once authenticated, a connection receives the tools its granted scopes allow. Refresh the tool list after sign-in.

You need an Infinite Audience account and the appropriate organization permissions. Use your client's OAuth sign-in; the service supports discovery, dynamic client registration, and PKCE. Tokens belong in the client's credential store, not these files. No API key or shared client secret is included.

Start with `discovery`. Add `account-read` for usage, balance, and existing top-up status. Grant `creator` only for creating, enriching, matching, or delivering data. Discovery can run backend queries or update cached state; it is not universally read-only. Some actions count toward usage under your Infinite Audience account. Review requested scopes, tool inputs, quotes where available, and each consequential action before approving it.

## Choose your client

See [client setup](docs/connectivity.md) for Antigravity, Gemini CLI, Claude Code, Claude web/desktop, Codex, ChatGPT, Cursor, and general remote MCP clients.

## Add the workflow skill

```sh
npx skills add no-fait/infinite-audience-mcp --skill infinite-audience
```

The [public skill](SKILL.md) helps an assistant discover the live schema, plan enrichment, build audiences, and prepare activation. Skill installation adds instructions; connect and authenticate the MCP server separately. The skill links to maintained public docs and uses the current tool catalog instead of embedding a copy of every tool definition.

## Reusable listing information

Use the [listing assets](docs/listing-assets.md) for canonical descriptions, icon, documentation, privacy, support, and connection links. `lhm.plugin.json` provides LobeHub-specific metadata with the hosted endpoint. Neither file contains credentials or a static copy of the tool catalog.

| File | Purpose |
| --- | --- |
| `plugin.json`, `mcp_config.json` | Antigravity plugin connecting to the hosted service |
| `gemini-extension.json` | Gemini CLI extension; install from this repository |
| `examples/claude-code/.mcp.json` | Claude Code project configuration |
| `examples/codex/config.toml` | Codex configuration fragment |
| `examples/cursor/mcp.json` | Cursor connection configuration; not a marketplace plugin |
| `server.json` | Public copy of official MCP Registry metadata |
| `SKILL.md` | Installable workflow guidance for agents |
| `lhm.plugin.json` | LobeHub Marketplace metadata generated from `server.json` |
| `docs/listing-assets.md` | Reusable public listing copy and canonical links |

These are configuration packages. No server binary, npm installation, dataset, or private platform source is distributed here. Additional vendor formats can share this repository. Vendor-specific archives can be produced if a future installer requires a different root layout.

## Maintenance

Run `python3 scripts/validate.py` to check manifest consistency without contacting the hosted service. Keep endpoint, identity, contact links, and billing disclosures aligned across formats. Do not replace format-specific field names with a single generic configuration.

`server.json` is the source for shared listing metadata. After changing it, run `python3 scripts/sync-listing-assets.py`; validation rejects stale generated assets. The LobeHub manifest version follows that metadata version and does not assert a new hosted-service deployment. Tool definitions remain discoverable from the live endpoint. See the [publishing guide](docs/publishing.md) for skills.sh and LobeHub maintenance.

Maintainers publish official Registry metadata using the manual **Publish official MCP Registry metadata** workflow on `main`, entering the version already recorded in `server.json`. The workflow validates the files, authenticates with GitHub Actions OIDC, publishes, and checks the Registry response. It does not require a personal access token and never runs automatically on a push. Keep `server.json` synchronized with the platform source before publication.

The distribution version and hosted server's registry version are separate release concepts, even when their numbers currently coincide. Publishing this repo does not update or deploy the service.

## License

The configuration and documentation in this repository are MIT licensed. This license does not grant access to the hosted service or license its datasets, trademarks, or private implementation. Hosted usage remains subject to the linked service terms.
