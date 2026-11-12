---
name: infinite-audience
description: Resolve and enrich customer identities, discover audience populations, build segments and audiences, and prepare activation through Infinite Audience's hosted MCP server. Use for Infinite Audience data workflows and connection setup.
---

# Infinite Audience

Help the user turn customer data into matched, enriched identities and useful audiences. Use the connected Infinite Audience MCP tools; this skill supplies workflow guidance, not an MCP connection or credentials.

## Connect and discover

The production server is `https://mcp.infiniteaudience.ai/mcp` over Streamable HTTP. Use the client's OAuth sign-in with an Infinite Audience account and organization access. Follow the [maintained connection guide](https://docs.infiniteaudience.ai/agents/mcp/) for client-specific setup. Keep credentials in the client's credential store.

Anonymous discovery exposes tool definitions, not customer data or permission to execute. All tool calls require authentication. Refresh the tool list after sign-in: the authenticated list reflects the granted scopes. Start with `discovery`; request `creator` when the user's workflow needs creation, matching, enrichment, or delivery, and `account-read` when account status is needed. Do not assume discovery tools are all read-only.

Before planning calls, inspect the currently available tool descriptions, input schemas, output schemas, and annotations. Use those live contracts and the [operating guide](https://docs.infiniteaudience.ai/developers/operating-guide/) for current limitations and recovery rules. Do not substitute remembered tool names, fields, or pricing for published metadata.

## Choose the workflow

- **Explore or size an audience:** Find relevant fields in the field catalog, including their supported operators, value types, codes, and labels. Request a focused catalog search rather than dumping the entire schema. Preview the population before saving it. If geography is required for the requested operation, ask for it rather than silently adding a location.
- **Build a reusable audience:** Discover existing objects first when the user refers to one. A segment defines a population; an audience composes segments for activation. Use IDs returned by list/search/create results, never invented names or IDs. Fetch the selected object's full definition before changing it; summary lists may omit conditions. Read `filter_groups` as the active saved definition.
- **Match and enrich customer data:** Establish the desired outcome, available identity columns, and enrichment attributes. Use the upload and mapping instructions returned by the tools. A signed upload URL is a separate destination: send only the approved file bytes with the required content type, without forwarding the MCP bearer token. Confirm the intended mappings before starting matching. A match is not guaranteed; report the returned match and quality results.
- **Prepare activation:** Confirm the audience and destination, inspect the current quote and any upper bound, and proceed within the user's authorization. Matching, enrichment, and delivery can consume organization subscription capacity. Do not treat a request to preview or quote as permission to deliver. For external destinations, confirm the intended recipient/account and data before transfer when not already specified.

## Interpret and recover

Use canonical field names and accepted values from the current catalog. Preserve coded values, numeric/string distinctions, and the documented filter-group logic. Do not introduce a `criteria` shorthand or guess normalization settings.

Distinguish an unknown count from zero and an empty page from an absent object. Follow pagination cursors when the task requires more results. Explain privacy or validation errors using their public message and correction guidance; do not invent a cause for a zero count.

Creation and delivery can be asynchronous. Keep the returned IDs. A wait timeout does not cancel the operation: inspect its status before retrying, and do not recreate the object or repeat delivery merely because the wait ended. After an uncertain mutation, inspect the existing result before taking another action. Prefer reversible archive/restore operations when offered.

Present returned estimates and capacity amounts in their documented units. Use formatted display amounts verbatim when supplied. Do not promise automatic retries, successful matching, unlimited access, or destination support that the current tools do not establish.

## Useful starting requests

- “Find the catalog fields for ZIP and state, and explain their accepted values.”
- “Show my available segments and explain the conditions for one I select.”
- “Help me plan enrichment for a CRM export; show the mapping and expected subscription capacity before starting.”
- “Prepare an audience for my chosen destination and show the quote before delivery.”

For detailed product behavior, use the [public documentation](https://docs.infiniteaudience.ai/) and the [Identity Resolution & Enrichment guide](https://docs.infiniteaudience.ai/product/identity-resolution/).
