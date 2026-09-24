"""Selected manual API submission/read checks, run inside the API network context."""

import hashlib
import json
import sys
import time
from uuid import UUID

import httpx

IDENTITY = {
    "meeting_id": "181075701",
    "started_at": "2026-09-08T21:54:33Z",
    "timezone": "America/Toronto",
    "local_date": "2026-09-08",
    "provider": "fathom",
}
KEY = "manual-production-181075701-weekly-20260910-v1"


def main():
    private = json.load(sys.stdin)
    assert time.time() < int(private["expires_at"])
    with httpx.Client(
        base_url="http://127.0.0.1:8090",
        timeout=30,
        headers={"Authorization": "Bearer " + private["token"]},
    ) as client:

        def request(method, path, **kwargs):
            response = client.request(method, path, **kwargs)
            if response.status_code >= 400:
                raise RuntimeError("Selected API HTTP " + str(response.status_code))
            return response

        if private["operation"] == "submit":
            jobs = request("GET", "/api/v1/jobs").json()["items"]
            assert len(jobs) == 2, (
                "Unexpected job baseline; reconcile before submitting"
            )
            source_id = str(UUID(private["chat_source_id"]))
            response = request(
                "POST",
                "/api/v1/jobs",
                json={
                    "identity": IDENTITY,
                    "mode": "weekly",
                    "sources": {"chat": source_id},
                },
                headers={"Idempotency-Key": KEY},
            )
            print(
                json.dumps(
                    {
                        "job_id": response.json()["id"],
                        "identity": IDENTITY,
                        "mode": "weekly",
                        "chat_source_id": source_id,
                        "idempotency_key": KEY,
                    }
                )
            )
        elif private["operation"] == "verify":
            job_id = str(UUID(private["job_id"]))
            job = request("GET", f"/api/v1/jobs/{job_id}").json()
            artifacts = request("GET", f"/api/v1/jobs/{job_id}/artifacts").json()[
                "items"
            ]
            for artifact in artifacts:
                body = request("GET", artifact["url"]).content
                assert (
                    hashlib.sha256(body).hexdigest() == artifact["sha256"]
                    and len(body) == artifact["bytes"]
                )
            print(
                json.dumps(
                    {
                        "job_id": job_id,
                        "job": job,
                        "artifacts": artifacts,
                        "download_hashes_verified": True,
                    }
                )
            )
        else:
            raise ValueError("unknown selected API operation")


if __name__ == "__main__":
    main()
