"""Submit exactly two idempotent synthetic jobs through the private API."""

import json
import sys
import time
from pathlib import Path

import httpx
from bounded_worker import MEETING

private = json.load(sys.stdin)
assert time.time() < int(private["CB_REHEARSAL_EXPIRES_AT"])
client = httpx.Client(
    base_url="http://cbm-bounded-submit:8090",
    timeout=30,
    headers={"Authorization": "Bearer " + private["CB_REHEARSAL_OPERATOR_TOKEN"]},
)


def request(method, path, **kwargs):
    response = client.request(method, path, **kwargs)
    if response.status_code >= 400:
        raise RuntimeError("Submission API HTTP " + str(response.status_code))
    return response.json()


assert request("GET", "/api/v1/jobs")["items"] == [], "Existing jobs require review"
fixture = json.loads(Path("/checks/synthetic-fixture.json").read_text())
sources = {
    kind: request(
        "POST",
        "/api/v1/sources",
        json={"meeting_id": MEETING, "kind": kind, "content": body},
    )["id"]
    for kind, body in fixture.items()
}
identity = {
    "meeting_id": MEETING,
    "started_at": "2026-09-10T00:00:00Z",
    "timezone": "Etc/UTC",
    "local_date": "2026-09-10",
    "provider": "manual",
}
result = {}
for mode in ("weekly", "transcript_backfill"):
    selected = sources if mode == "weekly" else {"transcript": sources["transcript"]}
    body = {"identity": identity, "mode": mode, "sources": selected}
    job = request(
        "POST",
        "/api/v1/jobs",
        json=body,
        headers={"Idempotency-Key": MEETING + "-" + mode},
    )
    result[mode] = job["id"]
print(json.dumps(result))
