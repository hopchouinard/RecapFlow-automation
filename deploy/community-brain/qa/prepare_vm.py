"""Prepare a scoped VM108 QA delivery from existing development authority."""

import hashlib
import json
import os
from pathlib import Path
import secrets
import shlex
import socket
import sqlite3
import time

from launch import PRIVATE, ROOT, read_env

R034 = Path('/srv/dev-data/workspaces/cbm-stage2-qualification-20260923-034/private')
AUTHORITY = Path('/etc/community-brain-development/runtime.env')
WEBUI_DB = Path('/srv/dev-data/docker/volumes/cbm-r034_webui/_data/webui.db')


def write(path, data):
    with path.open('xb') as stream:
        os.fchmod(stream.fileno(), 0o600)
        stream.write(data.encode())
        stream.flush()
        os.fsync(stream.fileno())


def dotenv(values):
    return ''.join(key + '=' + shlex.quote(str(value)) + '\n' for key, value in values.items())


def prepare():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    if not Path('/srv/dev-data').is_mount() or not ROOT.joinpath('source.tar').is_file():
        raise ValueError('QA source and data mount required')
    if PRIVATE.exists():
        raise FileExistsError('existing QA private state requires readback, not regeneration')
    runtime = read_env(AUTHORITY)
    r034_api = read_env(R034 / 'api.env')
    r034_webui = read_env(R034 / 'webui.env')
    identities = json.loads(r034_api['CB_SERVICE_IDENTITIES'])
    source_identity = next(x for x in identities if x['subject'] == 'community-brain-openwebui')
    if runtime['CB_CORPUS_SCOPE'] != 'community-brain-dev' or source_identity['expires_at'] <= time.time() + 86400:
        raise ValueError('development scope or authority expiry invalid')
    with sqlite3.connect('file:' + str(WEBUI_DB) + '?mode=ro', uri=True) as db:
        row = db.execute('SELECT valves FROM function WHERE id=?', ('community_brain_filter',)).fetchone()
    if not row:
        raise ValueError('source filter credential absent')
    filter_token = json.loads(row[0])['api_key']
    if hashlib.sha256(filter_token.encode()).hexdigest() != source_identity['sha256']:
        raise ValueError('Infisical identity and source filter credential differ')
    qa_identity = dict(source_identity, subject='community-brain-qa-webui',
                       scope='community-brain-dev', permissions=['retrieval:read'])
    runtime['CB_SERVICE_IDENTITIES'] = json.dumps([qa_identity], separators=(',', ':'))
    runtime['CB_QA_WEBUI_ENV_FILE'] = str(PRIVATE / 'webui.env')
    runtime['CB_ENABLE_MODEL_CALLS'] = 'false'
    runtime['CB_ENABLE_NETWORK_PUBLICATION'] = 'false'
    webui = {key: value for key, value in r034_webui.items()
             if key not in {'OPENAI_API_BASE_URL', 'OPENAI_API_KEY'}}
    webui.update(ENABLE_SIGNUP='true', ENABLE_OLLAMA_API='true', ENABLE_OPENAI_API='false',
                 OLLAMA_BASE_URL='http://10.1.50.219:11434',
                 OFFLINE_MODE='true', HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1')
    PRIVATE.mkdir(mode=0o700)
    write(PRIVATE / 'runtime.env', dotenv(runtime))
    write(PRIVATE / 'webui.env', dotenv(webui))
    write(PRIVATE / 'filter-token', filter_token + '\n')
    write(PRIVATE / 'admin.json', json.dumps({
        'name': 'Community Brain QA', 'email': 'community-brain-qa@example.invalid',
        'password': secrets.token_urlsafe(28)}, sort_keys=True) + '\n')
    write(PRIVATE / 'provenance.json', json.dumps({
        'scope': 'community-brain-dev', 'identity_source': 'Request034 development Infisical generation',
        'identity_expires_at': source_identity['expires_at'],
        'source_archive_sha256': hashlib.sha256((ROOT / 'source.tar').read_bytes()).hexdigest(),
        'webui_image': 'sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b',
    }, sort_keys=True) + '\n')
    fd = os.open(PRIVATE, os.O_RDONLY | os.O_DIRECTORY)
    os.fsync(fd)
    os.close(fd)
    return {'prepared': True, 'identity_expires_at': source_identity['expires_at'],
            'source_archive_sha256': hashlib.sha256((ROOT / 'source.tar').read_bytes()).hexdigest()}


if __name__ == '__main__':
    print(json.dumps(prepare(), sort_keys=True))
