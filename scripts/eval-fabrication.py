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
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import httpx
import yaml

from community_brain.openwebui.community_brain_filter import (
    Filter,
    _normalize_dashes,
    _recompute_metadata_summary,
    extract_grounding_facts,
    verify_answer_grounding,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_QUERIES = REPO_ROOT / "scripts" / "eval" / "fabrication-queries.yaml"
DEFAULT_SYSTEM_PROMPT = REPO_ROOT / "docs" / "inference-guidelines.md"

# Ollama defaults num_ctx to 4096. The rendered context on this corpus runs
# 17k-60k characters (~4k-15k tokens) before the system prompt, so the default
# silently truncated the prompt and clipped generation at the window edge —
# RecapFlow #16's 25% empty-answer rate, and answers produced from roughly a
# third of the retrieved context.
#
# 32768 was the first fix and was not enough. It sizes the window for the
# PROMPT and leaves whatever remains for generation, which is the wrong way
# round for a reasoning model. Measured across two independent 5-run blocks
# (2026-08-02), `unresolved-survey` failed identically in each:
#
#     prompt_eval_count = 16243
#     eval_count        = 16525   (16243 + 16525 = 32768, exactly num_ctx)
#     done_reason       = length
#     thinking_len      = 73861   (other runs: 11,737 - 30,364)
#     answer            = ""
#
# Byte-identical counts in both blocks, so this is deterministic, not flaky.
# The trigger is D26's retrieval nondeterminism: that probe receives three
# distinct context variants, and the largest (16,243 prompt tokens vs ~14,600)
# provokes runaway reasoning that then exhausts the window. One run in five
# hits it, which puts a clean 5-run block at ~33% and two consecutive clean
# blocks — what D19 acceptance requires — at roughly 1 in 9.
#
# gpt-oss:20b advertises gptoss.context_length = 131072, so 32768 was a
# quarter of capacity. 65536 leaves ~49k tokens for generation against the
# largest observed prompt, comfortably above the 16.5k this probe wants.
# Verified against the live Ollama host before adoption.
#
# This treats the symptom. The defect is that retrieval hands the model a
# different context per call (D26); fixing that is retrieval-package work and
# out of scope here. Recorded because the acceptance gate now depends on it.
DEFAULT_NUM_CTX = 65536

# With num_ctx correct the model finally reasons to completion, and the
# long-reasoning probes are slow: block 3 (2026-07-26) lost 5 of 60 probes to
# the previous hard-coded 600s, three of them `unresolved-survey`, which
# generated 4,531 tokens in the runs that did finish. A timeout converts a
# slow-but-valid answer into an `error`, and an error breaks unanimity — so
# the wall clock was silently deciding acceptance. ~10 tok/s observed here.
DEFAULT_ANSWER_TIMEOUT = 1800.0

# NOTE: refusal detection is a substring heuristic — it can still misclassify
# hedged answers. It skews fabrication_rate (refused answers are excluded from
# that denominator) and refusal_correctness, so operators should sanity-check
# per-query `answer` text and tune these patterns for their model.
#
# The 2026-07-25 v4 baseline scored refusal_correctness = 0.0 partly on a
# FALSE NEGATIVE: the fictitious-speaker probe refused correctly with "I
# couldn't locate any reference to … None of the sessions contain …", which
# matched nothing in the original pattern list. Patterns must stay narrow
# enough not to fire on substantive prose — "locate" alone would match "the
# team decided to locate the service in the EU region", so the locate/find
# forms are anchored to their negations.
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
    "couldn't locate",
    "could not locate",
    "unable to locate",
    "couldn't find",
    "could not find",
    "unable to find",
    "didn't find",
    "did not find",
    "don't find",
    "do not find",
    "none of the sessions",
    "none of the retrieved",
    "not mentioned in",
    "no mention of",
    "no reference to",
)

# Models emit typographic apostrophes (U+2019), so "don't see" written as
# "don’t see" would miss every ASCII-apostrophe pattern above. Same class of
# defect as the Unicode-dash bypass of the citation guard's date check.
_APOSTROPHES = str.maketrans({"’": "'", "‘": "'", "ʼ": "'", "＇": "'"})


