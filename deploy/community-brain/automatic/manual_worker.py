"""Production oneshot adapter; only a reviewed selection, never a queue sweep."""

import asyncio
import fcntl
import json
import os
import sys
from contextlib import ExitStack
from pathlib import Path
from uuid import UUID

import lancedb
import nats
from bounded_worker import STREAM, SUBJECT, connection_options
from community_brain.jobs.manual import run_selected, selection
from community_brain.jobs.models import Job
from community_brain.jobs.publication import PublicationHandlers, corpus_lock
from community_brain.jobs.runtime import make_store
from community_brain.jobs.worker import OpenRouter, Worker
from community_brain.processing.pipeline import OutcomeUnknown
from indexing_budget import allowance, audited_indexing
from selected_fathom import SelectedFathom
from sqlalchemy.orm import Session

EXCLUDED = (
    "f6e9abed-e862-4eb7-a231-e98467adcaba",
    "91d77409-afed-4625-97cb-748c8b637991",
)
PROCESSING_CEILING = 20  # Selected real weekly fixture previously required 15 requests.


class ManualProvider(OpenRouter):
    def __init__(self, key):
        super().__init__(key)
        self.calls = 0

    def __call__(self, request):
        if self.calls >= PROCESSING_CEILING:
            raise OutcomeUnknown("manual processing request ceiling reached")
        try:
            allowance(self.api_key)
        except Exception as exc:
            raise OutcomeUnknown("manual allowance requires review") from exc
        self.calls += 1
        return super().__call__(request)


def reviewed_selection(store, job_id, name, generation):
    approved = selection(
        store, job_id, name, generation, scope="community-brain", excluded_jobs=EXCLUDED
    )
    automatic = os.environ.get("CB_AUTOMATIC_ONLY") == "true"
    if automatic:
        from community_brain.jobs.automatic import require_automatic

        require_automatic(store, job_id)
    if automatic or name == "indexing":
        with Session(store.engine) as session:
            date = session.get(Job, UUID(str(job_id))).identity["local_date"]
        root = Path(os.environ["CB_CORPUS_ROOT"])
        reservation = root / "sessions" / f"{date}.json"
        if reservation.exists():
            if json.loads(reservation.read_text())["job_id"] != str(job_id):
                raise ValueError(
                    "existing session requires a separate replacement decision"
                )
        else:
            db = lancedb.connect(str(root / "lancedb/nomic-v1"))
            if "chunks" in db.list_tables().tables and db.open_table(
                "chunks"
            ).count_rows(f"session_id = '{date}'"):
                raise ValueError(
                    "existing session requires a separate replacement decision"
                )
    return approved


def complete_fts(handler, corpus, job_id):
    result = handler.indexing(job_id)
    # Operational maintenance after ingestion, under the same corpus lock.
    # Frozen extraction/chunking semantics and known partial outcomes stay intact.
    with corpus_lock(corpus):
        table = lancedb.connect(str(Path(corpus) / "lancedb/nomic-v1")).open_table(
            "chunks"
        )
        stats = table.index_stats("bm25_text_idx")
        if (
            not stats
            or stats["num_unindexed_rows"]
            or stats["num_indexed_rows"] != table.count_rows()
        ):
            table.create_fts_index("bm25_text", replace=True)
        stats = table.index_stats("bm25_text_idx")
        if (
            not stats
            or stats["num_unindexed_rows"]
            or stats["num_indexed_rows"] != table.count_rows()
        ):
            raise RuntimeError("FTS coverage requires reconciliation")
        result["fts_indexed_rows"] = stats["num_indexed_rows"]
    return result


async def execute(store, approved):
    if (
        reviewed_selection(
            store, approved["job_id"], approved["stage"], approved["generation"]
        )
        != approved
    ):
        raise ValueError("selection changed")
    if os.environ.get("CB_ENABLE_NETWORK_PUBLICATION") != "false":
        raise ValueError("network publication must remain disabled")
    name = approved["stage"]
    corpus = Path(os.environ["CB_CORPUS_ROOT"])

    def no_processing(request):
        raise RuntimeError("processing not selected")

    worker = Worker(store, no_processing)
    fathom = None
    context = ExitStack()
    try:
        if name == "acquisition":
            if "CB_OPENROUTER_API_KEY" in os.environ:
                raise ValueError("model key forbidden in acquisition worker")
            with Session(store.engine) as session:
                identity = session.get(Job, UUID(approved["job_id"])).identity
            fathom = SelectedFathom(
                os.environ["CB_FATHOM_API_KEY"],
                identity["meeting_id"],
                identity["started_at"],
            )
            worker.fathom = fathom
        else:
            if "CB_FATHOM_API_KEY" in os.environ:
                raise ValueError("Fathom key forbidden outside acquisition worker")
            if os.environ.get("CB_ENABLE_MODEL_CALLS") != "true":
                raise ValueError("model calls not enabled")
            key = os.environ["CB_OPENROUTER_API_KEY"]
            if name == "processing":
                worker.transport = ManualProvider(key)
            else:
                os.environ["OPENROUTER_API_KEY"] = key
                handler = PublicationHandlers(
                    store,
                    corpus,
                    os.environ["CB_PIPELINE_CONFIG_DIR"],
                    os.environ["OLLAMA_BASE_URL"],
                )
                worker.handlers = {
                    "indexing": lambda job: complete_fts(handler, corpus, job)
                }
                context.enter_context(
                    audited_indexing(
                        store,
                        key,
                        Path(os.environ["CB_STORAGE_ROOT"])
                        / f"indexing-{approved['job_id']}-{approved['generation']}.jsonl",
                    )
                )
        result = await run_selected(
            store,
            approved,
            worker,
            lambda: nats.connect(**connection_options(os.environ)),
            stream=STREAM,
            subject=SUBJECT,
            excluded_jobs=EXCLUDED,
        )
        print(
            json.dumps(
                {
                    "job_id": approved["job_id"],
                    "stage": name,
                    "generation": approved["generation"],
                    "state": result["state"],
                }
            )
        )
    finally:
        context.close()
        if fathom:
            fathom.close()


if __name__ == "__main__":
    store = make_store()
    if sys.argv[1] == "inspect":
        print(
            json.dumps(
                reviewed_selection(store, sys.argv[2], sys.argv[3], int(sys.argv[4])),
                indent=2,
            )
        )
    elif sys.argv[1] == "execute":
        with (Path(os.environ["CB_STORAGE_ROOT"]) / ".manual-worker.lock").open(
            "a"
        ) as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            asyncio.run(
                execute(store, json.loads(Path("/approval/selection.json").read_text()))
            )
    else:
        raise ValueError("explicit inspect or execute required")
