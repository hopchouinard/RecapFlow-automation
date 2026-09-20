from datetime import date, datetime
from pathlib import Path
import base64
import json
from typing import Literal
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from fastapi import Depends, FastAPI, Header, HTTPException, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, ConfigDict, Field, model_validator
from sqlalchemy import select, tuple_
from sqlalchemy.orm import Session

from .models import Artifact, Job, Source, Stage
from .store import Conflict


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Meeting(Contract):
    meeting_id: str = Field(min_length=1, max_length=200, pattern=r"^[A-Za-z0-9_.:-]+$")
    started_at: datetime
    timezone: str
    local_date: date
    provider: Literal["manual", "fathom"] = "manual"

    @model_validator(mode="after")
    def valid_date(self):
        try:
            zone = ZoneInfo(self.timezone)
        except (ZoneInfoNotFoundError, ValueError):
            raise ValueError("invalid timezone")
        if (
            self.started_at.utcoffset() is None
            or self.started_at.astimezone(zone).date() != self.local_date
        ):
            raise ValueError("meeting time/date mismatch")
        return self


class Submission(Contract):
    identity: Meeting
    mode: Literal["weekly", "transcript_backfill"] = "weekly"
    sources: dict[Literal["transcript", "chat", "aliases"], UUID] = Field(
        default_factory=dict
    )
    version: Literal["processing-v1"] = "processing-v1"


class Upload(Contract):
    meeting_id: str = Field(min_length=1, max_length=200, pattern=r"^[A-Za-z0-9_.:-]+$")
    kind: Literal["transcript", "chat", "aliases"]
    content: str = Field(min_length=1, max_length=5_000_000)


class Retry(Contract):
    generation: int = Field(ge=0)
    reason: str = Field(min_length=1, max_length=500)


class Rerun(Submission):
    reason: str = Field(min_length=1, max_length=500)


