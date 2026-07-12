#!/usr/bin/env python3
"""Fabrication-rate evaluation harness for Community Brain (v5 design D11).

Phases:
  RETRIEVAL  POST /query per adversarial probe; measure target-session
             recall@top_k. Deterministic; no LLM required.
  ANSWER     (--answer) Render the LLM context with the REAL filter code,
             call the answering model via Ollama /api/chat with the
             canonical system prompt, then run the filter's own grounding
             verifier over the answer. Fabrication is measured by the same
             functions that enforce the guard in production.
  REPORT     Aggregate + write JSON. --compare BASELINE.json prints deltas.

Run from community-brain/ with its venv, e.g.:
  ./.venv/bin/python ../scripts/eval-fabrication.py --out eval-v5.json
  ./.venv/bin/python ../scripts/eval-fabrication.py --answer \
      --model community-brain-v5-gpt-oss:20b --out eval-v5-answers.json
  ./.venv/bin/python ../scripts/eval-fabrication.py --compare eval-v4.json eval-v5.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import httpx
import yaml

from community_brain.openwebui.community_brain_filter import (
    Filter,
    _recompute_metadata_summary,
    extract_grounding_facts,
    verify_answer_grounding,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_QUERIES = REPO_ROOT / "scripts" / "eval" / "fabrication-queries.yaml"
DEFAULT_SYSTEM_PROMPT = REPO_ROOT / "docs" / "inference-guidelines.md"

# NOTE: refusal detection is a substring heuristic — it can misclassify
# hedged answers and misses phrasings not listed here (e.g. "not mentioned
# in the sources"). It skews fabrication_rate (refused answers are excluded
# from that denominator) and refusal_correctness. Operators should sanity-
# check per-query `answer` text and tune these patterns for their model.
REFUSAL_PATTERNS = (
    "don't see",
    "do not see",
    "doesn't cover",
    "does not cover",
    "not in the retrieved",
    "no retrieved sources",
    "cannot answer",
    "can't answer",
    "don't have",
)


def looks_like_refusal(answer: str) -> bool:
    lowered = answer.lower()
    return any(p in lowered for p in REFUSAL_PATTERNS)


def load_queries(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)["queries"]


def run_retrieval(server: str, api_key: str, question: str, top_k: int) -> dict:
    resp = httpx.post(
        f"{server}/query",
        json={"question": question, "top_k": top_k},
        headers={"X-API-Key": api_key},
        timeout=60.0,
    )
    resp.raise_for_status()
    return resp.json()


def render_context(chunks: list[dict], min_score: float) -> tuple[str, list[dict]]:
    """Mirror production: min_score cutoff, recomputed summary, then the
    filter's real context builder."""
    kept = [c for c in chunks if c.get("similarity", 0) >= min_score]
    filt = Filter()
    if not kept:
        return filt._build_no_sources_message(), []
    summary = _recompute_metadata_summary(kept)
    return filt._build_sources_message(kept, summary), kept


def run_answer(
    ollama_url: str, model: str, system_prompt: str, context: str,
    question: str, temperature: float,
) -> str:
    resp = httpx.post(
        f"{ollama_url}/api/chat",
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": context},
                {"role": "user", "content": question},
            ],
            "stream": False,
            "options": {"temperature": temperature},
        },
        timeout=600.0,
    )
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def evaluate_query(q: dict, args) -> dict:
    result: dict = {"id": q["id"], "class": q["class"], "question": q["question"]}

    data = run_retrieval(args.server, args.api_key, q["question"], args.top_k)
    retrieved_sessions = sorted({
        (c.get("ground_truth") or {}).get("session_date", "")
        for c in data.get("chunks", [])
    } - {""})
    result["retrieved_sessions"] = retrieved_sessions
    result["injected_counts"] = sum(
        1
        for c in data.get("chunks", [])
        if (c.get("score_breakdown") or {}).get("injected_by")
    )
    targets = q.get("target_sessions") or []
    if targets:
        hit = len(set(targets) & set(retrieved_sessions))
        result["target_recall"] = hit / len(targets)
    else:
        result["target_recall"] = None

    if not args.answer:
        return result

    context, kept = render_context(data.get("chunks", []), args.min_score)
    result["kept_sessions"] = sorted(
        {(c.get("ground_truth") or {}).get("session_date", "") for c in kept} - {""}
    )
    answer = run_answer(
        args.ollama_url, args.model, args.system_prompt_text, context,
        q["question"], args.temperature,
    )
    result["answer"] = answer
    result["refused"] = looks_like_refusal(answer)
    result["refusal_correct"] = (
        result["refused"] if q.get("expect_refusal") else None
    )

    facts = extract_grounding_facts(context)
    if facts is not None:
        verdict = verify_answer_grounding(answer, facts)
        result["unverified_dates"] = verdict["unverified_dates"]
        result["unverified_sources"] = verdict["unverified_sources"]
        result["unverified_chunk_ids"] = verdict["unverified_chunk_ids"]
    else:
        # No sources retrieved: only explicit traps are checkable.
        result["unverified_dates"] = [
            d for d in (q.get("forbidden_dates") or []) if d in answer
        ]
        result["unverified_sources"] = []
        result["unverified_chunk_ids"] = []
    result["forbidden_date_hits"] = [
        d for d in (q.get("forbidden_dates") or []) if d in answer
    ]
    result["fabricated"] = bool(
        result["unverified_dates"]
        or result["unverified_sources"]
        or result["unverified_chunk_ids"]
        or result["forbidden_date_hits"]
    )
    return result


