"""Side-effect-bounded recovery mechanics. CLI is VM108 synthetic-only.

No daemon, worker, boot reconciliation, checkpoint acknowledgement or restart.
Callers must exclude ALL writers; cooperative locks alone do not exclude an API.
"""
import argparse
import contextlib
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import socket
import stat
import subprocess
import sys
import time

SCHEMA = 'cbm.private-recovery/1'
DEV_ROOT = Path('/srv/dev-data/workspaces/cbm-protected-restore-20260921-030')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()


def write_new(path, data, mode=0o600):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, mode)
    with os.fdopen(fd, 'wb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    directory = os.open(Path(path).parent, os.O_RDONLY)
    try: os.fsync(directory)
    finally: os.close(directory)


def no_links(path):
    path = Path(path).absolute()
    for p in [path, *path.parents]:
        if p.is_symlink():
            raise ValueError('linked path refused')
    return path


def stable_bytes(path):
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, 'rb') as f:
        before = os.fstat(f.fileno())
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise ValueError('special or hard-linked file refused')
        data = f.read()
        after = os.fstat(f.fileno())
    fields = lambda s: (s.st_dev, s.st_ino, s.st_mode, s.st_uid, s.st_gid, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    if fields(before) != fields(after) or fields(after) != fields(path.lstat()):
        raise ValueError('file changed during observation')
    return data


def extended_names(path):
    if hasattr(os, 'listxattr'):
        return os.listxattr(path, follow_symlinks=False)
    if sys.platform == 'darwin':
        result = subprocess.run(['/usr/bin/xattr','-s',str(path)], capture_output=True, timeout=10)
        if result.returncode: raise ValueError('extended metadata inspection failed')
        return result.stdout.splitlines()
    raise ValueError('extended metadata inspection unsupported')


def tree(root, sink=None):
    """Include roots/empty directories. Links must resolve within their component."""
    root = no_links(root)
    if not root.is_dir():
        raise ValueError('component must be a real directory')
    entries = []
    def visit(p):
        s = p.lstat()
        if extended_names(p):
            raise ValueError('extended metadata unsupported; retain source')
        item = dict(path=str(p.relative_to(root)), uid=s.st_uid, gid=s.st_gid,
                    mode=stat.S_IMODE(s.st_mode), mtime_ns=s.st_mtime_ns)
        if stat.S_ISLNK(s.st_mode):
            target = os.readlink(p)
            if os.path.isabs(target) or not p.resolve(strict=True).is_relative_to(root):
                raise ValueError('escaping or absolute link refused')
            item.update(kind='symlink', target=target)
        elif stat.S_ISDIR(s.st_mode):
            item['kind'] = 'directory'
        elif stat.S_ISREG(s.st_mode):
            data = stable_bytes(p)
            item.update(kind='file', bytes=len(data), sha256=sha(data))
            if sink is not None:
                dest = sink / item['sha256']
                if not dest.exists():
                    write_new(dest, data)
        else:
            raise ValueError('special file refused')
        if s.st_mode & (stat.S_ISUID | stat.S_ISGID):
            raise ValueError('privileged mode refused')
        entries.append(item)
        if item['kind'] == 'directory':
            for child in sorted(p.iterdir()):
                visit(child)
    visit(root)
    return entries


def hold_state(paths):
    result = {}
    for name in paths:
        p = no_links(name)
        s = p.stat()
        result[str(p)] = dict(sha256=sha(stable_bytes(p)), inode=s.st_ino,
                             device=s.st_dev, mode=stat.S_IMODE(s.st_mode), uid=s.st_uid, gid=s.st_gid)
    return result


@contextlib.contextmanager
def quiet(locks, holds):
    """Open EXISTING locks; never create/replace a lock or mutate a hold."""
    before = hold_state(holds)
    descriptors = []
    try:
        for name in locks:
            p = no_links(name)
            fd = os.open(p, os.O_RDWR | os.O_NOFOLLOW)
            descriptors.append(fd)
            if not stat.S_ISREG(os.fstat(fd).st_mode):
                raise ValueError('nonregular lock')
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            if (os.fstat(fd).st_dev, os.fstat(fd).st_ino) != (p.stat().st_dev, p.stat().st_ino):
                raise ValueError('lock replaced')
        yield before
        if hold_state(holds) != before:
            raise ValueError('processing hold changed')
        for name, fd in zip(locks, descriptors):
            s = Path(name).stat()
            if (s.st_dev, s.st_ino) != (os.fstat(fd).st_dev, os.fstat(fd).st_ino):
                raise ValueError('lock replaced during operation')
    finally:
        for fd in reversed(descriptors):
            os.close(fd)


def capture(components, destination, capture_id, evidence, scope='synthetic-development'):
    if scope not in ('synthetic-development','authorized-private-preservation'):
        raise ValueError('unknown preservation scope')
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{7,100}', capture_id):
        raise ValueError('invalid capture id')
    if not components or any(not re.fullmatch(r'[a-z][a-z0-9_-]*', k) for k in components):
        raise ValueError('invalid components')
    destination = no_links(destination)
    roots = {k: no_links(v) for k, v in components.items()}
    if any(a != b and (a.is_relative_to(b) or b.is_relative_to(a)) for a in roots.values() for b in roots.values()) or len(set(roots.values())) != len(roots):
        raise ValueError('overlapping source components')
    if any(destination.is_relative_to(v) or v.is_relative_to(destination) for v in roots.values()):
        raise ValueError('capture overlaps source')
    destination.mkdir(mode=0o700)
    write_new(destination/'intent.json', encode(dict(capture_id=capture_id, state='capture_started', evidence=evidence)))
    blobs = destination/'blobs'
    blobs.mkdir(mode=0o700)
    entries = {k: tree(v, blobs) for k, v in roots.items()}
    if entries != {k: tree(v) for k, v in roots.items()}:
        raise ValueError('source drift; retain incomplete attempt')
    manifest = dict(schema=SCHEMA, scope=scope, capture_id=capture_id,
                    created_at=time.time(), sources={k:str(v) for k,v in roots.items()},
                    components=entries, writer_exclusion=evidence)
    data = encode(manifest)
    write_new(destination/'manifest.json', data)
    write_new(destination/'capture-complete.json', encode(dict(manifest_sha256=sha(data))))
    return sha(data)


def validate_bundle(bundle, expected, expected_scope='synthetic-development'):
    bundle = no_links(bundle)
    if {p.name for p in bundle.iterdir()} != {'intent.json','blobs','manifest.json','capture-complete.json'}:
        raise ValueError('bundle member set mismatch')
    no_links(bundle/'blobs')
    raw = stable_bytes(bundle/'manifest.json')
    if sha(raw) != expected:
        raise ValueError('untrusted manifest digest')
    value = json.loads(raw)
    if expected_scope not in ('synthetic-development','authorized-private-preservation') or value['schema'] != SCHEMA or value['scope'] != expected_scope:
        raise ValueError('production/private execution disabled')
    if json.loads(stable_bytes(bundle/'capture-complete.json'))['manifest_sha256'] != expected:
        raise ValueError('capture incomplete')
    blobs = set()
    for name, rows in value['components'].items():
        if not re.fullmatch(r'[a-z][a-z0-9_-]*', name):
            raise ValueError('invalid component')
        paths = {}
        for row in rows:
            path = PurePosixPath(row['path'])
            if path.is_absolute() or '..' in path.parts or str(path) != row['path'] or row['path'] in paths:
                raise ValueError('unsafe or duplicate member')
            if row['kind'] not in ('file', 'directory', 'symlink') or row['mode'] & ~0o777:
                raise ValueError('unsafe member type/mode')
            paths[row['path']] = row
            if row['kind'] == 'file':
                digest = row['sha256']
                if not re.fullmatch('[0-9a-f]{64}', digest):
                    raise ValueError('invalid blob identity')
                content = stable_bytes(bundle/'blobs'/digest)
                if sha(content) != digest or len(content) != row['bytes']:
                    raise ValueError('corrupt blob')
                blobs.add(digest)
        if paths.get('.', {}).get('kind') != 'directory':
            raise ValueError('missing component root')
        for path, row in paths.items():
            if path != '.' and paths.get(str(PurePosixPath(path).parent), {}).get('kind') != 'directory':
                raise ValueError('member through link or absent parent')
            if row['kind'] == 'symlink':
                # Normalize lexically, then resolve chains against manifest only.
                seen = set()
                target = str(PurePosixPath(path).parent/row['target'])
                while True:
                    if target in seen or len(seen)>len(paths):
                        raise ValueError('cyclic link')
                    seen.add(target)
                    parts = []
                    if target.startswith('/'):
                        raise ValueError('absolute link')
                    for part in PurePosixPath(target).parts:
                        if part == '..':
                            if not parts: raise ValueError('escaping link')
                            parts.pop()
                        elif part != '.': parts.append(part)
                    target = '/'.join(parts) or '.'
                    if target not in paths: raise ValueError('dangling or traversing link')
                    t = paths[target]
                    if t['kind'] != 'symlink': break
                    target = str(PurePosixPath(target).parent/t['target'])
    if {p.name for p in (bundle/'blobs').iterdir()} != blobs:
        raise ValueError('blob set mismatch')
    return value


def restore(bundle, expected, destination, expected_scope='synthetic-development'):
    value = validate_bundle(bundle, expected, expected_scope)
    destination = no_links(destination)
    if destination == Path(bundle) or destination.is_relative_to(Path(bundle)):
        raise ValueError('restore overlaps bundle')
    if any(destination.is_relative_to(Path(p)) or Path(p).is_relative_to(destination) for p in value['sources'].values()):
        raise ValueError('restore overlaps original')
    destination.mkdir(mode=0o700)  # exclusive, partial destination never reused
    write_new(destination/'restore-intent.json', encode(dict(capture_id=value['capture_id'], manifest_sha256=expected)))
    for name, rows in value['components'].items():
        root = destination/name
        for row in sorted(rows, key=lambda r: (len(PurePosixPath(r['path']).parts), r['path'])):
            p = root/row['path']
            if row['kind'] == 'directory': p.mkdir(mode=0o700)
            elif row['kind'] == 'file': write_new(p, stable_bytes(Path(bundle)/'blobs'/row['sha256']))
            else: p.symlink_to(row['target'])
        for row in sorted(rows, key=lambda r:len(PurePosixPath(r['path']).parts), reverse=True):
            p = root/row['path']
            if os.geteuid() == 0: os.chown(p, row['uid'], row['gid'], follow_symlinks=False)
            elif (p.lstat().st_uid,p.lstat().st_gid)!=(row['uid'],row['gid']):
                raise ValueError('ownership restoration requires privileged isolated target')
            if row['kind'] != 'symlink': os.chmod(p, row['mode'])
            os.utime(p, ns=(row['mtime_ns'],row['mtime_ns']), follow_symlinks=False)
        if tree(root) != rows:
            raise ValueError('restored tree differs')
    result = dict(schema='cbm.restore-receipt/1', scope=value['scope'], capture_id=value['capture_id'],
                  manifest_sha256=expected, destination=str(destination),
                  tree_comparison='exact', components={k:sha(encode(v)) for k,v in value['components'].items()},
                  database_acceptance=None, application_acceptance=None,
                  production_qualified=False)
    write_new(destination/'restore-receipt.json', encode(result))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=['capture','restore','verify'])
    parser.add_argument('spec')
    args = parser.parse_args()
    spec = json.loads(stable_bytes(no_links(args.spec)))
    if socket.gethostname() != 'community-brain-dev' or spec.get('scope') != 'synthetic-development':
        raise ValueError('Request030 CLI is VM108 synthetic-only')
    for key in ('bundle','destination'):
        if key in spec and not no_links(spec[key]).is_relative_to(DEV_ROOT):
            raise ValueError('outside fresh Request030 workspace')
    if args.operation == 'capture':
        for p in [*spec['components'].values(),*spec['locks'],*spec['holds']]:
            if not no_links(p).is_relative_to(DEV_ROOT): raise ValueError('foreign source')
        with quiet(spec['locks'],spec['holds']) as before:
            digest=capture(spec['components'],spec['destination'],spec['capture_id'],dict(holds=before,writer_policy='fresh synthetic stopped state'))
        print(json.dumps({'manifest_sha256':digest}))
    elif args.operation == 'restore':
        print(json.dumps(restore(spec['bundle'],spec['manifest_sha256'],spec['destination'])))
    else:
        value=validate_bundle(spec['bundle'],spec['manifest_sha256'])
        print(json.dumps({'capture_id':value['capture_id'],'verified':True,'scope':value['scope']}))

if __name__ == '__main__':
    main()
