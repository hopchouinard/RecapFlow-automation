"""Synthetic app-data persistence and final-candidate restart acceptance on VM108."""
import hashlib
import json
import os
from pathlib import Path
import socket
import sys
import urllib.request
from rehearse import ROOT, BASE, WEBUI, OPENER, api, atomic, docker, login, probe, ready


def main():
    assert socket.gethostname() == 'community-brain-dev' and os.geteuid() == 0
    assert (ROOT / 'acceptance.json').exists()
    marker = ROOT / 'private/data-test-started'
    assert not marker.exists(), 'inspect prior synthetic writes before retry'
    marker.touch(mode=0o600)
    state = json.loads((ROOT / 'private/credentials.json').read_text())
    token = login(state)
    chat = api('POST', '/api/v1/chats/new', {'chat': {
        'title': 'Request026 synthetic persistence',
        'messages': [{'id': 'synthetic-1', 'role': 'user', 'content': 'Synthetic only'}]
    }}, token)
    api('POST', '/api/v1/models/create', {'id': 'request026-custom-model',
        'base_model_id': 'cbm-synthetic-model', 'name': 'Request026 synthetic model',
        'meta': {'description': 'Synthetic persistence'}, 'params': {}}, token)
    api('POST', '/api/v1/prompts/create', {'command': 'request026-synthetic',
        'name': 'Request026 synthetic prompt', 'content': 'Synthetic only'}, token)
    content = b'Request026 synthetic upload; no private data.\n'
    boundary = 'cbm-request026-synthetic-upload'
    body = (f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="synthetic.txt"\r\n'
            'Content-Type: text/plain\r\n\r\n').encode() + content + f'\r\n--{boundary}--\r\n'.encode()
    request = urllib.request.Request(BASE + '/api/v1/files/?process=false', data=body,
        headers={'Authorization': 'Bearer ' + token,
                 'Content-Type': 'multipart/form-data; boundary=' + boundary})
    with OPENER.open(request, timeout=30) as response:
        assert response.status == 200
        file = json.load(response)
    atomic(ROOT / 'private/synthetic-records.json', {'chat_id': chat['id'], 'file_id': file['id']})
    docker('restart', WEBUI)
    verify()


def verify():
    assert socket.gethostname() == 'community-brain-dev' and os.geteuid() == 0
    state = json.loads((ROOT / 'private/credentials.json').read_text())
    records = json.loads((ROOT / 'private/synthetic-records.json').read_text())
    content = b'Request026 synthetic upload; no private data.\n'
    ready()
    token = login(state)
    restored = api('GET', '/api/v1/chats/' + records['chat_id'], token=token)
    assert restored['chat']['title'] == 'Request026 synthetic persistence'
    request = urllib.request.Request(BASE + '/api/v1/files/' + records['file_id'] + '/content',
        headers={'Authorization': 'Bearer ' + token})
    with OPENER.open(request, timeout=30) as response:
        assert response.read() == content
    # The authenticated list responses are real application reads, not DB fixtures.
    assert 'request026-custom-model' in json.dumps(api('GET', '/api/v1/models/list', token=token))
    assert 'request026-synthetic' in json.dumps(api('GET', '/api/v1/prompts/', token=token))
    cache = probe(token, state['new'])
    result = {'synthetic_chat_restored': True, 'synthetic_upload_restored': True,
              'upload_sha256': hashlib.sha256(content).hexdigest(),
              'custom_model_restored': True, 'prompt_restored': True,
              'login_after_restart': True, 'live_filter_cache_after_restart': cache,
              'upload_processing': False, 'paid_inference': False,
              'real_user_data_used': False}
    atomic(ROOT / 'data-recovery-acceptance.json', result)
    print(json.dumps(result))


if __name__ == '__main__':
    os.umask(0o077)
    assert sys.argv[1:] in ([], ['verify-only'])
    (verify if sys.argv[1:] else main)()
