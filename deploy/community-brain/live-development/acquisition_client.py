"""Submit selected acquisition via API; receives only scoped test token and metadata."""

import json
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import httpx

assert time.time() < 1789069401, "Renew the scoped test identity through Infisical"
inputs = json.load(sys.stdin)
selected = inputs["selected"]
assert selected["selected_call_url"] == "https://fathom.video/calls/812746883"
assert selected["recording_id"] == "181075701"
started = datetime.fromisoformat(selected["started_at"].replace("Z", "+00:00"))
local_date = started.astimezone(ZoneInfo("America/Toronto")).date().isoformat()
assert local_date == "2026-09-08", "Selected recording date mismatch"
with httpx.Client(
    base_url="http://api:8090",
    headers={"Authorization": "Bearer " + inputs["operator_token"]},
    timeout=20,
) as client:
    response = client.post(
        "/api/v1/jobs",
        headers={"Idempotency-Key": "fathom-acquisition-only-812746883-v1"},
        json={
            "identity": {
                "meeting_id": selected["recording_id"],
                "started_at": selected["started_at"],
                "timezone": "America/Toronto",
                "local_date": local_date,
                "provider": "fathom",
            },
            "mode": "weekly",
            "sources": {},
        },
    )
    if response.status_code not in (200, 202):
        raise SystemExit(
            "Acquisition submission failed; status " + str(response.status_code)
        )
    job_id = response.json()["id"]
    response = client.get("/api/v1/jobs/" + job_id)
    if response.status_code != 200:
        raise SystemExit("Acquisition job read failed")
    job = response.json()
    print(
        json.dumps(
            {
                "job_id": job_id,
                "recording_id": job["identity"]["meeting_id"],
                "started_at": job["identity"]["started_at"],
                "processing": job["processing"],
            },
            sort_keys=True,
        )
    )
