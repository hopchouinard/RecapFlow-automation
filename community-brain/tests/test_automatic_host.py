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
