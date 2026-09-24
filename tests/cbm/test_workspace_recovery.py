"""Same-job recovery against disposable PostgreSQL; no provider calls."""

import json

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from community_brain.jobs.api import create_app
from community_brain.jobs.auth import Principal
from community_brain.jobs.automatic import next_stage
from community_brain.jobs.models import Attempt, Job, ModelCall, Stage
from community_brain.jobs.store import Conflict
from test_automatic import store, request, accept


def failed(store, name="acquisition"):
    job_id = accept(store, request(store, fathom=name == "acquisition"))
    item = next_stage(store, "community-brain")
    from uuid import UUID

    stage_id = UUID(item["stage_id"])
    fence = store.claim(stage_id, "fixture")
    store.finish(stage_id, fence, "fixture", "failed", "fathom_unavailable")
    return job_id, stage_id


def client(
    store,
    root=None,
    permissions=frozenset({"jobs:read", "jobs:submit"}),
    scope="community-brain",
):
    app = create_app(
        store,
        lambda _: Principal("operator", scope, permissions),
        automatic=True,
        automation_root=root,
    )
    return TestClient(
        app, headers={"Authorization": "Bearer fixture", "Idempotency-Key": "recover"}
    )


def test_failed_acquisition_upload_continues_same_job_once(store):
    job_id, stage_id = failed(store)
    source = str(
        store.add_source(
            "community-brain", "new-fixture", "transcript", "Fallback transcript"
        )
    )
    for _ in range(2):
        store.bind_sources("community-brain", job_id, {"transcript": source})
    item = next_stage(store, "community-brain")
    assert item["job_id"] == str(job_id) and item["stage"] == "processing"
    with Session(store.engine) as s:
        assert s.scalar(select(func.count(Job.id))) == 1
        assert s.get(Stage, stage_id).state == "succeeded"
        assert (
            s.scalar(select(Attempt).where(Attempt.stage_id == stage_id)).state
            == "failed"
        )
        assert (
            s.scalar(
                select(Stage).where(Stage.job_id == job_id, Stage.name == "processing")
            ).generation
            == 1
        )


def test_scoped_safe_resume_is_idempotent_and_bounded(store):
    job_id, stage_id = failed(store)
    api = client(store)
    path = f"/api/v1/jobs/{job_id}/stages/{stage_id}/resume"
    body = {"generation": 1, "reason": "Fathom available again"}
    assert (
        client(store, permissions=frozenset({"jobs:read"}))
        .post(path, json=body)
        .status_code
        == 403
    )
    assert client(store, scope="other").post(path, json=body).status_code == 404
    for _ in range(2):
        assert api.post(path, json=body).status_code == 202
    assert next_stage(store, "community-brain")["generation"] == 2
    for generation in (2, 3):
        fence = store.claim(stage_id, "fixture", expected_generation=generation)
        store.finish(stage_id, fence, "fixture", "failed", "fathom_unavailable")
        result = api.post(
            path,
            json={**body, "generation": generation},
            headers={"Idempotency-Key": str(generation)},
        )
        assert result.status_code == (202 if generation == 2 else 409)
    assert next_stage(store, "community-brain") is None
    # Exhausted acquisition retries still allow a supplied transcript.
    source = str(
        store.add_source("community-brain", "new-fixture", "transcript", "Fallback")
    )
    store.bind_sources("community-brain", job_id, {"transcript": source})
    assert next_stage(store, "community-brain")["stage"] == "processing"


@pytest.mark.parametrize("state", ["running", "outcome_unknown", "partial"])
def test_uncertain_stages_cannot_be_safely_retried_or_overwritten(store, state):
    job_id, stage_id = failed(store)
    with Session(store.engine) as s, s.begin():
        s.get(Stage, stage_id).state = state
    with pytest.raises(Conflict):
        store.retry("community-brain", stage_id, 1, "retry", safe_only=True)
    if state != "partial":
        source = str(
            store.add_source("community-brain", "new-fixture", "transcript", "Fallback")
        )
        with pytest.raises(Conflict, match="acquisition_requires_review"):
            store.bind_sources("community-brain", job_id, {"transcript": source})


def test_processing_without_calls_can_resume(store):
    job_id, stage_id = failed(store, "processing")
    store.retry("community-brain", stage_id, 1, "dependency repaired", safe_only=True)
    assert next_stage(store, "community-brain")["generation"] == 2


@pytest.mark.parametrize("status", ["verified", "requires_review", "pending"])
def test_backup_reads_only_sanitized_job_status(store, tmp_path, status):
    job_id = accept(store, request(store))
    with Session(store.engine) as s, s.begin():
        s.get(Job, job_id).indexing = "complete"
    root = tmp_path / "automation-public"
    root.mkdir()
    (root / "checkpoints.json").write_text(
        json.dumps({"checkpoints": {str(job_id): status}})
    )
    assert client(store, root).get(f"/api/v1/jobs/{job_id}").json()["backup"] == status
    (root / "checkpoints.json").write_text("[]")
    assert (
        client(store, root).get(f"/api/v1/jobs/{job_id}").json()["backup"]
        == "unavailable"
    )
    (root / "checkpoints.json").unlink()
    assert (
        client(store, root).get(f"/api/v1/jobs/{job_id}").json()["backup"]
        == "unavailable"
    )