def create_app(
    store,
    authenticate,
    *,
    archive=None,
    hidden_jobs=(),
    automatic=False,
    automation_root=None,
):
    app = FastAPI(title="Community Brain Jobs", version="1.0.0")
    hidden_jobs = frozenset(UUID(str(value)) for value in hidden_jobs)

    if automatic:

        @app.middleware("http")
        async def checkpoint_boundary(request, call_next):
            if request.method not in {"POST", "PUT", "PATCH", "DELETE"} or (
                request.method == "POST" and request.url.path == "/retrieval/query"
            ):
                return await call_next(request)
            import fcntl

            with (store.storage.root / ".submission.lock").open("a") as lock:
                try:
                    fcntl.flock(lock, fcntl.LOCK_SH | fcntl.LOCK_NB)
                except BlockingIOError:
                    return JSONResponse(
                        {"code": "checkpoint_in_progress_retry_shortly"},
                        status_code=503,
                    )
                return await call_next(request)

    def permission(*required):
        def dependency(authorization: str | None = Header(default=None)):
            if not authorization or not authorization.startswith("Bearer "):
                raise HTTPException(401, "unauthenticated")
            try:
                principal = authenticate(authorization[7:])
            except Exception:
                raise HTTPException(401, "unauthenticated")
            if not any(value in principal.permissions for value in required):
                raise HTTPException(403, "forbidden")
            return principal

        return dependency

    from .archive import register_archive

    register_archive(app, permission, archive, store, hidden_jobs)

    @app.exception_handler(HTTPException)
    async def http_error(request, exc):
        return problem(exc.status_code, str(exc.detail), request)

    @app.exception_handler(Conflict)
    async def conflict_error(request, exc):
        return problem(409, str(exc), request)

    @app.exception_handler(RequestValidationError)
    async def validation_error(request, exc):
        return problem(422, "invalid_request", request)

    @app.exception_handler(KeyError)
    async def missing_error(request, exc):
        return problem(404, "not_found", request)

    @app.exception_handler(Exception)
    async def internal_error(request, exc):
        return problem(503, "dependency_unavailable", request)

    def problem(status, code, request):
        return JSONResponse(
            {
                "type": "urn:community-brain:error:" + code,
                "title": code,
                "status": status,
                "code": code,
                "detail": code,
                "instance": request.url.path,
                "trace_id": uuid4().hex,
                "retryable": False,
            },
            status_code=status,
            media_type="application/problem+json",
        )

    def get_job(session, identity, principal):
        job = session.get(Job, identity)
        if not job or job.scope != principal.scope or job.id in hidden_jobs:
            raise HTTPException(404, "not_found")
        return job

    def job_view(job):
        return {
            "id": str(job.id),
            "identity": job.identity,
            "mode": job.mode,
            "version": job.version,
            "parent_id": str(job.parent_id) if job.parent_id else None,
            "processing": job.processing,
            "artifacts": job.artifacts,
            "indexing": job.indexing,
            "git": job.git,
            "distribution": job.distribution,
            "created_at": job.created_at.isoformat(),
        }

    @app.get("/health")
    def health():
        with Session(store.engine) as s:
            s.execute(select(Job.id).limit(1))
        return {"status": "ok"}

    @app.get("/metrics")
    def metrics(p=Depends(permission("metrics:read"))):
        from sqlalchemy import func

        with Session(store.engine) as s:
            rows = s.execute(
                select(Stage.name, Stage.state, func.count())
                .join(Job)
                .where(Job.scope == p.scope)
                .group_by(Stage.name, Stage.state)
            ).all()
        lines = ["# TYPE community_brain_stages gauge"]
        for name, state, count in rows:
            lines.append(
                f'community_brain_stages{{stage="{name}",state="{state}"}} {count}'
            )
        return Response("\n".join(lines) + "\n", media_type="text/plain")

    @app.get("/api/v1/me")
    def me(p=Depends(permission("jobs:read"))):
        return {
            "subject": p.subject,
            "scope": p.scope,
            "permissions": sorted(p.permissions),
            "automatic_processing": automatic,
        }

    @app.post("/api/v1/sources", status_code=201)
    def upload(
        body: Upload, p=Depends(permission("sources:upload", "sources:upload:chat"))
    ):
        if "sources:upload" not in p.permissions and body.kind != "chat":
            raise HTTPException(403, "forbidden")
        if body.kind == "aliases" and "sources:aliases" not in p.permissions:
            raise HTTPException(403, "forbidden")
        data = body.content.encode("utf-8")
        if not body.content.strip() or len(data) > 10_000_000:
            raise HTTPException(422, "invalid_request")
        path, sha, size = store.storage.put(data)
        with Session(store.engine) as s, s.begin():
            from sqlalchemy.dialects.postgresql import insert

            values = dict(
                id=uuid4(),
                scope=p.scope,
                meeting_id=body.meeting_id,
                kind=body.kind,
                sha256=sha,
                path=path,
                size=size,
            )
            identity = s.execute(
                insert(Source)
                .values(**values)
                .on_conflict_do_nothing()
                .returning(Source.id)
            ).scalar_one_or_none()
            if identity is None:
                identity = s.scalar(
                    select(Source.id).where(
                        Source.scope == p.scope,
                        Source.meeting_id == body.meeting_id,
                        Source.kind == body.kind,
                        Source.sha256 == sha,
                    )
                )
        return {"id": str(identity), "sha256": sha, "bytes": size}

    @app.post("/api/v1/jobs")
    def submit(
        body: Submission,
        p=Depends(permission("jobs:submit")),
        idempotency_key: str = Header(min_length=1, max_length=200),
    ):
        identity, created = store.accept(
            p.scope,
            p.subject,
            idempotency_key,
            body.model_dump(mode="json"),
            automatic=automatic,
        )
        return JSONResponse(
            {"id": str(identity), "status_url": "/api/v1/jobs/" + str(identity)},
            status_code=202 if created else 200,
        )

    @app.post("/api/v1/jobs/{job_id}/sources", status_code=202)
    def bind(
        job_id: UUID,
        sources: dict[Literal["transcript", "chat", "aliases"], UUID],
        p=Depends(permission("jobs:submit")),
    ):
        store.bind_sources(p.scope, job_id, {k: str(v) for k, v in sources.items()})
        return {"id": str(job_id)}

    @app.get("/api/v1/jobs")
    def listing(
        p=Depends(permission("jobs:read")),
        limit: int = Query(50, ge=1, le=100),
        cursor: str | None = None,
        processing: str | None = None,
        indexing: str | None = None,
    ):
        with Session(store.engine) as s:
            query = (
                select(Job)
                .where(Job.scope == p.scope, Job.id.not_in(hidden_jobs))
                .order_by(Job.created_at.desc(), Job.id.desc())
                .limit(limit + 1)
            )
            if processing:
                query = query.where(Job.processing == processing)
            if indexing:
                query = query.where(Job.indexing == indexing)
            if cursor:
                try:
                    timestamp, identity = json.loads(base64.urlsafe_b64decode(cursor))
                    timestamp = datetime.fromisoformat(timestamp)
                    identity = UUID(identity)
                    if timestamp.tzinfo is None:
                        raise ValueError()
                except Exception:
                    raise HTTPException(422, "invalid_request")
                query = query.where(
                    tuple_(Job.created_at, Job.id) < tuple_(timestamp, identity)
                )
            rows = s.scalars(query).all()
            next_cursor = (
                base64.urlsafe_b64encode(
                    json.dumps(
                        [
                            rows[limit - 1].created_at.isoformat(),
                            str(rows[limit - 1].id),
                        ]
                    ).encode()
                ).decode()
                if len(rows) > limit
                else None
            )
            return {
                "items": [job_view(j) for j in rows[:limit]],
                "next_cursor": next_cursor,
            }

    def backup_state(job):
        if job.config.get("automation_policy") != "new-meeting-full-loop-v1":
            return "not_tracked"
        if job.indexing != "complete":
            return "not_started"
        if automation_root is None:
            return "unavailable"
        try:
            value = json.loads((Path(automation_root) / "checkpoints.json").read_text())
            if not isinstance(value, dict) or not isinstance(
                value.get("checkpoints"), dict
            ):
                return "unavailable"
            status = value["checkpoints"].get(str(job.id))
            if status in {"verified", "requires_review"}:
                return status
            return (
                "requires_review"
                if value.get("management_attention") is True
                else "pending"
            )
        except (OSError, ValueError, TypeError):
            return "unavailable"

    @app.get("/api/v1/jobs/{job_id}")
    def detail(job_id: UUID, p=Depends(permission("jobs:read"))):
        with Session(store.engine) as s:
            job = get_job(s, job_id, p)
            stages = s.scalars(select(Stage).where(Stage.job_id == job_id)).all()
            return {
                **job_view(job),
                "sources": job.sources,
                "backup": backup_state(job),
                "acquisition": "ready"
                if "transcript" in job.sources
                else next(
                    (x.state for x in stages if x.name == "acquisition"),
                    "not_requested",
                ),
                "missing_inputs": [
                    k
                    for k in (
                        ["transcript", "chat"]
                        if job.mode == "weekly"
                        else ["transcript"]
                    )
                    if k not in job.sources
                ],
                "stages": [
                    {
                        "id": str(x.id),
                        "name": x.name,
                        "state": x.state,
                        "generation": x.generation,
                        "attempts": x.attempts,
                        "error": x.error,
                        "result": x.result,
                        "retryable": x.state in ("failed", "partial"),
                        "safe_retryable": store.safe_retry_available(s, job, x),
                    }
                    for x in stages
                ],
            }

    @app.get("/api/v1/jobs/{job_id}/artifacts")
    def artifacts(job_id: UUID, p=Depends(permission("artifacts:read"))):
        with Session(store.engine) as s:
            get_job(s, job_id, p)
            return {
                "items": [
                    {
                        "id": str(a.id),
                        "name": a.name,
                        "sha256": a.sha256,
                        "bytes": a.size,
                        "url": f"/api/v1/artifacts/{a.id}/content",
                    }
                    for a in s.scalars(
                        select(Artifact).where(Artifact.job_id == job_id)
                    )
                ]
            }

    @app.get("/api/v1/artifacts/{artifact_id}/content")
    def content(artifact_id: UUID, p=Depends(permission("artifacts:read"))):
        with Session(store.engine) as s:
            artifact = s.get(Artifact, artifact_id)
            if not artifact:
                raise HTTPException(404, "not_found")
            job = get_job(s, artifact.job_id, p)
            try:
                data = store.storage.read(artifact.path, artifact.sha256)
            except (OSError, ValueError):
                job.artifacts = "corrupt"
                s.commit()
                raise HTTPException(409, "artifact_corrupt")
            return Response(
                data,
                media_type="text/plain",
                headers={
                    "ETag": '"' + artifact.sha256 + '"',
                    "Content-Disposition": f'attachment; filename="{artifact.name}"',
                    "X-Content-Type-Options": "nosniff",
                },
            )

    @app.post("/api/v1/jobs/{job_id}/stages/{stage_id}/resume", status_code=202)
    def safe_resume(
        job_id: UUID,
        stage_id: UUID,
        body: Retry,
        p=Depends(permission("jobs:submit")),
        idempotency_key: str = Header(min_length=1, max_length=200),
    ):
        with Session(store.engine) as s:
            get_job(s, job_id, p)
            stage = s.get(Stage, stage_id)
            if not stage or stage.job_id != job_id:
                raise HTTPException(404, "not_found")
        store.retry(
            p.scope,
            stage_id,
            body.generation,
            body.reason,
            p.subject,
            idempotency_key,
            safe_only=True,
        )
        return {"id": str(job_id)}

    @app.post("/api/v1/jobs/{job_id}/stages/{stage_id}/retry", status_code=202)
    def retry(
        job_id: UUID,
        stage_id: UUID,
        body: Retry,
        p=Depends(permission("jobs:retry")),
        idempotency_key: str = Header(min_length=1, max_length=200),
    ):
        with Session(store.engine) as s:
            get_job(s, job_id, p)
            stage = s.get(Stage, stage_id)
            if not stage or stage.job_id != job_id:
                raise HTTPException(404, "not_found")
        store.retry(
            p.scope, stage_id, body.generation, body.reason, p.subject, idempotency_key
        )
        return {"id": str(job_id)}

    @app.post("/api/v1/jobs/{job_id}/stages/{stage_id}/reconcile", status_code=202)
    def reconcile(
        job_id: UUID,
        stage_id: UUID,
        body: Retry,
        p=Depends(permission("jobs:reconcile")),
        idempotency_key: str = Header(min_length=1, max_length=200),
        acknowledge_duplicate_effect: bool = Header(default=False),
    ):
        if not acknowledge_duplicate_effect:
            raise HTTPException(409, "duplicate_effect_acknowledgment_required")
        with Session(store.engine) as s:
            get_job(s, job_id, p)
            stage = s.get(Stage, stage_id)
            if not stage or stage.job_id != job_id:
                raise HTTPException(404, "not_found")
        store.retry(
            p.scope,
            stage_id,
            body.generation,
            body.reason,
            p.subject,
            idempotency_key,
            reconcile=True,
        )
        return {"id": str(job_id)}

    @app.post("/api/v1/jobs/{job_id}/reruns")
    def rerun(
        job_id: UUID,
        body: Rerun,
        p=Depends(permission("jobs:rerun")),
        idempotency_key: str = Header(min_length=1, max_length=200),
    ):
        with Session(store.engine) as s:
            old = get_job(s, job_id, p)
            if old.identity["meeting_id"] != body.identity.meeting_id:
                raise HTTPException(409, "invalid_source_identity")
        identity, created = store.accept(
            p.scope,
            p.subject,
            idempotency_key,
            body.model_dump(mode="json"),
            parent=job_id,
        )
        return JSONResponse({"id": str(identity)}, status_code=202 if created else 200)

    @app.post("/api/v1/jobs/{job_id}/publications/{kind}", status_code=202)
    def publish(
        job_id: UUID,
        kind: Literal["git", "distribution"],
        p=Depends(permission("corpus:publish")),
        idempotency_key: str = Header(min_length=1, max_length=200),
    ):
        store.request_publication(p.scope, p.subject, job_id, kind, idempotency_key)
        return {"id": str(job_id)}

    return app
