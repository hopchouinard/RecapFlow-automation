"""Read public API artifacts using independent read identity; never emit content."""

import hashlib
import json
import sys
import time

import httpx

private = json.load(sys.stdin)
assert time.time() < int(private["CB_PROBE_EXPIRES_AT"])
client = httpx.Client(
    base_url="http://10.1.30.21:8090",
    headers={"Authorization": "Bearer " + private["CB_READ_PROBE_TOKEN"]},
    timeout=30,
)
results = []
for mode, job_id in private["jobs"].items():
    response = client.get("/api/v1/jobs/" + job_id)
    response.raise_for_status()
    job = response.json()
    response = client.get("/api/v1/jobs/" + job_id + "/artifacts")
    response.raise_for_status()
    items = response.json()["items"]
    for item in items:
        response = client.get(item["url"])
        response.raise_for_status()
        assert hashlib.sha256(response.content).hexdigest() == item["sha256"]
    results.append(
        {
            "job_id": job_id,
            "mode": mode,
            "processing": job["processing"],
            "artifacts": job["artifacts"],
            "indexing": job["indexing"],
            "stages": [{"name": s["name"], "state": s["state"]} for s in job["stages"]],
            "artifact_files": [
                {"name": a["name"], "sha256": a["sha256"]} for a in items
            ],
        }
    )
print(json.dumps(results))
