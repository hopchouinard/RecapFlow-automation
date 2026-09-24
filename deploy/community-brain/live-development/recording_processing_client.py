import json
import sys
import time

import httpx

assert time.time() < 1789069401, "Development identity expired"
token = json.load(sys.stdin)["token"]
parent = "33cc7538-e326-4f74-93ef-f2fcbb5c1624"
with httpx.Client(
    base_url="http://api:8090", headers={"Authorization": "Bearer " + token}, timeout=20
) as client:
    response = client.get("/api/v1/jobs/" + parent)
    response.raise_for_status()
    old = response.json()
    assert old["identity"]["meeting_id"] == "181075701"
    assert old["sources"]["transcript"] == "27969d75-10a9-4a46-8cf4-b63d1d7035d9"
    response = client.post(
        "/api/v1/jobs/" + parent + "/reruns",
        headers={"Idempotency-Key": "approved-backfill-812746883-20260909-v1"},
        json={
            "identity": old["identity"],
            "mode": "transcript_backfill",
            "sources": old["sources"],
            "reason": "Patrick explicitly approved transcript-only processing through OpenRouter within the existing US$5 total development cap",
        },
    )
    response.raise_for_status()
    print(
        json.dumps(
            {
                "job_id": response.json()["id"],
                "parent_id": parent,
                "mode": "transcript_backfill",
                "recording_id": "181075701",
            }
        )
    )
