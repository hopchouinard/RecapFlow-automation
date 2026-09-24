"""Pinned Git commits and release ordering, entirely local/mocked."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
from datetime import datetime, timezone, timedelta

import pytest
from community_brain.jobs.prepared_publication import (
    PreparedGit,
    PreparedPublication,
    REPOSITORIES,
)
from community_brain.processing.pipeline import PipelineFailure, OutcomeUnknown


def prepared(tmp_path, name, files):
    work = tmp_path / (name + "-work")
    work.mkdir()
    env = {
        **os.environ,
        "GIT_AUTHOR_NAME": "Fixture",
        "GIT_AUTHOR_EMAIL": "fixture@localhost",
        "GIT_COMMITTER_NAME": "Fixture",
        "GIT_COMMITTER_EMAIL": "fixture@localhost",
    }

    def git(*args):
        return (
            subprocess.check_output(
                ["git", "-c", "commit.gpgsign=false", *args],
                cwd=work,
                env=env,
                stderr=subprocess.DEVNULL,
            )
            .decode()
            .strip()
        )

    git("init", "-b", "main")
    git("commit", "--allow-empty", "-m", "base")
    base = git("rev-parse", "HEAD")
    remote = tmp_path / (name + "-remote.git")
    subprocess.run(
        ["git", "clone", "--bare", str(work), str(remote)],
        check=True,
        capture_output=True,
    )
    hashes = {}
    for path, content in files.items():
        p = work / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        if path == "download-corpus.sh":
            p.chmod(0o755)
        hashes[path] = hashlib.sha256(p.read_bytes()).hexdigest()
    git("add", ".")
    git("commit", "-m", "approved")
    commit = git("rev-parse", "HEAD")
    spec = {
        "repository": REPOSITORIES[name],
        "branch": "main",
        "base": base,
        "commit": commit,
    }
    return PreparedGit(work / ".git", spec, local_remote=str(remote)), hashes


def test_exact_commit_then_standard_fast_forward_push(tmp_path):
    git, files = prepared(
        tmp_path, "operator", {"output/2026-09-15/transcript.txt": "approved"}
    )
    git.validate(files)
    journal = tmp_path / "operations.jsonl"
    assert git.push("refs/heads/main", git.spec["base"], journal) == git.spec["commit"]
    entries = [json.loads(v) for v in journal.read_text().splitlines()]
    assert [v["state"] for v in entries] == ["intent", "verified"]
    with pytest.raises(PipelineFailure, match="remote_ref"):
        git.push("refs/heads/main", git.spec["base"], journal)


def test_changed_scope_or_content_rejected(tmp_path):
    git, files = prepared(
        tmp_path, "operator", {"output/2026-09-15/transcript.txt": "approved"}
    )
    with pytest.raises(PipelineFailure, match="file_scope"):
        git.validate({**files, "unapproved.txt": "a" * 64})
    with pytest.raises(PipelineFailure, match="content_mismatch"):
        git.validate({next(iter(files)): "a" * 64})


def test_distribution_tag_release_then_main_and_unknown_stops(tmp_path, monkeypatch):
    operator, _ = prepared(
        tmp_path, "operator", {"output/2026-09-15/transcript.txt": "approved"}
    )
    consumer, _ = prepared(
        tmp_path, "consumer", {"download-corpus.sh": "approved pins"}
    )
    journal = tmp_path / "journal"
    operator.push("refs/heads/main", operator.spec["base"], journal)

    class Publisher:
        def publish(self, *args):
            assert consumer.head("refs/tags/v1.2.0") == consumer.spec["commit"]
            assert consumer.head("refs/heads/main") == consumer.spec["base"]
            raise OutcomeUnknown("lost publish response")

    plan = {
        "job_id": "fixture",
        "operator": operator.spec,
        "consumer": consumer.spec,
        "version": "v1.2.0",
        "assets": {"corpus-v1.2.0.tar.gz": "a" * 64},
    }
    handler = PreparedPublication(
        plan, tmp_path, operator, consumer, Publisher(), journal
    )
    monkeypatch.setattr(handler, "validate", lambda: None)
    with pytest.raises(OutcomeUnknown):
        handler.distribution("fixture")
    assert consumer.head("refs/heads/main") == consumer.spec["base"]
    assert consumer.head("refs/tags/v1.2.0") == consumer.spec["commit"]
    with pytest.raises(PipelineFailure, match="remote_ref"):
        handler.distribution("fixture")


def test_distribution_success_updates_main_after_verified_release(
    tmp_path, monkeypatch
):
    operator, _ = prepared(
        tmp_path, "operator", {"output/2026-09-15/transcript.txt": "approved"}
    )
    consumer, files = prepared(
        tmp_path, "consumer", {"download-corpus.sh": "approved pins"}
    )
    consumer.validate(files)
    journal = tmp_path / "journal"
    operator.push("refs/heads/main", operator.spec["base"], journal)

    class Publisher:
        def publish(self, *args):
            assert consumer.head("refs/heads/main") == consumer.spec["base"]
            assert consumer.head("refs/tags/v1.2.0") == consumer.spec["commit"]
            return {"release_id": 1}

    plan = {
        "job_id": "fixture",
        "operator": operator.spec,
        "consumer": consumer.spec,
        "version": "v1.2.0",
        "assets": {"corpus-v1.2.0.tar.gz": "a" * 64},
    }
    handler = PreparedPublication(
        plan, tmp_path, operator, consumer, Publisher(), journal
    )
    monkeypatch.setattr(handler, "validate", lambda: None)
    assert handler.distribution("fixture")["receipt"] == {"release_id": 1}
    assert consumer.head("refs/heads/main") == consumer.spec["commit"]


def test_write_guard_runs_before_remote_mutation(tmp_path):
    git, _ = prepared(tmp_path, "operator", {"transcript.txt": "approved"})

    def reject():
        raise ValueError("lost claim")

    git.before_write = reject
    with pytest.raises(ValueError, match="lost claim"):
        git.push("refs/heads/main", git.spec["base"], tmp_path / "journal")
    assert git.head("refs/heads/main") == git.spec["base"]
    assert not (tmp_path / "journal").exists()


def test_oneshot_requires_fresh_scoped_identity_without_provider_keys():
    path = (
        Path(__file__).resolve().parents[2]
        / "deploy/community-brain/publication/publisher_worker.py"
    )
    spec = importlib.util.spec_from_file_location("publisher_controls", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    env = {
        "CB_ENABLE_NETWORK_PUBLICATION": "true",
        "CB_ENABLE_MODEL_CALLS": "false",
        "CB_PUBLISHER_GITHUB_APP_ID": "4978270",
        "CB_PUBLISHER_GITHUB_INSTALLATION_ID": "162488086",
        "CB_PUBLISHER_GITHUB_REPOSITORY_IDS": "[1176379254,1249770482]",
        "CB_PUBLISHER_GITHUB_TOKEN": "fixture",
        "CB_PUBLISHER_GITHUB_TOKEN_EXPIRES_AT": (
            datetime.now(timezone.utc) + timedelta(hours=1)
        ).isoformat(),
    }
    module.controls(env)
    for changes in (
        {"CB_ENABLE_NETWORK_PUBLICATION": "false"},
        {"CB_OPENROUTER_API_KEY": "fixture"},
        {"CB_PUBLISHER_GITHUB_REPOSITORY_IDS": "[1,2]"},
        {
            "CB_PUBLISHER_GITHUB_TOKEN_EXPIRES_AT": datetime.now(
                timezone.utc
            ).isoformat()
        },
    ):
        with pytest.raises(ValueError):
            module.controls({**env, **changes})


def test_host_passes_only_selected_credentials_and_read_only_inputs():
    path = (
        Path(__file__).resolve().parents[2]
        / "deploy/community-brain/publication/publisher_host.py"
    )
    spec = importlib.util.spec_from_file_location("publisher_host_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    pub = {
        k: "fixture"
        for k in [
            "CB_PUBLISHER_GITHUB_TOKEN",
            "CB_PUBLISHER_GITHUB_TOKEN_EXPIRES_AT",
            "CB_PUBLISHER_GITHUB_APP_ID",
            "CB_PUBLISHER_GITHUB_INSTALLATION_ID",
            "CB_PUBLISHER_GITHUB_REPOSITORY_IDS",
        ]
    }
    pub["CB_PUBLISHER_GITHUB_PRIVATE_KEY_BASE64"] = "forbidden"
    args, env = module.command(
        "execute",
        "git",
        {"CB_DATABASE_URL": "fixture", "CB_SERVICE_IDENTITIES": "forbidden"},
        {
            "CB_NATS_URL": "fixture",
            "CB_NATS_USER": "fixture",
            "CB_NATS_PASSWORD": "fixture",
            "CB_OPENROUTER_API_KEY": "forbidden",
        },
        pub,
    )
    assert "forbidden" not in env.values()
    assert (
        env["CB_ENABLE_NETWORK_PUBLICATION"] == "true"
        and env["CB_ENABLE_MODEL_CALLS"] == "false"
    )
    mounts = [args[i + 1] for i, v in enumerate(args) if v == "-v"]
    assert all(m.endswith(":ro") for m in mounts if ":/journal:" not in m)
    assert not any(":/state/corpus:" in m for m in mounts)
    assert args[-2:] == ["execute", "git"]
