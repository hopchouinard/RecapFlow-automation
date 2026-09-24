"""Request036 production *review* compiler. There is no execution switch here."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import tarfile
import time

HERE = Path(__file__).resolve().parent
MAPPING = HERE.parent / 'production-mapping-033'
SLOTS = json.loads((HERE.parent / 'stage2-controller-035/evidence-slots.json').read_text())
CONTROLS = ('automation/paused', 'automation/attention.json', 'automation/boot-state.json')
LOCKS = ('automation/runner.lock', 'files/.manual-worker.lock', 'files/.submission.lock')
HEX = re.compile(r'^[0-9a-f]{64}$')


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False) + '\n').encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def pinned_file(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise ValueError('missing or linked review input')
    before = path.stat()
    raw = path.read_bytes()
    after = path.stat()
    if (before.st_ino, before.st_dev, before.st_size, before.st_mtime_ns) != (after.st_ino, after.st_dev, after.st_size, after.st_mtime_ns):
        raise ValueError('changing review input')
    return raw


def compile_review(observation, source, *, now=None):
    """Bind source and current readback, while preserving every production null."""
    now = time.time() if now is None else now
    c_raw = pinned_file(MAPPING / 'production-contract.json')
    c = json.loads(c_raw)
    b_raw = pinned_file(MAPPING / 'production-runtime-bindings.json')
    b = json.loads(b_raw)
    if observation.get('schema') != 'cbm.vm109-read-only/1':
        raise ValueError('wrong observation schema')
    age = now - observation.get('observed_at', -1)
    if not 0 <= age <= 300:
        raise ValueError('VM109 observation stale or in future')
    if observation['machine_id'] != c['machine_id'] or observation['state_mount'] != c['state_mount']:
        raise ValueError('VM109 host/mount drift')
    inc = observation['incumbent']
    if inc['id'] != c['incumbent_id'] or inc['image'] != c['incumbent_image'] or inc['running'] is not True or inc['restart_policy'] != 'unless-stopped' or not HEX.fullmatch(inc['config_fingerprint']):
        raise ValueError('incumbent drift or unavailable')
    if set(observation['controls']) != set(CONTROLS + LOCKS):
        raise ValueError('control member set changed')
    for name, historic in b['controls'].items():
        live = observation['controls'][name]
        for key in ('sha256', 'mode', 'uid', 'gid', 'inode', 'device'):
            if live[key] != historic[key]:
                raise ValueError('control/lock drift: ' + name + ':' + key)
    if not re.fullmatch('[0-9a-f]{40}', source.get('commit', '')):
        raise ValueError('exact source commit required')
    for key in ('archive_sha256', 'member_manifest_sha256'):
        if not HEX.fullmatch(source.get(key, '')):
            raise ValueError('exact source ' + key + ' required')
    if source.get('archive_path') is None:
        raise ValueError('source archive path required')
    archive = pinned_file(source['archive_path'])
    manifest = pinned_file(source['member_manifest_path'])
    if sha(archive) != source['archive_sha256'] or sha(manifest) != source['member_manifest_sha256']:
        raise ValueError('source archive or member manifest drift')
    members = json.loads(manifest)
    if not isinstance(members, dict) or not members or any(not HEX.fullmatch(v) for v in members.values()):
        raise ValueError('invalid source member manifest')
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:*') as bundle:
        seen = {}
        for entry in bundle:
            if entry.isdir():
                continue
            if not entry.isfile() or entry.name.startswith('/') or '..' in Path(entry.name).parts or entry.name in seen:
                raise ValueError('unsafe source archive member')
            seen[entry.name] = sha(bundle.extractfile(entry).read())
        if seen != members:
            raise ValueError('source archive/member manifest mismatch')
    if c['production_compiler_enabled'] is not False or c['production_controller_enabled'] is not False:
        raise ValueError('historical mapping unexpectedly enabled')
    old_expiry = json.loads(pinned_file(MAPPING / 'evidence/production-expiry-metadata.json'))
    plan = dict(schema='cbm.stage2-production-review/1', scope='production-review-only',
        execution_enabled=False, stage2_complete=False,
        source=source, mapping_sha256=sha(c_raw), runtime_binding_sha256=sha(b_raw),
        host=dict(machine_id=observation['machine_id'], mount=observation['state_mount'],
                  observation_sha256=sha(canonical(observation)), observed_at=observation['observed_at']),
        incumbent=inc, controls={k: observation['controls'][k] for k in CONTROLS},
        locks={k: observation['controls'][k] for k in LOCKS},
        lock_order=list(LOCKS), mac_mutex=c['mac_mutex'],
        historical_authority_expiry=min(old_expiry['expiry_fields'].values()),
        current_authority_generation=None,
        authorities={'protected_preservation': None, 'serving': None, 'processing_resume': None},
        production_evidence={name: None for name in SLOTS},
        operation='bounded-protected-preservation-and-unchanged-serving-restore',
        private_destinations=dict(independent_restore=c['independent_restore'], offhost=c['offhost']),
        capture_id=c['capture_id'], deadline_epoch=None,
        deadlines_seconds=c['deadlines_seconds_from_admitted_start'],
        rollback_owner=c['rollback_owner'],
        retained=['original source', 'partial capture', 'partial restore', 'all checkpoints', 'attention and boot holds'],
        blockers=['historical authority expired', '21 production receipts absent',
                  'separate phase authorities absent', 'fresh deadline absent',
                  'production installer/controller not enrolled'])
    return plan


def require_executable(plan, *, now=None):
    now = time.time() if now is None else now
    if plan.get('schema') != 'cbm.stage2-production-review/1' or plan.get('scope') != 'production' or plan.get('execution_enabled') is not True:
        raise ValueError('review plan is never executable')
    if not isinstance(plan.get('deadline_epoch'), (int, float)) or plan['deadline_epoch'] <= now:
        raise ValueError('production deadline absent or expired')
    if set(plan.get('production_evidence', {})) != set(SLOTS) or any(plan['production_evidence'][s] is None for s in SLOTS):
        raise ValueError('production evidence absent')
    for phase in ('protected_preservation', 'serving', 'processing_resume'):
        authority = plan.get('authorities', {}).get(phase)
        if not isinstance(authority, dict) or authority.get('expires_at', 0) <= now:
            raise ValueError('separate authority absent or expired: ' + phase)
    raise ValueError('no enrolled production executor')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('observation')
    parser.add_argument('source')
    args = parser.parse_args()
    plan = compile_review(json.loads(pinned_file(args.observation)), json.loads(pinned_file(args.source)))
    print(canonical(plan).decode(), end='')


if __name__ == '__main__':
    main()
