"""VM-only isolated restore of the verified coordinated weekly snapshot."""

import hashlib
import json
import os
import secrets
import subprocess
import tempfile
import time
from pathlib import Path

os.umask(0o077)
root = Path("/srv/dev-data/artifacts/cbm-live-development-20260909")
snapshot = root / "weekly-snapshot-20260909T230655Z"
manifest = json.loads((snapshot / "manifest.json").read_text())
for name, expected in manifest.items():
    assert hashlib.sha256((snapshot / name).read_bytes()).hexdigest() == expected
network = "cbm-weekly-restore-check"
container = "cbm-weekly-restore-postgres"
# Fail closed before creating anything if these names already exist.
assert (
    subprocess.run(
        ["docker", "network", "inspect", network],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode
    != 0
)
assert (
    subprocess.run(
        ["docker", "inspect", container],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode
    != 0
)
with tempfile.TemporaryDirectory(
    prefix="cbm-private-restore-", dir="/srv/dev-data/workspaces"
) as scratch:
    state = Path(scratch)
    for kind in ("files", "config", "corpus"):
        (state / kind).mkdir()
        subprocess.run(
            [
                "tar",
                "-xzf",
                str(snapshot / (kind + ".tar.gz")),
                "-C",
                str(state / kind),
            ],
            check=True,
        )
    password = secrets.token_hex(24)
    envfile = state / "postgres.env"
    envfile.write_text(
        "POSTGRES_USER=cbmdev\nPOSTGRES_DB=cbm_dev\nPOSTGRES_PASSWORD="
        + password
        + "\n"
    )
    checkenv = state / "check.env"
    checkenv.write_text(
        "CB_DATABASE_URL=postgresql+psycopg://cbmdev:"
        + password
        + "@"
        + container
        + ":5432/cbm_dev\nCB_STORAGE_ROOT=/state/files\nCB_PIPELINE_CONFIG_DIR=/state/config\nCB_ENABLE_MODEL_CALLS=false\nCB_ENABLE_NETWORK_PUBLICATION=false\n"
    )
    subprocess.run(
        ["docker", "network", "create", "--internal", network],
        stdout=subprocess.DEVNULL,
        check=True,
    )
    try:
        subprocess.run(
            [
                "docker",
                "run",
                "-d",
                "--name",
                container,
                "--network",
                network,
                "--memory",
                "512m",
                "--cpus",
                "1",
                "--env-file",
                str(envfile),
                "--tmpfs",
                "/var/lib/postgresql:rw,size=384m",
                "postgres:18.6",
            ],
            stdout=subprocess.DEVNULL,
            check=True,
        )
        for _ in range(40):
            if (
                subprocess.run(
                    [
                        "docker",
                        "exec",
                        container,
                        "pg_isready",
                        "-U",
                        "cbmdev",
                        "-d",
                        "cbm_dev",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False,
                ).returncode
                == 0
            ):
                break
            time.sleep(1)
        else:
            raise RuntimeError("Restore database did not become ready")
        with (snapshot / "database.dump").open("rb") as stream:
            subprocess.run(
                [
                    "docker",
                    "exec",
                    "-i",
                    container,
                    "pg_restore",
                    "-U",
                    "cbmdev",
                    "-d",
                    "cbm_dev",
                    "--exit-on-error",
                    "--no-owner",
                ],
                stdin=stream,
                stdout=subprocess.DEVNULL,
                check=True,
            )
        cmd = [
            "docker",
            "run",
            "--rm",
            "--network",
            network,
            "--read-only",
            "--tmpfs",
            "/tmp",
            "--cap-drop",
            "ALL",
            "--memory",
            "768m",
            "--cpus",
            "1",
            "--env-file",
            str(checkenv),
        ]
        for kind in ("files", "config", "corpus"):
            cmd += ["-v", str(state / kind) + ":/state/" + kind + ":ro"]
        cmd += [
            "-v",
            str(Path(__file__).with_name("check_restored_weekly.py"))
            + ":/checks/check.py:ro",
            "community-brain:rehearsal",
            "python",
            "/checks/check.py",
        ]
        result = json.loads(subprocess.check_output(cmd))
        result["snapshot"] = snapshot.name
        result["backup_hashes_verified"] = True
        (root / "weekly-restore-result.json").write_text(
            json.dumps(result, sort_keys=True) + "\n"
        )
        print(json.dumps(result, sort_keys=True))
    finally:
        subprocess.run(
            ["docker", "rm", "-f", container],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        subprocess.run(
            ["docker", "network", "rm", network], stdout=subprocess.DEVNULL, check=True
        )
print(
    "Disposable restored copies, database and network removed; original snapshots preserved"
)
