"""Durable target-host operation with independent lifetime and read-only readback.

SSH loss does not kill the controller or release its locks. Never launch a second
operation for an uncertain invocation. Read back this operation's durable result.
"""
from contextlib import ExitStack
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback
from activate import Activation, atomic, validate_plan


def execute(operation_dir):
    root = Path(operation_dir)
    request = json.loads((root / 'request.json').read_text())
    # Atomic mkdir is the at-most-once dispatch boundary, including concurrent SSH.
    (root / 'started').mkdir(mode=0o700)
    try:
        plan = validate_plan(request['plan'], request['sha256'])
        with ExitStack() as stack:
            for name in plan['locks']:
                fd = os.open(name, os.O_RDWR | os.O_NOFOLLOW)
                stack.callback(os.close, fd)
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                if (os.fstat(fd).st_dev, os.fstat(fd).st_ino) != (os.stat(name).st_dev, os.stat(name).st_ino):
                    raise ValueError('lock inode changed')
            # Recheck everything after locks, before any effect.
            plan = validate_plan(request['plan'], request['sha256'])
            result = getattr(Activation(plan, request['sha256'], request['journal']), request['operation'])()
        value = {'state': 'completed', 'result': result}
    except Exception as error:
        value = {'state': 'reconciliation_required', 'error_type': type(error).__name__,
                 'frames': [{'file': Path(f.filename).name, 'line': f.lineno}
                            for f in traceback.extract_tb(error.__traceback__)]}
    atomic(root / 'result.json', dict(value, finished_at=time.time(), request=request))


def readback(root):
    root = Path(root)
    if not root.exists():
        return {'state': 'absent'}
    if (root / 'result.json').exists():
        return json.loads((root / 'result.json').read_text())
    return {'state': 'uncertain', 'started': (root / 'started').exists(),
            'request': json.loads((root / 'request.json').read_text())}


def main():
    mode, directory = sys.argv[1:3]
    root = Path(directory)
    if mode == 'worker':
        execute(root)
        return
    if mode == 'dispatch':
        request = json.load(sys.stdin)
        plan = validate_plan(request['plan'], request['sha256'])
        if not root.is_relative_to(Path(plan['state_root']).parent / 'activation-operations'):
            raise ValueError('operation directory outside workspace')
        if Path(request['journal']).parent != root.parent.parent / 'activation-journals':
            raise ValueError('journal outside workspace')
        root.mkdir(mode=0o700)  # never overwrite or re-dispatch
        atomic(root / 'request.json', request)
        with (root / 'private.log').open('xb') as log:
            subprocess.Popen([sys.executable, '-B', __file__, 'worker', str(root)],
                             stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                             start_new_session=True, close_fds=True)
        deadline = time.monotonic() + 900
        while not (root / 'result.json').exists() and time.monotonic() < deadline:
            time.sleep(0.25)
    elif mode != 'readback':
        raise ValueError('unknown mode')
    print(json.dumps(readback(root)))


if __name__ == '__main__':
    os.umask(0o077)
    main()
