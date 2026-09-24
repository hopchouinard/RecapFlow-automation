"""VM-only launcher: encode private connection URLs without emitting credentials."""

import os
import shlex
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

RUNTIME = "/etc/community-brain-development/runtime.env"


def read_env(path):
    values = {}
    for line in Path(path).read_text().splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            parts = shlex.split(value, comments=False)
            if len(parts) != 1:
                raise ValueError("Expected one quoted environment value")
            values[key] = parts[0]
    return values


if __name__ == "__main__":
    private = read_env(RUNTIME)
    env = dict(os.environ)
    env["CB_LIVE_DATABASE_URL"] = (
        "postgresql+psycopg://cbmdev:"
        + quote(private["CB_DEV_POSTGRES_PASSWORD"], safe="")
        + "@postgres:5432/cbm_dev"
    )
    env["CB_LIVE_NATS_URL"] = (
        "nats://cbmdev:"
        + quote(private["CB_DEV_NATS_PASSWORD"], safe="")
        + "@nats:4222"
    )
    # Never inherit an accidental enablement from an interactive shell.
    env["CB_ENABLE_MODEL_CALLS"] = "false"
    env["CB_ENABLE_NETWORK_PUBLICATION"] = "false"
    compose = Path(__file__).resolve().parents[1] / "compose.live-development.yml"
    args = sys.argv[1:]
    if not args or args[0] not in {"up", "ps", "stop", "down", "run", "config", "logs"}:
        raise SystemExit("Unsupported development operation")
    if args[0] == "config" and args != ["config", "--quiet"]:
        raise SystemExit(
            "Only config --quiet is permitted; resolved configuration contains secrets"
        )
    raise SystemExit(
        subprocess.call(
            ["docker", "compose", "--env-file", RUNTIME, "-f", str(compose), *args],
            env=env,
        )
    )
