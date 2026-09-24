"""CBM-01 executable contract probe; not an application store or worker.

Explicit SQL exercises PostgreSQL transactions/fencing before CBM-03 selects
its full ORM schema and Alembic migration. All files belong to pytest tmp_path.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from uuid import uuid4

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import insert

metadata = sa.MetaData()
jobs = sa.Table(
    "probe_jobs",
    metadata,
    sa.Column("id", sa.Uuid, primary_key=True),
    sa.Column("key", sa.Text, nullable=False, unique=True),
    sa.Column("request_hash", sa.Text, nullable=False),
    sa.Column("state", sa.Text, nullable=False, server_default="queued"),
    sa.Column("fence", sa.Integer, nullable=False, server_default="0"),
    sa.Column("lease_until", sa.DateTime(timezone=True)),
    sa.Column("path", sa.Text),
    sa.Column("sha256", sa.Text),
)
outbox = sa.Table(
    "probe_outbox",
    metadata,
    sa.Column("id", sa.Uuid, primary_key=True),
    sa.Column("job_id", sa.Uuid, sa.ForeignKey(jobs.c.id), nullable=False, unique=True),
    sa.Column("sent", sa.Boolean, nullable=False, server_default=sa.false()),
)


def accept(conn, key="fixture", request_hash="hash-a"):
    proposed = uuid4()
    job_id = conn.execute(
        insert(jobs)
        .values(id=proposed, key=key, request_hash=request_hash)
        .on_conflict_do_nothing(index_elements=[jobs.c.key])
        .returning(jobs.c.id)
    ).scalar_one_or_none()
    if job_id is None:
        existing = (
            conn.execute(sa.select(jobs).where(jobs.c.key == key)).mappings().one()
        )
        if existing["request_hash"] != request_hash:
            raise ValueError("idempotency_conflict")
        return existing["id"]
    conn.execute(outbox.insert().values(id=uuid4(), job_id=job_id))
    return job_id


def claim(conn, job_id):
    return conn.execute(
        jobs.update()
        .where(
            jobs.c.id == job_id,
            sa.or_(
                jobs.c.state == "queued",
                sa.and_(
                    jobs.c.state == "running",
                    jobs.c.lease_until < sa.func.clock_timestamp(),
                ),
            ),
        )
        .values(
            state="running",
            fence=jobs.c.fence + 1,
            lease_until=sa.func.clock_timestamp() + sa.text("interval '60 seconds'"),
        )
        .returning(jobs.c.fence)
    ).scalar_one_or_none()


def owned(job_id, fence):
    return sa.and_(
        jobs.c.id == job_id,
        jobs.c.fence == fence,
        jobs.c.state == "running",
        jobs.c.lease_until > sa.func.clock_timestamp(),
    )


def heartbeat(conn, job_id, fence):
    return (
        conn.execute(
            jobs.update()
            .where(owned(job_id, fence))
            .values(
                lease_until=sa.func.clock_timestamp() + sa.text("interval '60 seconds'")
            )
        ).rowcount
        == 1
    )


def complete(conn, job_id, fence, path, digest):
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError("artifact_corrupt")
    if (
        conn.execute(
            jobs.update()
            .where(owned(job_id, fence))
            .values(state="succeeded", path=str(path), sha256=digest, lease_until=None)
        ).rowcount
        != 1
    ):
        raise ValueError("claim_lost")


def publish_file(root: Path, job_id, fence, content: bytes, fail_at=None):
    # Attempt-specific namespace fences filesystem effects as well as DB updates.
    directory = root / str(job_id) / str(fence)
    directory.mkdir(parents=True, exist_ok=True)
    for parent in (root, root / str(job_id), directory):
        sync_directory(parent)
    staging = directory / f".{uuid4()}.staging"
    final = directory / "community-post.md"
    with staging.open("xb") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    if fail_at == "before_publish":
        raise RuntimeError("injected crash before publication")
    # Atomic no-clobber publication on the same filesystem.
    try:
        os.link(staging, final)
    except FileExistsError:
        if final.read_bytes() != content:
            raise ValueError("immutable_artifact_conflict")
    staging.unlink()
    sync_directory(directory)
    if fail_at == "after_publish":
        raise RuntimeError("injected crash before database commit")
    return final, hashlib.sha256(content).hexdigest()


def sync_directory(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
