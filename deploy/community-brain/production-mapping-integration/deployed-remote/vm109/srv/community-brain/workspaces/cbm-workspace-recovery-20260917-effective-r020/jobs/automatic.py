"""New-submission-only automatic stages; no broad recovery or outbox replay."""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Attempt, Job, Stage

POLICY = "new-meeting-full-loop-v1"
STAGES = ("acquisition", "processing", "indexing")


def eligible(job):
    return job.parent_id is None and job.config.get("automation_policy") == POLICY


def require_automatic(store, job_id):
    with Session(store.engine) as session:
        job = session.get(Job, UUID(str(job_id)))
        if not job or not eligible(job):
            raise ValueError("job is not opted into automatic processing")


def stop_stage(store, stage_id, reason):
    """Terminal attention state, never an inferred provider retry."""
    with Session(store.engine) as session, session.begin():
        stage = session.scalar(
            select(Stage).where(Stage.id == UUID(str(stage_id))).with_for_update()
        )
        if not stage or stage.name not in STAGES:
            return False
        job = session.get(Job, stage.job_id)
        if not eligible(job) or stage.state not in {"queued", "running"}:
            return False
        now = store.now(session)
        if stage.state == "running" and stage.lease_until and stage.lease_until > now:
            return False
        if stage.state == "running":
            attempt = session.scalar(
                select(Attempt).where(
                    Attempt.stage_id == stage.id, Attempt.fence == stage.fence
                )
            )
            if attempt:
                attempt.state = "outcome_unknown"
                attempt.reason = reason
                attempt.finished_at = now
        stage.fence += 1
        stage.state = "outcome_unknown"
        stage.error = reason
        stage.lease_until = None
        setattr(job, stage.name, "outcome_unknown")
        return True


def next_stage(store, scope):
    # Expired work is fenced and surfaced, never replayed automatically.
    with Session(store.engine) as session:
        stale = session.scalars(
            select(Stage.id)
            .join(Job)
            .where(
                Job.scope == scope,
                Job.config["automation_policy"].astext == POLICY,
                Stage.name.in_(STAGES),
                Stage.state == "running",
                Stage.lease_until <= store.now(session),
            )
        ).all()
    for stage_id in stale:
        stop_stage(store, stage_id, "automatic_lease_expired_requires_review")
    with Session(store.engine) as session:
        rows = session.execute(
            select(Job, Stage)
            .join(Stage)
            .where(
                Job.scope == scope,
                Job.parent_id.is_(None),
                Job.config["automation_policy"].astext == POLICY,
                Stage.name.in_(STAGES),
                Stage.state == "queued",
                Stage.attempts == 0,
                Stage.generation >= 1,
            )
            .order_by(Job.created_at, Stage.id)
        ).all()
        for job, stage in rows:
            if stage.generation > 1 and not session.scalar(
                select(Attempt.id)
                .where(
                    Attempt.stage_id == stage.id,
                    Attempt.fence == -stage.generation,
                    Attempt.state == "safe_resume_authorized",
                )
                .limit(1)
            ):
                continue
            # Acquisition must finish before its newly bound transcript can run.
            if stage.name == "processing":
                acquisition = session.scalar(
                    select(Stage).where(
                        Stage.job_id == job.id, Stage.name == "acquisition"
                    )
                )
                if acquisition.state not in {"blocked", "succeeded"}:
                    continue
            if stage.name == "indexing" and (
                job.processing != "succeeded" or job.artifacts != "ready"
            ):
                continue
            return {
                "job_id": str(job.id),
                "stage_id": str(stage.id),
                "stage": stage.name,
                "generation": stage.generation,
            }
    return None
