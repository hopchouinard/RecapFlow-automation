"""Install and inspect the real filter in the VM108 QA Open WebUI."""

import hashlib
import json
import os
from pathlib import Path
import socket
import sys
import urllib.error
import urllib.request

from launch import PRIVATE, ROOT

BASE = 'http://127.0.0.1:8080'
FILTER = ROOT / 'source/community-brain/src/community_brain/openwebui/community_brain_filter.py'
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def call(method, path, body=None, token=None, *, api=BASE, extra=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    if extra:
        headers.update(extra)
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(api + path, data=data, headers=headers, method=method)
    try:
        with OPENER.open(request, timeout=30) as response:
            return response.status, json.loads(response.read() or b'{}')
    except urllib.error.HTTPError as error:
        return error.code, {}


def login(admin):
    status, value = call('POST', '/api/v1/auths/signin',
                         {'email': admin['email'], 'password': admin['password']})
    return value['token'] if status == 200 else None


def install():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    admin = json.loads((PRIVATE / 'admin.json').read_text())
    filter_token = (PRIVATE / 'filter-token').read_text().strip()
    status, health = call('GET', '/health')
    if status != 200 or health.get('status') is not True:
        raise RuntimeError('WebUI not healthy')
    token = login(admin)
    intent = PRIVATE / 'signup-intent'
    if token is None:
        if intent.exists():
            raise RuntimeError('signup outcome uncertain; inspect before retry')
        with intent.open('x') as stream:
            os.fchmod(stream.fileno(), 0o600)
            stream.write('first QA admin signup\n')
            stream.flush()
            os.fsync(stream.fileno())
        status, _ = call('POST', '/api/v1/auths/signup', admin)
        if status not in (200, 201):
            raise RuntimeError('QA admin signup failed')
        token = login(admin)
        if token is None:
            raise RuntimeError('QA admin login failed after signup')
    content = FILTER.read_text()
    status, functions = call('GET', '/api/v1/functions/', token=token)
    if status != 200 or not isinstance(functions, list):
        raise RuntimeError('function inventory unavailable')
    installed = any(item.get('id') == 'community_brain_filter' for item in functions)
    if not installed:
        status, _ = call('POST', '/api/v1/functions/create', {
            'id': 'community_brain_filter', 'name': 'Community Brain',
            'content': content, 'meta': {'description': 'VM108 QA retrieval filter'},
        }, token)
        if status not in (200, 201):
            raise RuntimeError('filter creation failed')
    else:
        status, existing = call('GET', '/api/v1/functions/id/community_brain_filter', token=token)
        if status != 200 or existing.get('content') != content:
            raise RuntimeError('existing filter source differs')
    status, function = call('GET', '/api/v1/functions/id/community_brain_filter', token=token)
    if status != 200:
        raise RuntimeError('filter readback failed')
    if not function.get('is_active'):
        status, _ = call('POST', '/api/v1/functions/id/community_brain_filter/toggle', token=token)
        if status != 200:
            raise RuntimeError('filter activation failed')
    if not function.get('is_global'):
        status, _ = call('POST', '/api/v1/functions/id/community_brain_filter/toggle/global', token=token)
        if status != 200:
            raise RuntimeError('global filter activation failed')
    status, valves = call('GET', '/api/v1/functions/id/community_brain_filter/valves', token=token)
    if status != 200:
        raise RuntimeError('filter valves unavailable')
    valves.update(retrieval_url='http://api:8090/retrieval/query', api_key=filter_token)
    status, _ = call('POST', '/api/v1/functions/id/community_brain_filter/valves/update', valves, token)
    if status != 200:
        raise RuntimeError('filter valve update failed')
    return verify(token)


def verify(token=None):
    admin = json.loads((PRIVATE / 'admin.json').read_text())
    token = token or login(admin)
    if token is None:
        raise RuntimeError('QA admin login failed')
    status, function = call('GET', '/api/v1/functions/id/community_brain_filter', token=token)
    if status != 200 or not function.get('is_active') or not function.get('is_global'):
        raise RuntimeError('filter inactive')
    if function.get('content') != FILTER.read_text():
        raise RuntimeError('filter source changed')
    status, valves = call('GET', '/api/v1/functions/id/community_brain_filter/valves', token=token)
    expected = (PRIVATE / 'filter-token').read_text().strip()
    if status != 200 or valves.get('retrieval_url') != 'http://api:8090/retrieval/query' or valves.get('api_key') != expected:
        raise RuntimeError('filter credential or endpoint changed')
    status, response = call('POST', '/retrieval/query', {'question': 'community brain'},
                            api='http://127.0.0.1:8090', extra={'X-API-Key': expected})
    if status != 200:
        raise RuntimeError('real development retrieval refused')
    status, models = call('GET', '/api/models', token=token)
    if status != 200 or not isinstance(models.get('data'), list):
        raise RuntimeError('WebUI model list unavailable')
    return {'login': True, 'filter_active': True, 'filter_source_sha256': hashlib.sha256(FILTER.read_bytes()).hexdigest(),
            'retrieval_http_status': 200, 'retrieval_chunk_count': len(response.get('chunks', [])),
            'model_count': len(models['data'])}


def prepare_seal():
    values = (PRIVATE / 'webui.env').read_text()
    if values.count('ENABLE_SIGNUP=true\n') != 1:
        raise ValueError('signup environment precondition changed')
    path = PRIVATE / 'webui.env'
    temp = path.with_name('webui.env.next')
    with temp.open('x') as stream:
        os.fchmod(stream.fileno(), 0o600)
        stream.write(values.replace('ENABLE_SIGNUP=true\n', 'ENABLE_SIGNUP=false\n'))
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)
    return {'signup_environment_disabled': True, 'restart_required': True}


def check_sealed():
    admin = json.loads((PRIVATE / 'admin.json').read_text())
    if login(admin) is None:
        raise RuntimeError('existing QA admin login failed')
    status, _ = call('POST', '/api/v1/auths/signup', {
        'name': 'Unauthorized', 'email': 'unauthorized@example.invalid',
        'password': 'unusable-test-password'},
    )
    if status != 403:
        raise RuntimeError('signup remains available')
    result = verify()
    result['signup_status'] = status
    return result


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'install':
        result = install()
    elif mode == 'verify':
        result = verify()
    elif mode == 'prepare-seal':
        result = prepare_seal()
    elif mode == 'check-sealed':
        result = check_sealed()
    else:
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True))
