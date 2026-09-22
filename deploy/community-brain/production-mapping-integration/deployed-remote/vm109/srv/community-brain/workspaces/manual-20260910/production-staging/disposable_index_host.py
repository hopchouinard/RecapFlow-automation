"""Explicit host operations for one data-only VM108 rehearsal, no live URLs."""

import hashlib
import json
import os
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path("/srv/dev-data/workspaces/cbm-manual-index-20260910")
IMAGE = "sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449"
PACKAGES = (
    "/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs"
)


def run(args, *, input=None, env=None, log="host.log"):
    with (ROOT / log).open("ab") as output:
        result = subprocess.run(
            args, input=input, stdout=output, stderr=output, env=env, check=False
        )
    if result.returncode:
        raise RuntimeError(f"Operation failed; inspect private {log}")


def compose(*args, **kwargs):
    run(["docker", "compose", "-f", str(ROOT / "compose.json"), *args], **kwargs)


def setup():
    if (ROOT / "copy.json").exists():
        raise RuntimeError("Existing copy requires inspection; setup is not replayable")
    expected = {
        "production.dump": "9543dbb6eeb49ab7c8a6b37420e0514a2461e24f3924a6ce3f0cc7cf2bb1c60b",
        "managed-state.tar.gz": "8e0ae8cf17ebeea4e0248422fdea4f79eb7ea455fc3b4194e05b1622d8ac4941",
        "managed-state-manifest.json": "47c1450d1909fc46d49407fc9c7c38d50c7075b28e7488aa52c5af4c6c6d5763",
    }
    for name, sha in expected.items():
        assert hashlib.sha256((ROOT / "inputs" / name).read_bytes()).hexdigest() == sha
    assert not list((ROOT / "state").iterdir())
    manifest = json.loads((ROOT / "inputs/managed-state-manifest.json").read_text())
    with tarfile.open(ROOT / "inputs/managed-state.tar.gz") as archive:
        members = archive.getmembers()
        assert all(m.isfile() and m.name in manifest["files"] for m in members)
        assert len(members) == len(manifest["files"]) == 53
        archive.extractall(ROOT / "state", filter="data")
    for name, value in manifest["files"].items():
        assert (
            hashlib.sha256((ROOT / "state" / name).read_bytes()).hexdigest()
            == value["sha256"]
        )
    for path in [ROOT / "state", *(ROOT / "state").rglob("*")]:
        path.chmod(0o700 if path.is_dir() else 0o600)
        os.chown(path, 10001, 10001)
    (ROOT / "copy.json").write_text(
        json.dumps(
            {"identity": "cbm-manual-index-20260910-vm108", "input_sha256": expected}
        )
    )
    (ROOT / "copy.json").chmod(0o644)
    (ROOT / "inputs/managed-state-manifest.json").chmod(0o644)
    worker = {
        "image": IMAGE,
        "pull_policy": "never",
        "profiles": ["manual"],
        "user": "10001:10001",
        "read_only": True,
        "restart": "no",
        "tmpfs": ["/tmp"],
        "cap_drop": ["ALL"],
        "security_opt": ["no-new-privileges:true"],
        "mem_limit": "1500m",
        "cpus": 2,
        "networks": ["copy", "egress"],
        "environment": {
            "CB_DATABASE_URL": "postgresql+psycopg://cbmcopy@postgres:5432/cbm_copy",
            "CB_STORAGE_ROOT": "/state/files",
            "CB_PIPELINE_CONFIG_DIR": "/state/config",
            "COMMUNITY_BRAIN_CONFIG_DIR": "/state/config",
            "CB_CORPUS_ROOT": "/state/corpus",
            "COMMUNITY_BRAIN_ARTIFACT_ROOT": "/state/corpus/ingest",
            "CB_ENABLE_NETWORK_PUBLICATION": "false",
            "OLLAMA_BASE_URL": "http://10.1.50.219:11434",
        },
        "volumes": [
            f"{ROOT}/state:/state",
            f"{ROOT}/helpers:/helpers:ro",
            f"{ROOT}/inputs/managed-state-manifest.json:/inputs/managed-state-manifest.json:ro",
            f"{ROOT}/copy.json:/copy.json:ro",
            *[
                f"{ROOT}/helpers/{name}:{PACKAGES}/{name}:ro"
                for name in ("manual.py", "store.py", "worker.py")
            ],
        ],
        "entrypoint": ["python", "/helpers/disposable_index.py"],
    }
    config = {
        "name": "cbm-manual-copy",
        "services": {
            "postgres": {
                "image": "postgres:18.6",
                "pull_policy": "never",
                "restart": "no",
                "mem_limit": "384m",
                "cpus": 1,
                "networks": ["copy"],
                "environment": {
                    "POSTGRES_USER": "cbmcopy",
                    "POSTGRES_DB": "cbm_copy",
                    "POSTGRES_HOST_AUTH_METHOD": "trust",
                },
                "volumes": ["pg:/var/lib/postgresql"],
                "healthcheck": {
                    "test": ["CMD", "pg_isready", "-U", "cbmcopy", "-d", "cbm_copy"],
                    "interval": "2s",
                    "timeout": "2s",
                    "retries": 30,
                },
            },
            "nats": {
                "image": "nats:2.10.27",
                "pull_policy": "never",
                "restart": "no",
                "mem_limit": "128m",
                "cpus": 0.5,
                "networks": ["copy"],
                "command": ["--jetstream", "--store_dir", "/data"],
                "volumes": ["nats:/data"],
            },
            "worker": worker,
        },
        "networks": {"copy": {"internal": True}, "egress": {}},
        "volumes": {"pg": {}, "nats": {}},
    }
    (ROOT / "compose.json").write_text(json.dumps(config, indent=2))
    compose("up", "-d", "--wait", "postgres", "nats")
    compose(
        "exec",
        "-T",
        "postgres",
        "pg_restore",
        "-U",
        "cbmcopy",
        "-d",
        "cbm_copy",
        "--no-owner",
        "--no-acl",
        "--exit-on-error",
        input=(ROOT / "inputs/production.dump").read_bytes(),
    )
    print(
        "53 copied files verified; private DB restored; no host ports or live platform credentials"
    )


