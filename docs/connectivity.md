# Client setup

All clients connect to `https://mcp.infiniteaudience.ai/mcp` using Streamable HTTP. Complete OAuth in your own account and review scopes. Do not configure an approval bypass or blanket tool trust. Merge examples with existing configuration rather than replacing unrelated servers.

## Antigravity

Install the repository as a plugin using the documented CLI path:

```sh
agy plugin install https://github.com/no-fait/infinite-audience-mcp
```

Alternatively place a copy of the plugin directory in `.agents/plugins/infinite-audience/` in a test workspace, or in `~/.gemini/config/plugins/infinite-audience/` for global use. The root `plugin.json` provides metadata and `mcp_config.json` uses `serverUrl` for the hosted endpoint. In Customizations, authenticate the server when prompted. OAuth DCR does not require a secret in this package.

Manual connection: merge the root `mcp_config.json` into the raw MCP configuration shown in Antigravity.

Sources: [plugins](https://antigravity.google/docs/plugins), [MCP](https://antigravity.google/docs/mcp).

## Gemini CLI

```sh
gemini extensions install https://github.com/no-fait/infinite-audience-mcp
```

Restart your CLI session after installing. Run `/mcp auth infinite-audience` if authentication does not start automatically, then inspect `/mcp` for connection status and available tools. The root extension manifest uses `httpUrl` for Streamable HTTP, with automatic OAuth discovery.

Sources: [extension reference](https://geminicli.com/docs/extensions/reference/), [MCP and OAuth](https://geminicli.com/docs/tools/mcp-server/).

## Claude Code

```sh
claude mcp add --transport http infinite-audience https://mcp.infiniteaudience.ai/mcp
```

Open `/mcp`, select the server, and complete sign-in. For project configuration, merge `examples/claude-code/.mcp.json` into your project's `.mcp.json`. The explicit `type: http` is required for Claude Code's JSON format.

Source: [Claude Code MCP](https://code.claude.com/docs/en/mcp).

## Claude web and desktop

For accounts/workspaces supporting custom remote connectors, add a custom connector in Claude's connector settings with the hosted endpoint and complete OAuth. This uses a remote connector, not a local stdio server in `claude_desktop_config.json`. Availability and administrator permissions depend on your account. Each user connects with their own Infinite Audience account.

Source: [Anthropic remote connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

## Codex

```sh
codex mcp add infinite-audience --url https://mcp.infiniteaudience.ai/mcp
codex mcp login infinite-audience --scopes discovery
```

Alternatively merge `examples/codex/config.toml` into `~/.codex/config.toml`, then run the login command. Local Codex configuration does not configure ChatGPT.

Source: [OpenAI MCP documentation](https://developers.openai.com/codex/mcp).

## ChatGPT

Where your account and workspace permit developer connections, enable Developer mode in the relevant security settings, add a connection through ChatGPT Plugins, and supply the hosted endpoint. Complete OAuth. Follow the current official connection guide if labels or availability differ. ChatGPT connection settings are separate from local Codex configuration.

Source: [OpenAI connection guide](https://developers.openai.com/plugins/deploy/connect-chatgpt).

## Cursor

Merge `examples/cursor/mcp.json` into `~/.cursor/mcp.json` for global setup or `.cursor/mcp.json` for project setup. Enable the server and complete OAuth from Cursor's MCP settings. Cursor uses `url`, rather than Antigravity's `serverUrl` or Gemini CLI's `httpUrl`.

This example configures a direct MCP connection to Infinite Audience.

Source: [Cursor MCP](https://cursor.com/docs/context/mcp).

## Other clients

Use the HTTPS endpoint including `/mcp`, select Streamable HTTP, and choose OAuth discovery if supported. Select only the scopes you need. A client supporting only static bearer headers cannot refresh an expired credential by itself. Consult the [Infinite Audience authentication documentation](https://docs.infiniteaudience.ai/agents/mcp/) for supported programmatic authentication; never publish credentials in a shared manifest.

For initial verification, authenticate and inspect the tool list. Tool listing does not authorize matching or delivery. Stop and obtain the relevant approval before invoking billable actions.
