"""Host-only bounded production orchestration; private credentials stay on VM109."""

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from run import IMAGE, read_env

HERE = Path(__file__).resolve().parent
EVIDENCE = Path("/srv/community-brain/artifacts/cbm-bounded-production-20260910")
NETWORK = "community-brain-production-staging_default"
NAME = "cbm-bounded-submit"


def run(args, env=None, payload=None, label="check"):
    result = subprocess.run(
        args, env=env, input=payload, capture_output=True, check=False
    )
    (EVIDENCE / (label + ".log")).write_bytes(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(label + " failed; private log retained")
    return result.stdout


def docker():
    return [
        "docker",
        "run",
        "--rm",
        "-i",
        "--network",
        NETWORK,
        "--read-only",
        "--tmpfs",
        "/tmp",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges:true",
        "--memory",
        "1g",
        "--cpus",
        "1",
        "-v",
        str(HERE) + ":/checks:ro",
        "-v",
        "/etc/ssl/certs/ca-certificates.crt:/run/certs/ca-bundle.pem:ro",
    ]


def allowance(require_unused=False):
    key = read_env("bounded-model.env")["CB_OPENROUTER_API_KEY"]
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/key", headers={"Authorization": "Bearer " + key}
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        data = json.load(r)["data"]
    safe = {
        k: data[k]
        for k in (
            "limit",
            "limit_reset",
            "limit_remaining",
            "usage",
            "is_management_key",
            "include_byok_in_limit",
        )
    }
    assert (
        safe["limit"] == 2
        and safe["limit_reset"] is None
        and safe["is_management_key"] is False
        and safe["include_byok_in_limit"] is True
    )
    assert safe["limit_remaining"] > 0
    if require_unused:
        assert safe["usage"] == 0
    return safe


def main():
    os.umask(0o077)
    EVIDENCE.mkdir(mode=0o700, exist_ok=True)
    operation = sys.argv[1]
    assert operation in {"preflight", "submit", "worker", "allowance"}
    private = read_env("rehearsal-client.env")
    assert time.time() < int(private["CB_REHEARSAL_EXPIRES_AT"])
    if operation in {"preflight", "allowance"}:
        safe = allowance(operation == "preflight")
        if operation == "preflight":
            with urllib.request.urlopen(
                "https://openrouter.ai/api/v1/models", timeout=20
            ) as r:
                available = {v["id"] for v in json.load(r)["data"]}
            raw = run(
                docker()
                + [
                    IMAGE,
                    "python",
                    "-c",
                    'import json; from community_brain.processing.pipeline import SNAPSHOT; print(json.dumps(sorted({s["model"] for v in SNAPSHOT.values() for s in v["config"]["steps"].values()})))',
                ],
                label="models",
            )
            models = json.loads(raw)
            assert set(models) <= available
            safe["frozen_models_available"] = models
        (EVIDENCE / (operation + ".json")).write_text(json.dumps(safe) + "\n")
        print(json.dumps(safe))
        return
    if operation == "submit":
        assert not (EVIDENCE / "jobs.json").exists()
        allowance(True)
        env = dict(os.environ)
        env.update(read_env("rehearsal-api.env"))
        env.update(
            CB_CORPUS_SCOPE="community-brain",
            CB_STORAGE_ROOT="/state/files",
            CB_PIPELINE_CONFIG_DIR="/state/config",
            CB_ENABLE_MODEL_CALLS="false",
            CB_ENABLE_NETWORK_PUBLICATION="false",
            CB_ENABLE_RETRIEVAL="false",
        )
        args = docker()
        args.remove("--rm")
        args += [
            "-d",
            "--name",
            NAME,
            "-v",
            "/srv/community-brain/files:/state/files",
            "-v",
            "/srv/community-brain/config:/state/config:ro",
        ]
        for k in env:
            if k.startswith("CB_"):
                args += ["-e", k]
        try:
            run(args + [IMAGE], env=env, label="private-api")
            for _ in range(30):
                check = subprocess.run(
                    [
                        "docker",
                        "exec",
                        NAME,
                        "python",
                        "-c",
                        "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=2)",
                    ],
                    capture_output=True,
                    check=False,
                )
                if check.returncode == 0:
                    break
                time.sleep(1)
            else:
                raise RuntimeError("private API health timeout")
            raw = run(
                docker() + [IMAGE, "python", "/checks/submit_synthetic.py"],
                payload=json.dumps(private).encode(),
                label="submit",
            )
            jobs = json.loads(raw)
            assert (
                set(jobs) == {"weekly", "transcript_backfill"}
                and len(set(jobs.values())) == 2
            )
            (EVIDENCE / "jobs.json").write_text(json.dumps(jobs) + "\n")
            approval = EVIDENCE / "approval"
            approval.mkdir(mode=0o700)
            os.chown(approval, 10001, 10001)
            (approval / "jobs.json").write_text(json.dumps(jobs) + "\n")
            os.chown(approval / "jobs.json", 10001, 10001)
            print(json.dumps(jobs))
        finally:
            subprocess.run(
                ["docker", "rm", "-f", NAME],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
    else:
        allowance(True)
        sentinel = EVIDENCE / "worker-started"
        with sentinel.open("x") as f:
            f.write("Automatic restart forbidden\n")
        env = {"PATH": os.defpath}
        env.update(read_env("worker.env"))
        env.update(read_env("bounded-model.env"))
        env["CB_DATABASE_URL"] = read_env("api.env")["CB_DATABASE_URL"]
        env.update(
            CB_ENABLE_MODEL_CALLS="true",
            CB_ENABLE_NETWORK_PUBLICATION="false",
            CB_STORAGE_ROOT="/state/files",
            CB_PIPELINE_CONFIG_DIR="/state/config",
            SSL_CERT_FILE="/run/certs/ca-bundle.pem",
            REQUESTS_CA_BUNDLE="/run/certs/ca-bundle.pem",
        )
        args = docker() + [
            "--name",
            "cbm-bounded-worker",
            "-v",
            "/srv/community-brain/files:/state/files",
            "-v",
            "/srv/community-brain/config:/state/config:ro",
            "-v",
            str(EVIDENCE / "approval") + ":/approval:ro",
        ]
        for k in env:
            if k != "PATH":
                args += ["-e", k]
        manifest = {
            p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in HERE.iterdir()
            if p.is_file()
        }
        (EVIDENCE / "helper-hashes.json").write_text(
            json.dumps(manifest, sort_keys=True) + "\n"
        )
        output = run(
            args + [IMAGE, "python", "/checks/bounded_worker.py"],
            env=env,
            label="worker",
        )
        print(output.decode())


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001 - redact credential-bearing provider errors
        raise SystemExit(
            "Bounded operation failed; inspect private diagnostics, no automatic retry"
        ) from None
