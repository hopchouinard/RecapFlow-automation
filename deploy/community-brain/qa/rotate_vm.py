"""Rotate only VM108 QA service identities, without an external handoff."""

import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import socket
import sys
import time
import urllib.error
import urllib.request

from launch import PRIVATE, command, read_env
from prepare_vm import dotenv, write
from setup_webui import call, login


def replace(path, value):
    staging = path.with_name(path.name + '.next')
    if staging.exists():
        staging.unlink()
    write(staging, value)
    os.replace(staging, path)
    fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    os.fsync(fd)
    os.close(fd)


def api(path, token, payload=None):
    headers = {'Authorization': 'Bearer ' + token}
    data = None
    if payload is not None:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(payload).encode()
    request = urllib.request.Request('http://127.0.0.1:8090' + path, data=data,
                                     headers=headers, method='POST' if data else 'GET')
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def wait_api():
    for _ in range(40):
        try:
            with urllib.request.urlopen('http://127.0.0.1:8090/health', timeout=2) as response:
                if response.status == 200:
                    return
        except (OSError, urllib.error.URLError):
            pass
        time.sleep(2)
    raise RuntimeError('QA API did not recover after rotation')


def identity_for(identities, token):
    digest = hashlib.sha256(token.encode()).hexdigest()
    matches = [value for value in identities if value['sha256'] == digest]
    if len(matches) != 1 or matches[0]['scope'] != 'community-brain-dev':
        raise ValueError('current QA credential has no unique development identity')
    return matches[0]


def rotate(label):
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    if not re.fullmatch(r'20\d{6}[a-z0-9]{0,8}', label):
        raise ValueError('rotation label must be a bounded date identifier')
    candidate = PRIVATE / ('rotation-' + label)
    if (candidate / 'complete.json').exists():
        return {'rotation': label, 'already_complete': True}
    runtime_path = PRIVATE / 'runtime.env'
    runtime = read_env(runtime_path)
    if runtime['CB_CORPUS_SCOPE'] != 'community-brain-dev':
        raise ValueError('development scope changed')
    identities = json.loads(runtime['CB_SERVICE_IDENTITIES'])
    existing_webui = (PRIVATE / 'filter-token').read_text().strip()
    existing_operator = (PRIVATE / 'operator-token').read_text().strip()
    old_webui = identity_for(identities, existing_webui)
    old_operator = identity_for(identities, existing_operator)
    if not candidate.exists():
        candidate.mkdir(mode=0o700)
        webui = secrets.token_urlsafe(36)
        operator = secrets.token_urlsafe(36)
        expiry = int(time.time()) + 30 * 86400
        write(candidate / 'webui-token', webui + '\n')
        write(candidate / 'operator-token', operator + '\n')
        write(candidate / 'metadata.json', json.dumps({'scope': 'community-brain-dev',
            'expires_at': expiry, 'webui_permissions': old_webui['permissions'],
            'operator_permissions': old_operator['permissions']}, sort_keys=True) + '\n')
    webui = (candidate / 'webui-token').read_text().strip()
    operator = (candidate / 'operator-token').read_text().strip()
    meta = json.loads((candidate / 'metadata.json').read_text())
    if meta['scope'] != 'community-brain-dev' or meta['expires_at'] <= time.time() + 86400:
        raise ValueError('rotation candidate expired or wrong scope')
    new = [
        {'subject': 'community-brain-qa-webui-' + label, 'scope': 'community-brain-dev',
         'permissions': meta['webui_permissions'], 'expires_at': meta['expires_at'],
         'sha256': hashlib.sha256(webui.encode()).hexdigest()},
        {'subject': 'community-brain-qa-operator-' + label, 'scope': 'community-brain-dev',
         'permissions': meta['operator_permissions'], 'expires_at': meta['expires_at'],
         'sha256': hashlib.sha256(operator.encode()).hexdigest()},
    ]
    if old_webui['subject'] not in {value['subject'] for value in new}:
        identities = [old_webui, old_operator, *new]
        runtime['CB_SERVICE_IDENTITIES'] = json.dumps(identities, separators=(',', ':'))
        replace(runtime_path, dotenv(runtime))
        if command(['up', '-d', '--no-deps', 'api']):
            raise RuntimeError('QA API overlap activation failed')
        wait_api()
    if api('/api/v1/me', operator) != 200 or api('/retrieval/query', webui,
            {'question': 'community brain'}) != 200:
        raise RuntimeError('new QA identity readback failed')
    admin = json.loads((PRIVATE / 'admin.json').read_text())
    admin_token = login(admin)
    if not admin_token:
        raise RuntimeError('QA WebUI admin unavailable')
    status, valves = call('GET', '/api/v1/functions/id/community_brain_filter/valves', token=admin_token)
    if status != 200 or valves.get('api_key') not in (existing_webui, webui):
        raise RuntimeError('QA WebUI filter valve changed unexpectedly')
    if valves['api_key'] != webui:
        valves['api_key'] = webui
        status, _ = call('POST', '/api/v1/functions/id/community_brain_filter/valves/update',
                         valves, admin_token)
        if status != 200:
            raise RuntimeError('QA WebUI filter rotation failed')
    status, valves = call('GET', '/api/v1/functions/id/community_brain_filter/valves', token=admin_token)
    if status != 200 or valves.get('api_key') != webui:
        raise RuntimeError('QA WebUI filter rotation readback failed')
    replace(PRIVATE / 'filter-token', webui + '\n')
    replace(PRIVATE / 'operator-token', operator + '\n')
    runtime['CB_SERVICE_IDENTITIES'] = json.dumps(new, separators=(',', ':'))
    runtime['CB_QA_IDENTITY_EXPIRES_AT'] = str(meta['expires_at'])
    replace(runtime_path, dotenv(runtime))
    if command(['up', '-d', '--no-deps', 'api']):
        raise RuntimeError('QA API final activation failed')
    wait_api()
    if api('/api/v1/me', operator) != 200 or api('/retrieval/query', webui,
            {'question': 'community brain'}) != 200:
        raise RuntimeError('final QA identity readback failed')
    if existing_operator != operator and api('/api/v1/me', existing_operator) != 401:
        raise RuntimeError('old QA operator identity remains valid')
    if existing_webui != webui and api('/retrieval/query', existing_webui,
            {'question': 'community brain'}) != 401:
        raise RuntimeError('old QA WebUI identity remains valid')
    write(candidate / 'complete.json', json.dumps({'scope': 'community-brain-dev',
          'expires_at': meta['expires_at'], 'old_revoked': True,
          'new_verified': True}, sort_keys=True) + '\n')
    return {'rotation': label, 'expires_at': meta['expires_at'],
            'old_revoked': True, 'new_verified': True}


if __name__ == '__main__':
    print(json.dumps(rotate(sys.argv[1]), sort_keys=True))
