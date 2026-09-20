"""Download approved job artifacts with a scoped test identity; save metadata only."""

import json
import os
import subprocess
from pathlib import Path

from compose import read_env

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
script = Path(__file__).resolve().with_name("recording_retrieval.py")
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
        str(script) + ":/checks/recording_retrieval.py:ro",
        "community-brain:rehearsal",
        "python",
        "/checks/recording_retrieval.py",
    ],
    input=json.dumps(
        read_env("/etc/community-brain-development/test-client.env")
    ).encode(),
    stdout=subprocess.PIPE,
    check=True,
)
receipt = json.loads(result.stdout)
(root / "recording-retrieval-result.json").write_text(
    json.dumps(receipt, sort_keys=True) + "\n"
)
print(json.dumps(receipt, sort_keys=True))
