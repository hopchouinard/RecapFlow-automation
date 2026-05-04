#!/usr/bin/env python3
"""Re-extract all sessions in the Community Brain corpus.

Three phases (run in order):
  1. SMOKE — re-extract 3 sentinel sessions, compare metrics pre/post.
     Abort if non-target metrics regress > 30% or has_unresolved_question
     rate decreases.
  2. BULK — re-extract remaining sessions. Abort on 3 consecutive failures.
  3. REPORT — corpus-wide pre/post comparison, anomaly flags, validator.

Usage:
  python scripts/reextract-all-sessions.py --server http://10.1.30.10:8999 \\
      --output-root /home/pchouinard/n8n/output

Spec: docs/superpowers/specs/2026-05-03-retrieval-v4-quality-improvements-design.md §5.5
"""
from __future__ import annotations

import argparse
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


# Sentinel sessions for SMOKE phase. Chosen for coverage:
# - one short session
# - one medium session
# - one long session
# Adjust if these sessions don't exist in your corpus.
SMOKE_SESSIONS = [
    "2025-02-02",  # historical short
    "2025-12-30",  # mid-corpus medium
    "2026-04-21",  # recent long
]

# Failure thresholds (ratios — 0.7 means a 30% drop)
NON_TARGET_METRIC_DROP_THRESHOLD = 0.7  # any drop below this triggers abort

# Metrics we expect roughly stable
STABLE_METRICS = (
    "entity_count_avg",
    "decision_count_avg",
    "action_item_count_avg",
    "has_question_rate",
    "has_insight_rate",
    "topic_label_present_rate",
)
# Metric we want to INCREASE under v3
TARGET_METRICS = ("has_unresolved_question_rate",)


@dataclass
class SessionMetrics:
    session_id: str
    chunk_count: int
    entity_count_avg: float
    decision_count_avg: float
    action_item_count_avg: float
    has_question_rate: float
    has_unresolved_question_rate: float
    has_insight_rate: float
    topic_label_present_rate: float