_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+|\n+")


def _split_sentences(text: str) -> list[str]:
    """Split an answer into sentences for per-occurrence scoping (D23/D24)."""
    return [s for s in _SENTENCE_SPLIT_RE.split(text or "") if s.strip()]


def _is_refusal_sentence(sentence: str) -> bool:
    """Does THIS sentence, on its own, express a refusal?"""
    lowered = (sentence or "").lower().translate(_APOSTROPHES)
    return any(p in lowered for p in REFUSAL_PATTERNS)


# A leading clause that is nothing but a negation carries the refusal's
# SIGNAL but none of its vocabulary — the substance sits in the sentence
# after it. Anchoring to the first sentence alone therefore loses refusals
# that open this way: "No. I don't see that session in the retrieved
# sources." scored not-refused, while the comma form of the same sentence
# scored refused. One punctuation mark decided the verdict, and an
# expect_refusal probe would have failed on a correct answer.
_BARE_NEGATION_RE = re.compile(
    r"^(no|none|nope|negative|not really|unfortunately|afraid not)"
    r"[\s.!,;:—–-]*$",
    re.IGNORECASE,
)


def _leading_clause(answer: str) -> str:
    """The answer's first sentence, plus the next one if the first is a bare
    negation.

    Widening is capped at ONE extra sentence on purpose. The point of D24 is
    that a refusal phrase buried deep in a substantive answer must not
    classify it as a refusal; admitting the whole body back would undo that.
    A bare negation is also NOT treated as a refusal on its own — "No."
    answering "Has anyone used Codex in production?" is a grounded answer,
    not a failure to answer.
    """
    sentences = _split_sentences(answer)
    if not sentences:
        return ""
    lead = sentences[0]
    if len(sentences) > 1 and _BARE_NEGATION_RE.match(lead.strip()):
        return f"{lead} {sentences[1]}"
    return lead


def looks_like_refusal(answer: str) -> bool:
    """D24: classify from the LEADING CLAUSE only, never the whole body.

    The previous whole-body substring scan let one negative clause deep inside
    a substantive answer flip the classification: hemal-garron-conjunction
    opened "Yes - the mid-December call ... included both individuals" and
    scored refused=True because "no retrieved sources" appeared two sentences
    later. Refusals are excluded from the fabrication_rate denominator, so
    every false refusal silently shrinks it — the same denominator defect
    PR #17 fixed for empty answers, reached by a second route.
    """
    return _is_refusal_sentence(_leading_clause(answer))


def find_forbidden_dates(
    answer: str,
    forbidden: list[str] | None,
    exempt_refusal_sentences: bool = False,
) -> list[str]:
    """Return the configured trap dates that appear in `answer`.

    D23: with `exempt_refusal_sentences`, a date occurrence is scored only
    when the sentence carrying THAT occurrence is not itself a refusal. The
    trap asks whether the model ASSERTED something about a session that does
    not exist; naming the date in order to say it was not found is the only
    correct refusal available. `nonexistent-session` refused 15/15 across
    blocks 3-5 and was scored fabricated=True every time — the sole reason
    all_unanimous was False.

    Per-occurrence, never per-answer: the naive `if refused: ignore` converts
    the trap into a fabrication licence, especially under D24 where the
    classification comes from the leading clause alone.

    Default False keeps `verify_answer_grounding` and the deployed guard
    unchanged — the production filter still annotates the date, which is
    correct for a reader who needs to know it was not in the sources.

    KNOWN GAP (Patchou-plan FU-30): scoping is per SENTENCE, so a single
    sentence that both refuses and asserts — "I don't see a session from
    2025-12-15, but it covered the pricing rollout" — remains exempt. Closing
    it needs clause-level splitting, which produces false positives on
    ordinary prose. Approved as-is 2026-08-02; revisit if a probe exploits it.

    Compares modulo dash codepoint, reusing the filter's normalizer so the
    harness and the production guard cannot drift apart. A raw substring
    match misses "2025‑12‑15" written with U+2011 — which gpt-oss:20b does
    spontaneously, and which cost this check a real hit on the
    nonexistent-session probe of the 2026-07-25 v4 baseline. On the
    no-sources path these traps are the ONLY verification available, so a
    miss there silently undercounts fabrication.
    """
    if not forbidden:
        return []
    if exempt_refusal_sentences:
        scored_text = " ".join(
            s for s in _split_sentences(answer) if not _is_refusal_sentence(s)
        )
    else:
        scored_text = answer or ""
    normalized = _normalize_dashes(scored_text)
    return [d for d in forbidden if _normalize_dashes(d) in normalized]


