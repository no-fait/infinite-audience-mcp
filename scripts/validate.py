#!/usr/bin/env python3
"""Validate distribution invariants locally; never contact the hosted service."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def load(name):
    return json.loads((ROOT / name).read_text())


def main():
    for path in ROOT.rglob('*.json'):
        if '.git' not in path.parts:
            json.loads(path.read_text())
    server = load('server.json')
    require(server['name'] == 'io.github.no-fait/infinite-audience', 'Registry identity drift')
    require(len(server['remotes']) == 1, 'Expected one hosted remote')
    remote = server['remotes'][0]
    require(remote['type'] == 'streamable-http', 'Expected Streamable HTTP')
    endpoint = remote['url']
    require(endpoint == 'https://mcp.infiniteaudience.ai/mcp', 'Unexpected hosted endpoint')
    plugin = load('plugin.json')
    require(set(plugin) == {'name', 'description'}, 'Unexpected Antigravity metadata')
    require(plugin['name'] == 'infinite-audience', 'Plugin identity drift')
    require('billable' in plugin['description'].lower(), 'Plugin billing disclosure missing')
    configs = [
        ('mcp_config.json', {'serverUrl': endpoint}),
        ('gemini-extension.json', {'httpUrl': endpoint}),
        ('examples/cursor/mcp.json', {'url': endpoint}),
        ('examples/claude-code/.mcp.json', {'type': 'http', 'url': endpoint}),
    ]
    for name, expected in configs:
        config = load(name)
        require(config['mcpServers'] == {'infinite-audience': expected},
                f'{name}: endpoint/schema drift or unexpected credentials/trust settings')
    gemini = load('gemini-extension.json')
    require(gemini['name'] == plugin['name'], 'Extension identity drift')
    require(re.fullmatch(r'\d+\.\d+\.\d+', gemini['version']), 'Invalid extension version')
    require('billable' in gemini['description'].lower(), 'Extension billing disclosure missing')
    codex = (ROOT / 'examples/codex/config.toml').read_text()
    require(codex == f'[mcp_servers.infinite-audience]\nurl = "{endpoint}"\n',
            'Codex endpoint drift or unexpected configuration')
    require('billable' in server['description'].lower(), 'Registry billing disclosure missing')
    for path in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' not in target and not target.startswith('#'):
                require((path.parent / target.split('#')[0]).exists(),
                        f'{path.relative_to(ROOT)}: broken local link {target}')
    print('PASS: JSON, client transport schemas, endpoint/identity consistency, billing disclosures, and local links')
    print('No network or live tool calls performed. OAuth/client compatibility is not established by this check.')


if __name__ == '__main__':
    main()