def aggregate(per_query: list[dict], answered: bool) -> dict:
    agg: dict = {"queries": len(per_query)}
    recalls = [r["target_recall"] for r in per_query if r["target_recall"] is not None]
    agg["mean_target_recall"] = (sum(recalls) / len(recalls)) if recalls else None
    agg["queries_with_injection"] = sum(
        1 for r in per_query if r.get("injected_counts", 0) > 0
    )
    if answered:
        answered_qs = [r for r in per_query if not r.get("refused")]
        agg["fabrication_rate"] = (
            (sum(1 for r in answered_qs if r.get("fabricated")) / len(answered_qs))
            if answered_qs
            else 0.0
        )
        refusal_probes = [r for r in per_query if r.get("refusal_correct") is not None]
        agg["refusal_correctness"] = (
            (sum(1 for r in refusal_probes if r["refusal_correct"]) / len(refusal_probes))
            if refusal_probes
            else None
        )
    return agg


def compare(baseline_path: Path, current_path: Path) -> None:
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    current = json.loads(current_path.read_text(encoding="utf-8"))
    print(f"baseline: {baseline_path}  →  current: {current_path}")
    for key in ("mean_target_recall", "fabrication_rate", "refusal_correctness",
                "queries_with_injection"):
        b = baseline.get("aggregates", {}).get(key)
        c = current.get("aggregates", {}).get(key)
        print(f"  {key}: {b} → {c}")
    b_by_id = {r["id"]: r for r in baseline.get("per_query", [])}
    for r in current.get("per_query", []):
        b = b_by_id.get(r["id"], {})
        if b.get("target_recall") != r.get("target_recall") or b.get(
            "fabricated"
        ) != r.get("fabricated"):
            print(
                f"  {r['id']}: recall {b.get('target_recall')} → "
                f"{r.get('target_recall')}, fabricated {b.get('fabricated')} → "
                f"{r.get('fabricated')}"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queries", type=Path, default=DEFAULT_QUERIES)
    parser.add_argument("--server", default="http://127.0.0.1:8999")
    parser.add_argument(
        "--api-key", default=os.environ.get("RETRIEVAL_API_KEY") or ""
    )
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--min-score", type=float, default=0.2)
    parser.add_argument("--answer", action="store_true",
                        help="run the ANSWER phase via Ollama")
    parser.add_argument("--ollama-url", default="http://10.1.50.219:11434")
    parser.add_argument("--model", default="gpt-oss:20b")
    parser.add_argument("--system-prompt", type=Path, default=DEFAULT_SYSTEM_PROMPT)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--out", type=Path, default=Path("eval-fabrication.json"))
    parser.add_argument("--compare", nargs=2, type=Path, metavar=("BASELINE", "CURRENT"))
    args = parser.parse_args()

    if args.compare:
        compare(args.compare[0], args.compare[1])
        return 0

    args.system_prompt_text = args.system_prompt.read_text(encoding="utf-8")
    queries = load_queries(args.queries)

    per_query = []
    for q in queries:
        print(f"[eval] {q['id']} ...", file=sys.stderr)
        try:
            per_query.append(evaluate_query(q, args))
        except Exception as exc:
            print(f"[eval] {q['id']} FAILED: {exc}", file=sys.stderr)
            per_query.append({"id": q["id"], "error": str(exc)})

    report = {
        "server": args.server,
        "top_k": args.top_k,
        "answer_phase": bool(args.answer),
        "model": args.model if args.answer else None,
        "temperature": args.temperature if args.answer else None,
        "per_query": per_query,
        "aggregates": aggregate(
            [r for r in per_query if "error" not in r], args.answer
        ),
    }
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["aggregates"], indent=2))
    print(f"[eval] wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
