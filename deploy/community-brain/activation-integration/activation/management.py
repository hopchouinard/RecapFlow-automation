"""Mac scheduler mutex + existing SSH transport, without a nested quiet lease."""
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import shlex
import subprocess
import time
from uuid import uuid4

SCHEDULER = Path.home()/'.local/state/community-brain-management/scheduler.lock'
_owns_mutex = False


@contextmanager
def mutex():
    global _owns_mutex
    with SCHEDULER.open('a') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        _owns_mutex = True
        try:
            yield
        finally:
            _owns_mutex = False


def unresolved(directory, *, allow_active=False):
    pointer = Path(directory)/'activation-pending.json'
    if not pointer.exists():
        return False
    intent = Path(json.loads(pointer.read_text())['intent'])
    result = intent.with_name(intent.name+'.result.json')
    if not result.exists():
        return True
    value = json.loads(result.read_text())
    if value.get('state') not in ('completed', 'reconciliation_required'):
        return True
    return not allow_active and value.get('result', {}).get('phase') == 'active'


def command(host, remote, mode, directory):
    return ['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=8',
            '-o', 'ServerAliveInterval=5', '-o', 'ServerAliveCountMax=2', host,
            shlex.join(['sudo', '-n', 'python3', '-B', remote, mode, directory])]


def readback(host, remote, directory):
    result = subprocess.run(command(host, remote, 'readback', directory),
                            capture_output=True, timeout=30)
    if result.returncode:
        raise RuntimeError('SSH readback unavailable; keep uncertainty, never replay')
    return json.loads(result.stdout)


def invoke(host, remote, directory, request, local_intent, *, lose_ssh=False):
    """Caller owns mutex. Each intent is single use, even when no response arrives."""
    path = Path(local_intent)
    if not _owns_mutex:
        raise RuntimeError('existing Mac scheduler mutex must be owned')
    if unresolved(path.parent, allow_active=True):
        raise RuntimeError('prior transport outcome unresolved; readback required')
    with path.open('x') as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump({'state': 'intended', 'remote': directory, 'request': request}, stream)
        stream.flush(); os.fsync(stream.fileno())
    pointer = path.parent/'activation-pending.json'
    temporary = pointer.with_suffix('.tmp')
    with temporary.open('x') as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump({'intent': str(path)}, stream); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, pointer)
    process = subprocess.Popen(command(host, remote, 'dispatch', directory),
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write(json.dumps(request).encode()); process.stdin.close(); process.stdin = None
    interrupted = False
    deadline = time.monotonic() + 950
    if lose_ssh:
        # Actual SSH client termination after the remote worker has started.
        for _ in range(80):
            observed = readback(host, remote, directory)
            if observed.get('started'):
                process.terminate(); interrupted = True; break
            if observed['state'] == 'completed':
                raise RuntimeError('operation finished before transport-loss injection')
            time.sleep(0.1)
        if not interrupted:
            raise RuntimeError('remote start not observed; reconcile')
    try:
        stdout, stderr = process.communicate(timeout=max(1, deadline-time.monotonic()))
    except subprocess.TimeoutExpired:
        process.kill(); process.communicate(); interrupted = True
    # Whether SSH returned success, failed or timed out, read the same operation.
    # The mutex is retained during bounded readback. No effect command is retried.
    while time.monotonic() < deadline:
        observed = readback(host, remote, directory)
        if observed['state'] in ('completed', 'reconciliation_required'):
            result = dict(observed, actual_ssh_terminated=interrupted, effect_replayed=False)
            result_path = path.with_name(path.name + '.result.json')
            with result_path.open('x') as stream:
                os.fchmod(stream.fileno(), 0o600); json.dump(result, stream, indent=2)
                stream.flush(); os.fsync(stream.fileno())
            return result
        time.sleep(1)
    raise RuntimeError('remote outcome still uncertain; retain intent, read back without dispatch')
