"""Temporary authenticated retrieval against only the weekly corpus."""

import os
import subprocess
import sys
from pathlib import Path

from weekly_index_compose import context

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
cmd, env = context()
try:
    subprocess.run(
        cmd
        + ["up", "-d", "--no-deps", "--wait", "--wait-timeout", "120", "weekly-api"],
        env=env,
        check=True,
    )
    with (root / "weekly-indexing-result.json").open("wb") as out:
        subprocess.run(
            [
                "docker",
                "exec",
                "cbm-live-development-weekly-api-1",
                "python",
                "/checks/weekly_indexing_result.py",
            ],
            stdout=out,
            check=True,
        )
    subprocess.run(
        [sys.executable, str(Path(__file__).with_name("verify_weekly_retrieval.py"))],
        check=True,
    )
finally:
    subprocess.run(cmd + ["rm", "-s", "-f", "weekly-api"], env=env, check=True)
