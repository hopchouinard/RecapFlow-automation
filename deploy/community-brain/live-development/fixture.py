"""One idempotent synthetic weekly fixture, submitted through the authorized API."""

import hashlib
import json
import sys
import time

import httpx

if time.time() >= 1789069401:
    raise SystemExit("Development service identity expired")
tokens = json.load(sys.stdin)
client = httpx.Client(
    base_url="http://api:8090",
    headers={"Authorization": "Bearer " + tokens["CB_DEV_OPERATOR_TOKEN"]},
    timeout=20,
)
meeting = "live-development-synthetic-20260909"


def request(method, path, **kwargs):
    response = client.request(method, path, **kwargs)
    if response.status_code >= 400:
        raise SystemExit(
            f"Fixture API failed: {response.status_code}; no automatic retry"
        )
    return response.json()


if sys.argv[1] == "submit":
    sources = {}
    content = {
        "transcript": """00:00:00 - Alex
This is a synthetic development call. Today we discussed how to preserve meeting notes during a service migration. We agreed to keep the original transcript, test restoration from a backup, and check the resulting files before switching any users.
00:01:00 - Alex
The practical lesson is to test recovery while the old service still works. A successful startup alone does not prove that stored notes can be recovered. We should compare file hashes after restoration and record any missing files.
00:02:00 - Alex
Our next action is to run a disposable recovery exercise with made-up meeting content. No production data should enter the test. We will review the recovery result together at the next weekly call.
""",
        "chat": "00:01:20 Alex: Keep the original transcript and verify restored file hashes.\n00:02:10 Alex: Next call: review the disposable recovery exercise.\n",
    }
    for kind, value in content.items():
        sources[kind] = request(
            "POST",
            "/api/v1/sources",
            json={"meeting_id": meeting, "kind": kind, "content": value},
        )["id"]
    body = {
        "identity": {
            "meeting_id": meeting,
            "started_at": "2026-09-09T18:00:00Z",
            "timezone": "Etc/UTC",
            "local_date": "2026-09-09",
            "provider": "manual",
        },
        "mode": "weekly",
        "sources": sources,
    }
    job = request(
        "POST", "/api/v1/jobs", json=body, headers={"Idempotency-Key": meeting}
    )
    print(json.dumps({"job_id": job["id"]}))
elif sys.argv[1] == "inspect":
    job_id = sys.argv[2]
    job = request("GET", "/api/v1/jobs/" + job_id)
    items = request("GET", "/api/v1/jobs/" + job_id + "/artifacts")["items"]
    for item in items:
        response = client.get(item["url"])
        assert response.status_code == 200
        assert hashlib.sha256(response.content).hexdigest() == item["sha256"]
    print(json.dumps({"job": job, "artifacts": items}, sort_keys=True))

elif sys.argv[1] == "reconcile-index":
    job_id = sys.argv[2]
    job = request("GET", "/api/v1/jobs/" + job_id)
    stage = next(s for s in job["stages"] if s["name"] == "indexing")
    assert stage["state"] == "outcome_unknown" and stage["generation"] == 1
    result = request(
        "POST",
        "/api/v1/jobs/" + job_id + "/stages/" + stage["id"] + "/reconcile",
        json={
            "generation": 1,
            "reason": "Development initialization repaired; no indexing requests recorded; operator approves reconciliation",
        },
        headers={
            "Idempotency-Key": meeting + "-index-reconcile-1",
            "Acknowledge-Duplicate-Effect": "true",
        },
    )
    print(json.dumps(result))

elif sys.argv[1] == "retrieval":
    # Independently scoped read-only identity, including legacy X-API-Key transport.
    client.headers["Authorization"] = "Bearer " + tokens["CB_DEV_READER_TOKEN"]
    checks = []
    for question in (
        "How should restored meeting notes be verified?",
        "file hashes backup restoration",
    ):
        result = request(
            "POST", "/retrieval/query", json={"question": question, "top_k": 3}
        )
        assert result["chunks"]
        assert all(
            c["ground_truth"]["session_id"] == "2026-09-09" for c in result["chunks"]
        )
        assert all(
            c["ground_truth"]["full_text"] and c["provenance"] for c in result["chunks"]
        )
        assert any(
            c["score_breakdown"]["bm25_rank"] is not None for c in result["chunks"]
        )
        checks.append(result)
    excluded = request(
        "POST",
        "/retrieval/query",
        json={
            "question": "recovery",
            "filters": {"session_date_range": ["2000-01-01", "2000-01-02"]},
        },
    )
    assert excluded["chunks"] == []
    legacy = client.get(
        "/retrieval/sessions",
        headers={"Authorization": "", "X-API-Key": tokens["CB_DEV_READER_TOKEN"]},
    )
    assert legacy.status_code == 200
    for path in ("/retrieval/ingest", "/retrieval/reindex"):
        assert client.post(path, json={}).status_code == 404
    assert (
        client.post(
            "/retrieval/query",
            json={"question": "fixture"},
            headers={"Authorization": ""},
        ).status_code
        == 401
    )
    print(
        json.dumps(
            {
                "queries": checks,
                "unmatched_date_filter_empty": True,
                "legacy_read_transport": True,
                "mutations_hidden": True,
                "missing_auth_rejected": True,
            },
            sort_keys=True,
        )
    )
