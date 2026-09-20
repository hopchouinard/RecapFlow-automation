"""Read-only authenticated queries; print metadata, never retrieved text."""

import json
import sys
import time

import httpx

assert time.time() < 1789069401
private = json.load(sys.stdin)
client = httpx.Client(
    base_url="http://cbm-preserved-api:8090",
    timeout=60,
    headers={"Authorization": "Bearer " + private["CB_DEV_READER_TOKEN"]},
)
checks = []
for question, dates in (
    ("AI Developer Accelerator tools and decisions", None),
    ("coaching call questions and insights", ["2026-09-08", "2026-09-08"]),
    ("AI development tools", ["2025-02-01", "2025-03-31"]),
    ("workflow automation lessons", ["2026-04-01", "2026-06-30"]),
):
    body = {"question": question, "top_k": 5}
    if dates:
        body["filters"] = {"session_date_range": dates}
    response = client.post("/retrieval/query", json=body)
    assert response.status_code == 200
    chunks = response.json()["chunks"]
    assert chunks
    assert all(c["provenance"]["extraction_status"] == "success" for c in chunks)
    assert all(c["ground_truth"]["full_text"] for c in chunks)
    if dates:
        assert all(
            dates[0] <= c["ground_truth"]["session_id"][:10] <= dates[1] for c in chunks
        )
    assert any(c["score_breakdown"]["bm25_rank"] is not None for c in chunks)
    assert any(c["score_breakdown"]["vector_similarity"] > 0 for c in chunks)
    checks.append(
        {
            "question": question,
            "date_filter": dates,
            "results": len(chunks),
            "chunk_ids": [c["ground_truth"]["chunk_id"] for c in chunks],
            "only_successful_extractions": True,
            "bm25_and_vector_hits": True,
            "provenance_present": True,
        }
    )
response = client.post(
    "/retrieval/query",
    json={
        "question": "coaching",
        "filters": {"session_date_range": ["2000-01-01", "2000-01-02"]},
    },
)
assert response.status_code == 200 and not response.json()["chunks"]
assert (
    client.post(
        "/retrieval/query", json={"question": "coaching"}, headers={"Authorization": ""}
    ).status_code
    == 401
)
assert client.post("/retrieval/ingest", json={}).status_code == 404
assert (
    client.get(
        "/retrieval/sessions",
        headers={"Authorization": "", "X-API-Key": private["CB_DEV_READER_TOKEN"]},
    ).status_code
    == 200
)
print(
    json.dumps(
        {
            "queries": checks,
            "empty_date_filter": True,
            "missing_auth_denied": True,
            "mutations_hidden": True,
            "legacy_auth_passed": True,
            "generation_calls": 0,
        },
        sort_keys=True,
    )
)
