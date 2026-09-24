"""VM108-only automatic QA tick: one selected stage or one paired checkpoint."""

import fcntl
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tarfile
import threading
from datetime import datetime, timezone

from launch import PRIVATE, ROOT, compose, read_env

STATE = PRIVATE / 'automation'
VOLUMES = Path('/srv/dev-data/docker/volumes')
PROJECT = 'cbm-live-development'


def atomic(path, value, mode=0o600):
    path.parent.mkdir(mode=0o700, exist_ok=True)
    temporary = path.with_name('.' + path.name + '.next')
    with temporary.open('x') as stream:
        os.fchmod(stream.fileno(), mode)
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    fd = os.open(path.parent, os.O_DIRECTORY | os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def invoke(args, *, timeout=300):
    argv, env = compose(args)
    result = subprocess.run(argv, env=env, capture_output=True, text=True,
                            timeout=timeout, check=False)
    if result.returncode:
        # Deliberately retain no raw container stderr: providers may echo secrets.
        raise RuntimeError(f'QA command {args[0]} failed with exit {result.returncode}')
    return result.stdout


def scan(*args):
    lines = invoke(['scan', *args], timeout=90).splitlines()
    return json.loads(lines[-1])


def attention(reason):
    path = STATE / 'attention.json'
    if not path.exists():
        atomic(path, {'reason': reason, 'at': datetime.now(timezone.utc).isoformat()})


def checkpoints():
    result = {}
    for path in (STATE / 'checkpoints').glob('*.json'):
        try:
            value = json.loads(path.read_text())
            if value['verified'] is True and value['job_id'] == path.stem:
                result[path.stem] = 'verified'
            else:
                result[path.stem] = 'requires_review'
        except (KeyError, ValueError, OSError):
            result[path.stem] = 'requires_review'
    return result


def checkpoint(job_id):
    """Pair a PostgreSQL dump with frozen state volumes before another stage."""
    from uuid import UUID
    UUID(job_id)
    target = STATE / 'checkpoints' / job_id
    if target.exists():
        raise RuntimeError('existing checkpoint requires review')
    target.mkdir(mode=0o700, parents=True)
    lock = VOLUMES / f'{PROJECT}_files/_data/.submission.lock'
    with lock.open('a') as file_lock:
        fcntl.flock(file_lock, fcntl.LOCK_EX)
        dump = target / 'database.dump'
        with dump.open('xb') as stream:
            os.fchmod(stream.fileno(), 0o600)
            result = subprocess.run(['docker', 'exec', f'{PROJECT}-postgres-1',
                                     'pg_dump', '-U', 'cbmdev', '-Fc', 'cbm_dev'],
                                    stdout=stream, stderr=subprocess.DEVNULL,
                                    timeout=180, check=False)
            if result.returncode:
                raise RuntimeError('development DB dump failed')
            stream.flush()
            os.fsync(stream.fileno())
        with dump.open('rb') as stream:
            listing = subprocess.run(['docker', 'exec', '-i', f'{PROJECT}-postgres-1',
                                      'pg_restore', '-l'], stdin=stream,
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                     timeout=60, check=False)
            if listing.returncode:
                raise RuntimeError('development DB dump readback failed')
        nats = f'{PROJECT}-nats-1'
        try:
            subprocess.run(['docker', 'stop', '--time', '15', nats],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=30, check=True)
            with tarfile.open(target / 'state.tar.gz', 'w:gz') as archive:
                for name in ('files', 'config', 'corpus', 'jetstream'):
                    source = VOLUMES / f'{PROJECT}_{name}/_data'
                    if not source.is_dir():
                        raise RuntimeError('development state volume missing')
                    archive.add(source, arcname=name, recursive=True)
        finally:
            subprocess.run(['docker', 'start', nats], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, timeout=30, check=True)
    with tarfile.open(target / 'state.tar.gz', 'r:gz') as archive:
        if not {'files', 'config', 'corpus', 'jetstream'}.issubset(
            {member.name.split('/')[0] for member in archive.getmembers()}):
            raise RuntimeError('checkpoint volume readback incomplete')
    artifacts = {}
    for name in ('database.dump', 'state.tar.gz'):
        path = target / name
        artifacts[name] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                           'bytes': path.stat().st_size}
    manifest = {'job_id': job_id, 'verified': True,
                'created_at': datetime.now(timezone.utc).isoformat(),
                'scope': 'community-brain-dev', 'artifacts': artifacts}
    atomic(STATE / 'checkpoints' / f'{job_id}.json', manifest)
    return manifest


