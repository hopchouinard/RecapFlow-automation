"""Private VM Compose context and resolved-volume isolation assertions."""

import json
import os
import subprocess
from pathlib import Path
from urllib.parse import quote

from compose import RUNTIME, read_env


def context():
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
    cmd = ["docker", "compose", "--profile", "bounded", "--env-file", RUNTIME]
    for f in (
        "compose.live-development.yml",
        "compose.bounded-development.yml",
        "compose.weekly-index-development.yml",
    ):
        cmd += ["-f", str(Path(__file__).resolve().parent.parent / f)]
    services = json.loads(
        subprocess.check_output(cmd + ["config", "--format", "json"], env=env)
    )["services"]
    for name in ("bounded-worker", "weekly-api"):
        v = {v["target"]: v["source"] for v in services[name]["volumes"]}
        assert (
            v["/state/corpus"] == "weekly-corpus"
            and v["/state/config"] == "weekly-config"
        )
        assert "CB_FATHOM_API_KEY" not in services[name]["environment"]
    assert not services["weekly-api"].get("ports")
    assert "CB_OPENROUTER_API_KEY" not in services["weekly-api"]["environment"]
    assert (
        next(v for v in services["api"]["volumes"] if v["target"] == "/state/corpus")[
            "source"
        ]
        == "corpus"
    )
    return cmd, env


if __name__ == "__main__":
    context()
    print(
        "PASS: weekly volume isolation; no temporary API host port or provider keys; main API unchanged"
    )
