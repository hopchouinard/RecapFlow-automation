"""VM108-only synthetic OpenWebUI acceptance. No production inputs or endpoints."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import time
import urllib.error
import urllib.request

ROOT = Path('/srv/dev-data/workspaces/cbm-openwebui-migration-20260920')
SOURCE = ROOT / 'source'
# Docker's containerd store assigns an imported manifest ID. Source config/layers
# are checked against the original image in image-equivalence.json before use.
IMAGE = 'sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b'
FIXTURE_IMAGE = 'sha256:9534e5a8e315485d4061ed659af0fd78a284c015f9b73661b41d6bab25604534'
NETWORK = 'cbm-r026-isolated'
WEBUI = 'cbm-r026-webui'
FIXTURE = 'cbm-r026-fixture'
VOLUME = 'cbm-r026-synthetic-data'
BASE = 'http://127.0.0.1:18088'
RETRIEVAL = 'http://cbm-r026-fixture:8999/retrieval/query'
OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def docker(*args):
    r = subprocess.run(['docker', *args], capture_output=True, text=True, timeout=180)
    if r.returncode:
        raise RuntimeError('development docker operation failed: ' + args[0])
    return r.stdout.strip()


def atomic(path, data):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(data, indent=2) + '\n')
    temp.chmod(0o600)
    temp.replace(path)


def call(method, path, body=None, token=None, base=BASE):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(base + path, method=method, headers=headers,
                                 data=None if body is None else json.dumps(body).encode())
    try:
        with OPENER.open(req, timeout=90) as response:
            return response.status, json.load(response)
    except urllib.error.HTTPError as error:
        return error.code, None


def api(method, path, body=None, token=None):
    status, value = call(method, path, body, token)
    assert status == 200, f'{method} {path}: HTTP {status}'
    return value


def ready():
    # The exact legacy image's cold imports exceeded three minutes on VM108.
    for _ in range(300):
        try:
            if call('GET', '/health')[0] == 200:
                return
        except (OSError, ValueError):
            pass
        time.sleep(2)
    raise RuntimeError('development WebUI readiness timeout')


def accepted(tokens):
    atomic(ROOT / 'private/control.json', {'accepted_sha256': [
        hashlib.sha256(t.encode()).hexdigest() for t in tokens]})


def setup():
    assert not (ROOT / 'private').exists(), 'existing fixture: inspect; do not replay setup'
    for port in (18088, 18089):
        with socket.socket() as sock:
            sock.bind(('127.0.0.1', port))
    (ROOT / 'private').mkdir(mode=0o700)
    state = {'email': 'request026@example.invalid', 'password': secrets.token_urlsafe(32),
             'old': secrets.token_urlsafe(32), 'new': secrets.token_urlsafe(32)}
    atomic(ROOT / 'private/credentials.json', state)
    accepted([state['old']])
    env = {'WEBUI_SECRET_KEY': secrets.token_urlsafe(48), 'WEBUI_AUTH': 'true',
           'ENABLE_SIGNUP': 'true', 'OFFLINE_MODE': 'true', 'HF_HUB_OFFLINE': '1',
           'TRANSFORMERS_OFFLINE': '1', 'ENABLE_OLLAMA_API': 'false',
           'ENABLE_OPENAI_API': 'true', 'OPENAI_API_BASE_URL': 'http://cbm-r026-fixture:8999/v1',
           'OPENAI_API_KEY': secrets.token_urlsafe(24), 'RAG_EMBEDDING_ENGINE': 'ollama',
           'OLLAMA_BASE_URL': 'http://cbm-r026-fixture:8999', 'ANONYMIZED_TELEMETRY': 'false',
           'DO_NOT_TRACK': 'true', 'SCARF_NO_ANALYTICS': 'true'}
    ep = ROOT / 'private/webui.env'
    ep.write_text(''.join(k + '=' + v + '\n' for k, v in env.items()))
    ep.chmod(0o600)
    docker('network', 'create', '--internal', '--label', 'cbm.request=026', NETWORK)
    docker('volume', 'create', '--label', 'cbm.request=026', VOLUME)
    docker('run', '-d', '--name', FIXTURE, '--network', NETWORK, '--read-only',
           '--memory', '128m', '--cpus', '0.25', '--cap-drop', 'ALL',
           '--security-opt', 'no-new-privileges', '--publish', '127.0.0.1:18089:8999',
           '--mount', f'type=bind,src={SOURCE},dst=/source,readonly',
           '--mount', f'type=bind,src={ROOT}/private,dst=/state,readonly',
           FIXTURE_IMAGE, 'python', '-B', '/source/fixture.py')
    docker('run', '-d', '--name', WEBUI, '--network', NETWORK,
           '--memory', '1536m', '--cpus', '1.5', '--cap-drop', 'ALL',
           '--security-opt', 'no-new-privileges', '--publish', '127.0.0.1:18088:8080',
           '--env-file', str(ep), '--mount', f'type=volume,src={VOLUME},dst=/app/backend/data', IMAGE)
    # Internal Docker networks do not publish these ports on this engine. Keep
    # egress isolation and provide explicit host-loopback-only test relays.
    with (ROOT / 'private/relay.log').open('ab') as log:
        relay = subprocess.Popen(['python3', '-B', str(SOURCE / 'loopback_proxy.py')],
                                 stdout=log, stderr=log, start_new_session=True)
    atomic(ROOT / 'private/relay.json', {'pid': relay.pid})
    ready()


def login(state):
    return api('POST', '/api/v1/auths/signin',
               {'email': state['email'], 'password': state['password']})['token']


def probe(token, expected_key, expected_status='ok'):
    models = api('GET', '/api/models', token=token)['data']
    assert any(m['id'] == 'cbm-synthetic-model' for m in models)
    result = api('POST', '/api/chat/actions/cbm_request026_probe',
                 {'model': 'cbm-synthetic-model', 'chat_id': 'request026-synthetic',
                  'id': 'request026-synthetic', 'session_id': 'request026-synthetic'}, token)
    assert result['live_app_process'] and result['effective_url'] == RETRIEVAL
    assert result['effective_token_sha256'] == hashlib.sha256(expected_key.encode()).hexdigest()
    assert result['retrieval_status'] == expected_status
    assert result['context_emitted'] == (expected_status == 'ok')
    assert result['unavailable_context'] == (expected_status == 'error')
    return result


def test():
    state = json.loads((ROOT / 'private/credentials.json').read_text())
    assert not (ROOT / 'private/test-started').exists(), 'inspect prior test evidence before retry'
    (ROOT / 'private/test-started').touch(mode=0o600)
    result = {'boundaries': {'real_application': True, 'exact_existing_filter': True,
                            'retrieval_backend': 'synthetic isolated HTTP fixture',
                            'model_list': 'synthetic fixture; no inference',
                            'production_authority': False}}
    api('POST', '/api/v1/auths/signup', {'name': 'Request026 Fixture',
        'email': state['email'], 'password': state['password']})
    token = login(state)
    result['login'] = True
    assert call('POST', '/api/v1/auths/signin', {'email': state['email'], 'password': 'wrong'})[0] in (400, 401)
    result['wrong_password_rejected'] = True
    for fid, name, file in [('community_brain_filter', 'Community Brain fixture', 'community_brain_filter.py'),
                             ('cbm_request026_probe', 'Request026 cache probe', 'probe_action.py')]:
        api('POST', '/api/v1/functions/create', {'id': fid, 'name': name,
            'content': (SOURCE / file).read_text(), 'meta': {'description': 'Synthetic development only'}}, token)
    api('POST', '/api/v1/functions/id/community_brain_filter/toggle', token=token)
    api('POST', '/api/v1/functions/id/community_brain_filter/toggle/global', token=token)
    valves = api('GET', '/api/v1/functions/id/community_brain_filter/valves', token=token)
    valves.update(retrieval_url=RETRIEVAL, api_key=state['old'])
    api('POST', '/api/v1/functions/id/community_brain_filter/valves/update', valves, token)
    result['initial_cache'] = probe(token, state['old'])
    accepted([state['old'], state['new']])
    valves['api_key'] = state['new']
    api('POST', '/api/v1/functions/id/community_brain_filter/valves/update', valves, token)
    result['renewed_cache'] = probe(token, state['new'])
    accepted([state['new']])
    for key, expected in ((state['old'], 401), (state['new'], 200)):
        req = urllib.request.Request('http://127.0.0.1:18089/retrieval/query',
            data=b'{"question":"synthetic"}', headers={'Content-Type': 'application/json', 'X-API-Key': key})
        try:
            with OPENER.open(req, timeout=10) as response: status = response.status
        except urllib.error.HTTPError as error: status = error.code
        assert status == expected
    result['old_credential_rejected'] = True
    result['new_credential_accepted'] = True
    accepted([])
    result['unavailable_cache'] = probe(token, state['new'], 'error')
    accepted([state['new']])
    result['restored_cache'] = probe(token, state['new'])
    atomic(ROOT / 'acceptance-before-restart.json', result)
    docker('restart', WEBUI)
    finish_restart(state, result)


def finish_restart(state, result):
    ready()
    token = login(state)
    result['after_restart'] = probe(token, state['new'])
    result['restart_login_and_persistence'] = True
    result['network_internal'] = json.loads(docker('network', 'inspect', NETWORK))[0]['Internal']
    assert result['network_internal']
    for name in (WEBUI, FIXTURE):
        info = json.loads(docker('inspect', name))[0]
        assert all(p['HostIp'] == '127.0.0.1' for ports in info['HostConfig']['PortBindings'].values() for p in ports)
    result['ports_loopback_only'] = True
    atomic(ROOT / 'acceptance.json', result)
    print(json.dumps(result))


def verify_restart():
    """Continue verification after a readiness timeout; never replay renewal."""
    assert not (ROOT / 'acceptance.json').exists()
    state = json.loads((ROOT / 'private/credentials.json').read_text())
    result = json.loads((ROOT / 'acceptance-before-restart.json').read_text())
    finish_restart(state, result)


if __name__ == '__main__':
    os.umask(0o077)
    assert os.geteuid() == 0
    assert socket.gethostname() == 'community-brain-dev', 'VM108 only'
    assert Path('/srv/dev-data').is_mount()
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['setup', 'test', 'verify-restart'])
    mode = parser.parse_args().mode
    {'setup': setup, 'test': test, 'verify-restart': verify_restart}[mode]()
