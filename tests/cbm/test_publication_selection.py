"""Selected publication uses fixture DB/queue and local destinations only."""

import asyncio
import subprocess
from uuid import UUID

import nats
import pytest
from nats.js.api import ConsumerConfig
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from community_brain.jobs.models import Artifact, Job, ModelCall, Stage
from community_brain.jobs.publication import PublicationHandlers
from community_brain.jobs.publication_selection import selection, rehearse_selected
from community_brain.jobs.worker import Worker
from test_automatic import store, accept, request
from test_application import fake_model


def ready(store):
    job_id = accept(store, request(store))
    with Session(store.engine) as s:
        stage_id = s.scalar(
            select(Stage.id).where(Stage.job_id == job_id, Stage.name == "processing")
        )
    worker = Worker(store, fake_model)
    worker.execute(stage_id, store.claim(stage_id, worker.owner))
    with Session(store.engine) as s, s.begin():
        s.get(Job, job_id).indexing = "complete"
        stage = s.scalar(
            select(Stage).where(Stage.job_id == job_id, Stage.name == "indexing")
        )
        stage.state = "succeeded"
    checkpoint = {"job_id": str(job_id), "verified": True, "manifest_sha256": "a" * 64}
    store.request_publication("community-brain", "fixture", job_id, "git", "publish")
    return job_id, checkpoint


def approve(store, job_id, checkpoint):
    return selection(
        store, job_id, "git", 1, scope="community-brain", checkpoint=checkpoint
    )


def test_selected_local_git_publishes_all_six_without_model_calls(
    store, services, tmp_path
):
    job_id, checkpoint = ready(store)
    approved = approve(store, job_id, checkpoint)
    assert len(approved["artifacts"]) == 6 and "transcript.txt" in approved["artifacts"]
    seed = tmp_path / "seed"
    seed.mkdir()
    for args in (
        ["init", "-b", "main"],
        [
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@localhost",
            "-c",
            "commit.gpgsign=false",
            "commit",
            "--allow-empty",
            "-m",
            "fixture",
        ],
    ):
        subprocess.run(["git", *args], cwd=seed, check=True, capture_output=True)
    remote = tmp_path / "remote.git"
    subprocess.run(
        ["git", "clone", "--bare", str(seed), str(remote)],
        check=True,
        capture_output=True,
    )
    handlers = PublicationHandlers(
        store, tmp_path / "corpus", tmp_path / "config", None, str(remote)
    )
    with Session(store.engine) as s:
        calls_before = s.scalar(select(func.count(ModelCall.id)))

    async def exercise():
        nc = await nats.connect(services[1])
        js = nc.jetstream()
        await js.add_stream(name="PUBLICATION", subjects=["publication.ready"])
        await js.add_consumer(
            "PUBLICATION",
            ConsumerConfig(
                durable_name="community-brain-worker",
                filter_subject="publication.ready",
                ack_policy="explicit",
            ),
        )
        try:
            return await rehearse_selected(
                store,
                approved,
                handlers,
                checkpoint,
                lambda: nats.connect(services[1]),
                stream="PUBLICATION",
                subject="publication.ready",
            )
        finally:
            await js.delete_stream("PUBLICATION")
            await nc.close()

    result = asyncio.run(exercise())
    assert result["state"] == "succeeded"
    with Session(store.engine) as s:
        assert s.scalar(select(func.count(ModelCall.id))) == calls_before
        assert s.get(Job, job_id).git == "complete"
        assert s.get(Job, job_id).distribution == "not_requested"
    names = subprocess.check_output(
        ["git", "--git-dir", str(remote), "ls-tree", "-r", "--name-only", "HEAD"],
        text=True,
    ).splitlines()
    assert sorted(n.rsplit("/", 1)[-1] for n in names) == sorted(approved["artifacts"])
    with pytest.raises(ValueError, match="reconciliation"):
        approve(store, job_id, checkpoint)


@pytest.mark.parametrize("failure", ["checkpoint", "extra_file", "unknown", "scope"])
def test_selection_rejects_unreviewed_work(store, failure):
    job_id, checkpoint = ready(store)
    scope = "community-brain"
    if failure == "checkpoint":
        checkpoint["job_id"] = str(UUID(int=1))
    if failure == "scope":
        scope = "other"
    with Session(store.engine) as s, s.begin():
        if failure == "extra_file":
            a = s.scalar(select(Artifact).where(Artifact.job_id == job_id))
            a.name = "unexpected.txt"
        if failure == "unknown":
            a = s.scalar(
                select(Stage).where(Stage.job_id == job_id, Stage.name == "indexing")
            )
            a.state = "outcome_unknown"
    with pytest.raises(ValueError):
        selection(store, job_id, "git", 1, scope=scope, checkpoint=checkpoint)


def test_remote_enablement_rejected_before_queue_connection(store, tmp_path):
    job_id, checkpoint = ready(store)
    handlers = PublicationHandlers(
        store, tmp_path, tmp_path, None, allow_network_publish=True
    )

    async def no_connect():
        pytest.fail("must not connect")

    with pytest.raises(ValueError, match="disabled"):
        asyncio.run(
            rehearse_selected(
                store,
                approve(store, job_id, checkpoint),
                handlers,
                checkpoint,
                no_connect,
                stream="unused",
                subject="unused",
            )
        )