@pytest.mark.parametrize("state", ["intent", "failed", "succeeded"])
def test_any_model_call_prevents_safe_processing_resume(store, state):
    job_id, stage_id = failed(store, "processing")
    with Session(store.engine) as s, s.begin():
        s.add(
            ModelCall(
                job_id=job_id, key="fixture", fence=1, state=state, request_meta={}
            )
        )
    with pytest.raises(Conflict, match="stage_requires_operator_review"):
        store.retry("community-brain", stage_id, 1, "retry", safe_only=True)
    assert next_stage(store, "community-brain") is None


def test_artifact_prevents_safe_processing_resume(store):
    from community_brain.jobs.models import Artifact

    job_id, stage_id = failed(store, "processing")
    with Session(store.engine) as s, s.begin():
        s.add(
            Artifact(
                job_id=job_id,
                stage_id=stage_id,
                fence=1,
                name="transcript.txt",
                path="fixture",
                sha256="a" * 64,
                size=1,
            )
        )
    with pytest.raises(Conflict, match="stage_requires_operator_review"):
        store.retry("community-brain", stage_id, 1, "retry", safe_only=True)


def test_safe_resume_runs_new_generation_through_selected_worker(store, services):
    import asyncio
    from test_application import fake_model
    from test_manual import approve, exercise
    from community_brain.jobs.worker import Worker

    job_id, stage_id = failed(store)
    store.retry("community-brain", stage_id, 1, "provider recovered", safe_only=True)

    class Fathom:
        def fetch(self, identity):
            return "Recovered fixture transcript"

    worker = Worker(store, fake_model, fathom=Fathom())
    approval = approve(store, job_id, "acquisition", generation=2)
    assert approval["generation"] == 2
    asyncio.run(exercise(store, services, approval, worker))
    assert next_stage(store, "community-brain")["stage"] == "processing"
    with Session(store.engine) as s:
        assert s.get(Stage, stage_id).state == "succeeded"
        assert s.scalar(select(func.count(ModelCall.id))) == 0


@pytest.mark.parametrize(
    "code,expected",
    [
        (401, "fathom_authentication_failed"),
        (404, "fathom_transcript_unavailable"),
        (429, "fathom_rate_limited"),
        (503, "fathom_unavailable"),
    ],
)
def test_fathom_failure_surfaces_safe_code_without_response_details(
    store, services, code, expected
):
    import asyncio
    import httpx
    from test_application import fake_model
    from test_manual import approve, exercise
    from community_brain.jobs.worker import Worker

    job_id = accept(store, request(store, fathom=True))

    class Fathom:
        def fetch(self, identity):
            response = httpx.Response(
                code,
                request=httpx.Request("GET", "https://example.invalid/private"),
                text="private provider details",
            )
            response.raise_for_status()

    with pytest.raises(RuntimeError, match="incomplete"):
        asyncio.run(
            exercise(
                store,
                services,
                approve(store, job_id, "acquisition"),
                Worker(store, fake_model, fathom=Fathom()),
            )
        )
    data = client(store).get(f"/api/v1/jobs/{job_id}").json()
    acquisition = next(s for s in data["stages"] if s["name"] == "acquisition")
    assert acquisition["error"] == expected and acquisition["safe_retryable"]
    assert "private" not in json.dumps(data)


def test_readiness_api_reports_host_hold_without_exposing_markers(store, tmp_path):
    from datetime import datetime, timezone

    value = {
        "runner": "idle",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "paused": True,
        "attention": False,
        "boot_reconciled": True,
        "checkpoint_pending": False,
        "management_attention": False,
        "credentials_expired": False,
    }
    (tmp_path / "checkpoints.json").write_text(
        json.dumps({"processing": value, "private": "secret"})
    )
    response = client(store, tmp_path).get("/api/v1/me").json()
    assert response["automatic_processing"] is True
    assert response["processing_readiness"] == {"state": "paused", "ready": False}
    assert "secret" not in json.dumps(response)


def test_read_only_diagnosis_never_fences_expired_work(store):
    from datetime import datetime, timedelta, timezone
    from community_brain.jobs.automatic import inspect_state

    job_id = accept(store, request(store))
    item = next_stage(store, "community-brain")
    from uuid import UUID

    stage_id = UUID(item["stage_id"])
    store.claim(stage_id, "fixture")
    with Session(store.engine) as s, s.begin():
        stage = s.get(Stage, stage_id)
        stage.lease_until = datetime.now(timezone.utc) - timedelta(seconds=5)
        before = (stage.state, stage.fence, stage.attempts)
    snapshot = inspect_state(store, "community-brain")
    assert snapshot["read_only"] and str(job_id) in snapshot["automatic_jobs"]
    assert (
        next(s for s in snapshot["stages"] if s["id"] == str(stage_id))["state"]
        == "running"
    )
    with Session(store.engine) as s:
        stage = s.get(Stage, stage_id)
        assert (stage.state, stage.fence, stage.attempts) == before
