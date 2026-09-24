"""Submit one repository-owned synthetic fixture through the VM108 API."""

import hashlib
import json
import os
from pathlib import Path
import socket
import urllib.request

from launch import PRIVATE

BASE = 'http://127.0.0.1:8090/api/v1'
MEETING = 'qa-20260924-full-loop-001'
RECEIPT = PRIVATE / 'synthetic-job.json'
CHAT = ('[19:00] Alice Chen: QA fixture question: how should we compare vector search quality?\n'
        '[19:01] Bob Martinez: Please include hybrid search and embedding tradeoffs in the recap.\n'
        '[19:02] Carol Singh: The call agreed to test retrieval quality on the synthetic sample.\n')


def post(path, token, body, *, key=None):
    headers = {'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}
    if key:
        headers['Idempotency-Key'] = key
    request = urllib.request.Request(BASE + path, json.dumps(body).encode(),
                                     headers=headers, method='POST')
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.status, json.load(response)


def main():
    if os.geteuid() != 0 or socket.gethostname() != 'community-brain-dev':
        raise ValueError('VM108 root required')
    if RECEIPT.exists():
        raise FileExistsError('synthetic QA job already submitted')
    transcript = Path('/tmp/cbm-qa-sample-transcript-20260924.txt').read_text()
    if hashlib.sha256(transcript.encode()).hexdigest() != '04861f13d8637b5a3133024ad27d9a4ca29a4bc66165478983c413760c073e29':
        raise ValueError('synthetic fixture changed')
    token = (PRIVATE / 'operator-token').read_text().strip()
    status, source = post('/sources', token, {'meeting_id': MEETING,
                                             'kind': 'transcript', 'content': transcript})
    if status != 201:
        raise RuntimeError('synthetic source rejected')
    chat_status, chat = post('/sources', token, {'meeting_id': MEETING,
                                               'kind': 'chat', 'content': CHAT})
    if chat_status != 201:
        raise RuntimeError('synthetic chat source rejected')
    status, job = post('/jobs', token, {'identity': {
        'meeting_id': MEETING, 'started_at': '2026-09-24T19:00:00Z',
        'timezone': 'UTC', 'local_date': '2026-09-24', 'provider': 'manual'},
        'mode': 'weekly', 'sources': {'transcript': source['id'], 'chat': chat['id']},
        'version': 'processing-v1'}, key='qa-20260924-full-loop-001')
    if status != 202:
        raise RuntimeError('synthetic job not newly queued')
    with RECEIPT.open('x') as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump({'job_id': job['id'], 'source_id': source['id'], 'chat_id': chat['id'],
                   'fixture_sha256': '04861f13d8637b5a3133024ad27d9a4ca29a4bc66165478983c413760c073e29'}, stream)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    print(json.dumps({'job_id': job['id'], 'queued': True}))


if __name__ == '__main__':
    main()
