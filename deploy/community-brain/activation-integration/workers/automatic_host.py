"""Cron tick: one automatic stage at a time, selected through durable job state."""

import fcntl
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from run import HERE, IMAGE, read_env

from run import contract
ROOT = Path(contract()["root"])
STATE = ROOT / "automation"
PACKAGES = (
    "/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs"
)


def atomic(path, value):
    raw = (json.dumps(value, indent=2) + "\n").encode()
    temporary = path.with_suffix(".tmp")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def record_attention(error=None):
    # Preserve the first failure; cron heartbeats must not erase onset evidence.
    path = STATE / "attention.json"
    if path.exists():
        return
    value = {
        "reason": "automatic_execution_requires_review",
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }
    if error is not None:
        value["error_class"] = type(error).__name__
    atomic(path, value)


def publish_checkpoint_status():
    """Export only backup acknowledgement fields for the unprivileged API."""
    import re
    from uuid import UUID

    public = ROOT / "automation-public"
    public.mkdir(mode=0o755, exist_ok=True)
    public.chmod(0o755)
    checkpoints = {}
    for path in (STATE / "checkpoints").glob("*.json"):
        try:
            job_id = str(UUID(path.stem))
            value = json.loads(path.read_text())
            valid = (
                isinstance(value, dict)
                and value.get("job_id") == job_id
                and value.get("verified") is True
                and re.fullmatch(r"[a-f0-9]{64}", value.get("manifest_sha256", ""))
            )
            checkpoints[job_id] = "verified" if valid else "requires_review"
        except (ValueError, OSError, TypeError):
            continue
    atomic(
        public / "checkpoints.json",
        {
            "checkpoints": checkpoints,
            "management_attention": (STATE / "management-attention.json").exists(),
        },
    )
    (public / "checkpoints.json").chmod(0o644)


def scan(*operation):
    from run import worker_environment,container_args,invoke
    return json.loads(invoke(container_args(),worker_environment(),['python','-B','/packet/workers/scan.py',*operation],timeout=90))


def tick():
    from runtime_contract import load,held
    if held(load(os.environ['CBM_PACKET_SHA256'])):return 'paused'
    if (STATE / "attention.json").exists():
        return "attention_required"
    if (STATE / "paused").exists():
        return "paused"
    if (STATE / "checkpoint-needed.json").exists():
        return "awaiting_checkpoint"
    # An orphaned oneshot continues independently after its launcher disconnects.
    if subprocess.check_output(
        ["docker", "ps", "-q", "--filter", "label=cbm.r029.automatic-stage=true"]
    ).strip():
        return "worker_running"
    # Avoid racing a still-active manual worker; its lock is held inside container.
    with (ROOT / "files" / ".manual-worker.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return "worker_running"
    for _ in range(3):
        state = scan("next")
        if state.get("attention"):
            return (
                "needs_input"
                if state.get("known_failure_only")
                else "attention_required"
            )
        for job in state["completed"]:
            receipt = STATE / "checkpoints" / f"{job}.json"
            valid = False
            if receipt.exists():
                value = json.loads(receipt.read_text())
                import re

                valid = (
                    value.get("job_id") == job
                    and value.get("verified") is True
                    and bool(
                        re.fullmatch(r"[a-f0-9]{64}", value.get("manifest_sha256", ""))
                    )
                )
            if not valid:
                atomic(
                    STATE / "checkpoint-needed.json",
                    {
                        "job_id": job,
                        "requested_at": datetime.now(timezone.utc).isoformat(),
                        "policy": "new-meeting-full-loop-v1",
                        "requires": "paired DB/files/corpus/config/archive/runtime checkpoint",
                    },
                )
                return "awaiting_checkpoint"
        item = state["next"]
        if item is None:
            return "idle"
        selection = (
            ROOT
            / "manual-approvals"
            / f"{item['job_id']}-{item['stage']}-{item['generation']}.json"
        )
        if selection.with_suffix(".started").exists():
            scan("stop", item["stage_id"])
            return "attention_required"
        env = {**os.environ, "CB_AUTOMATIC_ONLY": "true"}
        with (STATE / "execution.log").open("ab") as log:
            if not selection.exists():
                result = subprocess.run(
                    [
                        sys.executable,
                        "-B",
                        str(HERE / "workers/manual_host.py"),
                        "inspect",
                        item["job_id"],
                        item["stage"],
                        str(item["generation"]),
                    ],
                    env=env,
                    stdout=log,
                    stderr=log,
                    check=False,
                )
                if result.returncode:
                    scan("stop", item["stage_id"])
                    return "attention_required"
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    str(HERE / "workers/manual_host.py"),
                    "execute",
                    str(selection),
                ],
                env=env,
                stdout=log,
                stderr=log,
                check=False,
            )
            if result.returncode:
                scan("stop", item["stage_id"])
                outcome = scan("next")
                return (
                    "needs_input"
                    if outcome.get("known_failure_only")
                    else "attention_required"
                )
    # Next tick records/checks the durable completion before selecting another job.
    return "stage_completed"


if __name__ == "__main__":
    os.umask(0o077)
    assert os.geteuid() == 0 and (ROOT / "files").is_dir()
    STATE.mkdir(mode=0o700, exist_ok=True)
    (STATE / "checkpoints").mkdir(mode=0o700, exist_ok=True)
    with (STATE / "runner.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            sys.exit(0)
        try:
            publish_checkpoint_status()
            status = tick()
        except Exception as error:  # noqa: BLE001 -- only the class is recorded
            record_attention(error)
            status = "attention_required"
        if status == "attention_required":
            record_attention()
        atomic(
            STATE / "status.json",
            {"state": status, "checked_at": datetime.now(timezone.utc).isoformat()},
        )
        print(json.dumps({"state": status}))
        if status == "attention_required":
            sys.exit(1)
