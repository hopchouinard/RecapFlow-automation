"""Download approved job artifacts with a scoped test identity; save metadata only."""

import json
import os
import subprocess
from pathlib import Path

from compose import read_env

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
job = json.loads((root / "weekly-processing-job.json").read_text())
script = Path(__file__).resolve().with_name("fixture.py")
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
        str(script) + ":/checks/fixture.py:ro",
        "community-brain:rehearsal",
        "python",
        "/checks/fixture.py",
        "inspect",
        job["job_id"],
    ],
    input=json.dumps(
        read_env("/etc/community-brain-development/test-client.env")
    ).encode(),
    stdout=subprocess.PIPE,
    check=True,
)
receipt = json.loads(result.stdout)
assert receipt["job"]["processing"] == "succeeded"
assert {a["name"] for a in receipt["artifacts"]} == {
    "transcript.txt",
    "community-post-compressed.md",
    "2026-09-15-weekly-invite.md",
    "prepared-transcript.md",
    "extracted-signal.md",
    "community-post.md",
}
(root / "weekly-artifact-verification.json").write_text(
    json.dumps(receipt, sort_keys=True) + "\n"
)
print("PASS: six authenticated artifact downloads verified by SHA-256")
