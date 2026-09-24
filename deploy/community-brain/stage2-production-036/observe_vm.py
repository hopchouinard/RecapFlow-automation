"""Read-only, deliberately redacted host observation. Run with python3 -B on VM109."""
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import time

ROOT = Path('/srv/community-brain')
CONTROLS = ('automation/paused', 'automation/attention.json',
            'automation/boot-state.json', 'automation/runner.lock',
            'files/.manual-worker.lock', 'files/.submission.lock')
INCUMBENT = '766a37a09d4ce16a4c69a8d3dd0634bc155de70085efb0eb6aad7d7281c528f6'


def run(*argv):
    return subprocess.run(argv, check=True, capture_output=True, timeout=12).stdout


def metadata(path):
    p = ROOT / path
    fd = os.open(p, os.O_RDONLY | os.O_NOFOLLOW)
    try:
        before = os.fstat(fd)
        if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
            raise ValueError('unsafe control: ' + path)
        digest = hashlib.sha256()
        while chunk := os.read(fd, 1048576):
            digest.update(chunk)
        after = os.fstat(fd)
        if (before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns) != (after.st_dev, after.st_ino, after.st_size, after.st_mtime_ns):
            raise ValueError('changing control: ' + path)
        return dict(sha256=digest.hexdigest(), bytes=after.st_size,
                    mode=stat.S_IMODE(after.st_mode), uid=after.st_uid,
                    gid=after.st_gid, inode=after.st_ino, device=after.st_dev)
    finally:
        os.close(fd)


def main():
    row = json.loads(run('docker', 'inspect', '--type', 'container', INCUMBENT))[0]
    fields = {k: row[k] for k in ('Id', 'Image', 'Config', 'HostConfig', 'Mounts')}
    fingerprint = hashlib.sha256((json.dumps(fields, sort_keys=True, separators=(',', ':')) + '\n').encode()).hexdigest()
    print(json.dumps(dict(schema='cbm.vm109-read-only/1', observed_at=time.time(),
        machine_id=Path('/etc/machine-id').read_text().strip(),
        state_mount=dict(path=str(ROOT), uuid=run('findmnt', '-no', 'UUID', str(ROOT)).decode().strip(),
                         filesystem=run('findmnt', '-no', 'FSTYPE', str(ROOT)).decode().strip()),
        incumbent=dict(id=row['Id'], image=row['Image'], running=row['State']['Running'],
                       restart_policy=row['HostConfig']['RestartPolicy']['Name'],
                       config_fingerprint=fingerprint),
        controls={name: metadata(name) for name in CONTROLS}), sort_keys=True))


if __name__ == '__main__':
    main()
