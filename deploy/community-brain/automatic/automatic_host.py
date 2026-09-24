"""Cron tick: one automatic stage at a time, selected through durable job state."""

import fcntl
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from run import HERE, IMAGE, read_env

ROOT = Path("/srv/community-brain")
STATE = ROOT / "automation"
PACKAGES = (
    "/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs"
)


class ScanFailure(RuntimeError):
    """Safe diagnostic metadata, never command arguments or provider output."""

    def __init__(self, code, result=None):
        super().__init__(code)
        self.diagnostic = {"code": code}
        if result is not None:
            self.diagnostic.update(
                returncode=result.returncode,
                stdout_sha256=hashlib.sha256(result.stdout or b"").hexdigest(),
                stderr_sha256=hashlib.sha256(result.stderr or b"").hexdigest(),
            )
            try:
                detail = json.loads(result.stderr)
                # Only accept a scanner-owned fixed diagnostic code. Hash all
                # other Docker/Python output without exporting its contents.
                if detail.get("code") == "automatic_scan_failed":
                    import re

                    name = detail.get("error_class", "")
                    if re.fullmatch(r"[A-Za-z_][A-Za-z_0-9]{0,79}", name):
                        self.diagnostic["scanner_error_class"] = name
            except (ValueError, TypeError, AttributeError):
                pass


def atomic(path, value):
    raw = (json.dumps(value, indent=2) + "\n").encode()
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix="." + path.name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
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
        if isinstance(error, ScanFailure):
            value["diagnostic"] = error.diagnostic
    atomic(path, value)


def publish_checkpoint_status(runner_state="checking"):
    """Export backup state and bounded readiness, never private diagnostics."""
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

    def read_object(path):
        try:
            value = json.loads(path.read_text())
            return value if isinstance(value, dict) else {}
        except (ValueError, OSError):
            return {}

    boot = read_object(STATE / "boot-state.json")
    management = read_object(ROOT / "management-status/maintenance.json")
    renewal = management.get("renewal")
    renewal = renewal if isinstance(renewal, dict) else {}
    identities = management.get("service_identities")
    identities = identities if isinstance(identities, list) else []
    now = datetime.now(timezone.utc)
    expired = not identities or any(
        not isinstance(i, dict)
        or type(i.get("expires_at")) not in (int, float)
        or not (now.timestamp() < i["expires_at"] < now.timestamp() + 8 * 86400)
        for i in identities
    )
    atomic(
        public / "checkpoints.json",
        {
            "checkpoints": checkpoints,
            "management_attention": (STATE / "management-attention.json").exists(),
            "processing": {
                "checked_at": now.isoformat(),
                "runner": runner_state,
                "paused": (STATE / "paused").exists(),
                "attention": (STATE / "attention.json").exists(),
                "boot_reconciled": boot.get("reconciled") is True,
                "checkpoint_pending": (STATE / "checkpoint-needed.json").exists(),
                "management_attention": (STATE / "management-attention.json").exists(),
                "credentials_expired": expired,
                "renewal": renewal.get("state")
                if renewal.get("state") in {"completed", "not_due", "failed"}
                else "unknown",
                "management_checked_at": management.get("checked_at")
                if isinstance(management.get("checked_at"), str)
                and len(management["checked_at"]) < 40
                else None,
            },
        },
    )
    (public / "checkpoints.json").chmod(0o644)


def publish_busy_status():
    """A locked cron tick refreshes read-only visibility during long calls."""
    try:
        running = subprocess.check_output(
            ["docker", "ps", "-q", "--filter", "label=cbm.automatic-stage=true"],
            stderr=subprocess.DEVNULL,
            timeout=10,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        running = b""
    publish_checkpoint_status("worker_running" if running else "checking")


def scan(*operation):
    env = {
        "PATH": os.defpath,
        "CB_DATABASE_URL": read_env("api.env")["CB_DATABASE_URL"],
        "CB_STORAGE_ROOT": "/state/files",
        "CB_PIPELINE_CONFIG_DIR": "/state/config",
        "CB_CORPUS_ROOT": "/state/corpus",
        "SSL_CERT_FILE": "/run/certs/ca-bundle.pem",
    }
    args = [
        "docker",
        "run",
        "--rm",
        "--label",
        "cbm.automatic-stage=true",
        "--read-only",
        "--tmpfs",
        "/tmp",
        "--user",
        "10001:10001",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--memory",
        "512m",
        "--cpus",
        "1",
        "-v",
        str(HERE) + ":/helpers:ro",
        "-v",
        str(ROOT / "files") + ":/state/files:rw",
        "-v",
        str(ROOT / "config") + ":/state/config:ro",
        "-v",
        str(ROOT / "corpus") + ":/state/corpus:ro",
        "-v",
        "/etc/ssl/certs/ca-certificates.crt:/run/certs/ca-bundle.pem:ro",
    ]
    for name in ("automatic", "store", "runtime", "worker"):
        args += ["-v", str(HERE / "jobs" / f"{name}.py") + f":{PACKAGES}/{name}.py:ro"]
    for key in env:
        if key != "PATH":
            args += ["-e", key]
    args += [IMAGE, "python", "/helpers/scan.py", *operation]
    try:
        result = subprocess.run(
            args, env=env, capture_output=True, timeout=90, check=False
        )
    except subprocess.TimeoutExpired:
        raise ScanFailure("automatic_scan_timeout") from None
    if result.returncode:
        raise ScanFailure("automatic_scan_exit", result)
    try:
        value = json.loads(result.stdout)
        if not isinstance(value, dict):
            raise ValueError()
        return value
    except (ValueError, TypeError):
        raise ScanFailure("automatic_scan_invalid_response", result) from None


def tick():
    if (STATE / "attention.json").exists():
        return "attention_required"
    if (STATE / "paused").exists():
        return "paused"
    if (STATE / "checkpoint-needed.json").exists():
        return "awaiting_checkpoint"
    # An orphaned oneshot continues independently after its launcher disconnects.
    if subprocess.check_output(
        ["docker", "ps", "-q", "--filter", "label=cbm.automatic-stage=true"]
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
                        str(HERE / "manual_host.py"),
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
                    str(HERE / "manual_host.py"),
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
            publish_busy_status()
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
        publish_checkpoint_status(status)
        print(json.dumps({"state": status}))
        if status == "attention_required":
            sys.exit(1)
