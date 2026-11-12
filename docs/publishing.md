# Publishing the skill and MCP listing

Keep public metadata in this repository and detailed product/setup guidance in the [public docs](https://docs.infiniteaudience.ai/agents/mcp/). `server.json` is the shared metadata source; regenerate listing assets with `python3 scripts/sync-listing-assets.py` and run `python3 scripts/validate.py` before publication. Keep the platform's Registry metadata synchronized when changing shared fields.

## skills.sh

The root [SKILL.md](../SKILL.md) is installable with:

```sh
npx skills add no-fait/infinite-audience-mcp --skill infinite-audience
```

Use a temporary project and an explicit agent target to verify installation without changing a user's working setup. For a local checkout, replace the repository name with its absolute directory. Check the installed skill content and remove the temporary project afterward. After the files reach the default branch, verify installation from GitHub as well.

The [skills.sh FAQ](https://skills.sh/docs/faq) describes listing discovery through actual CLI installations and their telemetry. A local validation or a committed file does not prove that a public listing exists. Do not manufacture installation counts; verify the public page separately. Skill installation does not configure OAuth or connect the MCP server.

## LobeHub

Consult the [current official publishing guide](https://market.lobehub.com/s/publish-mcp) before publishing; CLI authentication and manifest support may change. Use the official CLI, not hand-built marketplace API requests.

```sh
npx --yes @lobehub/market-cli auth status --output json
npx --yes @lobehub/market-cli github status
```

If needed, have the publisher complete `login` and `github connect` interactively. Use a GitHub account with push access to this repository. Check `plugin list --output json` and public search for an existing listing before creating one. If an existing listing has a different identifier, reconcile that identity before publication; do not create a duplicate.

Once the reviewed files are on the default branch, prepare a fresh owner declaration outside the repository:

```sh
python3 scripts/prepare-lobehub.py --output-dir /absolute/path/to/new-lobehub-staging
```

This uses the official CLI's public MCP discovery, supplies the canonical description when MCP server info omits one, and merges live tools/resources/prompts with the generated metadata. It does not authenticate to Infinite Audience, execute tools, or publish. Review the staged JSON before proceeding. Do not check this capability snapshot into Git; regenerate it for every update so retired tools are removed and new schemas are current.

For a new listing, publish the staged declaration:

```sh
npx --yes @lobehub/market-cli plugin publish https://github.com/no-fait/infinite-audience-mcp --dir /absolute/path/to/new-lobehub-staging
```

For an already-owned listing, use `plugin update --dir /absolute/path/to/new-lobehub-staging` instead. Updating with the metadata-only [manifest](../lhm.plugin.json) is insufficient to refresh LobeHub's capability flags/tool schemas. The repository intentionally omits static tool/resource/prompt arrays: the preparation script reads the remote MCP endpoint each time. Check the actual listing and install path after repository enrichment; metadata validation alone does not establish OAuth compatibility. Confirm that the preferred method is the hosted URL and OAuth, not an inferred local binary. If the marketplace cannot represent the endpoint's OAuth requirement accurately, correct that before recommending its installer.

Use `plugin list --output json` to verify ownership and the published version, then inspect the public listing for the description, endpoint, authentication requirements, documentation, icon, and tool discovery. This repository's publication does not imply approval in other directories.