def _dates_asserted_outside_refusals(
    answer: str, dates: list[str] | None
) -> list[str]:
    """D23 clause 2, applied to VERIFIER-produced date hits.

    `verify_answer_grounding` reports every date token the model emitted that
    is absent from the rendered context. For a correct refusal the named date
    is absent *by construction* — so the verifier flags precisely the token
    that proves the model behaved correctly.

    Measured 2026-08-02, and the reason this function exists: after exempting
    `forbidden_date_hits` and the no-sources branch, `nonexistent-session`
    still scored fabricated 5/5 with `forbidden_date_hits=[]` and
    `unverified_dates=['2025-12-15']`. That probe retrieves 36,717 characters
    of context, so `extract_grounding_facts` returns facts and this path runs
    instead of the no-sources one. Exempting only the other two inputs is
    insufficient for every probe that retrieves anything at all.

    Same per-occurrence rule as `find_forbidden_dates`: a date survives only
    if it appears in a sentence that is not itself a refusal. Dates only —
    `unverified_sources` and `unverified_chunk_ids` are never exempted, since
    an invented citation is a fabrication wherever it appears.
    """
    if not dates:
        return []
    assertive = _normalize_dashes(
        " ".join(s for s in _split_sentences(answer) if not _is_refusal_sentence(s))
    )
    return [d for d in dates if _normalize_dashes(d) in assertive]


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
    question: str, temperature: float, num_ctx: int = DEFAULT_NUM_CTX,
    timeout: float = DEFAULT_ANSWER_TIMEOUT,
) -> dict:
    """Ask the model one probe and report how the generation terminated.

    Returns content, thinking, and the termination evidence
    (done_reason/prompt_eval_count/eval_count). Reasoning models split the
    reply: `thinking` carries the chain, `content` the final answer.

    `num_ctx` MUST be sent. Ollama's 4096 default truncates both the prompt
    and the generation on this corpus, which produced answers grounded in a
    third of the context the verifier scored them against, and empty
    `content` whenever the model was still reasoning at the window edge
    (RecapFlow #16). `done_reason` is returned so that truncation is visible
    in the report rather than inferred from a suspiciously short answer.
    """
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
            "options": {"temperature": temperature, "num_ctx": num_ctx},
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    payload = resp.json()
    message = payload["message"]
    prompt_eval_count = payload.get("prompt_eval_count")
    # `done_reason` only reports how GENERATION ended. A prompt clipped to fit
    # the window can still produce a short reply that terminates normally with
    # done_reason="stop" — and that probe would pass while the verifier scores
    # it against sources the model never received, which is precisely the
    # unsound instrument this change exists to remove. Ollama reports the
    # tokens it actually evaluated, so a count that reaches the window is the
    # clip signal. Measured pre-fix: num_ctx=4096, prompt_eval_count=4098.
    prompt_clipped = (
        prompt_eval_count is not None and prompt_eval_count >= num_ctx
    )
    return {
        "content": message.get("content") or "",
        "thinking": message.get("thinking") or "",
        "done_reason": payload.get("done_reason"),
        "prompt_eval_count": prompt_eval_count,
        "eval_count": payload.get("eval_count"),
        "prompt_clipped": prompt_clipped,
    }


