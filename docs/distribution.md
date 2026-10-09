# Distribution and listing notes

Status recorded October 9, 2026. Recheck before relying on it.

| Surface | Recorded status |
| --- | --- |
| Official MCP Registry | Version 1.0.3 published under `io.github.no-fait/infinite-audience` |
| GitHub MCP directory | [Onboarding requested](https://github.com/github/github-mcp-server/discussions/1257#discussioncomment-18836640); inclusion not confirmed |
| OpenAI | Submission made; approval/public visibility not asserted |
| Anthropic | Submission made; approval/public visibility not asserted |
| Antigravity Marketplace | Interest form drafted, not submitted; package delivery and MCP Store coverage require confirmation |
| Gemini CLI gallery | Extension manifest prepared; gallery discovery topic not yet added |
| Cursor Marketplace | Deferred; direct connection example available |

One repository supplies shared documentation and client-specific manifests. Each marketplace retains its own submission, eligibility, review, and update rules. Neither creating this repository nor installing directly proves approval in a marketplace.

`server.json` is copied from the platform's maintained MCP Registry manifest. Its version is the official server listing version. `gemini-extension.json` version is the configuration distribution version. Changes to package documentation do not require inventing a new hosted server release or republishing an immutable registry version.

Before updating registry metadata, verify the current [official Registry entry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.no-fait%2Finfinite-audience/versions/latest), check the source manifest, and review the proposed public diff. Keep backend implementation and internal submission credentials outside this repository.

Publishing paths: [Antigravity intake](https://forms.gle/2EX5RFYPoJe1UgxR9), [Gemini CLI releases/gallery](https://geminicli.com/docs/extensions/releasing/), [Cursor publishing](https://cursor.com/docs/reference/plugins).
