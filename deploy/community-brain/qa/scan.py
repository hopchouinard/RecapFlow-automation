"""VM108 job selection and public readiness projection; no provider credential."""

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from community_brain.jobs.automatic import POLICY, next_stage, stop_stage
from community_brain.jobs.manual import selection
from community_brain.jobs.models import Job, Stage
from community_brain.jobs.runtime import make_store

SCOPE = 'community-brain-dev'
ROOT = Path('/state/files/qa-automation-public')


def atomic(path, value):
    path.parent.mkdir(mode=0o755, exist_ok=True)
    temporary = path.with_name('.' + path.name + '.next')
    with temporary.open('w') as stream:
        os.fchmod(stream.fileno(), 0o644)
        json.dump(value, stream, sort_keys=True)
        stream.write('\n')
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    fd = os.open(path.parent, os.O_DIRECTORY | os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def scan(store):
    selected = next_stage(store, SCOPE)
    with Session(store.engine) as session:
        jobs = session.scalars(select(Job).where(Job.scope == SCOPE,
            Job.parent_id.is_(None), Job.config['automation_policy'].astext == POLICY)).all()
        stages = session.scalars(select(Stage).where(Stage.job_id.in_([job.id for job in jobs]))).all()
        problems = [s for s in stages if s.name in ('acquisition', 'processing', 'indexing')
                    and s.state in ('failed', 'partial', 'outcome_unknown')]
        return {'next': selected, 'completed': [str(j.id) for j in jobs if j.indexing == 'complete'],
                'attention': bool(problems), 'problems': [
                    {'job_id': str(s.job_id), 'stage': s.name, 'state': s.state,
                     'error': s.error} for s in problems]}


def main():
    if os.environ.get('CB_CORPUS_SCOPE') != SCOPE or os.environ.get('CB_ENABLE_NETWORK_PUBLICATION') != 'false':
        raise ValueError('development scope required')
    store = make_store()
    command = sys.argv[1]
    if command == 'next':
        result = scan(store)
    elif command == 'select':
        result = selection(store, sys.argv[2], sys.argv[3], int(sys.argv[4]), scope=SCOPE)
    elif command == 'stop':
        result = {'stopped': stop_stage(store, sys.argv[2], 'qa_execution_requires_review')}
    elif command == 'project':
        runner, expiry, checkpoint_json = sys.argv[2], int(sys.argv[3]), sys.argv[4]
        if runner not in ('idle', 'worker_running', 'stage_completed', 'needs_input',
                          'paused', 'attention_required', 'awaiting_checkpoint'):
            raise ValueError('invalid runner status')
        checkpoints = json.loads(checkpoint_json)
        if not isinstance(checkpoints, dict) or not all(
            isinstance(UUID(key), UUID) and value in ('verified', 'requires_review')
            for key, value in checkpoints.items()
        ):
            raise ValueError('invalid checkpoint projection')
        now = datetime.now(timezone.utc).isoformat()
        expired = datetime.now(timezone.utc).timestamp() >= expiry
        result = {'processing': {
            'checked_at': now, 'management_checked_at': now,
            'paused': runner == 'paused', 'attention': runner == 'attention_required',
            'boot_reconciled': True, 'checkpoint_pending': runner == 'awaiting_checkpoint',
            'management_attention': False, 'credentials_expired': expired,
            'runner': runner, 'renewal': 'failed' if expired else 'not_due'},
            'checkpoints': checkpoints, 'management_attention': False}
        atomic(ROOT / 'checkpoints.json', result)
        result = {'projected': runner, 'checkpoints': len(checkpoints)}
    else:
        raise ValueError('unsupported QA scan')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
