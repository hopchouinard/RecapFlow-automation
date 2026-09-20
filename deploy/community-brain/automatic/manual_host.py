"""VM109 manual API staging and explicitly selected, non-restarting workers."""

import json
import os
import subprocess
import sys
from pathlib import Path

from run import HERE, IMAGE, read_env

ROOT = Path("/srv/community-brain")
PACKAGES = (
    "/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs"
)
PERMISSIONS = {
    "community-brain-prod-mac-collector": {"sources:upload:chat"},
    "community-brain-prod-manual-operator": {
        "sources:upload",
        "jobs:submit",
        "jobs:read",
        "artifacts:read",
    },
}


def validate_identities(private):
    identities = json.loads(private["CB_SERVICE_IDENTITIES"])
    found = set()
    for identity in identities:
        assert identity["scope"] == "community-brain"
        subject = identity["subject"]
        if subject in PERMISSIONS:
            assert set(identity["permissions"]) == PERMISSIONS[subject]
            found.add(subject)
        else:
            assert set(identity["permissions"]) <= {
                "jobs:read",
                "artifacts:read",
                "retrieval:read",
                "metrics:read",
            }
    assert found == set(PERMISSIONS)


def main():
    os.umask(0o077)
    assert os.geteuid() == 0 and (ROOT / "files").is_dir()
    command = sys.argv[1]
    if command == "api-up":
        private = read_env("api.env")
        validate_identities(private)
        env = {**os.environ, **private, "CB_IMAGE": IMAGE, "CB_API_BIND": "10.1.30.21"}
        args = [
            "docker",
            "compose",
            "--env-file",
            "/dev/null",
            "-f",
            str(HERE.parent / "compose.production-staging.yml"),
            "-f",
            str(HERE.parent / "compose.production-manual.yml"),
            "up",
            "-d",
            "--no-build",
            "api",
        ]
        with (HERE / "manual-api-up.log").open("ab") as output:
            subprocess.run(args, env=env, stdout=output, stderr=output, check=True)
        print("Manual API staged; corpus/config remain read-only; no workers started")
        return
    if command not in {"inspect", "execute"}:
        raise ValueError("explicit api-up, inspect or execute required")
    approvals = ROOT / "manual-approvals"
    approvals.mkdir(mode=0o700, exist_ok=True)
    env = {
        "PATH": os.defpath,
        "CB_DATABASE_URL": read_env("api.env")["CB_DATABASE_URL"],
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
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--memory",
        "1500m",
        "--cpus",
        "2",
        "-v",
        f"{ROOT}/files:/state/files:rw",
        "-v",
        f"{ROOT}/config:/state/config:ro",
        "-v",
        f"{HERE}:/helpers:ro",
        "-v",
        "/etc/ssl/certs/ca-certificates.crt:/run/certs/ca-bundle.pem:ro",
    ]
    for name in ("manual.py", "store.py", "worker.py", "automatic.py", "acquisition.py"):
        args += ["-v", f"{HERE}/jobs/{name}:{PACKAGES}/{name}:ro"]
    env.update(
        CB_STORAGE_ROOT="/state/files",
        CB_PIPELINE_CONFIG_DIR="/state/config",
        COMMUNITY_BRAIN_CONFIG_DIR="/state/config",
        CB_CORPUS_ROOT="/state/corpus",
        CB_ENABLE_NETWORK_PUBLICATION="false",
        OLLAMA_BASE_URL="http://10.1.50.219:11434",
        SSL_CERT_FILE="/run/certs/ca-bundle.pem",
    )
    if os.environ.get("CB_AUTOMATIC_ONLY") == "true":
        env["CB_AUTOMATIC_ONLY"] = "true"
        args += ["--label", "cbm.automatic-stage=true"]
    if command == "inspect":
        from uuid import UUID

        job = str(UUID(sys.argv[2]))
        name = sys.argv[3]
        generation = int(sys.argv[4])
        assert name in {"acquisition", "processing", "indexing"} and generation >= 1
        destination = approvals / f"{job}-{name}-{generation}.json"
        assert not destination.exists()
        extra = ["inspect", job, name, str(generation)]
        args += ["-v", f"{ROOT}/corpus:/state/corpus:ro"]
    else:
        destination = Path(sys.argv[2])
        assert (
            destination.resolve().parent == approvals.resolve()
            and not destination.is_symlink()
        )
        selected = json.loads(destination.read_text())
        name = selected["stage"]
        assert name in {"acquisition", "processing", "indexing"}
        with destination.with_suffix(".started").open("x") as marker:
            marker.write(
                "One manual execution; reconcile durable outcome before any further run.\n"
            )
            marker.flush()
            os.fsync(marker.fileno())
        fd = os.open(destination.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        worker = read_env("worker.env")
        env.update(
            {
                key: worker[key]
                for key in ("CB_NATS_URL", "CB_NATS_USER", "CB_NATS_PASSWORD")
            }
        )
        if name == "acquisition":
            env["CB_FATHOM_API_KEY"] = read_env("acquisition.env")["CB_FATHOM_API_KEY"]
        else:
            env["CB_OPENROUTER_API_KEY"] = read_env("bounded-model.env")[
                "CB_OPENROUTER_API_KEY"
            ]
            env["CB_ENABLE_MODEL_CALLS"] = "true"
        if name == "indexing":
            args[args.index(f"{ROOT}/config:/state/config:ro")] = (
                f"{ROOT}/config:/state/config:rw"
            )
        args += [
            "-v",
            f"{ROOT}/corpus:/state/corpus:{'rw' if name == 'indexing' else 'ro'}",
            "-v",
            f"{destination}:/approval/selection.json:ro",
        ]
        destination.chmod(
            0o644
        )  # root-private parent, read-only selected-file container mount
        extra = ["execute"]
    for key in env:
        if key != "PATH":
            args += ["-e", key]
    args += [IMAGE, "python", "/helpers/manual_worker.py", *extra]
    with destination.with_suffix(".log").open("ab") as log:
        result = subprocess.run(
            args, env=env, stdout=subprocess.PIPE, stderr=log, check=False
        )
        if result.returncode:
            raise RuntimeError(
                "Manual operation failed; inspect private log and durable stage"
            )
    if command == "inspect":
        value = json.loads(result.stdout)
        with destination.open("x") as output:
            json.dump(value, output, indent=2)
        print(f"Selection prepared: {destination}")
    else:
        print(result.stdout.decode())


if __name__ == "__main__":
    main()