def _context_digest(context: str) -> str:
    """A stable short digest of the rendered context (D26).

    Retrieval returns materially different chunk sets for byte-identical
    queries — measured at two variants sharing 4 of 10 chunks, with
    bit-identical embeddings and one uvicorn worker, so the nondeterminism is
    inside LanceDB hybrid search. mean_target_recall cannot see it: the
    targets are stable, and the variance lives in the non-target chunks that
    make up most of the context. Answer-phase results are not evidence of
    model behaviour without this figure alongside them.
    """
    return hashlib.sha256((context or "").encode("utf-8")).hexdigest()[:16]


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
    # D25 must gate on what the model ACTUALLY SAW. `target_recall` above is
    # computed from the unfiltered server response; render_context then drops
    # everything below --min-score. If that filter removes every chunk from
    # the target session, recall stays positive while the model receives a
    # context without the target — and an honest no-source refusal would then
    # score unhelpful_refusal=False and pass, which is exactly the
    # vacuous-probe behaviour D25 exists to stop.
    #
    # Both figures are kept and they answer different questions:
    #   target_recall       — what RETRIEVAL returned (mean_target_recall)
    #   kept_target_recall  — what reached the MODEL (D25's gate)
    #
    # Latent as of 2026-08-02: 0 of 60 probe-runs diverged at min_score 0.2.
    if targets:
        kept_hit = len(set(targets) & set(result["kept_sessions"]))
        result["kept_target_recall"] = kept_hit / len(targets)
    else:
        result["kept_target_recall"] = None
    # D26: recorded BEFORE the answer phase, so a probe that errors still
    # carries the context it was handed.
    result["context_digest"] = _context_digest(context)
    # The retrieval phase has already succeeded by this point. An answer-phase
    # failure must NOT discard it: main() used to turn the whole probe into
    # {"id", "error"}, which removed an already-computed target_recall from
    # the aggregate denominator and made a retrieval metric move whenever
    # Ollama hiccuped. Block 3 run 1 read mean_target_recall 0.2889 for
    # exactly that reason — two timeouts, six probes in the mean instead of
    # eight. Only the answer phase is marked errored.
    try:
        reply = run_answer(
            args.ollama_url, args.model, args.system_prompt_text, context,
            q["question"], args.temperature, args.num_ctx, args.answer_timeout,
        )
    except Exception as exc:
        result["answer_error"] = str(exc) or exc.__class__.__name__
        return result

    result.update(
        score_answer(q, reply["content"], context,
                     result.get("kept_target_recall"))
    )
    result["thinking_len"] = len(reply["thinking"])
    result["done_reason"] = reply["done_reason"]
    result["prompt_eval_count"] = reply["prompt_eval_count"]
    result["eval_count"] = reply["eval_count"]
    result["prompt_clipped"] = reply["prompt_clipped"]
    # Two independent ways the window can invalidate a probe: generation cut
    # off at the edge (done_reason == "length"), or the prompt clipped before
    # generation even began (prompt_eval_count reaching num_ctx). The second
    # can coexist with a perfectly normal-looking short answer.
    result["truncated"] = (
        reply["done_reason"] == "length" or reply["prompt_clipped"]
    )
    return result


