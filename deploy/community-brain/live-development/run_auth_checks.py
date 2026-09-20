"""Deliver raw test tokens only over stdin to the short-lived scoped test process."""

import json
import subprocess
from pathlib import Path

from compose import read_env

checks = Path(__file__).resolve().with_name("check_auth.py")
result = subprocess.run(
    [
        "docker",
        "run",
        "--rm",
        "-i",
        "--network",
        "cbm-live-development_default",
        "--read-only",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges:true",
        "--memory",
        "512m",
        "--cpus",
        "1",
        "-v",
        str(checks) + ":/checks/check_auth.py:ro",
        "community-brain:rehearsal",
        "python",
        "/checks/check_auth.py",
    ],
    check=False,
    input=json.dumps(
        read_env("/etc/community-brain-development/test-client.env")
    ).encode(),
)
raise SystemExit(result.returncode)