def fetch_session_metrics(server: str, session_id: str) -> SessionMetrics | None:
    """Query the retrieval server for chunks in a session and compute metrics.
    Returns None if the session has no chunks.
    """
    resp = requests.post(
        f"{server}/query",
        json={
            "question": f"chunks for session {session_id}",
            "top_k": 100,
            "session_filter": session_id,
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    chunks = data.get("chunks", [])
    chunks = [c for c in chunks if (c.get("ground_truth") or {}).get("session_id") == session_id]
    if not chunks:
        return None

    n = len(chunks)

    def avg(field: str) -> float:
        total = sum(len((c.get("derived_metadata") or {}).get(field) or []) for c in chunks)
        return total / n if n else 0.0

    def rate(field: str) -> float:
        true_count = sum(
            1 for c in chunks
            if (c.get("derived_metadata") or {}).get(field) is True
        )
        return true_count / n if n else 0.0

    def topic_rate() -> float:
        present = sum(
            1 for c in chunks
            if ((c.get("derived_metadata") or {}).get("topic_label") or "").strip()
        )
        return present / n if n else 0.0

    return SessionMetrics(
        session_id=session_id,
        chunk_count=n,
        entity_count_avg=avg("entities"),
        decision_count_avg=avg("decisions"),
        action_item_count_avg=avg("action_items"),
        has_question_rate=rate("has_question"),
        has_unresolved_question_rate=rate("has_unresolved_question"),
        has_insight_rate=rate("has_insight"),
        topic_label_present_rate=topic_rate(),
    )


def reextract_session(
    server: str, session_id: str, output_root: Path
) -> dict[str, Any]:
    """POST /ingest force_reextract for the given session.
    Returns the response JSON.
    """
    payload = {
        "session_id": session_id,
        "session_date": session_id,  # ISO date == session_id by convention
        "session_title": f"Re-extract {session_id}",  # filled in actually by Stage B
        "artifact_paths": {
            "prepared_transcript": f"{output_root}/{session_id}/prepared-transcript.md",
            "extracted_signal": f"{output_root}/{session_id}/extracted-signal.md",
            "community_post": f"{output_root}/{session_id}/community-post.md",
        },
        "force_reextract": True,
    }
    resp = requests.post(f"{server}/ingest", json=payload, timeout=1800)
    resp.raise_for_status()
    return resp.json()


def smoke_phase(
    server: str, output_root: Path, smoke_sessions: list[str]
) -> bool:
    """Re-extract sentinel sessions, compare pre/post metrics. Return True if all pass."""
    print("=" * 70)
    print("PHASE 1: SMOKE")
    print("=" * 70)
    print(f"Sentinel sessions: {smoke_sessions}\n")

    for sid in smoke_sessions:
        print(f"--- {sid} ---")
        pre = fetch_session_metrics(server, sid)
        if pre is None:
            print(f"  ABORT: no chunks for {sid} pre-extract — sentinel missing from corpus")
            return False
        print(f"  pre:  chunks={pre.chunk_count} unresolved_rate={pre.has_unresolved_question_rate:.2f}")

        t0 = time.time()
        result = reextract_session(server, sid, output_root)
        elapsed = time.time() - t0
        chunks_failed = result.get("chunks_failed", 0)
        if chunks_failed > 0:
            print(f"  ABORT: {sid} re-extract had failures: {result}")
            return False
        print(f"  re-extract: chunks_written={result.get('chunks_written')} elapsed={elapsed:.1f}s")

        post = fetch_session_metrics(server, sid)
        if post is None:
            print(f"  ABORT: no chunks for {sid} post-extract")
            return False
        print(f"  post: chunks={post.chunk_count} unresolved_rate={post.has_unresolved_question_rate:.2f}")

        # Compare metrics
        for metric in STABLE_METRICS:
            pre_val = getattr(pre, metric)
            post_val = getattr(post, metric)
            if pre_val == 0:
                continue  # avoid divide-by-zero; skip if pre was zero
            ratio = post_val / pre_val
            if ratio < NON_TARGET_METRIC_DROP_THRESHOLD:
                print(f"  ABORT: {metric} dropped from {pre_val:.3f} → {post_val:.3f} (ratio {ratio:.2f})")
                return False

        for metric in TARGET_METRICS:
            pre_val = getattr(pre, metric)
            post_val = getattr(post, metric)
            if post_val < pre_val:
                print(f"  ABORT: {metric} did not increase ({pre_val:.3f} → {post_val:.3f}) — v3 prompt change is not effective")
                return False
            print(f"  {metric}: {pre_val:.3f} → {post_val:.3f} ✓ (target metric increased or stable)")

        print(f"  {sid} SMOKE OK\n")

    print(f"\nSMOKE phase passed for {len(smoke_sessions)} sessions ✓")
    return True


def main():
    parser = argparse.ArgumentParser(description="Re-extract all sessions")
    parser.add_argument("--server", default="http://10.1.30.10:8999")
    parser.add_argument("--output-root", default="/home/pchouinard/n8n/output")
    parser.add_argument("--smoke-only", action="store_true",
                        help="Run only the SMOKE phase and exit")
    args = parser.parse_args()

    output_root = Path(args.output_root)

    # Phase 1: SMOKE
    smoke_passed = smoke_phase(args.server, output_root, SMOKE_SESSIONS)
    if not smoke_passed:
        print("\nSMOKE phase failed. Aborting.")
        sys.exit(1)

    if args.smoke_only:
        print("--smoke-only specified; exiting after SMOKE.")
        sys.exit(0)

    # Phase 2 (BULK) and Phase 3 (REPORT) added in Tasks 15 and 16.
    print("\nPhase 2 (BULK) and Phase 3 (REPORT) are added in Task 15 and 16.")


if __name__ == "__main__":
    main()
