"""Real selected DB/JetStream stages with local Git and mocked release effects."""

import asyncio
import hashlib
import importlib.util
from pathlib import Path

import nats
import pytest
from nats.js.api import ConsumerConfig
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from community_brain.jobs.manual import run_selected
from community_brain.jobs.models import Artifact, Job, ModelCall
from community_brain.jobs.prepared_publication import PreparedPublication
from community_brain.jobs.publication_selection import selection
from community_brain.jobs.worker import Worker
from community_brain.processing.pipeline import OutcomeUnknown
from test_publication_selection import store, ready

spec = importlib.util.spec_from_file_location(
    "local_prepared_git",
    Path(__file__).resolve().parents[2]
    / "community-brain/tests/test_prepared_publication.py",
)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


@pytest.mark.parametrize("lose_release", [False, True])
def test_two_selected_publication_stages_leave_models_and_inputs_unchanged(
    store, services, tmp_path, monkeypatch, lose_release
):
    job_id, checkpoint = ready(store)
    with Session(store.engine) as s:
        job = s.get(Job, job_id)
        local_date = job.identity["local_date"]
        sources = job.sources
        records = s.scalars(select(Artifact).where(Artifact.job_id == job_id)).all()
        content = {
            a.name: store.storage.read(a.path, a.sha256).decode() for a in records
        }
        calls = s.scalar(select(func.count(ModelCall.id)))
    operator, files = helper.prepared(
        tmp_path,
        "operator",
        {"output/" + local_date + "/" + n: b for n, b in content.items()},
    )
    consumer, pins = helper.prepared(
        tmp_path, "consumer", {"download-corpus.sh": "reviewed pins"}
    )
    candidate = tmp_path / "candidate"
    candidate.mkdir()
    for name in ["corpus-v1.2.0.tar.gz", "corpus-manifest.json", "sha256sum.txt"]:
        (candidate / name).write_text("fixture")
    plan = {
        "job_id": str(job_id),
        "scope": "community-brain",
        "version": "v1.2.0",
        "local_date": local_date,
        "operator": operator.spec,
        "consumer": consumer.spec,
        "installer_sha256": pins["download-corpus.sh"],
        "artifacts": {
            n: hashlib.sha256(b.encode()).hexdigest() for n, b in content.items()
        },
        "assets": {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in candidate.iterdir()
        },
    }
    # Candidate archive integrity is independently exercised against the real
    # delivered corpus. This test isolates durable queue + external-effect order.
    monkeypatch.setattr(
        "community_brain.jobs.prepared_publication.validate_bundle",
        lambda _: {
            "corpus_version": "v1.2.0",
            "session_count": 88,
            "chunk_count": 1924,
        },
    )

    class Publisher:
        repository = consumer.spec["repository"]
        commit = consumer.spec["commit"]

        def publish(self, *args):
            assert consumer.head("refs/heads/main") == consumer.spec["base"]
            if lose_release:
                raise OutcomeUnknown("lost release response")
            return {"release_id": 1, "tag": "v1.2.0"}

    handler = PreparedPublication(
        plan, candidate, operator, consumer, Publisher(), tmp_path / "journal"
    )

    def no_model(_):
        pytest.fail("publication must not call a model")

    worker = Worker(
        store,
        no_model,
        handlers={"git": handler.git, "distribution": handler.distribution},
    )

    async def exercise(stage):
        approved = selection(
            store, job_id, stage, 1, scope="community-brain", checkpoint=checkpoint
        )
        nc = await nats.connect(services[1])
        js = nc.jetstream()
        await js.add_stream(name="PUBLISH", subjects=["publish.ready"])
        await js.add_consumer(
            "PUBLISH",
            ConsumerConfig(
                durable_name="community-brain-worker",
                filter_subject="publish.ready",
                ack_policy="explicit",
            ),
        )
        try:
            return await run_selected(
                store,
                approved,
                worker,
                lambda: nats.connect(services[1]),
                stream="PUBLISH",
                subject="publish.ready",
                select_manifest=lambda *a, **kw: selection(
                    *a, checkpoint=checkpoint, **kw
                ),
            )
        finally:
            await js.delete_stream("PUBLISH")
            await nc.close()

    assert asyncio.run(exercise("git"))["state"] == "succeeded"
    store.request_publication(
        "community-brain", "fixture", job_id, "distribution", "release"
    )
    if lose_release:
        with pytest.raises(RuntimeError, match="incomplete"):
            asyncio.run(exercise("distribution"))
    else:
        assert asyncio.run(exercise("distribution"))["state"] == "succeeded"
    with Session(store.engine) as s:
        job = s.get(Job, job_id)
        assert job.git == "complete"
        assert job.distribution == ("outcome_unknown" if lose_release else "released")
        assert (
            job.sources == sources
            and s.scalar(select(func.count(ModelCall.id))) == calls
        )
        assert s.scalar(select(func.count(Artifact.id))) == 6
    assert (
        consumer.head("refs/heads/main")
        == consumer.spec["base" if lose_release else "commit"]
    )
