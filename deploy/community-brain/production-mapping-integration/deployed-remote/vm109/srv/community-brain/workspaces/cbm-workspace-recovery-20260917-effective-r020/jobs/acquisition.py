"""Backend-owned Fathom reads and a restricted local Zoom collector."""

import hashlib
import json
import os
import re
import stat
from datetime import datetime, timedelta
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

import httpx


class Fathom:
    def __init__(self, api_key, transport=None):
        self.client = httpx.Client(
            base_url="https://api.fathom.ai/external/v1/",
            headers={"X-Api-Key": api_key},
            timeout=30,
            follow_redirects=False,
            transport=transport,
        )

    def close(self):
        self.client.close()

    @staticmethod
    def call_id(value):
        parsed = urlparse(value)
        if parsed.scheme == "https" and parsed.hostname == "fathom.video":
            match = re.fullmatch(r"/calls/(\d+)/?", parsed.path)
            if match and not parsed.username and not parsed.password:
                return match.group(1)
        return value if re.fullmatch(r"\d+", value) else None

    def fetch(self, identity):
        self.resolved_recording = None
        recording = self.call_id(identity["meeting_id"])
        if recording is None:
            raise ValueError("invalid recording identity")
        start = datetime.fromisoformat(identity["started_at"].replace("Z", "+00:00"))
        cursor = None
        found = None
        seen = set()
        for _ in range(5):
            params = {
                "created_after": (start - timedelta(days=1)).isoformat(),
                "created_before": (start + timedelta(days=1)).isoformat(),
            }
            if cursor:
                params["cursor"] = cursor
            result = self.client.get("meetings", params=params)
            result.raise_for_status()
            body = result.json()
            found = next(
                (
                    m
                    for m in body.get("items", [])
                    if str(m.get("recording_id")) == recording
                    or any(self.call_id(m.get(k, "") or "") == recording for k in ("url", "share_url"))
                ),
                None,
            )
            if found:
                break
            cursor = body.get("next_cursor")
            if not cursor:
                break
            if cursor in seen:
                raise ValueError("fathom pagination cycle")
            seen.add(cursor)
        if not found:
            raise ValueError("recording not found in meeting window")
        recorded = datetime.fromisoformat(
            found["recording_start_time"].replace("Z", "+00:00")
        )
        if start.utcoffset() is None or recorded.utcoffset() is None:
            raise ValueError("timezone-aware meeting timestamp required")
        if abs((recorded - start).total_seconds()) > 600:
            raise ValueError("meeting timestamp mismatch: outside 10-minute window")
        resolved = str(found.get("recording_id", ""))
        if not re.fullmatch(r"\d+", resolved):
            raise ValueError("invalid resolved recording identity")
        self.resolved_recording = resolved
        self.recorded_start = recorded.isoformat()
        result = self.client.get(f"recordings/{resolved}/transcript")
        result.raise_for_status()
        entries = result.json().get("transcript")
        if not isinstance(entries, list) or not entries:
            raise ValueError("transcript unavailable")
        lines = []
        for entry in entries:
            text = entry.get("text")
            if not isinstance(text, str):
                raise ValueError("invalid transcript text")
            speaker = (entry.get("speaker") or {}).get("display_name") or "Unknown"
            timestamp = entry.get("timestamp") or "00:00:00"
            if not re.fullmatch(r"\d{2}:\d{2}:\d{2}", timestamp):
                raise ValueError("invalid timestamp")
            lines.append(f"[{timestamp}] {speaker}: {text}")
        return "\n".join(lines)


class ZoomCollector:
    """No shell, mutation or caller-selected destination. Use upload for Hermes."""

    def __init__(self, root, backend, token, transport=None):
        self.root = Path(root).absolute()
        if self.root.is_symlink():
            raise ValueError("symlink root")
        url = urlparse(backend)
        if (
            url.scheme != "https"
            or url.username
            or url.password
            or url.query
            or url.fragment
        ):
            raise ValueError("collector requires a fixed HTTPS backend")
        self.backend = backend.rstrip("/")
        self.token = token
        self.transport = transport

    def read(self, key):
        parts = PurePosixPath(key).parts
        if (
            not parts
            or key.startswith("/")
            or any(p in (".", "..") for p in key.split("/"))
            or not key.endswith(".txt")
        ):
            raise ValueError("invalid Zoom path")
        fd = os.open(self.root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            for part in parts[:-1]:
                child = os.open(
                    part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd
                )
                os.close(fd)
                fd = child
            leaf = os.open(
                parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd
            )
            with os.fdopen(leaf, "rb") as stream:
                before = os.fstat(stream.fileno())
                if not stat.S_ISREG(before.st_mode) or before.st_size > 10_000_000:
                    raise ValueError("invalid Zoom file")
                content = stream.read(10_000_001)
                after = os.fstat(stream.fileno())
                if len(content) > 10_000_000 or (
                    before.st_size,
                    before.st_mtime_ns,
                ) != (after.st_size, after.st_mtime_ns):
                    raise ValueError("Zoom file changed during read")
                return content.decode("utf-8")
        finally:
            os.close(fd)

    def listing(self):
        files = []
        for directory, dirs, names in os.walk(self.root, followlinks=False):
            dirs[:] = sorted(d for d in dirs if not (Path(directory) / d).is_symlink())
            for name in sorted(names):
                path = Path(directory) / name
                if name.endswith(".txt") and not path.is_symlink() and path.is_file():
                    files.append(
                        {
                            "path": path.relative_to(self.root).as_posix(),
                            "bytes": path.stat().st_size,
                        }
                    )
                    if len(files) > 10000:
                        raise ValueError("Zoom listing limit exceeded")
        return files

    def upload(self, key, meeting_id, *, expected_sha256=None):
        if not re.fullmatch(r"[A-Za-z0-9_.:-]{1,200}", meeting_id):
            raise ValueError("invalid meeting identity")
        content = self.read(key)
        if (
            expected_sha256 is not None
            and hashlib.sha256(content.encode()).hexdigest() != expected_sha256
        ):
            raise ValueError("selected Zoom file hash mismatch")
        with httpx.Client(
            transport=self.transport, timeout=30, follow_redirects=False
        ) as client:
            result = client.post(
                self.backend + "/api/v1/sources",
                headers={"Authorization": "Bearer " + self.token},
                json={"meeting_id": meeting_id, "kind": "chat", "content": content},
            )
            result.raise_for_status()
            return result.json()


def main():
    """Restricted JSON-over-stdin entrypoint; root/destination are operator settings."""
    import sys

    request = json.loads(sys.stdin.read(16384))
    collector = ZoomCollector(
        Path.home() / "Documents/Zoom",
        os.environ["CB_COLLECTOR_BACKEND"],
        os.environ["CB_COLLECTOR_TOKEN"],
    )
    operation = request.get("operation")
    fields = {
        "list": {"operation"},
        "read": {"operation", "path"},
        "upload": {"operation", "path", "meeting_id"},
    }
    if operation not in fields or set(request) != fields[operation]:
        raise ValueError("invalid collector operation")
    if operation == "list":
        result = collector.listing()
    elif operation == "read":
        result = {"content": collector.read(request["path"])}
    else:
        result = collector.upload(request["path"], request["meeting_id"])
    print(json.dumps(result))


if __name__ == "__main__":
    main()
