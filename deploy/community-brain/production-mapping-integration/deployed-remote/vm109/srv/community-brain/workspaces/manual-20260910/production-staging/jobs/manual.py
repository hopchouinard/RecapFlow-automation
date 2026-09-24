"""One explicitly reviewed stage; never recover or dispatch the whole queue."""

import json
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Artifact, Job, Outbox, Source, Stage
from .store import fingerprint


def selection(store, job_id, name, generation, *, scope, excluded_jobs=()):
    """Return a nonsecret manifest binding approval to immutable inputs/artifacts."""
    job_id = UUID(str(job_id))
    if name not in {"acquisition", "processing", "indexing"}:
        raise ValueError("manual stage not permitted")
    if job_id in {UUID(str(value)) for value in excluded_jobs}:
        raise ValueError("excluded job")
    with Session(store.engine) as session:
        job = session.get(Job, job_id)
        stage = session.scalar(
            select(Stage).where(Stage.job_id == job_id, Stage.name == name)
        )
        if not job or job.scope != scope or not stage:
            raise ValueError("job/stage scope mismatch")
        if stage.generation != generation or stage.state != "queued":
            raise ValueError("stage requires explicit reconciliation or new selection")
        if stage.attempts != 0:
            raise ValueError("previous attempt requires reconciliation")
        if name == "indexing" and (
            job.processing != "succeeded" or job.artifacts != "ready"
        ):
            raise ValueError("artifacts not ready")
        event = session.scalar(
            select(Outbox).where(
                Outbox.stage_id == stage.id, Outbox.generation == generation
            )
        )
        if not event:
            raise ValueError("missing durable event")
        sources = {}
        for kind, source_id in job.sources.items():
            source = session.get(Source, UUID(source_id))
            if not source or source.scope != scope:
                raise ValueError("invalid source")
            store.storage.read(source.path, source.sha256)
            sources[kind] = [str(source.id), source.sha256]
        artifacts = {}
        for artifact in session.scalars(
            select(Artifact).where(Artifact.job_id == job_id)
        ):
            store.storage.read(artifact.path, artifact.sha256)
            artifacts[artifact.name] = artifact.sha256
        return {
            "job_id": str(job_id),
            "stage_id": str(stage.id),
            "stage": name,
            "generation": generation,
            "event_id": str(event.id),
            "scope": scope,
            "mode": job.mode,
            "identity_sha256": fingerprint(job.identity),
            "config_sha256": fingerprint(job.config),
            "sources": sources,
            "artifacts": artifacts,
        }


async def run_selected(
    store,
    approved,
    worker,
    connect,
    *,
    stream,
    subject,
    durable="community-brain-worker",
    excluded_jobs=(),
):
    """No daemon or implicit retries; unexpected queue delivery stops this run."""
    current = selection(
        store,
        approved["job_id"],
        approved["stage"],
        approved["generation"],
        scope=approved["scope"],
        excluded_jobs=excluded_jobs,
    )
    if current != approved or worker.store is not store:
        raise ValueError("selection changed")
    stage_id, event_id = UUID(approved["stage_id"]), UUID(approved["event_id"])
    with Session(store.engine) as session:
        event = session.get(Outbox, event_id)
        body = {
            "schema_version": 1,
            "event_id": str(event_id),
            "stage_id": str(stage_id),
            "generation": approved["generation"],
            "job_id": approved["job_id"],
            "occurred_at": event.created_at.isoformat(),
            "trace_id": str(event_id),
        }
    nc = await connect()
    try:
        js = nc.jetstream()
        sub = await js.pull_subscribe_bind(durable, stream=stream)
        await js.publish(
            subject, json.dumps(body).encode(), headers={"Nats-Msg-Id": str(event_id)}
        )
        with Session(store.engine) as session, session.begin():
            session.get(Outbox, event_id).sent_at = store.now(session)
        message = (await sub.fetch(1, timeout=10))[0]
        try:
            if json.loads(message.data) != body:
                raise ValueError("unexpected queued work")
            if (
                selection(
                    store,
                    approved["job_id"],
                    approved["stage"],
                    approved["generation"],
                    scope=approved["scope"],
                    excluded_jobs=excluded_jobs,
                )
                != approved
            ):
                raise ValueError("selection changed before execution")
        except Exception:
            await message.nak(delay=60)
            raise
        await worker.handle(message)
        with Session(store.engine) as session:
            stage = session.get(Stage, stage_id)
            if stage.state != "succeeded":
                raise RuntimeError("selected stage incomplete; review durable outcome")
            return {
                "stage_id": str(stage_id),
                "state": stage.state,
                "generation": stage.generation,
                "result": stage.result,
            }
    finally:
        await nc.close()
