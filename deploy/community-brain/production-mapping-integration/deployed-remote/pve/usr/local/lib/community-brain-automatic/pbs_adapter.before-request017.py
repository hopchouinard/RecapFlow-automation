"""PVE1-side durable, non-pruning VM109 PBS operation; no blind repeat on ambiguity."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from uuid import UUID

BASE = Path("/var/lib/community-brain-automatic-pbs")


def api(*args):
    result = subprocess.run(["pvesh", *args, "--output-format", "json"], capture_output=True, timeout=90)
    if result.returncode:
        raise RuntimeError("PBS management call failed; reconcile durable intent")
    return json.loads(result.stdout)


def atomic(path, value):
    fd, temporary = tempfile.mkstemp(dir=path.parent, prefix="." + path.name + ".")
    with os.fdopen(fd, "w") as stream:
        os.fchmod(stream.fileno(), 0o600)
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    fd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def start(job, manifest_hash):
    directory = BASE / job
    directory.mkdir(mode=0o700, parents=True, exist_ok=False)
    config = api("get", "/nodes/pve1/qemu/109/config")
    if any("backup=0" in config.get(disk, "") or not config.get(disk) for disk in ("scsi0", "scsi1")) or "enabled=1" not in str(config.get("agent", "")):
        raise ValueError("required included disks or guest agent missing")
    before = api("get", "/nodes/pve1/storage/pbs/content", "--vmid", "109")
    record = {"job_id": job, "manifest_sha256": manifest_hash, "state": "intent",
              "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "existing_snapshots": sorted(item["volid"] for item in before),
              "notes": "CBM automatic " + job + " " + manifest_hash}
    atomic(directory / "operation.json", record)
    # If the transport dies after this request but before UPID persistence, the
    # intent is deliberately unresolved. Never submit a second backup blindly.
    upid = api("create", "/nodes/pve1/vzdump", "--vmid", "109", "--storage", "pbs",
               "--mode", "snapshot", "--remove", "0", "--notes-template", record["notes"])
    if not isinstance(upid, str) or not upid.startswith("UPID:pve1:"):
        raise ValueError("unexpected PBS task identity")
    record.update(state="submitted", upid=upid)
    atomic(directory / "operation.json", record)
    return {"job_id": job, "upid": upid, "state": "submitted"}


def inspect(job, manifest_hash):
    directory = BASE / job
    record = json.loads((directory / "operation.json").read_text())
    if record["job_id"] != job or record["manifest_sha256"] != manifest_hash or not record.get("upid"):
        raise ValueError("PBS identity or uncertain submission requires reconciliation")
    upid = record["upid"]
    status = api("get", "/nodes/pve1/tasks/" + upid + "/status")
    if status["status"] != "stopped":
        return {"job_id": job, "state": "running", "upid": upid}
    if status.get("exitstatus") != "OK":
        raise ValueError("PBS task failed")
    lines = api("get", "/nodes/pve1/tasks/" + upid + "/log", "--limit", "10000")
    log = "\n".join(line["t"] for line in lines)
    snapshots = set(re.findall(r"vm/109/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", log))
    if len(snapshots) != 1:
        raise ValueError("PBS archive identity ambiguous")
    snapshot = "pbs:backup/" + snapshots.pop()
    contents = api("get", "/nodes/pve1/storage/pbs/content", "--vmid", "109")
    exact = [item for item in contents if item["volid"] == snapshot]
    if len(exact) != 1 or exact[0].get("notes") != record["notes"]:
        raise ValueError("PBS snapshot metadata does not bind checkpoint")
    if not set(record["existing_snapshots"]).issubset({item["volid"] for item in contents}):
        raise ValueError("prior PBS recovery points missing")
    if any("include disk '" + disk + "'" not in log for disk in ("scsi0", "scsi1")) or "fs-freeze" not in log or "fs-thaw" not in log:
        raise ValueError("PBS included disks or freeze/thaw not proven")
    receipt = {"job_id": job, "manifest_sha256": manifest_hash, "status": "OK",
               "upid": upid, "snapshot": snapshot, "guest_freeze_thaw": True,
               "included_disks": ["scsi0", "scsi1"], "existing_backups_pruned": False,
               "log_sha256": hashlib.sha256(log.encode()).hexdigest(),
               "consistency_limit": "Logical pair verified separately; paired files present on included state disk before snapshot. No full guest restore or PITR claim."}
    if not (directory / "receipt.json").exists():
        atomic(directory / "receipt.json", receipt)
    elif json.loads((directory / "receipt.json").read_text()) != receipt:
        raise ValueError("PBS receipt changed")
    return receipt


if __name__ == "__main__":
    os.umask(0o077)
    try:
        operation, job, manifest_hash = sys.argv[1:4]
        if str(UUID(job)) != job or not re.fullmatch(r"[a-f0-9]{64}", manifest_hash):
            raise ValueError("invalid checkpoint identity")
        if operation not in {"start", "inspect"}:
            raise ValueError("unknown PBS operation")
        print(json.dumps(start(job, manifest_hash) if operation == "start" else inspect(job, manifest_hash)))
    except Exception:
        print("PBS adapter failed; reconcile private operation journal", file=sys.stderr)
        raise SystemExit(1) from None
