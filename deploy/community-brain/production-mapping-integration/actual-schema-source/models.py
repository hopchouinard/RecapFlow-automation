from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Source(Base):
    __tablename__ = "cb_sources"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    scope: Mapped[str]
    meeting_id: Mapped[str]
    kind: Mapped[str]
    sha256: Mapped[str]
    path: Mapped[str]
    size: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    __table_args__ = (UniqueConstraint("scope", "meeting_id", "kind", "sha256"),)


class Job(Base):
    __tablename__ = "cb_jobs"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    scope: Mapped[str]
    principal: Mapped[str]
    key: Mapped[str]
    request_hash: Mapped[str]
    identity: Mapped[dict] = mapped_column(JSONB)
    sources: Mapped[dict] = mapped_column(JSONB)
    mode: Mapped[str]
    config: Mapped[dict] = mapped_column(JSONB)
    version: Mapped[str] = mapped_column(default="processing-v1")
    reason: Mapped[str | None]
    parent_id: Mapped[UUID | None] = mapped_column(ForeignKey("cb_jobs.id"))
    processing: Mapped[str] = mapped_column(default="waiting_for_input")
    artifacts: Mapped[str] = mapped_column(default="pending")
    indexing: Mapped[str] = mapped_column(default="pending")
    git: Mapped[str] = mapped_column(default="not_requested")
    distribution: Mapped[str] = mapped_column(default="not_requested")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class Operation(Base):
    __tablename__ = "cb_operations"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    scope: Mapped[str]
    principal: Mapped[str]
    operation: Mapped[str]
    key: Mapped[str]
    request_hash: Mapped[str]
    job_id: Mapped[UUID] = mapped_column(ForeignKey("cb_jobs.id"))
    __table_args__ = (UniqueConstraint("scope", "principal", "operation", "key"),)


class Stage(Base):
    __tablename__ = "cb_stages"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    job_id: Mapped[UUID] = mapped_column(ForeignKey("cb_jobs.id"), index=True)
    name: Mapped[str]
    state: Mapped[str] = mapped_column(default="blocked")
    generation: Mapped[int] = mapped_column(default=0)
    fence: Mapped[int] = mapped_column(default=0)
    attempts: Mapped[int] = mapped_column(default=0)
    owner: Mapped[str | None]
    lease_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    due_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    error: Mapped[str | None]
    result: Mapped[dict | None] = mapped_column(JSONB)
    __table_args__ = (UniqueConstraint("job_id", "name"),)


class Attempt(Base):
    __tablename__ = "cb_attempts"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    stage_id: Mapped[UUID] = mapped_column(ForeignKey("cb_stages.id"))
    fence: Mapped[int]
    owner: Mapped[str]
    state: Mapped[str] = mapped_column(default="running")
    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    reason: Mapped[str | None]
    __table_args__ = (UniqueConstraint("stage_id", "fence"),)


class ModelCall(Base):
    __tablename__ = "cb_model_calls"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    job_id: Mapped[UUID] = mapped_column(ForeignKey("cb_jobs.id"))
    key: Mapped[str]
    fence: Mapped[int]
    state: Mapped[str] = mapped_column(default="intent")
    request_meta: Mapped[dict] = mapped_column(JSONB)
    response_path: Mapped[str | None]
    response_hash: Mapped[str | None]
    usage: Mapped[dict | None] = mapped_column(JSONB)
    __table_args__ = (UniqueConstraint("job_id", "key"),)


class Artifact(Base):
    __tablename__ = "cb_artifacts"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    job_id: Mapped[UUID] = mapped_column(ForeignKey("cb_jobs.id"), index=True)
    stage_id: Mapped[UUID] = mapped_column(ForeignKey("cb_stages.id"))
    fence: Mapped[int]
    name: Mapped[str]
    path: Mapped[str]
    sha256: Mapped[str]
    size: Mapped[int]
    __table_args__ = (UniqueConstraint("job_id", "name"),)


class Outbox(Base):
    __tablename__ = "cb_outbox"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    stage_id: Mapped[UUID] = mapped_column(ForeignKey("cb_stages.id"))
    generation: Mapped[int]
    sent_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    __table_args__ = (UniqueConstraint("stage_id", "generation"),)


class RejectedEvent(Base):
    __tablename__ = "cb_rejected_events"
    sha256: Mapped[str] = mapped_column(primary_key=True)
    reason: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
