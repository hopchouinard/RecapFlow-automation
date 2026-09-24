"""Install the VM108 QA stack and bounded processing timer."""

import os
from pathlib import Path
import socket
import subprocess

from launch import SOURCE

UNIT = Path('/etc/systemd/system')
PYTHON = '/usr/bin/python3'


def write(name, body):
    path = UNIT / name
    if path.exists() and path.read_text() != body:
        raise FileExistsError(f'existing {name} differs; review before replacement')
    if not path.exists():
        with path.open('x') as stream:
            os.fchmod(stream.fileno(), 0o644)
            stream.write(body)
            stream.flush()
            os.fsync(stream.fileno())


def install():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    qa = SOURCE / 'qa'
    write('community-brain-dev-qa-stack.service', f'''[Unit]
Description=Community Brain VM108 QA stack
Requires=docker.service
After=docker.service network-online.target
Wants=network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart={PYTHON} {qa / 'launch.py'} up -d webui
TimeoutStartSec=300

[Install]
WantedBy=multi-user.target
''')
    write('community-brain-dev-qa-runner.service', f'''[Unit]
Description=Community Brain VM108 QA processing tick
Requires=community-brain-dev-qa-stack.service
After=community-brain-dev-qa-stack.service

[Service]
Type=oneshot
ExecStart={PYTHON} {qa / 'runner.py'}
TimeoutStartSec=2400
''')
    write('community-brain-dev-qa-runner.timer', '''[Unit]
Description=Community Brain VM108 QA processing schedule

[Timer]
OnBootSec=45s
OnUnitInactiveSec=30s
Persistent=true
Unit=community-brain-dev-qa-runner.service

[Install]
WantedBy=timers.target
''')
    subprocess.run(['systemctl', 'daemon-reload'], check=True)
    subprocess.run(['systemctl', 'enable', '--now', 'community-brain-dev-qa-stack.service'], check=True)
    subprocess.run(['systemctl', 'enable', '--now', 'community-brain-dev-qa-runner.timer'], check=True)
    print('VM108 QA units enabled')


if __name__ == '__main__':
    install()