if __name__ == "__main__":
    os.umask(0o077)
    if os.geteuid() != 0 or not ROOT.is_dir():
        raise RuntimeError("VM108 root context required")
    action = sys.argv[1]
    if action == "setup":
        setup()
    elif action in ("preflight", "verify"):
        compose("run", "--rm", "--no-deps", "worker", action, log=f"{action}.log")
        print(f"{action} completed; private receipt at {ROOT}/{action}.log")
    elif action == "execute":
        marker = ROOT / "worker-started"
        with marker.open("x") as output:
            output.write(
                "One approved copy-only indexing execution; do not remove to replay.\n"
            )
        import shlex

        lines = (ROOT / "bounded-model.env").read_text().splitlines()
        values = dict(
            line.split("=", 1) for line in lines if line and not line.startswith("#")
        )
        assert set(values) == {"CB_OPENROUTER_API_KEY"}
        env = {
            **os.environ,
            "CB_OPENROUTER_API_KEY": shlex.split(values["CB_OPENROUTER_API_KEY"])[0],
        }
        try:
            compose(
                "run",
                "--rm",
                "--no-deps",
                "-e",
                "CB_OPENROUTER_API_KEY",
                "worker",
                "execute",
                env=env,
                log="execute.log",
            )
        finally:
            (ROOT / "bounded-model.env").unlink()
        print("Approved copy indexing completed; temporary key delivery removed")
    elif action == "down":
        compose("down", "--volumes")
        print(
            "Disposable containers/networks/DB/queue volumes removed; private file evidence retained"
        )
    else:
        raise ValueError("unknown action")
