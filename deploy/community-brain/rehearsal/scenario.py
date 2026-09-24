"""HTTP-driven checks against the containerized application and durable worker."""

import hashlib
import json
from pathlib import Path
import sys
import subprocess
import time
from uuid import UUID

import httpx
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from community_brain.jobs.models import ModelCall
from community_brain.jobs.runtime import make_store

client = httpx.Client(
    base_url="http://api:8090",
    timeout=20,
    headers={"Authorization": "Bearer cbm-disposable-fixture"},
)
record = Path("/state/files/scenario.json")


def request(method, path, **kwargs):
    response = client.request(method, path, **kwargs)
    response.raise_for_status()
    return response.json()


def submit(day, mode, interrupt=False):
    meeting = "fixture-" + day
    sources = {}
    for kind in ["transcript", "chat"] if mode == "weekly" else ["transcript"]:
        sources[kind] = request(
            "POST",
            "/api/v1/sources",
            json={
                "meeting_id": meeting,
                "kind": kind,
                "content": ("INTERRUPT_FIXTURE " if interrupt else "")
                + "00:00:00 - Alex\nFixture recovery uses durable storage.\n",
            },
        )["id"]
    body = {
        "identity": {
            "meeting_id": meeting,
            "started_at": day + "T22:00:00Z",
            "timezone": "America/Toronto",
            "local_date": day,
        },
        "mode": mode,
        "sources": sources,
    }
    headers = {"Idempotency-Key": meeting}
    job = request("POST", "/api/v1/jobs", json=body, headers=headers)
    assert (
        request("POST", "/api/v1/jobs", json=body, headers=headers)["id"] == job["id"]
    )
    return job["id"]


def wait(job, field, state, seconds=100):
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        data = request("GET", "/api/v1/jobs/" + job)
        if data[field] == state:
            return data
        if data[field] in ("failed", "partial", "outcome_unknown"):
            raise AssertionError(data)
        time.sleep(1)
    raise AssertionError(data)


def verify(job, count):
    state = wait(job, "indexing", "complete")
    assert state["processing"] == "succeeded" and state["artifacts"] == "ready"
    items = request("GET", "/api/v1/jobs/" + job + "/artifacts")["items"]
    assert len(items) == count, items
    for item in items:
        response = client.get(item["url"])
        response.raise_for_status()
        assert hashlib.sha256(response.content).hexdigest() == item["sha256"]
    return {item["name"]: item["sha256"] for item in items}


def counts(ids=None):
    with Session(make_store().engine) as session:
        query = select(func.count()).select_from(ModelCall)
        if ids is not None:
            query = query.where(ModelCall.job_id.in_([UUID(value) for value in ids]))
        return session.scalar(query)


def check():
    state = json.loads(record.read_text())
    for item in state["jobs"]:
        assert verify(item["id"], len(item["hashes"])) == item["hashes"]
    assert counts() == state["calls"], "Completed calls were repeated"
    response = client.post(
        "/retrieval/query",
        json={"question": "fixture recovery", "top_k": 3},
        headers={"X-API-Key": "cbm-disposable-fixture", "Authorization": ""},
    )
    response.raise_for_status()
    result = response.json()
    assert result["chunks"], result
    assert all(c["ground_truth"]["full_text"] for c in result["chunks"])
    print(
        "PASS: persisted artifacts, unchanged model-call count, authenticated hybrid retrieval",
        flush=True,
    )


def main():
    mode = sys.argv[1]
    if mode == "submit":
        jobs = []
        for day, kind, count in [
            ("2026-09-08", "weekly", 6),
            ("2026-09-01", "transcript_backfill", 3),
        ]:
            job = submit(day, kind)
            jobs.append({"id": job, "hashes": verify(job, count)})
        record.write_text(json.dumps({"jobs": jobs, "calls": counts()}))
        check()
    elif mode == "check":
        check()
    elif mode == "pending":
        state = json.loads(record.read_text())
        state["pending"] = submit("2026-08-11", "transcript_backfill")
        record.write_text(json.dumps(state))
        print("READY: queued job accepted with worker stopped", flush=True)
    elif mode == "restore-check":
        state = json.loads(record.read_text())
        # Verify old hashes/call count before adding the recovered pending job.
        assert counts([item["id"] for item in state["jobs"]]) == state["calls"]
        for item in state["jobs"]:
            assert verify(item["id"], len(item["hashes"])) == item["hashes"]
        job = state.pop("pending")
        state["jobs"].append({"id": job, "hashes": verify(job, 3)})
        state["calls"] = counts()
        record.write_text(json.dumps(state))
        check()
        print(
            "PASS: database/files restored; empty queue reconstructed pending work",
            flush=True,
        )
    elif mode == "publish":
        state = json.loads(record.read_text())
        job = state["jobs"][0]["id"]
        for kind, final in (("git", "complete"), ("distribution", "validated")):
            path = "/api/v1/jobs/" + job + "/publications/" + kind
            headers = {"Idempotency-Key": "fixture-" + kind}
            request("POST", path, headers=headers)
            data = wait(job, kind, final)
            result = next(s["result"] for s in data["stages"] if s["name"] == kind)
            request("POST", path, headers=headers)
            if kind == "git":
                actual = subprocess.check_output(
                    [
                        "git",
                        "--git-dir=/state/corpus/artifacts.git",
                        "rev-parse",
                        "HEAD",
                    ],
                    text=True,
                ).strip()
                assert result["commit"] == actual
                assert result["artifact_hashes"] == state["jobs"][0]["hashes"]
            else:
                from community_brain.jobs.publication import validate_bundle

                manifest = validate_bundle(
                    Path("/state/corpus/releases") / result["version"]
                )
                assert manifest["session_count"] == 4
                assert not Path("/state/corpus/releases/current.json").exists()
        check()
        print(
            "PASS: local Git receipt and consumer package verified; no remote release",
            flush=True,
        )
    elif mode == "interrupt":
        job = submit("2026-08-18", "transcript_backfill", True)
        (record.parent / "interrupt-job").write_text(job)
        deadline = time.monotonic() + 30
        while not (record.parent / "interrupted").exists():
            assert time.monotonic() < deadline
            time.sleep(0.5)
        print("READY: simulated provider entered; kill worker container", flush=True)
    elif mode == "reconcile":
        job = (record.parent / "interrupt-job").read_text()
        data = wait(job, "processing", "outcome_unknown")
        stage = next(s for s in data["stages"] if s["name"] == "processing")
        payload = {
            "generation": stage["generation"],
            "reason": "Fixture effect confirmed simulated; explicitly permit retry",
        }
        path = "/api/v1/jobs/" + job + "/stages/" + stage["id"] + "/reconcile"
        assert (
            client.post(
                path, json=payload, headers={"Idempotency-Key": "no-ack"}
            ).status_code
            == 409
        )
        request(
            "POST",
            path,
            json=payload,
            headers={
                "Idempotency-Key": "fixture-reconcile",
                "Acknowledge-Duplicate-Effect": "true",
            },
        )
        hashes = verify(job, 3)
        state = json.loads(record.read_text())
        state["jobs"].append({"id": job, "hashes": hashes})
        state["calls"] = counts()
        record.write_text(json.dumps(state))
        print(
            "PASS: killed effect held unknown; explicit reconciliation recovered job",
            flush=True,
        )
    else:
        raise SystemExit("unknown scenario")


if __name__ == "__main__":
    main()
