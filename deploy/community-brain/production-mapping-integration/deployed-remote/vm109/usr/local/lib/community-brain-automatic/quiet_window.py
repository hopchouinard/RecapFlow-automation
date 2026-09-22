"""Fail-closed lock-holder primitive. Not installed or wired to production yet."""
import contextlib
import fcntl
import json
import os
from pathlib import Path
import select
import stat
import sys
import time
from uuid import UUID

LOCKS = ("automation/runner.lock", "files/.manual-worker.lock", "files/.submission.lock")

@contextlib.contextmanager
def quiet_window(root):
    root = Path(root)
    handles = []
    identities = {}
    try:
        for name in LOCKS:
            path = root / name
            fd = os.open(path, os.O_RDWR | os.O_NOFOLLOW)
            handles.append(fd)
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise ValueError("unsafe lock inode")
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            current = path.stat(follow_symlinks=False)
            if (current.st_dev, current.st_ino) != (info.st_dev, info.st_ino):
                raise ValueError("lock inode changed")
            identities[name] = (info.st_dev, info.st_ino)
        yield identities
    finally:
        for fd in reversed(handles):
            os.close(fd)


def serve(root, job_id, nonce, timeout=30, allow_ack=False):
    """Identity-bound lease; acknowledgment is opt-in for the reviewed consumer."""
    if str(UUID(job_id)) != job_id or len(nonce) != 64 or any(c not in "0123456789abcdef" for c in nonce):
        raise ValueError("invalid lease identity")
    with quiet_window(root) as identities:
        def reply(kind, sequence, **details):
            print(json.dumps({"kind": kind, "job_id": job_id, "nonce": nonce,
                              "sequence": sequence, "lock_inodes": identities, **details}), flush=True)
        def assert_inodes():
            for name, expected in identities.items():
                info = (Path(root) / name).stat(follow_symlinks=False)
                if (info.st_dev, info.st_ino) != expected:
                    raise ValueError("held lock inode replaced")
        reply("ready", 0)
        sequence = 0
        while True:
            ready, _, _ = select.select([sys.stdin], [], [], timeout)
            if not ready:
                raise TimeoutError("lease heartbeat expired")
            line = sys.stdin.readline()
            if not line:
                raise EOFError("lease owner disconnected")
            value = json.loads(line)
            if value.get("job_id") != job_id or value.get("nonce") != nonce or value.get("sequence") != sequence + 1:
                raise ValueError("lease identity or ordering mismatch")
            sequence += 1
            assert_inodes()
            if value.get("operation") == "release":
                reply("released", sequence)
                return
            if value.get("operation") == "ack" and allow_ack:
                from checkpoint_acceptance import acknowledge
                result = acknowledge(root, job_id, value.get("manifest_sha256"), assert_inodes)
                reply("acknowledged", sequence, manifest_sha256=result["manifest_sha256"])
                continue
            if value.get("operation") != "ping":
                raise ValueError("unsupported lease operation")
            reply("alive", sequence)

if __name__ == "__main__":
    try:
        serve(sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), len(sys.argv) == 6 and sys.argv[5] == "ack-enabled")
    except Exception:
        print("Quiet-window lease failed; checkpoint acceptance forbidden", file=sys.stderr)
        raise SystemExit(1) from None
