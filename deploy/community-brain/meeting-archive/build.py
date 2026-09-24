"""Build only verified preserved artifacts, on VM108; no model/database writes."""

import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path

source, destination, sessions_path = map(Path, sys.argv[1:])
manifest_path = source / "manifest.json"
assert (
    hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    == "4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7"
)
manifest = json.loads(manifest_path.read_text())
expected = {f["path"]: f for f in manifest["files"]}
sessions = set(json.loads(sessions_path.read_text()))
assert len(sessions) == 87
meetings = {d: {"date": d, "artifacts": []} for d in sessions}
destination.mkdir(mode=0o700)
(destination / "files").mkdir(mode=0o755)
with tarfile.open(source / "data-only.tar.gz") as tar:
    members = tar.getmembers()
    assert len({m.name for m in members}) == len(members)
    historical_dates = {}
    for m in members:
        if m.name.startswith("n8n/historical/") and m.name.endswith("/meta.json"):
            assert m.isfile()
            raw = tar.extractfile(m).read()
            assert hashlib.sha256(raw).hexdigest() == expected[m.name]["sha256"]
            folder = m.name.split("/")[2]
            date = folder[:10]
            if date not in sessions:
                date = json.loads(raw)["recording_start_time"][:10]
            assert date in sessions
            historical_dates[folder] = date
    for m in members:
        match = re.fullmatch(r"n8n/(output|historical)/([^/]+)/([^/]+)", m.name)
        if not match:
            continue
        origin, folder, name = match.groups()
        if not (name.endswith((".md", ".txt", ".md.legacy"))):
            continue
        assert m.isfile() and re.fullmatch(r"[A-Za-z0-9_.-]+", name)
        date = folder if origin == "output" else historical_dates[folder]
        assert date in sessions
        raw = tar.extractfile(m).read()
        record = expected[m.name]
        assert len(raw) == record["bytes"]
        assert hashlib.sha256(raw).hexdigest() == record["sha256"]
        key = hashlib.sha256(m.name.encode()).hexdigest()
        (destination / "files" / key).write_bytes(raw)
        (destination / "files" / key).chmod(0o644)
        meetings[date]["artifacts"].append(
            {
                "id": key,
                "name": name,
                "origin": origin,
                "preserved_path": m.name,
                "bytes": len(raw),
                "sha256": record["sha256"],
                "url": f"/api/v1/meeting-artifacts/{key}/content",
            }
        )
for meeting in meetings.values():
    assert {a["name"] for a in meeting["artifacts"] if a["origin"] == "output"} >= {
        "prepared-transcript.md",
        "extracted-signal.md",
        "community-post.md",
    }
    meeting["artifacts"].sort(key=lambda a: (a["origin"] != "output", a["name"]))
result = {
    "scope": "community-brain",
    "preservation_manifest_sha256": hashlib.sha256(
        manifest_path.read_bytes()
    ).hexdigest(),
    "meetings": [meetings[d] for d in sorted(meetings, reverse=True)],
}
raw = (json.dumps(result, indent=2) + "\n").encode()
(destination / "manifest.json").write_bytes(raw)
(destination / "manifest.json").chmod(0o644)
print(
    json.dumps(
        {
            "meetings": len(meetings),
            "files": sum(len(m["artifacts"]) for m in meetings.values()),
            "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        }
    )
)
