"""One-time VM108 delivery of a test operator and Fathom key to QA only."""

import hashlib
import json
import os
from pathlib import Path
import shlex
import socket

from launch import PRIVATE, read_env
from prepare_vm import R034, dotenv, write


def extend():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    runtime_path = PRIVATE / 'runtime.env'
    runtime = read_env(runtime_path)
    identities = json.loads(runtime['CB_SERVICE_IDENTITIES'])
    if len(identities) != 1 or identities[0]['subject'] != 'community-brain-qa-webui':
        raise ValueError('unexpected QA identity baseline')
    if (PRIVATE / 'operator-token').exists():
        raise FileExistsError('operator delivery already exists')
    api = read_env(R034 / 'api.env')
    operator = read_env(R034 / 'operator-client.env')
    token = operator['CB_MANUAL_OPERATOR_TOKEN']
    source = next(x for x in json.loads(api['CB_SERVICE_IDENTITIES'])
                  if x['subject'] == 'community-brain-prod-manual-operator')
    if hashlib.sha256(token.encode()).hexdigest() != source['sha256']:
        raise ValueError('development operator identity mismatch')
    identities.append(dict(source, subject='community-brain-qa-operator',
                           scope='community-brain-dev'))
    runtime['CB_SERVICE_IDENTITIES'] = json.dumps(identities, separators=(',', ':'))
    runtime['CB_QA_IDENTITY_EXPIRES_AT'] = str(min(x['expires_at'] for x in identities))
    fathom = read_env(Path('/etc/community-brain-development/fathom.env'))
    runtime['CB_QA_FATHOM_API_KEY'] = fathom['CB_FATHOM_API_KEY']
    next_path = runtime_path.with_name('runtime.env.next')
    write(next_path, dotenv(runtime))
    os.replace(next_path, runtime_path)
    write(PRIVATE / 'operator-token', token + '\n')
    return {'operator_scoped': True, 'fathom_dev_delivery': True,
            'identity_expires_at': int(runtime['CB_QA_IDENTITY_EXPIRES_AT'])}


if __name__ == '__main__':
    print(json.dumps(extend(), sort_keys=True))
