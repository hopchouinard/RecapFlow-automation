"""Internal I/O helpers for the ingestion package.

Centralizes atomic YAML write semantics so SpeakerRegistry, EntityRegistry,
and any future on-disk state can share one tested implementation.
"""

from __future__ import annotations

import collections
import os
import threading
import uuid
from pathlib import Path

import yaml

_LOCKS_META = threading.Lock()
_FLUSH_LOCKS: collections.OrderedDict[Path, threading.Lock] = collections.OrderedDict()
_MAX_FLUSH_LOCKS = 256


def _get_flush_lock(path: Path) -> threading.Lock:
    """Return the per-path lock, creating it if needed (thread-safe).

    Uses an LRU-capped OrderedDict (max 256 entries) so the dict stays
    bounded even if callers pass many distinct paths over a long run.
    Active paths are moved to the end on each access; truly stale entries
    are evicted from the front when the cap is exceeded.
    """
    resolved = path.resolve()
    with _LOCKS_META:
        if resolved in _FLUSH_LOCKS:
            _FLUSH_LOCKS.move_to_end(resolved)
            return _FLUSH_LOCKS[resolved]
        lock = threading.Lock()
        _FLUSH_LOCKS[resolved] = lock
        while len(_FLUSH_LOCKS) > _MAX_FLUSH_LOCKS:
            _FLUSH_LOCKS.popitem(last=False)
        return lock


def _atomic_write_locked(path: Path, payload: dict) -> None:
    """Write payload atomically. Caller must hold the per-path lock."""
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
        try:
            dir_fd = os.open(str(path.parent), os.O_RDONLY)
        except OSError:
            return
        try:
            os.fsync(dir_fd)
        except OSError:
            pass
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


def atomic_write_yaml(path: Path, payload: dict) -> None:
    """Atomically write a YAML payload to disk.

    Crash-safe across the temp-file write, the rename, AND the parent directory
    update (the parent dir is fsynced after replace so the rename survives a
    power loss). Concurrent calls to this function for the SAME path are
    serialized via a per-path lock; concurrent calls for different paths run
    independently.

    Does NOT merge with on-disk content. For concurrent-safe pending queue
    updates, use merge_and_atomic_write_yaml with merge_list_keys=('pending',).
    """
    lock = _get_flush_lock(path)
    with lock:
        _atomic_write_locked(path, payload)


def merge_and_atomic_write_yaml(
    path: Path,
    payload: dict,
    merge_list_keys: tuple[str, ...] = (),
) -> None:
    """Atomically write a YAML payload, merging specified list fields with
    whatever is currently on disk under the same lock.

    For each key in merge_list_keys, the on-disk list is loaded and union'd
    with payload[key] (order: on-disk entries first, then any new ones from
    payload not already present). This closes the TOCTOU window where two
    concurrent processes each load -> append -> write and lose one update.

    The per-path lock serializes the read-merge-write cycle so no update can
    be lost between concurrent flushes.
    """
    lock = _get_flush_lock(path)
    with lock:
        if path.exists() and merge_list_keys:
            try:
                with path.open(encoding="utf-8") as fh:
                    existing = yaml.safe_load(fh) or {}
            except (yaml.YAMLError, OSError):
                existing = {}
            for key in merge_list_keys:
                on_disk = existing.get(key) or []
                in_memory = payload.get(key) or []
                if not isinstance(on_disk, list):
                    on_disk = []
                seen: set = set()
                merged: list = []
                for item in list(on_disk) + list(in_memory):
                    if item not in seen:
                        merged.append(item)
                        seen.add(item)
                payload[key] = merged
        _atomic_write_locked(path, payload)
