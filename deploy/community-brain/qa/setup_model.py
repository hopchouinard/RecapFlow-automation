"""Install the canonical Community Brain answering model in VM108 WebUI."""

import hashlib
import json
import os
from pathlib import Path
import socket
import sys

from launch import PRIVATE, ROOT
from setup_webui import call, login

MODEL_ID = 'community-brain-v4-gpt-oss20b'
BASE_MODEL = 'gpt-oss:20b'
PROMPT = ROOT / 'source/docs/inference-guidelines.md'
PROMPT_SHA256 = '5d3efe6493e42f8c4322a7291d49ebcf374060040efdcbb72472ebb7d643db2c'


def check_host():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')


def admin_token():
    admin = json.loads((PRIVATE / 'admin.json').read_text())
    token = login(admin)
    if token is None:
        raise RuntimeError('QA WebUI administrator unavailable')
    return token


def current(token):
    status, model = call('GET', '/api/v1/models/model?id=' + MODEL_ID, token=token)
    return model if status == 200 else None


def verify():
    check_host()
    content = PROMPT.read_text()
    if hashlib.sha256(content.encode()).hexdigest() != PROMPT_SHA256:
        raise RuntimeError('canonical Community Brain prompt changed')
    token = admin_token()
    model = current(token)
    if not model or model.get('id') != MODEL_ID or model.get('base_model_id') != BASE_MODEL:
        raise RuntimeError('Community Brain custom model absent or changed')
    if model.get('params', {}).get('system') != content:
        raise RuntimeError('Community Brain system prompt differs from source')
    status, config = call('GET', '/api/v1/configs/models', token=token)
    if status != 200 or config.get('DEFAULT_MODELS') != MODEL_ID:
        raise RuntimeError('Community Brain is not the default model')
    status, available = call('GET', '/api/models', token=token)
    if status != 200 or MODEL_ID not in {item['id'] for item in available.get('data', [])}:
        raise RuntimeError('Community Brain missing from model picker')
    return {'model_id': MODEL_ID, 'base_model': BASE_MODEL,
            'prompt_sha256': PROMPT_SHA256, 'visible': True, 'default': True,
            'model_count': len(available['data'])}


def install():
    check_host()
    content = PROMPT.read_text()
    if hashlib.sha256(content.encode()).hexdigest() != PROMPT_SHA256:
        raise RuntimeError('canonical Community Brain prompt changed')
    token = admin_token()
    model = current(token)
    if model is None:
        status, model = call('POST', '/api/v1/models/create', {
            'id': MODEL_ID, 'base_model_id': BASE_MODEL,
            'name': 'Community Brain (Development)',
            'meta': {'description': 'Development Community Brain retrieval with source-grounded answers'},
            'params': {'system': content}, 'is_active': True}, token)
        if status != 200:
            raise RuntimeError('Community Brain custom model creation failed')
    else:
        if model.get('base_model_id') != BASE_MODEL or model.get('params', {}).get('system') != content:
            raise RuntimeError('existing Community Brain model differs')
    status, config = call('GET', '/api/v1/configs/models', token=token)
    if status != 200:
        raise RuntimeError('WebUI model defaults unavailable')
    if config.get('DEFAULT_MODELS') != MODEL_ID:
        config['DEFAULT_MODELS'] = MODEL_ID
        status, _ = call('POST', '/api/v1/configs/models', config, token)
        if status != 200:
            raise RuntimeError('Community Brain default model update failed')
    return verify()


if __name__ == '__main__':
    operation = sys.argv[1]
    if operation == 'install':
        result = install()
    elif operation == 'verify':
        result = verify()
    else:
        raise SystemExit(2)
    print(json.dumps(result, sort_keys=True))