def tick():
    if (STATE / 'attention.json').exists():
        return 'attention_required'
    if (STATE / 'paused').exists():
        return 'paused'
    if (STATE / 'checkpoint-needed.json').exists():
        return 'awaiting_checkpoint'
    state = scan('next')
    if state['attention']:
        attention('stage_terminal_requires_review')
        return 'attention_required'
    known = checkpoints()
    for job_id in state['completed']:
        if job_id not in known:
            atomic(STATE / 'checkpoint-needed.json', {'job_id': job_id})
            checkpoint(job_id)
            (STATE / 'checkpoint-needed.json').unlink()
            return 'stage_completed'
        if known[job_id] != 'verified':
            attention('checkpoint_requires_review')
            return 'attention_required'
    item = state['next']
    if item is None:
        return 'idle'
    approved = scan('select', item['job_id'], item['stage'], str(item['generation']))
    if approved['stage_id'] != item['stage_id'] or approved['scope'] != 'community-brain-dev':
        attention('selection_mismatch')
        return 'attention_required'
    approvals = PRIVATE / 'approvals'
    approvals.mkdir(mode=0o700, exist_ok=True)
    selection_path = approvals / f"{item['job_id']}-{item['stage']}-{item['generation']}.json"
    started = selection_path.with_suffix('.started')
    if selection_path.exists() or started.exists():
        scan('stop', item['stage_id'])
        attention('selected_stage_previously_started')
        return 'attention_required'
    atomic(selection_path, approved, mode=0o644)
    atomic(started, {'stage_id': item['stage_id'],
                     'started_at': datetime.now(timezone.utc).isoformat()})
    kind = 'acquisition' if item['stage'] == 'acquisition' else 'model'
    expiry = int(read_env(PRIVATE / 'runtime.env')['CB_QA_IDENTITY_EXPIRES_AT'])
    done = threading.Event()

    def heartbeat():
        while not done.is_set():
            try:
                scan('project', 'worker_running', str(expiry),
                     json.dumps(checkpoints(), separators=(',', ':')))
            except Exception:
                # The final tick will mark attention if its own projection fails.
                pass
            done.wait(60)

    pulse = threading.Thread(target=heartbeat, daemon=True)
    pulse.start()
    try:
        invoke(['worker', kind, str(selection_path)], timeout=1800)
    except Exception:
        scan('stop', item['stage_id'])
        attention('selected_stage_failed_or_unknown')
        return 'attention_required'
    finally:
        done.set()
        pulse.join(timeout=5)
    return 'stage_completed'


def main():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    STATE.mkdir(mode=0o700, exist_ok=True)
    (STATE / 'checkpoints').mkdir(mode=0o700, exist_ok=True)
    with (STATE / 'runner.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        runtime = read_env(PRIVATE / 'runtime.env')
        expiry = int(runtime['CB_QA_IDENTITY_EXPIRES_AT'])
        if datetime.now(timezone.utc).timestamp() >= expiry:
            attention('development_service_identity_expired')
        try:
            status = tick()
        except Exception as exc:
            attention('runner_' + type(exc).__name__)
            status = 'attention_required'
        scan('project', status, str(expiry), json.dumps(checkpoints(), separators=(',', ':')))
        atomic(STATE / 'status.json', {'state': status,
                                      'checked_at': datetime.now(timezone.utc).isoformat()})
        print(json.dumps({'state': status}))


if __name__ == '__main__':
    main()
