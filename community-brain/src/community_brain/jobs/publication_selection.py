"""Explicit offline publication selection; never extends the weekly selector."""

from datetime import date, timedelta
import re
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from .manual import run_selected
from .models import Artifact, Job, Outbox, Stage
from .store import fingerprint
from .worker import Worker


def six_files(local_date):
    day = date.fromisoformat(local_date)
    invite = day + timedelta(days=(1 - day.weekday()) % 7 or 7)
    return {
        "transcript.txt",
        "prepared-transcript.md",
        "extracted-signal.md",
        "community-post.md",
        "community-post-compressed.md",
        f"{invite.isoformat()}-weekly-invite.md",
    }


def selection(store, job_id, name, generation, *, scope, checkpoint, excluded_jobs=()):
    job_id = UUID(str(job_id))
    if name not in {"git", "distribution"}:
        raise ValueError("only publication stages permitted")
    if job_id in {UUID(str(v)) for v in excluded_jobs}:
        raise ValueError("excluded job")
    if (
        checkpoint.get("job_id") != str(job_id)
        or checkpoint.get("verified") is not True
        or not re.fullmatch(r"[a-f0-9]{64}", checkpoint.get("manifest_sha256", ""))
    ):
        raise ValueError("matching verified checkpoint required")
    with Session(store.engine) as session:
        job = session.get(Job, job_id)
        stage = session.scalar(
            select(Stage).where(Stage.job_id == job_id, Stage.name == name)
        )
        if not job or job.scope != scope or not stage:
            raise ValueError("job/stage scope mismatch")
        if (
            job.parent_id
            or job.mode != "weekly"
            or job.processing != "succeeded"
            or job.artifacts != "ready"
            or job.indexing != "complete"
        ):
            raise ValueError("complete root weekly job required")
        if session.scalar(
            select(Stage.id).where(
                Stage.job_id == job_id,
                Stage.state.in_(["running", "partial", "outcome_unknown"]),
            )
        ):
            raise ValueError("job requires reconciliation")
        if (
            stage.state != "queued"
            or stage.generation != generation
            or stage.attempts != 0
        ):
            raise ValueError("stage requires reconciliation or new selection")
        event = session.scalar(
            select(Outbox).where(
                Outbox.stage_id == stage.id, Outbox.generation == generation
            )
        )
        if not event:
            raise ValueError("missing durable event")
        artifacts = {}
        for artifact in session.scalars(
            select(Artifact).where(Artifact.job_id == job_id)
        ):
            store.storage.read(artifact.path, artifact.sha256)
            artifacts[artifact.name] = artifact.sha256
        if set(artifacts) != six_files(job.identity["local_date"]):
            raise ValueError("exact six approved files required")
        return {
            "job_id": str(job_id),
            "stage_id": str(stage.id),
            "stage": name,
            "generation": generation,
            "event_id": str(event.id),
            "scope": scope,
            "identity_sha256": fingerprint(job.identity),
            "config_sha256": fingerprint(job.config),
            "artifacts": artifacts,
            "checkpoint_sha256": checkpoint["manifest_sha256"],
        }


async def rehearse_selected(
    store,
    approved,
    handlers,
    checkpoint,
    connect,
    *,
    stream,
    subject,
    durable="community-brain-worker",
):
    """Fixture/local destinations only. Live activation needs separate wiring."""
    from pathlib import Path

    if (
        handlers.store is not store
        or handlers.allow_network_publish
        or handlers.release_publisher is not None
    ):
        raise ValueError("remote publication must remain disabled")
    if approved["stage"] == "git" and (
        not handlers.git_remote or not Path(handlers.git_remote).is_dir()
    ):
        raise ValueError("local Git fixture required")

    def no_model(_):
        raise RuntimeError("model calls forbidden in publication worker")

    def select_manifest(*args, **kwargs):
        return selection(*args, checkpoint=checkpoint, **kwargs)

    worker = Worker(
        store,
        no_model,
        handlers={name: getattr(handlers, name) for name in ("git", "distribution")},
    )
    return await run_selected(
        store,
        approved,
        worker,
        connect,
        stream=stream,
        subject=subject,
        durable=durable,
        select_manifest=select_manifest,
    )
