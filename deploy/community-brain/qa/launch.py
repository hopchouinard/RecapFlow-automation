"""VM108-only launcher for the persistent QA overlay; never prints secrets."""

import os
from pathlib import Path
import shlex
import socket
import subprocess
import sys
from urllib.parse import quote

ROOT = Path('/srv/dev-data/workspaces/cbm-dev-qa-20260924-v2')
SOURCE = ROOT / 'source/deploy/community-brain'
PRIVATE = ROOT / 'private'


def read_env(path):
    values = {}
    for line in path.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith('#'):
            key, raw = line.split('=', 1)
            parts = shlex.split(raw, comments=False)
            if len(parts) != 1:
                raise ValueError('invalid private environment value')
            values[key] = parts[0]
    return values


def compose(args):
    if socket.gethostname() != 'community-brain-dev' or not Path('/srv/dev-data').is_mount():
        raise ValueError('VM108 development data mount required')
    runtime = PRIVATE / 'runtime.env'
    if runtime.stat().st_uid != 0 or runtime.stat().st_mode & 0o777 != 0o600:
        raise ValueError('QA runtime ownership or mode changed')
    values = read_env(runtime)
    if values['CB_CORPUS_SCOPE'] != 'community-brain-dev':
        raise ValueError('development scope required')
    if values['CB_ENABLE_NETWORK_PUBLICATION'] != 'false':
        raise ValueError('remote publication forbidden')
    env = dict(os.environ)
    env['CB_LIVE_DATABASE_URL'] = (
        'postgresql+psycopg://cbmdev:'
        + quote(values['CB_DEV_POSTGRES_PASSWORD'], safe='')
        + '@postgres:5432/cbm_dev'
    )
    env['CB_LIVE_NATS_URL'] = (
        'nats://cbmdev:'
        + quote(values['CB_DEV_NATS_PASSWORD'], safe='')
        + '@nats:4222'
    )
    env['CB_ENABLE_MODEL_CALLS'] = 'false'
    env['CB_ENABLE_NETWORK_PUBLICATION'] = 'false'
    base = ['docker', 'compose', '--env-file', str(runtime),
            '-f', str(SOURCE / 'compose.live-development.yml'),
            '-f', str(SOURCE / 'compose.qa.yml')]
    if args in (['config', '--quiet'], ['up', '-d', '--no-deps', 'api'],
                ['up', '-d', 'webui'], ['up', '-d', '--force-recreate', '--no-deps', 'webui'],
                ['ps']):
        return base + args, env
    if args[:1] == ['scan'] and args[1:2] in (['next'], ['select'], ['stop'], ['project']):
        operation = args[1]
        expected = {'next': 2, 'select': 5, 'stop': 3, 'project': 5}[operation]
        if len(args) != expected:
            raise ValueError('invalid scan arguments')
        return base + ['run', '--rm', '-T', '--no-deps', 'qa-scan',
                       'python', '-B', '/qa/scan.py', *args[1:]], env
    if args[:1] == ['worker'] and len(args) == 3:
        kind, approval = args[1:]
        if kind not in ('acquisition', 'model'):
            raise ValueError('invalid worker kind')
        path = Path(approval)
        if path.parent != PRIVATE / 'approvals' or not path.is_file():
            raise ValueError('approval must be private QA selection')
        service = 'qa-' + kind
        return base + ['run', '--rm', '-T', '--no-deps',
                       '--volume', str(path) + ':/approval/selection.json:ro', service], env
    raise ValueError('unsupported QA operation')


def command(args):
    argv, env = compose(args)
    return subprocess.call(argv, env=env)


if __name__ == '__main__':
    raise SystemExit(command(sys.argv[1:]))
