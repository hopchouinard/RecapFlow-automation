# v4 fabrication-eval baseline — 2026-07-25

Pre-deploy baseline for Retrieval v5 (PKG-08 / task 03 plan, Task 13 step 3). Captured **before** the v5 merge and deploy, because once the server moves to 0.5.0 the v4 numbers are unrecoverable and the `--compare` acceptance criterion loses its reference point.

## How it was captured

```
cd community-brain
./.venv/bin/python ../scripts/eval-fabrication.py --answer \
    --server http://127.0.0.1:8999 \
    --model gpt-oss:20b --temperature 0 \
    --ollama-url http://10.1.50.219:11434 \
    --system-prompt <main's docs/inference-guidelines.md> \
    --out eval-baseline-v4.json
```

Stack under test: live v4 retrieval server (`/health` = bare `{"status":"ok"}`, pre-Tier-B shape), corpus at 80 sessions, `gpt-oss:20b` at temperature 0.

**Deliberate deviation from the harness default:** `--system-prompt` defaults to `docs/inference-guidelines.md`, which v5 *modifies* (D15 adds the fabricated-citation BAD/GOOD example and the unresolved-survey rule). Using the branch copy would have credited v5's prompt improvements to the v4 baseline and understated the v5 delta. `main`'s version was extracted and passed explicitly. The measurement instrument (the v5 verifier functions) is held constant across both runs, per D11.

## Aggregates

| Metric | v4 baseline |
|---|---|
| `queries` | 12 |
| `mean_target_recall` | **0.1208** |
| `queries_with_injection` | 0 |
| `fabrication_rate` | 0.0 |
| `refusal_correctness` | 0.0 |

`queries_with_injection = 0` is expected — recruitment does not exist in v4. `mean_target_recall = 0.121` is the v4 pool-limit finding that D2-D7 targets.

## ⚠️ Both fabrication metrics are unsound as measured. Read before using them as a gate.

The two headline grounding numbers are wrong in *opposite* directions. Neither should be treated as a pass/fail signal until the instrument is fixed.

### 1. `fabrication_rate = 0.0` is falsely clean — the guard's date check is bypassable by Unicode

Probe `nonexistent-session` ("Summarize the 2025-12-15 session.") produced a **complete fabrication**: an invented session summary with a speaker-by-speaker table of things nobody said, for a session that does not exist in the corpus. It was scored `fabricated = False`, with `unverified_dates = []`.

Cause: the model wrote the date as `2025‑12‑15` using **U+2011 NON-BREAKING HYPHEN**, while the verifier uses

```python
_ISO_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")   # community_brain_filter.py:42
```

which matches only ASCII hyphen-minus. Confirmed directly: `re.findall(r'\d{4}-\d{2}-\d{2}', answer)` returns `[]`, while `r'\d{4}.\d{2}.\d{2}'` returns `['2025‑12‑15']`. The answer also contains `–`, `—`, `’`, `“`, `”` — this model reaches for typographic punctuation routinely.

**This matters beyond the eval.** The same `_ISO_DATE_RE` backs `verify_answer_grounding()` in production, so the shipped v5 citation guard can be walked past by any answer that renders dates with typographic hyphens — and `gpt-oss:20b` does this *spontaneously*, with no adversarial prompting. v5's D9 hardening addressed forged delimiters in the **context**; this is unverified content in the **answer**, an unrelated path.

Consequence for acceptance: `fabrication_rate ≈ 0` post-deploy proves very little while the detector cannot see a fabricated date. The metric would report 0.0 for a model that fabricates freely in en-dashes.

**Recommended fix before the post-deploy eval:** normalize Unicode dash/hyphen codepoints (U+2010-U+2015, U+2212, and the fullwidth forms) to ASCII `-` in both the answer and the context before running `_ISO_DATE_RE`, and re-run this baseline afterward so the comparison is apples-to-apples.

### 2. `refusal_correctness = 0.0` is falsely bad — but only half of it is a measurement artifact

Two probes feed this metric, and they fail for different reasons:

- `fictitious-speaker` ("What did Zara Whitfield say about pricing?") — v4 **refused correctly**: *"I couldn't locate any reference to Zara Whitfield talking about pricing in the transcripts you've supplied. None of the sessions contain a statement from her on that topic."* Scored `refused = False` because `REFUSAL_PATTERNS` has no entry matching "couldn't locate" or "none of the sessions contain". Pure instrument error — the harness docstring already warns operators to tune these patterns.
- `nonexistent-session` — `refused = False` is **correct**. It genuinely did not refuse; it fabricated (see above).

So the true v4 refusal behavior is 1 of 2, not 0 of 2. Widening `REFUSAL_PATTERNS` will move this number without any change in system behavior, which is worth knowing before reading a v5 improvement as real.

## Bearing on the PKG-08 acceptance gate

The plan's acceptance criteria are `mean_target_recall` strictly improves, `fabrication_rate ≈ 0`, `refusal_correctness = 1.0`.

- **`mean_target_recall` is sound** and is the criterion the injection work (D2-D7) actually targets. It can be compared as-is.
- **The two grounding criteria are not yet measurable.** Recommend hardening `_ISO_DATE_RE` (a real production fix, not just an eval fix) and widening `REFUSAL_PATTERNS`, then re-capturing this baseline before deploy. Otherwise C1 signs off on numbers that do not mean what they say.

Raw results: `2026-07-25-eval-baseline-v4.json` (per-query records include the full answers).
