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

# v4 target: corpus-wide has_unresolved_question chunk count must reach at least this
MIN_UNRESOLVED_COUNT_TARGET = 35

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
            "filters": {"session_date_range": [session_id, session_id]},
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
        total = 0
        for c in chunks:
            value = (c.get("derived_metadata") or {}).get(field)
            if isinstance(value, list):
                total += len(value)
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


def fetch_session_title_lookup(server: str) -> dict[str, str]:
    """Map session_id -> session_title from /sessions response.
    Returns empty dict on failure (callers should fall back defensively).
    """
    try:
        resp = requests.get(f"{server}/sessions", timeout=60)
        resp.raise_for_status()
    except Exception as exc:
        print(f"WARN: could not fetch /sessions for title lookup: {exc}")
        return {}
    data = resp.json()
    sessions = data.get("sessions", [])
    return {
        s.get("session_id"): s.get("session_title") or s.get("session_id", "")
        for s in sessions
        if s.get("session_id")
    }


def reextract_session(
    server: str,
    session_id: str,
    session_title: str,
    output_root: Path,
) -> dict[str, Any]:
    """POST /ingest force_reextract for the given session.
    Returns the response JSON.
    """
    payload = {
        "session_id": session_id,
        "session_date": session_id,  # ISO date == session_id by convention
        "session_title": session_title,
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
    server: str,
    output_root: Path,
    smoke_sessions: list[str],
    title_lookup: dict[str, str],
) -> bool:
    """Re-extract sentinel sessions, compare pre/post metrics. Return True if all pass."""
    print("=" * 70)
    print("PHASE 1: SMOKE")
    print("=" * 70)
    print(f"Sentinel sessions: {smoke_sessions}\n")

    for sid in smoke_sessions:
        print(f"--- {sid} ---")
        title = title_lookup.get(sid)
        if title is None:
            print(f"  ABORT: no title found in /sessions for {sid} — sentinel missing or registry broken")
            return False
        pre = fetch_session_metrics(server, sid)
        if pre is None:
            print(f"  ABORT: no chunks for {sid} pre-extract — sentinel missing from corpus")
            return False
        print(f"  pre:  chunks={pre.chunk_count} unresolved_rate={pre.has_unresolved_question_rate:.2f}")

        t0 = time.time()
        result = reextract_session(server, sid, title, output_root)
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


def list_corpus_sessions(server: str) -> list[str]:
    """Return sorted list of session_ids in the corpus."""
    resp = requests.get(f"{server}/sessions", timeout=60)
    resp.raise_for_status()
    data = resp.json()
    sessions = data.get("sessions", [])
    return sorted({s.get("session_id") for s in sessions if s.get("session_id")})


def bulk_phase(
    server: str,
    output_root: Path,
    smoke_sessions: list[str],
    title_lookup: dict[str, str],
) -> tuple[list[str], list[tuple[str, str]], list[str]]:
    """Re-extract all sessions not in smoke_sessions.
    Returns (succeeded_session_ids, failed_session_ids_with_reason, unprocessed_session_ids).
    Aborts on 3 consecutive failures; unprocessed tracks sessions not yet attempted.
    """
    print("=" * 70)
    print("PHASE 2: BULK")
    print("=" * 70)

    all_sessions = list_corpus_sessions(server)
    queue = [s for s in all_sessions if s not in smoke_sessions]
    print(f"Remaining sessions: {len(queue)}\n")

    succeeded: list[str] = []
    failed: list[tuple[str, str]] = []
    consecutive_failures = 0
    abort_index: int | None = None

    for i, sid in enumerate(queue, start=1):
        print(f"[{i}/{len(queue)}] {sid}")
        title = title_lookup.get(sid)
        if title is None:
            reason = "no title in /sessions"
            print(f"  FAIL: {reason}")
            failed.append((sid, reason))
            consecutive_failures += 1
        else:
            try:
                t0 = time.time()
                result = reextract_session(server, sid, title, output_root)
                elapsed = time.time() - t0
                chunks_failed = result.get("chunks_failed", 0)
                chunks_written = result.get("chunks_written", 0)
                if chunks_failed > 0:
                    reason = f"chunks_failed={chunks_failed}"
                    print(f"  FAIL: {reason}")
                    failed.append((sid, reason))
                    consecutive_failures += 1
                else:
                    print(f"  OK: chunks_written={chunks_written} elapsed={elapsed:.1f}s")
                    succeeded.append(sid)
                    consecutive_failures = 0
            except Exception as exc:
                reason = f"exception: {exc}"
                print(f"  FAIL: {reason}")
                failed.append((sid, reason))
                consecutive_failures += 1

        if consecutive_failures >= 3:
            print(f"\nABORT: 3 consecutive failures. Stopping bulk phase.")
            abort_index = i  # queue is 0-indexed, enumerate started at 1
            break

    unprocessed: list[str] = []
    if abort_index is not None:
        unprocessed = queue[abort_index:]  # everything after the abort index (0-based: abort_index == i-1+1 == i)

    print(f"\nBULK phase done: {len(succeeded)} succeeded, {len(failed)} failed, {len(unprocessed)} unprocessed")
    return succeeded, failed, unprocessed


