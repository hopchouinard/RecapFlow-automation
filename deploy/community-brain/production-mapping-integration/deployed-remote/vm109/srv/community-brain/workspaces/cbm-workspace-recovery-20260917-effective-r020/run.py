"""VM109-only scoped launcher. Never print resolved credentials or Compose config."""

import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

IMAGE = "community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449"
HERE = Path(__file__).resolve().parent


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


def main():
    os.umask(0o077)
    operation = sys.argv[1]
    assert operation in {"migrate", "dbcheck", "up", "check"}
    env = dict(os.environ)
    private = read_env("migration.env" if operation == "migrate" else "api.env")
    env.update(private)
    if operation == "up":
        identities = json.loads(private["CB_SERVICE_IDENTITIES"])
        assert all(
            set(i["permissions"])
            <= {"jobs:read", "artifacts:read", "retrieval:read", "metrics:read"}
            for i in identities
        )
        env.update(CB_IMAGE=IMAGE, CB_API_BIND="10.1.30.21")
        command = [
            "docker",
            "compose",
            "--env-file",
            "/dev/null",
            "-f",
            str(HERE.parent / "compose.production-staging.yml"),
            "up",
            "-d",
            "--no-build",
            "api",
        ]
    else:
        command = [
            "docker",
            "run",
            "--rm",
            "-i",
            "--read-only",
            "--tmpfs",
            "/tmp",
            "--cap-drop",
            "ALL",
            "--memory",
            "512m",
            "-v",
            "/etc/ssl/certs/ca-certificates.crt:/run/certs/ca-bundle.pem:ro",
        ]
        if operation in {"migrate", "dbcheck"}:
            command += ["-e", "CB_DATABASE_URL"]
        if operation == "check":
            command += ["--network", "host"]
        command += [IMAGE]
        if operation == "migrate":
            command += [
                "alembic",
                "-c",
                "/app/community-brain/alembic.ini",
                "upgrade",
                "head",
            ]
        else:
            command += ["python", "-"]
    payload = None
    if operation == "dbcheck":
        payload = (HERE / "dbcheck.py").read_bytes()
    elif operation == "check":
        probes = read_env("probes.env")
        control = json.loads(
            Path(
                "/srv/community-brain/artifacts/cbm-staging-inputs/control-retrieval-result.json"
            ).read_text()
        )
        payload = (
            "PRIVATE = " + repr(probes) + "\nCONTROL = " + repr(control) + "\n"
        ).encode() + (HERE / "api_checks.py").read_bytes()
    result = subprocess.run(
        command, env=env, input=payload, capture_output=True, check=False
    )
    # Private diagnostic output remains only on the production guest.
    (HERE / (operation + ".log")).write_bytes(result.stdout + result.stderr)
    if result.returncode:
        raise SystemExit(operation + " failed; inspect private diagnostic log locally")
    print(operation + ": passed")
    if operation in {"dbcheck", "check"}:
        print(result.stdout.decode())


if __name__ == "__main__":
    main()
