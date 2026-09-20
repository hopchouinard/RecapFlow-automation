"""Validate only: do not start a worker before Patrick selects a recording."""

import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

from compose import RUNTIME, read_env

private = read_env(RUNTIME)
env = dict(os.environ)
env["CB_LIVE_DATABASE_URL"] = (
    "postgresql+psycopg://cbmdev:"
    + quote(private["CB_DEV_POSTGRES_PASSWORD"], safe="")
    + "@postgres:5432/cbm_dev"
)
env["CB_LIVE_NATS_URL"] = (
    "nats://cbmdev:" + quote(private["CB_DEV_NATS_PASSWORD"], safe="") + "@nats:4222"
)
root = Path(__file__).resolve().parents[1]
command = [
    "docker",
    "compose",
    "--env-file",
    RUNTIME,
    "--env-file",
    "/etc/community-brain-development/fathom.env",
    "-f",
    str(root / "compose.live-development.yml"),
    "-f",
    str(root / "compose.acquisition-development.yml"),
]
subprocess.run(command + ["config", "--quiet"], env=env, check=True)
if len(sys.argv) == 1:
    print("Acquisition-only configuration valid; no worker started")
elif sys.argv[1] == "--lookup" and len(sys.argv) == 5:
    subprocess.run(
        command + ["run", "--rm", "--no-deps", "acquisition-worker", *sys.argv[1:]],
        env=env,
        check=True,
    )
elif sys.argv[1] == "--acquire" and len(sys.argv) == 5:
    subprocess.run(
        command + ["run", "--rm", "--no-deps", "acquisition-worker", *sys.argv[2:]],
        env=env,
        check=True,
    )
else:
    raise SystemExit(
        "Use no arguments to validate, --lookup ID AFTER BEFORE, or --acquire JOB_ID RECORDING_ID STARTED_AT"
    )
