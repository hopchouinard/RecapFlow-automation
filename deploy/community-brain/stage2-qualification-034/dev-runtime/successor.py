"""Immutable Request034 packets with explicit profile bindings."""
import hashlib,json
from pathlib import Path
from profiles import API_IMAGE,WEBUI_IMAGE,DEV_ROOT,DEV_HOST,profile,validate,render

def sha(raw):return hashlib.sha256(raw).hexdigest()

def descriptor(image_files,helpers,name='development',revision='packet-v1'):
    if image_files['image']!=API_IMAGE:raise ValueError('unapproved image')
    value=profile(name,revision)
    value.update(image_files=image_files['files'],helper_files=helpers)
    return value

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