def score_answer(
    q: dict, answer: str, context: str, target_recall: float | None = None
) -> dict:
    """Pure scoring of one answer against the context it was given.

    Split out of evaluate_query (which does network I/O and so could not be
    unit-tested) and returns `context` per D20, so a later change to the
    verifier can be re-scored offline against saved runs instead of
    requiring a re-baseline the deployed stack can no longer produce.
    """
    result: dict = {
        "answer": answer,
        "context": context,
        "expect_refusal": bool(q.get("expect_refusal")),
        # gpt-oss:20b is a reasoning model: Ollama returns `thinking`
        # separately from `content`, and when the model spends its budget
        # reasoning without emitting a final answer, `content` is "".
        # Such a probe trivially satisfies "did not fabricate" and would be
        # scored a clean pass, inflating pass rates. It is a non-result.
        "no_answer": not (answer or "").strip(),
    }
    result["refused"] = looks_like_refusal(answer)
    result["refusal_correct"] = (
        result["refused"] if q.get("expect_refusal") else None
    )
    # D25: a probe that expected an ANSWER and returned a refusal BECAUSE
    # RETRIEVAL FAILED has demonstrated nothing about grounding.
    # phrased-date-with-day refuses in every run because its target session
    # 2026-03-04 exists in historical/ but was never ingested into the corpus
    # manifest (FU-19) — correct model behaviour on a vacuous probe, and it
    # scored as a PASS because it did not fabricate and no refusal was
    # expected. Same defect class the no_answer flag closed.
    #
    # `target_recall == 0.0` is load-bearing, not decoration. Scoping only on
    # "refused and not expect_refusal" was measured against the 2026-08-02
    # block and broke three further probes that have nothing to do with
    # retrieval failure:
    #
    #   codex-production   3/5 — two semantically identical answers, one
    #                            opening "The retrieved transcripts do not
    #                            contain..." (not matched) and one "I don't
    #                            see any..." (matched). Same meaning,
    #                            opposite verdict, decided by phrasing.
    #   unresolved-survey  4/5 — "I don't find any question that was left
    #                            unanswered" is a substantive ANSWER (the
    #                            answer is "none") wearing a refusal keyword.
    #
    # Both declare no target_sessions, so target_recall is None and neither
    # can have suffered a retrieval failure by definition. Without this
    # condition D25 promotes `looks_like_refusal` — a 23-keyword heuristic
    # that is demonstrably both over- and under-inclusive — into the arbiter
    # of the acceptance gate for all ten answer-expecting probes. D24
    # rejected lookaround whack-a-mole and an LLM classifier when nothing
    # depended on the outcome; this keeps it that way.
    # `target_recall` here is evaluate_query's kept_target_recall: what
    # reached the model, not what retrieval returned. See the note at that
    # call site.
    result["unhelpful_refusal"] = bool(
        result["refused"]
        and not q.get("expect_refusal")
        and target_recall == 0.0
    )

    facts = extract_grounding_facts(context)
    if facts is not None:
        verdict = verify_answer_grounding(answer, facts)
        # D23 clause 2: the exemption covers BOTH fabrication inputs. This is
        # the branch that fires whenever the probe retrieves any context at
        # all, and it is where nonexistent-session was still scoring
        # fabricated 5/5 after forbidden_date_hits had been exempted.
        result["unverified_dates"] = _dates_asserted_outside_refusals(
            answer, verdict["unverified_dates"]
        )
        result["unverified_sources"] = verdict["unverified_sources"]
        result["unverified_chunk_ids"] = verdict["unverified_chunk_ids"]
    else:
        # No sources retrieved: only explicit traps are checkable.
        # D23: the exemption MUST cover this list too. score_answer ORs four
        # independent lists into `fabricated`, and on the no-sources path
        # unverified_dates is populated from the same trap call. Verified
        # against the artifacts: block4/block5 run1 both carried
        # forbidden_hits=['2025-12-15'] AND unverified_dates=['2025-12-15'],
        # so suppressing only the former would leave fabricated=True and
        # would NOT produce the unanimous pass D23 promises.
        result["unverified_dates"] = find_forbidden_dates(
            answer, q.get("forbidden_dates"), exempt_refusal_sentences=True
        )
        result["unverified_sources"] = []
        result["unverified_chunk_ids"] = []
    result["forbidden_date_hits"] = find_forbidden_dates(
        answer, q.get("forbidden_dates"), exempt_refusal_sentences=True
    )
    result["fabricated"] = bool(
        result["unverified_dates"]
        or result["unverified_sources"]
        or result["unverified_chunk_ids"]
        or result["forbidden_date_hits"]
    )
    return result


def probe_passed(r: dict) -> bool:
    """A probe passes a run when it did not fabricate and, where a refusal
    was expected, actually refused."""
    if "error" in r or r.get("answer_error"):
        return False
    if r.get("no_answer"):
        return False
    # D25: an honest refusal caused by retrieval failure is not a pass.
    if r.get("unhelpful_refusal"):
        return False
    if r.get("truncated"):
        return False
    if r.get("fabricated"):
        return False
    if r.get("expect_refusal"):
        return bool(r.get("refused"))
    return True


MIN_ACCEPTANCE_RUNS = 5


