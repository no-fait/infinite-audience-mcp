#!/usr/bin/env python3
"""Prepare a LobeHub owner declaration from canonical metadata and live public MCP discovery.

Only reads public protocol metadata; never authenticates, calls tools, or publishes.
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True, type=Path,
                        help='New staging directory outside this repository')
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if output == ROOT or ROOT in output.parents or output.exists():
        raise SystemExit('Use a new staging directory outside this repository')
    subprocess.run([sys.executable, str(ROOT / 'scripts/sync-listing-assets.py'), '--check'], check=True)
    metadata = json.loads((ROOT / 'lhm.plugin.json').read_text())
    with tempfile.TemporaryDirectory(prefix='ia-lobehub-discovery-') as staging:
        directory = Path(staging)
        # MCP server info need not include a description. Supply canonical fallback metadata.
        (directory / 'package.json').write_text(json.dumps({
            'name': metadata['identifier'], 'description': metadata['description'],
            'version': metadata['version'],
        }))
        subprocess.run([
            'npx', '--yes', '@lobehub/market-cli@0.0.46', 'plugin', 'init',
            '--url', metadata['cloudEndpoint'], '--dir', str(directory),
        ], check=True, timeout=120)
        discovered = json.loads((directory / 'lhm.plugin.json').read_text())
    if discovered.get('cloudEndpoint') != metadata['cloudEndpoint']:
        raise SystemExit('Discovered endpoint differs from canonical metadata')
    capabilities = {}
    for key in ('tools', 'resources', 'prompts'):
        value = discovered.get(key)
        if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
            raise SystemExit(f'Invalid discovery result: {key}')
        capabilities[key] = value
    names = [tool.get('name') for tool in capabilities['tools']]
    if not names or any(not isinstance(name, str) or not name for name in names) or len(set(names)) != len(names):
        raise SystemExit('Expected nonempty, uniquely named public tools')
    output.mkdir(parents=True)
    manifest = output / 'lhm.plugin.json'
    manifest.write_text(json.dumps({**metadata, **capabilities}, indent=2) + '\n')
    print(f'Prepared {len(names)} live public tool definitions in {manifest}')
    print('Review this declaration, then use the official CLI to publish/update it.')


if __name__ == '__main__':
    main()
