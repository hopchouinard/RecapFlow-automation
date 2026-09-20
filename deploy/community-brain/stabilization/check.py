"""VM108 only: real DB/queue, synthetic pipeline, host holds and recovery visibility."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace
from unittest.mock import patch
from datetime import datetime, timedelta, timezone

from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session
from community_brain.jobs.api import create_app
from community_brain.jobs.auth import Principal
from community_brain.jobs.automatic import inspect_state
from community_brain.jobs.models import Stage
from community_brain.jobs.runtime import make_store

assert (
    os.environ["CB_DATABASE_URL"]
    == "postgresql+psycopg://fixture@cbm-auto-pg/cbm_stabilization"
)
assert not any(k.endswith(("API_KEY", "TOKEN", "PASSWORD")) for k in os.environ)
workspace = Path("/workspace")
root = Path("/state")
# Run the preserved fixture against this image's actual frontend.
fixture = workspace / "deploy/community-brain/automatic-rehearsal/check.py"
code = (
    fixture.read_text()
    .replace('directory="/dist"', 'directory="/app/web/dist"')
    .replace('Path("/dist")', 'Path("/app/web/dist")')
    .replace('relative_to("/dist")', 'relative_to("/app/web/dist")')
)
exec(compile(code, str(fixture), "exec"), {"__name__": "__main__"})
store = make_store()
old_run = sys.modules.get("run")
sys.modules["run"] = SimpleNamespace(
    HERE=workspace / "deploy/community-brain/automatic",
    IMAGE="fixture",
    read_env=lambda _: {},
)
spec = importlib.util.spec_from_file_location(
    "stabilization_host",
    workspace / "deploy/community-brain/automatic/automatic_host.py",
)
host = importlib.util.module_from_spec(spec)
spec.loader.exec_module(host)
host.ROOT = root
host.STATE = root / "automation"
host.STATE.mkdir()
(host.STATE / "checkpoints").mkdir()
(root / "manual-approvals").mkdir()
(root / "management-status").mkdir()
now = datetime.now(timezone.utc)
(root / "management-status/maintenance.json").write_text(
    json.dumps(
        {
            "checked_at": now.isoformat(),
            "renewal": {"state": "not_due"},
            "service_identities": [
                {"expires_at": (now + timedelta(days=7)).timestamp()}
            ],
        }
    )
)
api = TestClient(
    create_app(
        store,
        lambda _: Principal(
            "fixture", "community-brain", frozenset({"jobs:read", "artifacts:read"})
        ),
        automatic=True,
        automation_root=root / "automation-public",
    ),
    headers={"Authorization": "Bearer fixture"},
)


def status():
    return api.get("/api/v1/me").json()["processing_readiness"]


# Reproduce the real independent attention and boot holds, without clearing
# production markers or performing any inference from empty queues.
(host.STATE / "boot-state.json").write_text(
    json.dumps({"reconciled": False, "boot_id": "fixture"})
)
(host.STATE / "paused").write_text("fixture boot hold")
host.record_attention(RuntimeError("private diagnostic must not escape"))
# Compare the preserved pre-change API/host on this same development state.
baseline = workspace / "baseline"
legacy_spec = importlib.util.spec_from_file_location(
    "community_brain.jobs.stabilization_baseline_api", baseline / "api.py"
)
legacy_api = importlib.util.module_from_spec(legacy_spec)
legacy_spec.loader.exec_module(legacy_api)
legacy_spec = importlib.util.spec_from_file_location(
    "stabilization_baseline_host", baseline / "automatic_host.py"
)
legacy_host = importlib.util.module_from_spec(legacy_spec)
legacy_spec.loader.exec_module(legacy_host)
legacy_host.ROOT = root
legacy_host.STATE = host.STATE
legacy_host.publish_checkpoint_status()
legacy = TestClient(
    legacy_api.create_app(
        store,
        lambda _: Principal("fixture", "community-brain", frozenset({"jobs:read"})),
        automatic=True,
        automation_root=root / "automation-public",
    ),
    headers={"Authorization": "Bearer fixture"},
)
legacy_me = legacy.get("/api/v1/me").json()
assert legacy_me["automatic_processing"] is True
assert "processing_readiness" not in legacy_me
assert "processing" not in json.loads(
    (root / "automation-public/checkpoints.json").read_text()
)
host.publish_checkpoint_status("attention_required")
assert status() == {"state": "attention_required", "ready": False}
with patch.object(
    host, "scan", side_effect=AssertionError("held runner must not scan")
):
    assert host.tick() == "attention_required"
first = (host.STATE / "attention.json").read_bytes()
host.record_attention(ValueError("later"))
assert first == (host.STATE / "attention.json").read_bytes()
(host.STATE / "attention.json").rename(host.STATE / "fixture-archived-attention.json")
host.publish_checkpoint_status("paused")
assert status() == {"state": "paused", "ready": False}
# Explicit fixture-only reconciliation, preserving the independent boot gate.
(host.STATE / "boot-state.json").write_text(
    json.dumps({"reconciled": True, "boot_id": "fixture"})
)
(host.STATE / "paused").unlink()
host.publish_checkpoint_status("idle")
assert status() == {"state": "ready", "ready": True}
with patch.object(host.subprocess, "check_output", return_value=b"fixture-worker"):
    host.publish_busy_status()
assert status() == {"state": "busy", "ready": True}
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as pool:
    list(
        pool.map(
            lambda n: host.atomic(host.STATE / "atomic-fixture.json", {"n": n}),
            range(20),
        )
    )
assert json.loads((host.STATE / "atomic-fixture.json").read_text())["n"] in range(20)
assert not list(host.STATE.glob(".atomic-fixture.json*"))
m = root / "management-status/maintenance.json"
value = json.loads(m.read_text())
value["renewal"]["state"] = "failed"
m.write_text(json.dumps(value))
host.publish_checkpoint_status("idle")
assert status() == {"state": "credentials_require_review", "ready": False}
value["renewal"]["state"] = "completed"
m.write_text(json.dumps(value))
host.publish_checkpoint_status("idle")
assert status()["ready"]
public = root / "automation-public/checkpoints.json"
value = json.loads(public.read_text())
value["processing"]["checked_at"] = (now - timedelta(minutes=4)).isoformat()
public.write_text(json.dumps(value))
assert status() == {"state": "unavailable", "ready": False}
# Verify real SQL read-only inspection preserves expired-running state.
with Session(store.engine) as s, s.begin():
    stage = s.scalar(select(Stage).where(Stage.name == "processing"))
    sid = stage.id
    before = stage.state
    stage.state = "running"
    stage.lease_until = now - timedelta(seconds=10)
snapshot = inspect_state(store, "community-brain")
assert snapshot["read_only"]
with Session(store.engine) as s, s.begin():
    stage = s.get(Stage, sid)
    assert stage.state == "running"
    stage.state = before
    stage.lease_until = None
# Actual scanner subprocess: valid inspection and sanitized connection failure.
script = workspace / "deploy/community-brain/automatic/scan.py"
r = subprocess.run(
    [sys.executable, str(script), "inspect"],
    capture_output=True,
    env=os.environ,
    timeout=20,
)
assert r.returncode == 0 and json.loads(r.stdout)["read_only"]
env = {
    **os.environ,
    "CB_DATABASE_URL": "postgresql+psycopg://fixture@127.0.0.1:1/unavailable?connect_timeout=2",
}
r = subprocess.run(
    [sys.executable, str(script), "inspect"], capture_output=True, env=env, timeout=20
)
assert r.returncode == 1
error = json.loads(r.stderr)
assert error == {"code": "automatic_scan_failed", "error_class": "OperationalError"}
assert b"postgresql" not in r.stderr and b"Traceback" not in r.stderr
safe = host.ScanFailure("automatic_scan_exit", r)
assert safe.diagnostic["scanner_error_class"] == "OperationalError"

# Boot the actual application factory as the unprivileged container user, using
# only the disposable database and an explicitly synthetic scoped identity.
import time
import httpx

host.publish_checkpoint_status("idle")
env = {
    **os.environ,
    "CB_OIDC_ISSUER": "https://fixture.invalid",
    "CB_OIDC_AUDIENCE": "fixture",
    "CB_OIDC_JWKS_URL": "https://fixture.invalid/jwks",
    "CB_OIDC_CLIENT_ID": "fixture",
    "CB_CORPUS_SCOPE": "community-brain",
    "CB_AUTOMATIC_PROCESSING": "true",
    "CB_AUTOMATION_ROOT": str(root / "automation-public"),
    "CB_ENABLE_RETRIEVAL": "false",
    "CB_ENABLE_MODEL_CALLS": "false",
    "CB_ENABLE_NETWORK_PUBLICATION": "false",
    "CB_SERVICE_IDENTITIES": json.dumps(
        [
            {
                "subject": "dev-fixture",
                "scope": "community-brain",
                "sha256": hashlib.sha256(b"dev-fixture").hexdigest(),
                "expires_at": int(now.timestamp()) + 3600,
                "permissions": ["jobs:read", "artifacts:read"],
            }
        ]
    ),
}
with (root / "api-smoke.log").open("wb") as log:
    server = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "community_brain.jobs.runtime:app",
            "--factory",
            "--host",
            "127.0.0.1",
            "--port",
            "18190",
            "--no-access-log",
        ],
        env=env,
        stdout=log,
        stderr=log,
    )
    try:
        with httpx.Client(base_url="http://127.0.0.1:18190", timeout=2) as live:
            deadline = time.monotonic() + 20
            while True:
                try:
                    if live.get("/health").status_code == 200:
                        break
                except httpx.TransportError:
                    pass
                assert server.poll() is None and time.monotonic() < deadline, (
                    "fixture API startup failed"
                )
                time.sleep(0.1)
            assert live.get("/api/v1/me").status_code == 401
            live.headers["Authorization"] = "Bearer dev-fixture"
            assert live.get("/api/v1/me").json()["processing_readiness"]["ready"]
            (host.STATE / "paused").touch()
            host.publish_checkpoint_status("paused")
            assert live.get("/api/v1/me").json()["processing_readiness"] == {
                "state": "paused",
                "ready": False,
            }
            (host.STATE / "paused").unlink()
            host.publish_checkpoint_status("idle")
            assert live.get("/api/v1/me").json()["processing_readiness"]["ready"]
            assert (
                live.get("/callback").content
                == Path("/app/web/dist/index.html").read_bytes()
            )
    finally:
        server.terminate()
        server.wait(timeout=10)
print(
    json.dumps(
        {
            "stabilization_passed": True,
            "baseline_missing_readiness_reproduced": True,
            "independent_attention_boot_holds": True,
            "renewal_failure_visible": True,
            "stale_readiness_fails_closed": True,
            "busy_heartbeat_and_concurrent_projection": True,
            "read_only_inspection_preserves_expired_stage": True,
            "real_database_failure_diagnostic": "OperationalError",
            "actual_api_factory_http_auth_and_readiness": True,
            "production_mutations": 0,
            "external_provider_calls": 0,
            "image_frontend_hash": hashlib.sha256(
                Path("/app/web/dist/index.html").read_bytes()
            ).hexdigest(),
        }
    )
)
