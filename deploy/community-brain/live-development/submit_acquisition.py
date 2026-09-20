"""VM-only submission launcher; provider key never enters this scoped client."""

import json
import os
import subprocess
from pathlib import Path

from compose import read_env

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
selected = json.loads((root / "fathom-selected-metadata.json").read_text())
script = Path(__file__).resolve().with_name("acquisition_client.py")
inputs = {
    "selected": selected,
    "operator_token": read_env("/etc/community-brain-development/test-client.env")[
        "CB_DEV_OPERATOR_TOKEN"
    ],
}
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
        "-v",
        str(script) + ":/checks/acquisition_client.py:ro",
        "community-brain:rehearsal",
        "python",
        "/checks/acquisition_client.py",
    ],
    input=json.dumps(inputs).encode(),
    stdout=subprocess.PIPE,
    check=True,
)
output = json.loads(result.stdout)
(root / "fathom-acquisition-job.json").write_text(
    json.dumps(output, sort_keys=True) + "\n"
)
print(json.dumps(output, sort_keys=True))
