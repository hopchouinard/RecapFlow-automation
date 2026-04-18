"""Internal I/O helpers for the ingestion package.

Centralizes atomic YAML write semantics so SpeakerRegistry, EntityRegistry,
and any future on-disk state can share one tested implementation.
"""

from __future__ import annotations

import os
import threading
import uuid
from pathlib import Path

import yaml

_LOCKS_META = threading.Lock()
_FLUSH_LOCKS: dict[Path, threading.Lock] = {}


def _get_flush_lock(path: Path) -> threading.Lock:
    """Return the per-path lock, creating it if needed (thread-safe)."""
    resolved = path.resolve()
    with _LOCKS_META:
        lock = _FLUSH_LOCKS.get(resolved)
        if lock is None:
            lock = threading.Lock()
            _FLUSH_LOCKS[resolved] = lock
        return lock


def atomic_write_yaml(path: Path, payload: dict) -> None:
    """Atomically write a YAML payload to disk.

    Crash-safe across the temp-file write, the rename, AND the parent directory
    update (the parent dir is fsynced after replace so the rename survives a
    power loss). Concurrent calls to this function for the SAME path are
    serialized via a per-path lock; concurrent calls for different paths run
    independently.

    The temp file uses a UUID suffix so concurrent writes (even with the lock
    bypassed by future code) cannot collide.
    """
    lock = _get_flush_lock(path)
    with lock:
        tmp = path.with_suffix(f"{path.suffix}.tmp.{uuid.uuid4().hex}")
        try:
            tmp.write_text(
                yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
            # fsync the temp file's contents
            fd = os.open(str(tmp), os.O_RDONLY)
            try:
                os.fsync(fd)
            finally:
                os.close(fd)
            os.replace(tmp, path)
            # fsync the parent directory so the rename survives a crash
            dir_fd = os.open(str(path.parent), os.O_RDONLY)
            try:
                os.fsync(dir_fd)
            finally:
                os.close(dir_fd)
        except Exception:
            # Best-effort cleanup of the temp file on any failure
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
            raise
