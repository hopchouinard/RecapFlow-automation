"""Final VM-side validation and acknowledgment, called only inside all held locks.

The Mac must additionally re-read actual off-host copies and the actual PBS task
under the same supervised lease. These local receipts alone are insufficient.
"""
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from datetime import datetime, timezone
from uuid import UUID

REQUIRED = {"database.dump", "database-capture.json", "database-restore.json",
            "managed-state.tar.gz", "files-capture.json", "files-restore.json",
            "corpus-before.json", "management-controls.tar.gz", "management-controls.json",
            "host-controls.json"}


def sha(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read_private(path):
    path = Path(path)
    if path.is_symlink() or not path.is_file() or path.stat().st_mode & 0o777 != 0o600 or path.stat().st_uid != os.geteuid():
        raise ValueError("unsafe checkpoint evidence file")
    return json.loads(path.read_text())


def validate(root, job, manifest_hash):
    if str(UUID(job)) != job or not re.fullmatch(r"[a-f0-9]{64}", manifest_hash):
        raise ValueError("invalid checkpoint identity")
    root = Path(root)
    directory = root / "artifacts/automatic" / job
    if directory.is_symlink():
        raise ValueError("unsafe checkpoint directory")
    manifest_path = directory / "paired-manifest.json"
    manifest = read_private(manifest_path)
    if sha(manifest_path) != manifest_hash or manifest.get("job_id") != job or set(manifest.get("files", {})) != REQUIRED:
        raise ValueError("paired manifest mismatch")
    for name, info in manifest["files"].items():
        p = directory / name
        if p.is_symlink() or not p.is_file() or p.stat().st_mode & 0o777 != 0o600 or p.stat().st_size != info["bytes"] or sha(p) != info["sha256"]:
            raise ValueError("paired file mismatch")
    db = read_private(directory / "database-capture.json")
    db_restore = read_private(directory / "database-restore.json")
    files = read_private(directory / "files-capture.json")
    files_restore = read_private(directory / "files-restore.json")
    if any(v.get("job_id") != job for v in (db, db_restore, files, files_restore)):
        raise ValueError("restore receipt job mismatch")
    if db["dump"]["sha256"] != manifest["files"]["database.dump"]["sha256"] or files["archive"]["sha256"] != manifest["files"]["managed-state.tar.gz"]["sha256"]:
        raise ValueError("capture does not bind actual pair")
    if db_restore.get("dump_sha256") != db["dump"]["sha256"] or db_restore.get("capture_sha256") != sha(directory / "database-capture.json") or db_restore.get("schema_owners_grants_rows_sequences_match") is not True:
        raise ValueError("database restore evidence mismatch")
    if files_restore.get("archive_sha256") != files["archive"]["sha256"] or files_restore.get("capture_sha256") != sha(directory / "files-capture.json") or files_restore.get("temporary_restore_removed") is not True:
        raise ValueError("file restore evidence mismatch")
    if files_restore.get("corpus") != read_private(directory / "corpus-before.json"):
        raise ValueError("corpus restore evidence mismatch")
    copy = read_private(directory / "offhost-copy.json")
    expected_files = {**manifest["files"], "paired-manifest.json": {"sha256": manifest_hash, "bytes": manifest_path.stat().st_size}}
    if copy.get("job_id") != job or copy.get("files") != expected_files or copy.get("verified") is not True:
        raise ValueError("off-host copy evidence mismatch")
    pbs = read_private(directory / "pbs-receipt.json")
    if pbs.get("job_id") != job or pbs.get("manifest_sha256") != manifest_hash or pbs.get("status") != "OK" or pbs.get("guest_freeze_thaw") is not True or pbs.get("included_disks") != ["scsi0", "scsi1"] or not re.fullmatch(r"pbs:backup/vm/109/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", pbs.get("snapshot", "")):
        raise ValueError("PBS evidence mismatch")
    return directory


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


def acknowledge(root, job, manifest_hash, assert_inodes):
    """Caller holds runner/manual/submission locks continuously through this call."""
    root = Path(root)
    assert_inodes()
    directory = validate(root, job, manifest_hash)
    marker_path = root / "automation/checkpoint-needed.json"
    marker = read_private(marker_path)
    if marker.get("job_id") != job or marker.get("policy") != "new-meeting-full-loop-v1":
        raise ValueError("pending marker identity mismatch")
    target = root / "automation/checkpoints" / (job + ".json")
    if target.exists():
        prior = read_private(target)
        if prior.get("job_id") != job or prior.get("manifest_sha256") != manifest_hash or prior.get("verified") is not True:
            raise ValueError("conflicting prior acknowledgment")
    else:
        assert_inodes()
        atomic(target, {"job_id": job, "verified": True, "manifest_sha256": manifest_hash,
                       "receipt": str(directory / "paired-manifest.json"),
                       "checked_at": datetime.now(timezone.utc).isoformat()})
    # A crash after the durable acknowledgment is recovered by validating it and
    # removing this same marker, never repeating capture/copy/PBS operations.
    assert_inodes()
    if read_private(marker_path) != marker:
        raise ValueError("pending marker changed")
    marker_path.unlink()
    fd = os.open(marker_path.parent, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)
    return {"job_id": job, "manifest_sha256": manifest_hash, "verified": True}
