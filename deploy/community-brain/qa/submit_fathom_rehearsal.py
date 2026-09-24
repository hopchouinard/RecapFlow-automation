"""Selected prior Fathom fixture: acquisition only, no chat or paid processing."""

import json
import os
from pathlib import Path
import socket
import urllib.request

from launch import PRIVATE

RECEIPT = PRIVATE / 'fathom-acquisition-job.json'


def main():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    if RECEIPT.exists():
        raise FileExistsError('selected Fathom acquisition already submitted')
    token = (PRIVATE / 'operator-token').read_text().strip()
    # Previously selected and read on VM108: docs/migrations/cbm-fathom-fixed-dev-receipt.json.
    body = {'identity': {
        'meeting_id': '183401214', 'started_at': '2026-09-15T21:56:10Z',
        'timezone': 'America/Toronto', 'local_date': '2026-09-15',
        'provider': 'fathom'}, 'mode': 'weekly', 'sources': {},
        'version': 'processing-v1'}
    request = urllib.request.Request('http://127.0.0.1:8090/api/v1/jobs',
        json.dumps(body).encode(), headers={'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
        'Idempotency-Key': 'qa-fathom-acquisition-20260915'}, method='POST')
    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status != 202:
            raise RuntimeError('selected Fathom job not newly queued')
        job = json.load(response)
    with RECEIPT.open('x') as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump({'job_id': job['id'], 'recording_id': '183401214',
                   'prior_transcript_sha256': '76c44ab52cd4105d6c4d9fd0762c5d4a6e72f9ffc10721175f4969368a918cd5'}, stream)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    print(json.dumps({'job_id': job['id'], 'acquisition_queued': True,
                      'model_processing_requested': False}))


if __name__ == '__main__':
    main()
