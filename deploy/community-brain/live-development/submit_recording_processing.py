"""Create an explicitly approved child job without fetching or printing its source."""

import json
import os
import subprocess
from pathlib import Path

from compose import read_env

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
script = Path(__file__).resolve().with_name("recording_processing_client.py")
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
        "--memory",
        "512m",
        "-v",
        str(script) + ":/checks/client.py:ro",
        "community-brain:rehearsal",
        "python",
        "/checks/client.py",
    ],
    input=json.dumps(
        {
            "token": read_env("/etc/community-brain-development/test-client.env")[
                "CB_DEV_OPERATOR_TOKEN"
            ]
        }
    ).encode(),
    stdout=subprocess.PIPE,
    check=True,
)
receipt = json.loads(result.stdout)
(root / "recording-processing-job.json").write_text(json.dumps(receipt) + "\n")
print(json.dumps(receipt))
