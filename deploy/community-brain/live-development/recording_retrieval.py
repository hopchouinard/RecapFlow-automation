"""Authenticated real-recording retrieval checks; emit metadata only."""

import json
import sys
import time

import httpx

assert time.time() < 1789069401, "Development service identity expired"
tokens = json.load(sys.stdin)
client = httpx.Client(
    base_url="http://api:8090",
    timeout=60,
    headers={"Authorization": "Bearer " + tokens["CB_DEV_READER_TOKEN"]},
)
checks = []
for question in ("AI Developer Accelerator coaching call", "tools decisions questions"):
    response = client.post(
        "/retrieval/query",
        json={
            "question": question,
            "top_k": 5,
            "filters": {"session_date_range": ["2026-09-08", "2026-09-08"]},
        },
    )
    assert response.status_code == 200
    chunks = response.json()["chunks"]
    assert chunks
    assert all(c["ground_truth"]["session_id"] == "2026-09-08" for c in chunks)
    assert all(c["ground_truth"]["full_text"] and c["provenance"] for c in chunks)
    assert any(c["score_breakdown"]["bm25_rank"] is not None for c in chunks)
    assert any(c["score_breakdown"]["vector_similarity"] > 0 for c in chunks)
    checks.append(
        {
            "question": question,
            "returned_chunks": len(chunks),
            "session_filter_verified": True,
            "provenance_present": True,
            "bm25_and_vector_hits": True,
        }
    )
response = client.post(
    "/retrieval/query",
    json={
        "question": "coaching",
        "filters": {"session_date_range": ["2000-01-01", "2000-01-02"]},
    },
)
assert response.status_code == 200 and response.json()["chunks"] == []
assert (
    client.get(
        "/retrieval/sessions",
        headers={"Authorization": "", "X-API-Key": tokens["CB_DEV_READER_TOKEN"]},
    ).status_code
    == 200
)
assert (
    client.post(
        "/retrieval/query", json={"question": "coaching"}, headers={"Authorization": ""}
    ).status_code
    == 401
)
for route in ("/retrieval/ingest", "/retrieval/reindex"):
    assert client.post(route, json={}).status_code == 404
print(
    json.dumps(
        {
            "queries": checks,
            "unmatched_date_filter_empty": True,
            "legacy_read_transport": True,
            "missing_auth_rejected": True,
            "mutations_hidden": True,
        },
        sort_keys=True,
    )
)
