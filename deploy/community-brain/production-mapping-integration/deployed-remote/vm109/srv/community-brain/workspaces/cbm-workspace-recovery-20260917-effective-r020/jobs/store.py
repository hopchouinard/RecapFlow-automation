from datetime import timedelta
import hashlib
import json
from uuid import uuid4

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from community_brain.processing.pipeline import SNAPSHOT
from .models import Artifact, Attempt, Job, ModelCall, Operation, Outbox, Source, Stage


class Conflict(ValueError):
    pass


def fingerprint(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()


class Store:
    def __init__(self, engine, storage, aliases_supplier=None, indexed_date=None):
        self.engine, self.storage = engine, storage
        self.aliases_supplier = aliases_supplier
        self.indexed_date = indexed_date

    @staticmethod
    def now(session):
        return session.scalar(select(func.clock_timestamp()))

    @staticmethod
    def enqueue(session, stage):
        stage.generation += 1
        session.add(Outbox(stage_id=stage.id, generation=stage.generation))

    def accept(self, scope, principal, key, request, parent=None, automatic=False):
        # Serialize natural meeting identity as well as caller idempotency keys.
        with Session(self.engine) as s, s.begin():
            from sqlalchemy import text

            operation = "submit" if parent is None else "rerun:" + str(parent)
            key_lock = int(fingerprint([scope, principal, operation, key])[:15], 16)
            s.execute(text("SELECT pg_advisory_xact_lock(:key)"), {"key": key_lock})
            lock = int(fingerprint([scope, request["identity"]["meeting_id"]])[:15], 16)
            s.execute(text("SELECT pg_advisory_xact_lock(:key)"), {"key": lock})
            request_hash = fingerprint(request)
            existing = s.scalar(
                select(Operation).where(
                    Operation.scope == scope,
                    Operation.principal == principal,
                    Operation.operation == operation,
                    Operation.key == key,
                )
            )
            if existing:
                if existing.request_hash != request_hash:
                    raise Conflict("idempotency_conflict")
                return existing.job_id, False
            if parent is None:
                candidates = s.scalars(
                    select(Job).where(
                        Job.scope == scope,
                        Job.identity["meeting_id"].astext
                        == request["identity"]["meeting_id"],
                    )
                ).all()
                if any(
                    candidate.identity != request["identity"]
                    for candidate in candidates
                ):
                    raise Conflict("meeting_identity_conflict")
                existing = s.scalar(
                    select(Job).where(
                        Job.scope == scope,
                        Job.request_hash == request_hash,
                        Job.parent_id.is_(None),
                    )
                )
                if existing is None:
                    requested = {
                        k: v
                        for k, v in request.get("sources", {}).items()
                        if k != "aliases"
                    }
                    existing = next(
                        (
                            candidate
                            for candidate in candidates
                            if candidate.parent_id is None
                            and candidate.mode == request["mode"]
                            and candidate.version
                            == request.get("version", "processing-v1")
                            and {
                                k: v
                                for k, v in candidate.sources.items()
                                if k != "aliases"
                            }
                            == requested
                        ),
                        None,
                    )
                if existing:
                    s.add(
                        Operation(
                            scope=scope,
                            principal=principal,
                            operation=operation,
                            key=key,
                            request_hash=request_hash,
                            job_id=existing.id,
                        )
                    )
                    return existing.id, False
            if automatic and parent is None:
                date = request["identity"]["local_date"]
                date_lock = int(fingerprint([scope, "automatic-date", date])[:15], 16)
                s.execute(
                    text("SELECT pg_advisory_xact_lock(:key)"), {"key": date_lock}
                )
                if self.indexed_date is None:
                    raise Conflict("automatic_date_guard_unavailable")
                if self.indexed_date(date):
                    raise Conflict("meeting_already_indexed")
                if s.scalar(
                    select(Job.id).where(
                        Job.scope == scope, Job.identity["local_date"].astext == date
                    )
                ):
                    raise Conflict("meeting_date_already_submitted")
            sources = dict(request.get("sources", {}))
            self.validate_sources(s, scope, request["identity"]["meeting_id"], sources)
            if "aliases" not in sources and self.aliases_supplier is not None:
                sources["aliases"] = self.add_source(
                    scope,
                    request["identity"]["meeting_id"],
                    "aliases",
                    self.aliases_supplier(),
                )
            ready = "transcript" in sources and (
                request["mode"] == "transcript_backfill" or "chat" in sources
            )
            job = Job(
                scope=scope,
                principal=principal,
                key=key,
                request_hash=request_hash,
                identity=request["identity"],
                sources=sources,
                mode=request["mode"],
                parent_id=parent,
                config={
                    **SNAPSHOT[request["mode"]]["config"],
                    **(
                        {"automation_policy": "new-meeting-full-loop-v1"}
                        if automatic and parent is None
                        else {}
                    ),
                    "prompt_snapshot_sha256": fingerprint(
                        SNAPSHOT[request["mode"]]["prompts"]
                    ),
                },
                reason=request.get("reason"),
                processing="queued" if ready else "waiting_for_input",
            )
            s.add(job)
            s.flush()
            s.add(
                Operation(
                    scope=scope,
                    principal=principal,
                    operation=operation,
                    key=key,
                    request_hash=request_hash,
                    job_id=job.id,
                )
            )
            acquire = (
                request["identity"].get("provider") == "fathom"
                and "transcript" not in sources
            )
            for name in (
                "acquisition",
                "processing",
                "indexing",
                "git",
                "distribution",
            ):
                stage = Stage(
                    job_id=job.id,
                    name=name,
                    state="queued"
                    if (ready and name == "processing")
                    or (acquire and name == "acquisition")
                    else "blocked",
                )
                s.add(stage)
                s.flush()
                if stage.state == "queued":
                    self.enqueue(s, stage)
            return job.id, True

    def add_source(self, scope, meeting_id, kind, content):
        from sqlalchemy.dialects.postgresql import insert

        path, sha, size = self.storage.put(content.encode())
        with Session(self.engine) as s, s.begin():
            identity = s.execute(
                insert(Source)
                .values(
                    id=uuid4(),
                    scope=scope,
                    meeting_id=meeting_id,
                    kind=kind,
                    sha256=sha,
                    path=path,
                    size=size,
                )
                .on_conflict_do_nothing()
                .returning(Source.id)
            ).scalar_one_or_none()
            if identity is None:
                identity = s.scalar(
                    select(Source.id).where(
                        Source.scope == scope,
                        Source.meeting_id == meeting_id,
                        Source.kind == kind,
                        Source.sha256 == sha,
                    )
                )
            return str(identity)

    def validate_sources(self, s, scope, meeting, sources):
        from uuid import UUID

        for kind, identity in sources.items():
            source = s.get(Source, UUID(str(identity)))
            if (
                not source
                or source.scope != scope
                or source.meeting_id != meeting
                or source.kind != kind
            ):
                raise Conflict("invalid_source_identity")

    @staticmethod
    def safe_retry_available(session, job, stage):
        if (
            job.parent_id is not None
            or job.config.get("automation_policy") != "new-meeting-full-loop-v1"
            or stage.state != "failed"
            or stage.generation >= 3
        ):
            return False
        if stage.name == "acquisition":
            return (
                job.processing == "waiting_for_input"
                and "transcript" not in job.sources
            )
        if stage.name == "processing":
            return not session.scalar(
                select(ModelCall.id).where(ModelCall.job_id == job.id).limit(1)
            ) and not session.scalar(
                select(Artifact.id).where(Artifact.job_id == job.id).limit(1)
            )
        return False

    def bind_sources(self, scope, job_id, sources, *, acquisition_owner=None):
        with Session(self.engine) as s, s.begin():
            # Match the worker's stage-before-job lock order.
            acquisition = s.scalar(
                select(Stage)
                .join(Job)
                .where(
                    Stage.job_id == job_id,
                    Job.scope == scope,
                    Stage.name == "acquisition",
                )
                .with_for_update(of=Stage)
            )
            job = s.scalar(
                select(Job)
                .where(Job.id == job_id, Job.scope == scope)
                .with_for_update()
            )
            if not job:
                raise KeyError("not_found")
            if sources and all(job.sources.get(k) == v for k, v in sources.items()):
                return
            if job.processing != "waiting_for_input":
                raise Conflict("source_revision_frozen")
            if "transcript" in sources and acquisition.state in {
                "running",
                "outcome_unknown",
                "partial",
            }:
                if acquisition_owner is None:
                    raise Conflict("acquisition_requires_review")
                fence, owner = acquisition_owner
                self.owned(s, acquisition.id, fence, owner)
            self.validate_sources(s, scope, job.identity["meeting_id"], sources)
            if any(
                k in job.sources and job.sources[k] != v for k, v in sources.items()
            ):
                raise Conflict("source_revision_frozen")
            job.sources = {**job.sources, **sources}
            if "transcript" in sources and acquisition.state in {"failed", "queued"}:
                acquisition.state = "succeeded"
                acquisition.error = None
                acquisition.fence += 1
                acquisition.result = {
                    "source_id": sources["transcript"],
                    "resolution": "user_supplied_transcript",
                    "prior_attempt_preserved": True,
                }
            if "transcript" in job.sources and (
                job.mode == "transcript_backfill" or "chat" in job.sources
            ):
                job.processing = "queued"
                stage = s.scalar(
                    select(Stage).where(
                        Stage.job_id == job.id, Stage.name == "processing"
                    )
                )
                stage.state = "queued"
                self.enqueue(s, stage)

    def claim(self, stage_id, owner, expected_generation=None):
        with Session(self.engine) as s, s.begin():
            stage = s.scalar(
                select(Stage).where(Stage.id == stage_id).with_for_update()
            )
            now = self.now(s)
            if (
                not stage
                or (
                    expected_generation is not None
                    and stage.generation != expected_generation
                )
                or stage.state not in ("queued", "retry_wait")
                or (stage.due_at and stage.due_at > now)
            ):
                return None
            stage.fence += 1
            stage.attempts += 1
            stage.owner = owner
            stage.state = "running"
            stage.lease_until = now + timedelta(seconds=60)
            job = s.get(Job, stage.job_id)
            setattr(job, stage.name, "running")
            s.add(Attempt(stage_id=stage.id, fence=stage.fence, owner=owner))
            return stage.fence

    def owned(self, s, stage_id, fence, owner):
        stage = s.scalar(select(Stage).where(Stage.id == stage_id).with_for_update())
        if (
            not stage
            or stage.state != "running"
            or stage.fence != fence
            or stage.owner != owner
            or stage.lease_until <= self.now(s)
        ):
            raise Conflict("claim_lost")
        return stage

    def heartbeat(self, stage_id, fence, owner):
        with Session(self.engine) as s, s.begin():
            stage = self.owned(s, stage_id, fence, owner)
            stage.lease_until = self.now(s) + timedelta(seconds=60)

    def finish(
        self, stage_id, fence, owner, state="succeeded", error=None, result=None
    ):
        with Session(self.engine) as s, s.begin():
            stage = self.owned(s, stage_id, fence, owner)
            stage.state = state
            stage.error = error
            stage.result = result
            stage.lease_until = None
            attempt = s.scalar(
                select(Attempt).where(
                    Attempt.stage_id == stage_id, Attempt.fence == fence
                )
            )
            attempt.state = state
            attempt.reason = error
            attempt.finished_at = self.now(s)
            job = s.get(Job, stage.job_id)
            setattr(
                job,
                stage.name,
                (
                    "complete"
                    if stage.name in ("indexing", "git")
                    else "released"
                    if stage.name == "distribution"
                    else "succeeded"
                )
                if state == "succeeded"
                else state,
            )
            if (
                stage.name == "distribution"
                and result
                and result.get("state") == "validated"
            ):
                job.distribution = "validated"
            if state == "succeeded" and stage.name == "processing":
                job.artifacts = "ready"
                following = s.scalar(
                    select(Stage).where(
                        Stage.job_id == job.id, Stage.name == "indexing"
                    )
                )
                following.state = "queued"
                self.enqueue(s, following)

    def request_publication(self, scope, principal, job_id, name, key):
        with Session(self.engine) as s, s.begin():
            from sqlalchemy import text

            operation = "publish:" + name
            lock = int(fingerprint([scope, principal, operation, key])[:15], 16)
            s.execute(text("SELECT pg_advisory_xact_lock(:key)"), {"key": lock})
            previous = s.scalar(
                select(Operation).where(
                    Operation.scope == scope,
                    Operation.principal == principal,
                    Operation.operation == operation,
                    Operation.key == key,
                )
            )
            if previous:
                if previous.request_hash != str(job_id):
                    raise Conflict("idempotency_conflict")
                return
            stage = s.scalar(
                select(Stage)
                .join(Job)
                .where(Job.id == job_id, Job.scope == scope, Stage.name == name)
                .with_for_update()
            )
            if not stage:
                raise KeyError("not_found")
            job = s.get(Job, job_id)
            if job.artifacts != "ready" or (
                name == "distribution" and job.indexing != "complete"
            ):
                raise Conflict("publication_prerequisites_incomplete")
            if stage.state == "blocked" or (
                name == "distribution" and job.distribution == "validated"
            ):
                stage.state = "queued"
                setattr(job, name, "pending")
                self.enqueue(s, stage)
            s.add(
                Operation(
                    scope=scope,
                    principal=principal,
                    operation=operation,
                    key=key,
                    request_hash=str(job_id),
                    job_id=job_id,
                )
            )

    def retry(
        self,
        scope,
        stage_id,
        generation,
        reason,
        principal="operator",
        key=None,
        reconcile=False,
        safe_only=False,
    ):
        with Session(self.engine) as s, s.begin():
            stage = s.scalar(
                select(Stage)
                .join(Job)
                .where(Stage.id == stage_id, Job.scope == scope)
                .with_for_update()
            )
            if not stage:
                raise KeyError("not_found")
            operation = (
                "reconcile:" if reconcile else ("resume:" if safe_only else "retry:")
            )
            operation += str(stage_id)
            hashed = fingerprint([generation, reason, reconcile])
            if key:
                previous = s.scalar(
                    select(Operation).where(
                        Operation.scope == scope,
                        Operation.principal == principal,
                        Operation.operation == operation,
                        Operation.key == key,
                    )
                )
                if previous:
                    if previous.request_hash != hashed:
                        raise Conflict("idempotency_conflict")
                    return
            if safe_only and not self.safe_retry_available(
                s, s.get(Job, stage.job_id), stage
            ):
                raise Conflict("stage_requires_operator_review")
            if stage.generation != generation:
                raise Conflict("stale_generation")
            if stage.state not in (
                ("outcome_unknown",) if reconcile else ("failed", "partial")
            ):
                raise Conflict("stage_not_retryable")
            if key:
                s.add(
                    Operation(
                        scope=scope,
                        principal=principal,
                        operation=operation,
                        key=key,
                        request_hash=hashed,
                        job_id=stage.job_id,
                    )
                )
            if stage.name == "processing":
                for call in s.scalars(
                    select(ModelCall).where(
                        ModelCall.job_id == stage.job_id,
                        ModelCall.state.in_(["failed", "intent"]),
                    )
                ):
                    # Preserve evidence while removing it from the active request cache.
                    call.key = call.key + ":archived:" + str(call.id)
                    if call.state == "intent":
                        call.state = "unknown_retry_authorized"
            stage.state = "queued"
            stage.error = None
            stage.attempts = 0
            stage.due_at = None
            setattr(s.get(Job, stage.job_id), stage.name, "queued")
            self.enqueue(s, stage)
            s.add(
                Attempt(
                    stage_id=stage.id,
                    fence=-stage.generation,
                    owner="operator",
                    state="safe_resume_authorized" if safe_only else "retry_authorized",
                    reason=reason,
                )
            )

    def recover(self):
        """DB-authoritative sweep: expired intent is unknown; queue loss is repairable."""
        with Session(self.engine) as s, s.begin():
            now = self.now(s)
            stages = s.scalars(
                select(Stage)
                .where(Stage.state.in_(["running", "queued", "retry_wait"]))
                .with_for_update(skip_locked=True)
            ).all()
            for stage in stages:
                if stage.state == "running" and stage.lease_until > now:
                    continue
                job = s.get(Job, stage.job_id)
                if stage.state == "running":
                    intent = s.scalar(
                        select(ModelCall.id).where(
                            ModelCall.job_id == job.id, ModelCall.state == "intent"
                        )
                    )
                    unknown = bool(intent) or stage.name in (
                        "indexing",
                        "git",
                        "distribution",
                    )
                    state = (
                        "outcome_unknown"
                        if unknown
                        else "retry_wait"
                        if stage.attempts < 3
                        else "failed"
                    )
                    attempt = s.scalar(
                        select(Attempt).where(
                            Attempt.stage_id == stage.id, Attempt.fence == stage.fence
                        )
                    )
                    attempt.state = state
                    attempt.finished_at = now
                    attempt.reason = "lease_expired"
                    stage.state = state
                    stage.error = "lease_expired"
                    stage.lease_until = None
                    setattr(job, stage.name, state)
                    if state != "retry_wait":
                        continue
                    stage.due_at = now + timedelta(
                        seconds=30 if stage.attempts == 1 else 120
                    )
                if stage.due_at and stage.due_at > now:
                    continue
                latest = s.scalar(
                    select(Outbox)
                    .where(Outbox.stage_id == stage.id)
                    .order_by(Outbox.generation.desc())
                    .limit(1)
                )
                # Unsent rows already have a durable dispatcher intent. After five
                # minutes re-dispatch sent work in case broker state was lost.
                if latest and (
                    latest.sent_at is None
                    or latest.sent_at > now - timedelta(minutes=5)
                ):
                    continue
                self.enqueue(s, stage)
