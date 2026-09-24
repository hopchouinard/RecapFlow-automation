"""Exactly one selected VM108 stage, with separate acquisition/model credentials."""

import asyncio
from contextlib import contextmanager
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
from uuid import UUID

import httpx
import lancedb
import nats
from sqlalchemy.orm import Session

from community_brain import llm
from community_brain.jobs.acquisition import Fathom
from community_brain.jobs.automatic import require_automatic
from community_brain.jobs.manual import run_selected, selection
from community_brain.jobs.models import Job
from community_brain.jobs.publication import PublicationHandlers, corpus_lock
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import OpenRouter, Worker
from community_brain.processing.pipeline import OutcomeUnknown
from indexing_replay import completed_prefix

SCOPE = 'community-brain-dev'
JOURNALS = Path('/state/files/qa-model-journals')


def allowance(key):
    try:
        response = httpx.get('https://openrouter.ai/api/v1/key',
                             headers={'Authorization': 'Bearer ' + key}, timeout=20)
        response.raise_for_status()
        value = response.json()['data']
        remaining = value['limit_remaining']
        if not (value['limit'] == 5 and value['limit_reset'] is None
                and type(remaining) in (int, float) and math.isfinite(remaining)
                and 0 < remaining <= 5 and value['is_management_key'] is False
                and value['include_byok_in_limit'] is True):
            raise ValueError('development allowance changed')
        return {'limit': 5, 'remaining': remaining}
    except Exception as exc:
        raise OutcomeUnknown('development allowance uncertain or exhausted') from exc


class BudgetedOpenRouter(OpenRouter):
    def __init__(self, key):
        super().__init__(key)
        self.calls = 0

    def __call__(self, request):
        if self.calls >= 20:
            raise OutcomeUnknown('QA processing call ceiling reached')
        allowance(self.api_key)
        self.calls += 1
        return super().__call__(request)


class SelectedFathom(Fathom):
    def __init__(self, key, recording, started_at):
        super().__init__(key)
        if self.call_id(recording) is None:
            raise ValueError('numeric recording ID required')
        self.recording, self.started_at = recording, started_at
        self.lookup_count = self.transcript_count = 0
        self.client.event_hooks['request'] = [self.guard]

    def guard(self, request):
        if (request.method != 'GET' or request.url.scheme != 'https'
                or request.url.host != 'api.fathom.ai'):
            raise ValueError('only selected Fathom reads permitted')
        if request.url.path == '/external/v1/meetings':
            self.lookup_count += 1
            if self.lookup_count > 5:
                raise ValueError('metadata page ceiling reached')
            request.url = request.url.copy_merge_params({
                'include_transcript': 'false', 'include_summary': 'false',
                'include_action_items': 'false', 'include_highlights': 'false',
                'include_crm_matches': 'false'})
        elif request.url.path == f'/external/v1/recordings/{getattr(self, "resolved_recording", None)}/transcript':
            self.transcript_count += 1
            if self.transcript_count > 1:
                raise ValueError('transcript already requested')
        else:
            raise ValueError('unselected Fathom operation')

    def fetch(self, identity):
        if identity['meeting_id'] != self.recording or identity['started_at'] != self.started_at:
            raise ValueError('selected recording/time mismatch')
        return super().fetch(identity)


@contextmanager
def audited_indexing(store, key, job_id, generation):
    JOURNALS.mkdir(mode=0o700, exist_ok=True)
    journal = JOURNALS / f'indexing-{job_id}-{generation}.jsonl'
    replay_hash, replay = (completed_prefix(store.storage, job_id, generation - 1)
                           if generation == 2 else (None, []))
    if generation > 2:
        raise ValueError('further indexing reconciliation requires separate review')
    original = llm.httpx.post
    count = 0
    with journal.open('x') as stream:
        os.fchmod(stream.fileno(), 0o600)

        def record(value):
            stream.write(json.dumps(value, sort_keys=True) + '\n')
            stream.flush()
            os.fsync(stream.fileno())

        record({'state': 'started', 'job_id': str(job_id), 'ceiling': 64,
                'replay_sha256': replay_hash, 'replay_count': len(replay)})

        def post(url, **kwargs):
            nonlocal count
            if url != llm.OPENROUTER_URL or count >= 64:
                raise llm.LLMOutcomeUnknown('QA indexing request ceiling reached')
            count += 1
            request_hash = hashlib.sha256(json.dumps(kwargs['json'], sort_keys=True).encode()).hexdigest()
            if count <= len(replay):
                previous_hash, previous_model, body, response_hash = replay[count - 1]
                if request_hash != previous_hash or kwargs['json']['model'] != previous_model:
                    raise llm.LLMOutcomeUnknown('indexing replay request changed')
                record({'state': 'replayed', 'request': count, 'request_sha256': request_hash,
                        'response_sha256': response_hash})
                return httpx.Response(200, json=body, request=httpx.Request('POST', url))
            budget = allowance(key)
            record({'state': 'intent', 'request': count, 'request_sha256': request_hash,
                    'model': kwargs['json']['model'], 'allowance': budget})
            try:
                response = original(url, **kwargs)
                response.raise_for_status()
                body = response.json()
                path, sha, _ = store.storage.put(json.dumps(body).encode())
                record({'state': 'response', 'request': count, 'path': path,
                        'sha256': sha, 'usage': body.get('usage')})
                return response
            except Exception as exc:
                raise llm.LLMOutcomeUnknown('QA indexing outcome requires review') from exc

        llm.httpx.post = post
        try:
            yield
        finally:
            llm.httpx.post = original