def summarize_runs(runs: list[list[dict]], answered: bool = True) -> dict:
    """Aggregate N repeated runs of the probe set (D19).

    A probe counts as passing only if it passes in EVERY run. Unanimity, not
    majority: a probe that refuses 3 times in 5 has not been fixed, and
    averaging hides exactly the instability that matters. The 2026-07-25
    eval reported refusal_correctness 0.5 -> 0.0 off a single run; a
    replicate disconfirmed it, with 11 of 12 probes identical and one probe
    flipping at temperature 0.
    """
    per_probe: dict[str, dict] = {}
    for run in runs:
        for r in run:
            e = per_probe.setdefault(
                r["id"],
                {
                    "runs": 0,
                    "passes": 0,
                    "fabricated_count": 0,
                    "refused_count": 0,
                    "no_answer_count": 0,
                    "truncated_count": 0,
                    "error_count": 0,
                    "unhelpful_refusal_count": 0,
                    "context_digests": set(),
                },
            )
            e["runs"] += 1
            if r.get("context_digest"):
                e["context_digests"].add(r["context_digest"])
            if r.get("unhelpful_refusal"):
                e["unhelpful_refusal_count"] += 1
            if probe_passed(r):
                e["passes"] += 1
            if r.get("fabricated"):
                e["fabricated_count"] += 1
            if r.get("refused"):
                e["refused_count"] += 1
            if r.get("no_answer"):
                e["no_answer_count"] += 1
            if r.get("truncated"):
                e["truncated_count"] += 1
            if "error" in r or r.get("answer_error"):
                e["error_count"] += 1
    for e in per_probe.values():
        e["pass_rate"] = (e["passes"] / e["runs"]) if e["runs"] else 0.0
        e["unanimous"] = e["runs"] > 0 and e["passes"] == e["runs"]
        # D26. The count is the reportable figure, and a set is not
        # JSON-encodable — main() writes this structure with json.dumps.
        e["distinct_contexts"] = len(e.pop("context_digests"))

    aggregates: dict = {}
    per_run = [aggregate(run, answered) for run in runs]
    for key in (
        "mean_target_recall",
        "fabrication_rate",
        "refusal_correctness",
        "queries_with_injection",
    ):
        vals = [a[key] for a in per_run if a.get(key) is not None]
        if vals:
            aggregates[key] = {
                "mean": sum(vals) / len(vals),
                "min": min(vals),
                "max": max(vals),
            }
    out = {
        "runs": len(runs),
        "per_probe": per_probe,
        "aggregates": aggregates,
        # D19 sets N >= 5. Fewer runs may still be useful diagnostically, but
        # they are not acceptance evidence and must not present as such.
        "acceptance_eligible": answered and len(runs) >= MIN_ACCEPTANCE_RUNS,
    }
    # Without the answer phase there is no fabricated/refused/no_answer data,
    # so a unanimity verdict would itself be fabricated evidence.
    out["all_unanimous"] = (
        (bool(per_probe) and all(e["unanimous"] for e in per_probe.values()))
        if answered else None
    )
    return out


