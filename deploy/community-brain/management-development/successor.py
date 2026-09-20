"""Immutable successor descriptor/render primitives; no deployment entry point."""
import hashlib
import json
from pathlib import Path

API_IMAGE = 'sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b'
WEBUI_IMAGE = 'sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b'
DEV_ROOT = '/srv/dev-data/workspaces/cbm-management-integration-20260920-027'
DEV_HOST = 'pchouinard@10.1.30.20'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def descriptor(image_files, helpers):
    if image_files['image'] != API_IMAGE:
        raise ValueError('unapproved stabilization image')
    names = image_files['files']
    if not any('/jobs/api.py' in name for name in names) or not any('/web/dist/' in name for name in names):
        raise ValueError('missing module or UI evidence')
    return {
        'schema': 1, 'request_id': 'CBM-MANAGEMENT-INTEGRATION-20260920-027',
        'execution_scope': 'development-only', 'host': DEV_HOST, 'root': DEV_ROOT,
        'api_image': API_IMAGE, 'webui_image': WEBUI_IMAGE,
        'webui_container': 'cbm-r027-webui', 'api_container': 'cbm-r027-api',
        'retrieval_url': 'http://api:8090/retrieval/query',
        'image_files': names, 'helper_files': helpers,
        'module_source': 'pinned-image', 'frontend_source': 'pinned-image',
        'external_api_environment': DEV_ROOT + '/private/api.env',
        'external_signing_environment': DEV_ROOT + '/private/webui.env',
        'holds_root': DEV_ROOT + '/state', 'allow_hold_clearance': False,
        'production_promotion_ready': False,
    }


def validate(value):
    expected = {'schema': 1, 'execution_scope': 'development-only', 'host': DEV_HOST,
                'root': DEV_ROOT, 'api_image': API_IMAGE, 'webui_image': WEBUI_IMAGE,
                'webui_container': 'cbm-r027-webui', 'api_container': 'cbm-r027-api',
                'retrieval_url': 'http://api:8090/retrieval/query',
                'module_source': 'pinned-image', 'frontend_source': 'pinned-image',
                'external_api_environment': DEV_ROOT + '/private/api.env',
                'external_signing_environment': DEV_ROOT + '/private/webui.env',
                'holds_root': DEV_ROOT + '/state', 'allow_hold_clearance': False,
                'production_promotion_ready': False}
    if any(value.get(key) != item for key, item in expected.items()):
        raise ValueError('descriptor deviates from validated development boundary')


def render(value):
    validate(value)
    root = value['root']
    # Image-owned modules/UI cannot be shadowed by old r020 or frontend mounts.
    # Database/provider are external isolated development dependencies, not
    # supplied by this renderer. This is not a ready-to-run production Compose.
    return {'name': 'cbm-r027', 'services': {
        'api': {'container_name': value['api_container'], 'image': value['api_image'],
                'read_only': True, 'user': '10001:10001', 'cap_drop': ['ALL'],
                'security_opt': ['no-new-privileges:true'], 'tmpfs': ['/tmp'],
                'env_file': [value['external_api_environment']],
                'volumes': [root + '/state:/state'], 'mem_limit': '900m',
                'command': ['uvicorn', 'community_brain.jobs.runtime:app', '--factory',
                            '--host', '0.0.0.0', '--port', '8090', '--no-access-log']},
        'webui': {'container_name': value['webui_container'], 'image': value['webui_image'],
                  'env_file': [value['external_signing_environment']],
                  'volumes': ['webui:/app/backend/data'], 'mem_limit': '1536m',
                  'cap_drop': ['ALL'], 'security_opt': ['no-new-privileges:true']},
        }, 'networks': {'default': {'internal': True}}, 'volumes': {'webui': {}}}


def seal(directory):
    root = Path(directory)
    entries = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('packet symlink prohibited')
        if path.is_file() and path != root / 'packet-manifest.json':
            entries[str(path.relative_to(root))] = {'bytes': path.stat().st_size,
                                                  'sha256': sha(path.read_bytes())}
    (root / 'packet-manifest.json').write_text(json.dumps(entries, sort_keys=True, indent=2) + '\n')
    return sha((root / 'packet-manifest.json').read_bytes())


def verify(directory, expected_manifest):
    root = Path(directory)
    raw = (root / 'packet-manifest.json').read_bytes()
    if sha(raw) != expected_manifest:
        raise ValueError('packet manifest identity mismatch')
    entries = json.loads(raw)
    actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
              and p != root / 'packet-manifest.json'}
    if actual != set(entries) or any(p.is_symlink() for p in root.rglob('*')):
        raise ValueError('packet file set mismatch')
    for name, item in entries.items():
        path = root / name
        if path.stat().st_size != item['bytes'] or sha(path.read_bytes()) != item['sha256']:
            raise ValueError('packet member mismatch')