def report_phase(
    server: str,
    succeeded: list[str],
    failed: list[tuple[str, str]],
    unprocessed: list[str],
) -> None:
    """Phase 3: print corpus-wide post-extract report."""
    print("=" * 70)
    print("PHASE 3: REPORT")
    print("=" * 70)

    print(f"\nSucceeded: {len(succeeded)} sessions")
    if failed:
        print(f"\nFailed: {len(failed)} sessions")
        for sid, reason in failed:
            print(f"  - {sid}: {reason}")
    if unprocessed:
        print(f"\nUnprocessed: {len(unprocessed)} sessions (BULK aborted before reaching them)")
        for sid in unprocessed:
            print(f"  - {sid}")

    # Aggregate metrics across all succeeded sessions
    print("\nCollecting post-extract metrics...")
    all_metrics: list[SessionMetrics] = []
    for sid in succeeded:
        m = fetch_session_metrics(server, sid)
        if m is not None:
            all_metrics.append(m)

    if not all_metrics:
        print("No metrics collected.")
        return

    total_chunks = sum(m.chunk_count for m in all_metrics)
    if total_chunks == 0:
        print("No chunks across reported sessions.")
        return

    avg_unresolved = sum(m.has_unresolved_question_rate * m.chunk_count for m in all_metrics) / total_chunks
    avg_entity = sum(m.entity_count_avg * m.chunk_count for m in all_metrics) / total_chunks
    avg_decisions = sum(m.decision_count_avg * m.chunk_count for m in all_metrics) / total_chunks
    avg_topic_present = sum(m.topic_label_present_rate * m.chunk_count for m in all_metrics) / total_chunks

    print(f"\nCorpus-wide post-extract metrics ({len(all_metrics)} sessions, {total_chunks} chunks):")
    print(f"  has_unresolved_question rate: {avg_unresolved:.3f}")
    print(f"  entities/chunk avg:           {avg_entity:.2f}")
    print(f"  decisions/chunk avg:          {avg_decisions:.2f}")
    print(f"  topic_label present rate:     {avg_topic_present:.3f}")

    # Validator: corpus-wide has_unresolved_question count target
    unresolved_total = sum(
        m.has_unresolved_question_rate * m.chunk_count for m in all_metrics
    )
    if unresolved_total < MIN_UNRESOLVED_COUNT_TARGET:
        print(f"\nWARNING: corpus-wide has_unresolved_question count is "
              f"{unresolved_total:.0f}, below v4 target of {MIN_UNRESOLVED_COUNT_TARGET}")
    else:
        print(f"\nv4 has_unresolved_question target met: {unresolved_total:.0f} ≥ {MIN_UNRESOLVED_COUNT_TARGET} ✓")

    # Anomaly flag: any session with 0 chunks?
    zero_chunk_sessions = [m.session_id for m in all_metrics if m.chunk_count == 0]
    if zero_chunk_sessions:
        print(f"\nANOMALY: {len(zero_chunk_sessions)} sessions have 0 chunks: {zero_chunk_sessions}")

    print("\nReport complete.")


def main():
    parser = argparse.ArgumentParser(description="Re-extract all sessions")
    parser.add_argument("--server", default="http://10.1.30.10:8999")
    parser.add_argument("--output-root", default="/home/pchouinard/n8n/output")
    parser.add_argument("--smoke-only", action="store_true",
                        help="Run only the SMOKE phase and exit")
    parser.add_argument("--skip-smoke", action="store_true",
                        help="Skip SMOKE phase (use only if already passed)")
    args = parser.parse_args()

    output_root = Path(args.output_root)

    title_lookup = fetch_session_title_lookup(args.server)
    if not title_lookup:
        print("ABORT: empty title lookup — server unreachable or /sessions returned no entries")
        sys.exit(1)
    print(f"Loaded {len(title_lookup)} session titles from /sessions\n")

    # Phase 1: SMOKE
    if not args.skip_smoke:
        smoke_passed = smoke_phase(args.server, output_root, SMOKE_SESSIONS, title_lookup)
        if not smoke_passed:
            print("\nSMOKE phase failed. Aborting.")
            sys.exit(1)

    if args.smoke_only:
        print("--smoke-only specified; exiting after SMOKE.")
        sys.exit(0)

    # Phase 2: BULK
    succeeded, failed, unprocessed = bulk_phase(args.server, output_root, SMOKE_SESSIONS, title_lookup)

    # Phase 3: REPORT — runs even on partial bulk failure so the operator
    # gets a corpus-wide view of what landed.
    all_succeeded = SMOKE_SESSIONS + succeeded
    report_phase(args.server, all_succeeded, failed, unprocessed)

    if failed or unprocessed:
        sys.exit(2)


if __name__ == "__main__":
    main()