def aggregate(per_query: list[dict], answered: bool) -> dict:
    # Errored probes carry no metrics; they are counted for unanimity in
    # summarize_runs, but must not enter the numeric aggregates.
    per_query = [r for r in per_query if "error" not in r]
    agg: dict = {"queries": len(per_query)}
    recalls = [
        r["target_recall"] for r in per_query
        if r.get("target_recall") is not None
    ]
    agg["mean_target_recall"] = (sum(recalls) / len(recalls)) if recalls else None
    agg["queries_with_injection"] = sum(
        1 for r in per_query if r.get("injected_counts", 0) > 0
    )
    if answered:
        # A probe that returned nothing — or was cut off at the context
        # window — is not an answer: counting it in the denominator dilutes
        # the fabrication rate with non-results, which is the same inflation
        # the no_answer flag exists to remove.
        answered_qs = [
            r for r in per_query
            if not r.get("refused") and not r.get("no_answer")
            and not r.get("truncated") and not r.get("answer_error")
            and "error" not in r
        ]
        # An empty denominator is NOT a rate of zero. Reporting 0.0 when
        # nothing was measurable makes "every answer was clipped" read
        # identical to "nothing fabricated" — the most reassuring possible
        # rendering of no evidence at all.
        agg["fabrication_rate"] = (
            (sum(1 for r in answered_qs if r.get("fabricated")) / len(answered_qs))
            if answered_qs
            else None
        )
        # Same rule as the fabrication denominator: a truncated fragment that
        # happens to contain a refusal phrase, or an empty answer, has not
        # demonstrated a refusal. Counting them here let a non-result claim
        # success on the metric the harness is least able to afford it on.
        refusal_probes = [
            r for r in per_query
            if r.get("refusal_correct") is not None
            and not r.get("no_answer") and not r.get("truncated")
            and not r.get("answer_error") and "error" not in r
        ]
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

    # Answer-phase settings decide what the numbers below can possibly mean.
    # A pre-fix report carries no num_ctx at all and was produced under
    # Ollama's 4096 default; diffing it against a 32768-window report
    # attributes prompt truncation to the evaluated system. Timeout
    # mismatches do the same thing via errored probes.
    if baseline.get("answer_phase") or current.get("answer_phase"):
        for field, label in (("num_ctx", "num_ctx"),
                             ("answer_timeout", "answer_timeout")):
            b_val, c_val = baseline.get(field), current.get(field)
            if b_val != c_val:
                print(
                    f"  ⚠ WARNING: {label} differs ({b_val} → {c_val}) — "
                    f"answer-phase deltas below are NOT attributable to the "
                    f"evaluated system"
                )
            elif b_val is None:
                print(
                    f"  ⚠ WARNING: {label} not recorded on either side — "
                    f"cannot confirm these reports are comparable"
                )

    b_sum, c_sum = baseline.get("summary"), current.get("summary")
    if b_sum or c_sum:
        # Multi-run reports: the top-level per_query/aggregates hold only the
        # LAST run, so comparing them would discard the spread and unanimity
        # evidence and report deltas between two arbitrary stochastic runs —
        # exactly what D19 exists to prevent.
        print(
            f"  [multi-run] runs={(b_sum or {}).get('runs')} → "
            f"{(c_sum or {}).get('runs')}  "
            f"acceptance_eligible={(b_sum or {}).get('acceptance_eligible')} → "
            f"{(c_sum or {}).get('acceptance_eligible')}"
        )
        print(
            f"  all_unanimous: {(b_sum or {}).get('all_unanimous')} → "
            f"{(c_sum or {}).get('all_unanimous')}"
        )
        for key in ("mean_target_recall", "fabrication_rate",
                    "refusal_correctness", "queries_with_injection"):
            b = (b_sum or {}).get("aggregates", {}).get(key)
            c = (c_sum or {}).get("aggregates", {}).get(key)
            if b is None and c is None:
                continue
            def _f(v):
                if not isinstance(v, dict):
                    return v
                return f"{v['mean']:.4g} [{v['min']:.4g}–{v['max']:.4g}]"
            print(f"  {key}: {_f(b)} → {_f(c)}")
        for pid, e in sorted((c_sum or {}).get("per_probe", {}).items()):
            be = (b_sum or {}).get("per_probe", {}).get(pid, {})
            if be.get("passes") != e.get("passes"):
                print(
                    f"  {pid}: {be.get('passes')}/{be.get('runs')} → "
                    f"{e.get('passes')}/{e.get('runs')} passed"
                )
        return

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
    parser.add_argument(
        "--num-ctx", type=int, default=DEFAULT_NUM_CTX,
        help="Ollama context window for the answer phase. Ollama's own "
             "default (4096) truncates this corpus's rendered context and "
             "produces empty answers (RecapFlow #16); it is recorded in the "
             "report so evidence carries the window it was produced under",
    )
    parser.add_argument(
        "--answer-timeout", type=float, default=DEFAULT_ANSWER_TIMEOUT,
        help="per-probe answer-phase timeout in seconds. A timeout is scored "
             "as an error and breaks unanimity, so this must not be tighter "
             "than the long-reasoning probes need",
    )
    parser.add_argument("--out", type=Path, default=Path("eval-fabrication.json"))
    parser.add_argument("--compare", nargs=2, type=Path, metavar=("BASELINE", "CURRENT"))
    parser.add_argument(
        "--runs", type=int, default=1,
        help="repeat the probe set N times and summarize (D19: acceptance "
             "requires N>=5 with per-probe unanimity; a single run is not "
             "evidence for the answer phase)",
    )
    args = parser.parse_args()

    # A run count below 1 previously executed one run anyway while reporting
    # runs_requested as the invalid value and skipping the summary — output
    # describing a run that never happened.
    if args.runs < 1:
        parser.error(f"--runs must be >= 1 (got {args.runs})")

    if args.compare:
        compare(args.compare[0], args.compare[1])
        return 0

    args.system_prompt_text = args.system_prompt.read_text(encoding="utf-8")
    queries = load_queries(args.queries)

    runs: list[list[dict]] = []
    for run_index in range(max(1, args.runs)):
        if args.runs > 1:
            print(f"[eval] === run {run_index + 1}/{args.runs} ===", file=sys.stderr)
        per_query = []
        for q in queries:
            print(f"[eval] {q['id']} ...", file=sys.stderr)
            try:
                per_query.append(evaluate_query(q, args))
            except Exception as exc:
                print(f"[eval] {q['id']} FAILED: {exc}", file=sys.stderr)
                per_query.append({"id": q["id"], "error": str(exc)})
        runs.append(per_query)

    # Errors are NOT filtered out of the summary: a probe that fails once must
    # break unanimity, and one that fails every time must still appear.
    clean = [[r for r in run if "error" not in r] for run in runs]  # aggregates only
    report = {
        "server": args.server,
        "top_k": args.top_k,
        "answer_phase": bool(args.answer),
        "model": args.model if args.answer else None,
        "temperature": args.temperature if args.answer else None,
        "num_ctx": args.num_ctx if args.answer else None,
        "answer_timeout": args.answer_timeout if args.answer else None,
        "runs_requested": args.runs,
        "per_query": runs[-1],
        "aggregates": aggregate(clean[-1], args.answer),
    }
    if args.runs > 1:
        report["all_runs"] = runs
        report["summary"] = summarize_runs(runs, answered=bool(args.answer))
    args.out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.runs > 1:
        s = report["summary"]
        print(json.dumps(s["aggregates"], indent=2))
        flaky = sorted(
            pid for pid, e in s["per_probe"].items() if not e["unanimous"]
        )
        print(
            f"[eval] runs={s['runs']}  all_unanimous={s['all_unanimous']}  "
            f"acceptance_eligible={s['acceptance_eligible']}"
        )
        # D26: a pass verdict MUST NOT be presented without the stability
        # figure beside it. The verdict can reproduce while the substantive
        # answer does not.
        unstable = sorted(
            (pid, e["distinct_contexts"])
            for pid, e in s["per_probe"].items()
            if e["distinct_contexts"] > 1
        )
        print(
            f"[eval] probes receiving >1 distinct context: "
            f"{len(unstable)}/{len(s['per_probe'])}"
        )
        for pid, n in unstable:
            print(f"[eval]   unstable context: {pid} ({n} distinct)")
        if not s["acceptance_eligible"]:
            reason = (
                "answer phase not run" if not args.answer
                else f"D19 requires >= {MIN_ACCEPTANCE_RUNS} runs"
            )
            print(
                f"[eval] WARNING: NOT acceptance evidence ({reason}).",
                file=sys.stderr,
            )
        for pid in flaky:
            e = s["per_probe"][pid]
            print(f"[eval]   NOT unanimous: {pid} ({e['passes']}/{e['runs']} passed)")
    else:
        print(json.dumps(report["aggregates"], indent=2))
        if args.answer:
            print(
                "[eval] WARNING: single run — per D19 this is NOT acceptance "
                "evidence for the answer phase; use --runs 5 or more.",
                file=sys.stderr,
            )
    print(f"[eval] wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
