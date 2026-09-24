"""Capture consistent private development state after the weekly worker exits."""

import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
target = root / (
    "weekly-snapshot-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
)
names = (
    subprocess.check_output(["docker", "ps", "--format", "{{.Names}}"])
    .decode()
    .splitlines()
)
assert all("worker" not in n for n in names), "Stop all development workers first"
api = "cbm-live-development-api-1"
mounts = json.loads(
    subprocess.check_output(["docker", "inspect", "--format", "{{json .Mounts}}", api])
)
paths = {m["Destination"]: m["Source"] for m in mounts}
assert all(p in paths for p in ("/state/files", "/state/config", "/state/corpus"))
target.mkdir(mode=0o700)
subprocess.run(["docker", "stop", api], check=True, stdout=subprocess.DEVNULL)
try:
    with (target / "database.dump").open("wb") as stream:
        subprocess.run(
            [
                "docker",
                "exec",
                "cbm-live-development-postgres-1",
                "pg_dump",
                "-U",
                "cbmdev",
                "-d",
                "cbm_dev",
                "-Fc",
            ],
            stdout=stream,
            check=True,
        )
    for kind in ("files", "config", "corpus"):
        subprocess.run(
            [
                "tar",
                "-czf",
                str(target / (kind + ".tar.gz")),
                "-C",
                paths["/state/" + kind],
                ".",
            ],
            check=True,
        )
finally:
    subprocess.run(["docker", "start", api], check=True, stdout=subprocess.DEVNULL)
manifest = {
    p.name: hashlib.file_digest(p.open("rb"), "sha256").hexdigest()
    for p in target.iterdir()
}
for kind in ("files", "config", "corpus"):
    subprocess.run(
        ["tar", "-tzf", str(target / (kind + ".tar.gz"))],
        stdout=subprocess.DEVNULL,
        check=True,
    )
with (target / "database.dump").open("rb") as stream:
    subprocess.run(
        [
            "docker",
            "exec",
            "-i",
            "cbm-live-development-postgres-1",
            "pg_restore",
            "--list",
        ],
        stdin=stream,
        stdout=subprocess.DEVNULL,
        check=True,
    )
(target / "manifest.json").write_text(json.dumps(manifest, sort_keys=True) + "\n")
print(
    json.dumps(
        {
            "snapshot": str(target),
            "hashes": manifest,
            "archive_read_checks": True,
            "full_restore_tested": False,
        },
        sort_keys=True,
    )
)
