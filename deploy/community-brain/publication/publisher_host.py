"""Root-only launcher, called under management's ordered quiet locks."""

import json
import os
from pathlib import Path
import shlex
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = Path("/srv/community-brain")
RUN = ROOT / "artifacts/first-publication-20260917"
IMAGE = "community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449"
PACKAGES = (
    "/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs"
)


def read_env(name):
    path = Path("/etc/community-brain-production") / name
    assert path.stat().st_uid == 0 and path.stat().st_mode & 0o777 == 0o600
    result = {}
    for line in path.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            key, value = line.split("=", 1)
            parts = shlex.split(value)
            assert len(parts) == 1
            result[key] = parts[0]
    return result


def command(operation, stage, api, worker, publisher):
    if operation not in {"preflight", "enqueue", "execute"} or stage not in {
        "git",
        "distribution",
    }:
        raise ValueError("unapproved command")
    permitted = {
        "CB_PUBLISHER_GITHUB_TOKEN",
        "CB_PUBLISHER_GITHUB_TOKEN_EXPIRES_AT",
        "CB_PUBLISHER_GITHUB_APP_ID",
        "CB_PUBLISHER_GITHUB_INSTALLATION_ID",
        "CB_PUBLISHER_GITHUB_REPOSITORY_IDS",
    }
    env = {
        "PATH": os.defpath,
        "CB_DATABASE_URL": api["CB_DATABASE_URL"],
        **{k: publisher[k] for k in permitted},
        **{k: worker[k] for k in ("CB_NATS_URL", "CB_NATS_USER", "CB_NATS_PASSWORD")},
        "CB_ENABLE_NETWORK_PUBLICATION": "true",
        "CB_ENABLE_MODEL_CALLS": "false",
        "CB_PUBLICATION_PLAN_SHA256": "a7ac3cf3f0d2ee31c184f956b6c1c2fd61545d8c3d23179ca8506a53ad506759",
        "SSL_CERT_FILE": "/run/certs/ca-bundle.pem",
        "REQUESTS_CA_BUNDLE": "/run/certs/ca-bundle.pem",
    }
    args = [
        "docker",
        "run",
        "--rm",
        "--read-only",
        "--tmpfs",
        "/tmp",
        "--user",
        "10001:10001",
        "--memory",
        "1500m",
        "--cpus",
        "2",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--label",
        "cbm.selected-publication=true",
    ]
    for source, target in [
        (ROOT / "files", "/files"),
        (RUN / "repos", "/repos"),
        (RUN / "candidate", "/candidate"),
        (RUN / "approval", "/approval"),
        (HERE, "/helpers"),
        (Path("/etc/ssl/certs/ca-certificates.crt"), "/run/certs/ca-bundle.pem"),
    ]:
        args += ["-v", f"{source}:{target}:ro"]
    args += ["-v", f"{RUN}/journal:/journal:rw"]
    for name in (
        "manual",
        "store",
        "worker",
        "publication",
        "publication_selection",
        "prepared_publication",
        "github_release",
    ):
        args += ["-v", f"{HERE}/jobs/{name}.py:{PACKAGES}/{name}.py:ro"]
    for key in env:
        if key != "PATH":
            args += ["-e", key]
    args += [
        "--entrypoint",
        "/app/community-brain/.venv/bin/python",
        IMAGE,
        "/helpers/publisher_worker.py",
        operation,
        stage,
    ]
    return args, env


if __name__ == "__main__":
    os.umask(0o077)
    try:
        assert os.geteuid() == 0 and RUN.is_dir()
        args, env = command(
            sys.argv[1],
            sys.argv[2],
            read_env("api.env"),
            read_env("worker.env"),
            read_env("publication.env"),
        )
        with (RUN / "launcher.log").open("ab") as log:
            result = subprocess.run(args, env=env, stdout=log, stderr=log, check=False)
        print(
            json.dumps(
                {
                    "operation": sys.argv[1],
                    "stage": sys.argv[2],
                    "exit_code": result.returncode,
                }
            )
        )
        raise SystemExit(result.returncode)
    except Exception as exc:
        print(
            json.dumps({"state": "requires_review", "error_class": type(exc).__name__})
        )
        raise SystemExit(1)
