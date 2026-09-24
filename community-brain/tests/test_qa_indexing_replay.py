"""A completed indexing prefix is replayed without new provider spend."""

import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from uuid import uuid4

import httpx
import pytest

from community_brain.jobs.storage import Storage
from community_brain import llm

QA = Path(__file__).resolve().parents[2] / 'deploy/community-brain/qa'
sys.path.insert(0, str(QA))
spec = importlib.util.spec_from_file_location('qa_worker_replay_test', QA / 'worker.py')
worker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(worker)
import indexing_replay  # noqa: E402


def prior_journal(tmp_path, store, job_id, payload):
    body = {'choices': [{'message': {'content': 'valid response'}}]}
    path, sha, _ = store.storage.put(json.dumps(body).encode())
    request_hash = worker.hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode()
    ).hexdigest()
    journal = tmp_path / f'indexing-{job_id}-1.jsonl'
    journal.write_text('\n'.join(json.dumps(row) for row in (
        {'state': 'started', 'job_id': str(job_id), 'ceiling': 32},
        {'state': 'intent', 'request': 1, 'request_sha256': request_hash,
         'model': payload['model']},
        {'state': 'response', 'request': 1, 'path': path, 'sha256': sha},
    )) + '\n')
    return journal


def test_replay_uses_recorded_response_then_pays_only_for_new_request(tmp_path, monkeypatch):
    job_id = uuid4()
    store = SimpleNamespace(storage=Storage(tmp_path / 'storage'))
    monkeypatch.setattr(worker, 'JOURNALS', tmp_path)
    monkeypatch.setattr(indexing_replay, 'journal_path',
                        lambda job, generation: tmp_path / f'indexing-{job}-{generation}.jsonl')
    payload = {'model': 'fixture', 'messages': [{'role': 'user', 'content': 'one'}]}
    prior_journal(tmp_path, store, job_id, payload)
    sent = []

    def post(url, **kwargs):
        sent.append(kwargs['json'])
        return httpx.Response(200, json={'choices': [{'message': {'content': 'new'}}]},
                              request=httpx.Request('POST', url))

    monkeypatch.setattr(llm.httpx, 'post', post)
    monkeypatch.setattr(worker, 'allowance', lambda key: {'remaining': 1})
    with worker.audited_indexing(store, 'fixture', job_id, 2):
        assert llm.httpx.post(llm.OPENROUTER_URL, json=payload).json()['choices'][0]['message']['content'] == 'valid response'
        second = {**payload, 'messages': [{'role': 'user', 'content': 'two'}]}
        assert llm.httpx.post(llm.OPENROUTER_URL, json=second).json()['choices'][0]['message']['content'] == 'new'
    assert sent == [second]
    assert [json.loads(line)['state'] for line in
            (tmp_path / f'indexing-{job_id}-2.jsonl').read_text().splitlines()] == [
                'started', 'replayed', 'intent', 'response']


def test_incomplete_or_changed_replay_stops_before_paid_call(tmp_path, monkeypatch):
    job_id = uuid4()
    store = SimpleNamespace(storage=Storage(tmp_path / 'storage'))
    monkeypatch.setattr(worker, 'JOURNALS', tmp_path)
    monkeypatch.setattr(indexing_replay, 'journal_path',
                        lambda job, generation: tmp_path / f'indexing-{job}-{generation}.jsonl')
    payload = {'model': 'fixture', 'messages': []}
    journal = prior_journal(tmp_path, store, job_id, payload)
    with journal.open('a') as stream:
        stream.write(json.dumps({'state': 'intent', 'request': 2}) + '\n')
    with pytest.raises(ValueError, match='unresolved'):
        with worker.audited_indexing(store, 'fixture', job_id, 2):
            pytest.fail('must not enter indexing')
    journal.write_text(journal.read_text().splitlines()[0] + '\n' +
                       '\n'.join(journal.read_text().splitlines()[1:3]) + '\n')
    monkeypatch.setattr(worker, 'allowance', lambda _: pytest.fail('no paid call'))
    with worker.audited_indexing(store, 'fixture', job_id, 2):
        with pytest.raises(llm.LLMOutcomeUnknown, match='changed'):
            llm.httpx.post(llm.OPENROUTER_URL, json={'model': 'fixture', 'messages': ['changed']})
