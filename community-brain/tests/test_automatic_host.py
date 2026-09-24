"""Host orchestration stops at durable uncertainty and recovery boundaries."""

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def host(tmp_path, monkeypatch):
    directory = ROOT / "deploy/community-brain/automatic"
    # Pin the helper's HERE independently of any previously imported manual run.
    monkeypatch.setitem(
        sys.modules,
        "run",
        SimpleNamespace(HERE=directory, IMAGE="fixture", read_env=lambda _: {}),
    )
    spec = importlib.util.spec_from_file_location(
        "automatic_host_fixture", directory / "automatic_host.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "STATE", tmp_path / "automation")
    for directory in ("files", "manual-approvals", "automation/checkpoints"):
        (tmp_path / directory).mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(module.subprocess, "check_output", lambda *_: b"")
    return module


def test_completed_job_blocks_next_stage_until_matching_verified_checkpoint(
    host, monkeypatch
):
    monkeypatch.setattr(
        host, "scan", lambda *_: {"completed": ["job"], "next": {"would": "run"}}
    )
    assert host.tick() == "awaiting_checkpoint"
    assert (
        json.loads((host.STATE / "checkpoint-needed.json").read_text())["job_id"]
        == "job"
    )
    monkeypatch.setattr(
        host, "scan", lambda *_: pytest.fail("checkpoint must block scans")
    )
    assert host.tick() == "awaiting_checkpoint"
    (host.STATE / "checkpoint-needed.json").unlink()
    (host.STATE / "checkpoints/job.json").write_text(
        json.dumps({"job_id": "wrong", "verified": True, "manifest_sha256": "a" * 64})
    )
    monkeypatch.setattr(host, "scan", lambda *_: {"completed": ["job"], "next": None})
    assert host.tick() == "awaiting_checkpoint"
    (host.STATE / "checkpoint-needed.json").unlink()
    (host.STATE / "checkpoints/job.json").write_text(
        json.dumps({"job_id": "job", "verified": True, "manifest_sha256": "a" * 64})
    )
    assert host.tick() == "idle"


def test_crashed_launcher_marker_never_executes_twice(host, monkeypatch):
    item = {
        "job_id": "job",
        "stage_id": "stage",
        "stage": "processing",
        "generation": 1,
    }
    (host.ROOT / "manual-approvals/job-processing-1.started").write_text(
        "already attempted"
    )
    calls = []

    def scan(*args):
        calls.append(args)
        return {"completed": [], "next": item}

    monkeypatch.setattr(host, "scan", scan)
    monkeypatch.setattr(
        host.subprocess, "run", lambda *_a, **_k: pytest.fail("must not launch")
    )
    assert host.tick() == "attention_required"
    assert calls == [("next",), ("stop", "stage")]


def test_pause_attention_and_orphan_container_prevent_scans(host, monkeypatch):
    monkeypatch.setattr(host, "scan", lambda *_: pytest.fail("must not scan"))
    (host.STATE / "paused").touch()
    assert host.tick() == "paused"
    (host.STATE / "attention.json").write_text("{}")
    assert host.tick() == "attention_required"
    (host.STATE / "paused").unlink()
    (host.STATE / "attention.json").unlink()
    monkeypatch.setattr(
        host.subprocess, "check_output", lambda *_: b"running-container"
    )
    assert host.tick() == "worker_running"


def test_scanner_is_visible_to_quiet_window_and_receives_only_database_access(
    host, monkeypatch
):
    monkeypatch.setattr(
        host,
        "read_env",
        lambda _: {
            "CB_DATABASE_URL": "fixture-db",
            "CB_OPENROUTER_API_KEY": "must-not-forward",
        },
    )

    def run(args, **kwargs):
        assert args[args.index("--label") + 1] == "cbm.automatic-stage=true"
        assert kwargs["env"]["CB_DATABASE_URL"] == "fixture-db"
        assert not any(
            "KEY" in key or "TOKEN" in key or "NATS" in key for key in kwargs["env"]
        )
        return SimpleNamespace(returncode=0, stdout=b'{"completed":[],"next":null}')

    monkeypatch.setattr(host.subprocess, "run", run)
    assert host.scan("next") == {"completed": [], "next": None}


def test_known_recoverable_failure_waits_without_latching(host, monkeypatch):
    monkeypatch.setattr(
        host,
        "scan",
        lambda *_: {
            "attention": True,
            "known_failure_only": True,
            "completed": [],
            "next": None,
        },
    )
    assert host.tick() == "needs_input"
    assert not (host.STATE / "attention.json").exists()
    monkeypatch.setattr(
        host, "scan", lambda *_: {"attention": False, "completed": [], "next": None}
    )
    assert host.tick() == "idle"


def test_unknown_failure_remains_held_and_keeps_first_evidence(host, monkeypatch):
    monkeypatch.setattr(
        host, "scan", lambda *_: {"attention": True, "known_failure_only": False}
    )
    assert host.tick() == "attention_required"
    host.record_attention(ValueError("private details must not leak"))
    original = (host.STATE / "attention.json").read_text()
    host.record_attention(RuntimeError("later"))
    assert (host.STATE / "attention.json").read_text() == original
    assert "private details" not in original and "ValueError" in original


def test_backup_projection_requires_matching_receipt_and_excludes_private_paths(host):
    job_id = "744d0f3f-8da7-4c12-bc15-5ec0a046518d"
    path = host.STATE / "checkpoints" / f"{job_id}.json"
    value = {
        "job_id": "wrong",
        "verified": True,
        "manifest_sha256": "a" * 64,
        "receipt": "/private/path",
    }
    path.write_text(json.dumps(value))
    host.publish_checkpoint_status()
    public = host.ROOT / "automation-public/checkpoints.json"
    assert json.loads(public.read_text())["checkpoints"][job_id] == "requires_review"
    value["job_id"] = job_id
    path.write_text(json.dumps(value))
    host.publish_checkpoint_status()
    assert json.loads(public.read_text())["checkpoints"][job_id] == "verified"
    assert (
        "/private" not in public.read_text()
        and "manifest_sha256" not in public.read_text()
    )
    assert public.stat().st_mode & 0o777 == 0o644


def test_readiness_projection_keeps_independent_boot_and_attention_holds(host):
    from datetime import datetime, timedelta, timezone

    now = datetime.now(timezone.utc)
    (host.STATE / "boot-state.json").write_text(
        json.dumps({"reconciled": False, "boot_id": "private"})
    )
    (host.STATE / "paused").write_text("private operational details")
    host.record_attention(RuntimeError("secret"))
    management = host.ROOT / "management-status"
    management.mkdir()
    (management / "maintenance.json").write_text(
        json.dumps(
            {
                "checked_at": now.isoformat(),
                "renewal": {"state": "failed", "private": "secret"},
                "service_identities": [
                    {
                        "expires_at": (now + timedelta(days=2)).timestamp(),
                        "token": "secret",
                    }
                ],
            }
        )
    )
    host.publish_checkpoint_status("attention_required")
    raw = (host.ROOT / "automation-public/checkpoints.json").read_text()
    value = json.loads(raw)["processing"]
    assert value["paused"] and value["attention"] and not value["boot_reconciled"]
    assert value["renewal"] == "failed" and not value["credentials_expired"]
    assert "secret" not in raw and "boot_id" not in raw


def test_scan_failure_preserves_safe_root_class_and_first_event(host, monkeypatch):
    monkeypatch.setattr(host, "read_env", lambda _: {"CB_DATABASE_URL": "secret"})
    monkeypatch.setattr(
        host.subprocess,
        "run",
        lambda *_a, **_k: SimpleNamespace(
            returncode=1,
            stdout=b"",
            stderr=b'{"code":"automatic_scan_failed","error_class":"OperationalError"}',
        ),
    )
    with pytest.raises(host.ScanFailure) as error:
        host.scan("next")
    host.record_attention(error.value)
    value = json.loads((host.STATE / "attention.json").read_text())
    assert value["diagnostic"]["scanner_error_class"] == "OperationalError"
    assert value["diagnostic"]["returncode"] == 1
    assert "secret" not in json.dumps(value)
    first = (host.STATE / "attention.json").read_bytes()
    host.record_attention(RuntimeError("later"))
    assert (host.STATE / "attention.json").read_bytes() == first


def test_raw_docker_errors_never_leak_into_diagnostics(host, monkeypatch):
    monkeypatch.setattr(host, "read_env", lambda _: {"CB_DATABASE_URL": "secret"})
    monkeypatch.setattr(
        host.subprocess,
        "run",
        lambda *_a, **_k: SimpleNamespace(
            returncode=125,
            stdout=b"private stdout",
            stderr=b"password=private stderr",
        ),
    )
    with pytest.raises(host.ScanFailure) as error:
        host.scan("next")
    assert "private" not in json.dumps(error.value.diagnostic)
    assert error.value.diagnostic["returncode"] == 125


def test_scan_timeout_is_not_retried(host, monkeypatch):
    monkeypatch.setattr(host, "read_env", lambda _: {"CB_DATABASE_URL": "secret"})
    calls = []

    def timeout(*args, **kwargs):
        calls.append(args)
        raise host.subprocess.TimeoutExpired(["secret-command"], 90, stderr=b"secret")

    monkeypatch.setattr(host.subprocess, "run", timeout)
    with pytest.raises(host.ScanFailure) as error:
        host.scan("next")
    assert error.value.diagnostic == {"code": "automatic_scan_timeout"}
    assert len(calls) == 1


def test_busy_tick_refreshes_status_without_scanning_or_running_work(host, monkeypatch):
    monkeypatch.setattr(host, "scan", lambda *_: pytest.fail("read-only heartbeat"))
    monkeypatch.setattr(host.subprocess, "check_output", lambda *_a, **_k: b"worker")
    host.publish_busy_status()
    p = host.ROOT / "automation-public/checkpoints.json"
    assert json.loads(p.read_text())["processing"]["runner"] == "worker_running"
    (host.STATE / "paused").touch()
    host.publish_busy_status()
    assert json.loads(p.read_text())["processing"]["paused"] is True


def test_atomic_projection_writers_never_share_a_temporary_file(host):
    from concurrent.futures import ThreadPoolExecutor

    path = host.STATE / "concurrent.json"
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda i: host.atomic(path, {"value": i}), range(20)))
    assert json.loads(path.read_text())["value"] in range(20)
    assert not list(host.STATE.glob(".concurrent.json*"))
