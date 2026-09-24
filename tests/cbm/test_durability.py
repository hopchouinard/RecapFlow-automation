"""Failure-boundary acceptance examples against real PostgreSQL and JetStream."""

import asyncio
from concurrent.futures import ThreadPoolExecutor
import json
from threading import Barrier
from uuid import uuid4

import nats
from nats.js.api import AckPolicy, ConsumerConfig, StorageType
import pytest
import sqlalchemy as sa

from reference import accept, claim, complete, heartbeat, jobs, outbox, publish_file


def row(engine, table):
    with engine.connect() as conn:
        return conn.execute(sa.select(table)).mappings().one()


def accepted(engine):
    with engine.begin() as conn:
        return accept(conn)


def test_acceptance_and_outbox_commit_together(engine):
    with pytest.raises(RuntimeError), engine.begin() as conn:
        accept(conn)
        raise RuntimeError("lost process before commit")
    with engine.connect() as conn:
        assert conn.execute(sa.select(jobs)).all() == []
        assert conn.execute(sa.select(outbox)).all() == []
    job_id = accepted(engine)
    assert row(engine, outbox)["job_id"] == job_id
    assert not row(engine, outbox)["sent"]
    with engine.begin() as conn:
        assert accept(conn) == job_id
    with (
        pytest.raises(ValueError, match="idempotency_conflict"),
        engine.begin() as conn,
    ):
        accept(conn, request_hash="different")
    assert row(engine, jobs)["id"] == job_id


def test_concurrent_acceptance_has_one_job_and_event(engine):
    barrier = Barrier(2)

    def submit():
        with engine.begin() as conn:
            barrier.wait(timeout=5)
            return accept(conn)

    with ThreadPoolExecutor(2) as pool:
        a, b = list(pool.map(lambda _: submit(), range(2)))
    assert a == b == row(engine, jobs)["id"]
    assert row(engine, outbox)["job_id"] == a


def test_claim_race_expiry_and_stale_worker_fencing(engine, tmp_path):
    job_id = accepted(engine)
    barrier = Barrier(2)

    def acquire():
        with engine.begin() as conn:
            barrier.wait(timeout=5)
            return claim(conn, job_id)

    with ThreadPoolExecutor(2) as pool:
        claims = list(pool.map(lambda _: acquire(), range(2)))
    assert sorted(claims, key=lambda x: x or 0) == [None, 1]
    with engine.begin() as conn:
        assert heartbeat(conn, job_id, 1)
        conn.execute(
            jobs.update().values(
                lease_until=sa.func.clock_timestamp() - sa.text("interval '1 second'")
            )
        )
    with engine.begin() as conn:
        assert not heartbeat(conn, job_id, 1)
        assert claim(conn, job_id) == 2
    stale, digest = publish_file(tmp_path, job_id, 1, b"old result")
    with pytest.raises(ValueError, match="claim_lost"), engine.begin() as conn:
        complete(conn, job_id, 1, stale, digest)
    valid, digest = publish_file(tmp_path, job_id, 2, b"new result")
    with engine.begin() as conn:
        complete(conn, job_id, 2, valid, digest)
    assert row(engine, jobs)["path"] == str(valid)
    assert stale.read_bytes() == b"old result"


@pytest.mark.parametrize(
    "boundary", ["before_publish", "after_publish", "before_commit"]
)
def test_artifact_crash_never_exposes_uncommitted_file(engine, tmp_path, boundary):
    job_id = accepted(engine)
    with engine.begin() as conn:
        fence = claim(conn, job_id)
    with pytest.raises(RuntimeError):
        path, digest = publish_file(
            tmp_path, job_id, fence, b"fixture", fail_at=boundary
        )
        with engine.begin() as conn:
            complete(conn, job_id, fence, path, digest)
            raise RuntimeError("lost process before database commit")
    assert row(engine, jobs)["path"] is None
    # Recovery reuses identical immutable bytes, then records the durable pointer.
    path, digest = publish_file(tmp_path, job_id, fence, b"fixture")
    with engine.begin() as conn:
        complete(conn, job_id, fence, path, digest)
    assert row(engine, jobs)["state"] == "succeeded"
    with pytest.raises(ValueError, match="immutable_artifact_conflict"):
        publish_file(tmp_path, job_id, fence, b"replacement")
    assert path.read_bytes() == b"fixture"


def test_corrupt_artifact_cannot_be_ready(engine, tmp_path):
    job_id = accepted(engine)
    with engine.begin() as conn:
        fence = claim(conn, job_id)
    path, digest = publish_file(tmp_path, job_id, fence, b"fixture")
    path.write_bytes(b"disk corruption")
    with pytest.raises(ValueError, match="artifact_corrupt"), engine.begin() as conn:
        complete(conn, job_id, fence, path, digest)
    assert row(engine, jobs)["state"] == "running"


def test_publish_and_ack_crashes_do_not_repeat_completed_work(
    engine, services, tmp_path
):
    async def scenario():
        job_id = accepted(engine)
        event_id = row(engine, outbox)["id"]
        stream = "CBM_" + uuid4().hex
        subject = "cbm.test." + uuid4().hex
        nc = await nats.connect(services[1], connect_timeout=2, allow_reconnect=False)
        try:
            js = nc.jetstream()
            await js.add_stream(
                name=stream, subjects=[subject], storage=StorageType.FILE
            )
            subscription = await js.pull_subscribe(
                subject,
                durable="probe",
                stream=stream,
                config=ConsumerConfig(
                    ack_policy=AckPolicy.EXPLICIT, ack_wait=0.2, max_deliver=5
                ),
            )
            payload = json.dumps(
                {
                    "schema_version": 1,
                    "event_id": str(event_id),
                    "job_id": str(job_id),
                    "stage": "community_post",
                }
            ).encode()
            # Publish succeeded; publisher died before recording sent in PostgreSQL.
            await js.publish(subject, payload)
            assert not row(engine, outbox)["sent"]
            # Intentionally bypass broker dedup to prove the business fence works.
            await js.publish(subject, payload)
            with engine.begin() as conn:
                conn.execute(outbox.update().values(sent=True))
            message = (await subscription.fetch(1, timeout=3))[0]
            with engine.begin() as conn:
                fence = claim(conn, job_id)
            path, digest = publish_file(tmp_path, job_id, fence, b"one model result")
            with engine.begin() as conn:
                complete(conn, job_id, fence, path, digest)
            # Lose connection after durable outcome, before ACK; reconnect as a new worker.
            await nc.close()
            nc = await nats.connect(
                services[1], connect_timeout=2, allow_reconnect=False
            )
            js = nc.jetstream()
            subscription = await js.pull_subscribe_bind("probe", stream=stream)
            seen = set()
            redelivered = False
            for _ in range(4):
                duplicate = (await subscription.fetch(1, timeout=3))[0]
                seen.add(duplicate.metadata.sequence.stream)
                redelivered |= duplicate.metadata.num_delivered > 1
                with engine.begin() as conn:
                    assert claim(conn, job_id) is None
                await duplicate.ack_sync(timeout=3)
                if len(seen) == 2 and redelivered:
                    break
            assert len(seen) == 2 and redelivered
            assert message.data == payload
            assert row(engine, jobs)["fence"] == 1
            assert row(engine, jobs)["sha256"] == digest
            await js.delete_stream(stream)
        finally:
            await nc.close()

    asyncio.run(scenario())
