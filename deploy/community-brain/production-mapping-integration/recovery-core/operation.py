"""Durable, non-replayable synthetic operation core. No production executor.

The caller owns writer exclusion. SIGKILL leaves a readable uncertain intent;
SIGTERM/deadline unwinds the caller's fences. Never repairs holds or retries work.
"""
import contextlib
import fcntl
import json
import math
import os
from pathlib import Path
import signal
import time
import recovery as r


class Interrupted(RuntimeError):
    pass


def readback(directory, spec):
    directory = r.no_links(directory)
    intent = json.loads(r.stable_bytes(directory/'intent.json'))
    if intent['spec_sha256'] != r.sha(r.encode(spec)):
        raise ValueError('operation binding mismatch')
    fd = os.open(directory/'owner.lock', os.O_RDWR | os.O_NOFOLLOW)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return {'state': 'running', 'replay_allowed': False}
        terminal = directory/'terminal.json'
        if terminal.exists():
            value = json.loads(r.stable_bytes(terminal))
            if value['spec_sha256'] != intent['spec_sha256']:
                raise ValueError('terminal binding mismatch')
            return value
        return {'state': 'uncertain', 'replay_allowed': False}
    finally:
        os.close(fd)


@contextlib.contextmanager
def deadline(seconds):
    if signal.getitimer(signal.ITIMER_REAL) != (0.0, 0.0):
        raise ValueError('existing alarm refused')
    old = {s: signal.getsignal(s) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGALRM)}
    def interrupt(signum, frame):
        raise Interrupted('deadline' if signum == signal.SIGALRM else 'signal')
    try:
        for s in old:
            signal.signal(s, interrupt)
        signal.setitimer(signal.ITIMER_REAL, seconds)
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        for s, handler in old.items():
            signal.signal(s, handler)


def run(directory, spec, action):
    """Run once under existing locks; callbacks must not spawn unmanaged work.

    This core has no remote/process cancellation guarantee and is NOT a bounded
    production maintenance controller. SSH and DB-fence loss need integration.
    """
    if spec.get('scope') != 'synthetic-development':
        raise ValueError('production execution disabled')
    now = time.time()
    end, limit = spec['deadline_epoch'], spec['max_seconds']
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v)
           for v in (end, limit)) or not 0 < limit <= 7200 or end <= now:
        raise ValueError('invalid or expired deadline')
    directory = r.no_links(directory)
    # Exclusive creation is the replay barrier, even after a process dies.
    directory.mkdir(mode=0o700)
    r.write_new(directory/'owner.lock', b'')
    fd = os.open(directory/'owner.lock', os.O_RDWR | os.O_NOFOLLOW)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        binding = r.sha(r.encode(spec))
        r.write_new(directory/'intent.json', r.encode({
            'schema': 'cbm.capture-operation/1', 'spec_sha256': binding,
            'started_epoch': now, 'deadline_epoch': min(end, now + limit),
            'scope': spec['scope']}))
        terminal = {'spec_sha256': binding, 'replay_allowed': False,
                    'production_qualified': False}
        try:
            with deadline(min(end - time.time(), limit)):
                with r.quiet(spec['locks'], spec['holds']):
                    result = action()
                if time.time() >= end or time.time() - now >= limit:
                    raise Interrupted('deadline')
            terminal.update(state='completed', result=result)
        except BaseException as exc:
            # Exception messages may contain private data; record only type.
            terminal.update(state='uncertain', error_type=type(exc).__name__)
            r.write_new(directory/'terminal.json', r.encode(terminal))
            raise
        r.write_new(directory/'terminal.json', r.encode(terminal))
        return terminal
    finally:
        os.close(fd)
