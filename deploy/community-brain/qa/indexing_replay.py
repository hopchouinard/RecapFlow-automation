"""Read-only validation of a completed VM108 indexing request prefix."""

import hashlib
import json
from pathlib import Path
from uuid import UUID


def journal_path(job_id, generation):
    return Path('/state/files/qa-model-journals') / (
        f'indexing-{UUID(str(job_id))}-{int(generation)}.jsonl'
    )


def completed_prefix(storage, job_id, generation):
    path = journal_path(job_id, generation)
    data = path.read_bytes()
    rows = [json.loads(line) for line in data.splitlines()]
    if not rows or rows[0].get('state') != 'started' or rows[0].get('job_id') != str(job_id):
        raise ValueError('indexing journal header mismatch')
    if (len(rows) - 1) % 2 or len(rows) < 3:
        raise ValueError('indexing journal has an unresolved request')
    calls = []
    for number in range(1, (len(rows) + 1) // 2):
        intent, response = rows[2 * number - 1:2 * number + 1]
        if (intent.get('state') != 'intent' or response.get('state') != 'response'
                or intent.get('request') != number or response.get('request') != number
                or not isinstance(intent.get('request_sha256'), str)
                or len(intent['request_sha256']) != 64):
            raise ValueError('indexing journal request/response mismatch')
        body = json.loads(storage.read(response['path'], response['sha256']))
        if not isinstance(body, dict) or not isinstance(body.get('choices'), list):
            raise ValueError('indexing journal response is invalid')
        calls.append((intent['request_sha256'], intent.get('model'), body,
                      response['sha256']))
    return hashlib.sha256(data).hexdigest(), calls