def complete_fts(handler, corpus, job_id):
    result = handler.indexing(job_id)
    with corpus_lock(corpus):
        table = lancedb.connect(str(Path(corpus) / 'lancedb/nomic-v1')).open_table('chunks')
        stats = table.index_stats('bm25_text_idx')
        if (not stats or stats['num_unindexed_rows']
                or stats['num_indexed_rows'] != table.count_rows()):
            table.create_fts_index('bm25_text', replace=True)
        stats = table.index_stats('bm25_text_idx')
        if (not stats or stats['num_unindexed_rows']
                or stats['num_indexed_rows'] != table.count_rows()):
            raise RuntimeError('FTS coverage requires reconciliation')
        result['fts_indexed_rows'] = stats['num_indexed_rows']
    return result


async def execute(store, approved, kind):
    if approved['scope'] != SCOPE or approved['stage'] not in ('acquisition', 'processing', 'indexing'):
        raise ValueError('development selection required')
    if selection(store, approved['job_id'], approved['stage'], approved['generation'], scope=SCOPE) != approved:
        raise ValueError('selection changed')
    require_automatic(store, approved['job_id'])
    if os.environ.get('CB_ENABLE_NETWORK_PUBLICATION') != 'false':
        raise ValueError('network publication forbidden')
    if time.time() >= int(os.environ['CB_QA_IDENTITY_EXPIRES_AT']):
        raise ValueError('development identity expired')
    name = approved['stage']
    if (name == 'acquisition') != (kind == 'acquisition'):
        raise ValueError('wrong credential compartment for stage')
    if kind == 'acquisition':
        if 'CB_OPENROUTER_API_KEY' in os.environ:
            raise ValueError('model key forbidden in acquisition worker')
        with Session(store.engine) as session:
            identity = session.get(Job, UUID(approved['job_id'])).identity
        fathom = SelectedFathom(os.environ['CB_FATHOM_API_KEY'], identity['meeting_id'], identity['started_at'])
        worker = Worker(store, lambda _: (_ for _ in ()).throw(RuntimeError('model call forbidden')), fathom=fathom)
    else:
        if 'CB_FATHOM_API_KEY' in os.environ or os.environ.get('CB_ENABLE_MODEL_CALLS') != 'true':
            raise ValueError('model compartment invalid')
        key = os.environ['CB_OPENROUTER_API_KEY']
        allowance(key)
        worker = Worker(store, BudgetedOpenRouter(key))
        fathom = None
        if name == 'indexing':
            os.environ['OPENROUTER_API_KEY'] = key
            corpus = Path(os.environ['CB_CORPUS_ROOT'])
            handler = PublicationHandlers(store, corpus, os.environ['CB_PIPELINE_CONFIG_DIR'],
                                          os.environ['OLLAMA_BASE_URL'])
            worker.handlers = {'indexing': lambda job: complete_fts(handler, corpus, job)}
    try:
        if name == 'indexing':
            with audited_indexing(store, key, approved['job_id'], approved['generation']):
                result = await run_selected(store, approved, worker,
                                            lambda: nats.connect(os.environ['CB_NATS_URL']),
                                            stream=os.environ['CB_NATS_STREAM'], subject=os.environ['CB_NATS_SUBJECT'])
        else:
            result = await run_selected(store, approved, worker,
                                        lambda: nats.connect(os.environ['CB_NATS_URL']),
                                        stream=os.environ['CB_NATS_STREAM'], subject=os.environ['CB_NATS_SUBJECT'])
        print(json.dumps({'job_id': approved['job_id'], 'stage': name, 'state': result['state']}))
    finally:
        if fathom:
            fathom.close()


def main():
    kind = sys.argv[1]
    if kind not in ('acquisition', 'model'):
        raise ValueError('worker kind required')
    approved = json.loads(Path('/approval/selection.json').read_text())
    asyncio.run(execute(make_store(), approved, kind))


if __name__ == '__main__':
    main()
