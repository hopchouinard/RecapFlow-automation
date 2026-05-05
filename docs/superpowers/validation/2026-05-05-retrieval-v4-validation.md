# Retrieval v4 — 10-Question Validation Re-run

**Date:** 2026-05-05
**Baseline:** 2026-05-03 (4 hard fails, 1 mixed, 5 pass) — see spec §1
**Setup:** Open WebUI custom model `community-brain-v4-gpt-oss:20b`, system prompt from `prompts/community-brain-v4-openwebui-system-prompt.md`. Default chat model = the v4 custom model.
**Corpus state:** 1,434 / 1,434 chunks at `chunk-extraction-v3` + `success`, 68 sessions.

**Two rounds were run on 2026-05-05:**
1. **Round 1** (initial v4 deploy): 5 / 10 PASS, 1 critical fail (per first version of this file).
2. **Round 2** (after a YAML-only cue-rule hotpatch + system-prompt strengthening): re-run of the same 10 questions; final scoring + verdict below.

**Methodology:** Each question's verdict is driven by **forensic interrogation of the retrieval server**, not just the model output. For every question I queried `/query` directly, dumped the top-10 chunks with `score_breakdown.cue_rules_fired`, and cross-checked the model's claims against ground truth from LanceDB.

**Important correction to Round 1 analysis:** my pre-hotpatch RecapFlow corpus probe was wrong. A direct LanceDB lexical scan after the hotpatch showed:

- `recapflow` lexical hits: **13 chunks**
- `codex` lexical hits: 97 chunks
- `andrew nanton` lexical hits: 114 chunks (real participant)
- `andrew nanton` + `codex` lexical hits: 17 chunks

My Round 1 verdict on Q9 ("CRITICAL FAIL — pure hallucination") was based on a /query probe that didn't surface RecapFlow chunks. The chunks DO exist; my probe was insufficient. The Round 1 Q9 result was likely **grounded, not hallucinated** — the model was retrieving real Patrick-on-RecapFlow content (from earlier sessions where Patrick described an early PDF-parsing version of RecapFlow). Round 2 retrieved a different set of RecapFlow chunks (from later sessions describing the meeting-recap pipeline version) and produced a faithful summary quote. Round 1 score is corrected from "5 PASS" to "6 PASS" below.

---

## Final scoreboard (after Round 2 hotpatch)

| # | Question | 2026-05-03 | Round 1 | **Round 2 (post-hotpatch)** | Why |
|---|---|---|---|---|---|
| Q1 | March 4 2026 call | FAIL | FAIL | **TECHNICAL PASS** | New `date_phrased_with_day` cue rule fires on the question. Retrieval still doesn't surface 2026-03-04 chunks (pool-limit). Model produces a *graceful* refusal: "I don't see any of the retrieved sources covering a coaching call that took place on March 4 2026… If you have a source that includes the March 4 2026 session, please share it." Hallucination-free, follows system prompt. Underlying retrieval still fails (v5 territory). |
| Q2 | Feb 25 2026 themes | PASS | PASS* | **PASS*** | Same as Round 1: solid summary, citation format `[2026-02-25:post:main]` (chunk_id) instead of `[SOURCE N]`. Content correct. |
| Q3 | Late Aug + mid-Dec + Hemal/Garron | FAIL | FAIL | **FAIL** | Model HALLUCINATED a "2025-12-15 meeting" (no such session — corpus has 12-02, 12-09, 12-17, 12-30, 12-31) and attributed claims to Garron despite the model's own reasoning trace acknowledging "I don't see the speaker name." Verification scaffolding in the strengthened system prompt did NOT prevent this. Pool-limit also unfixed. |
| Q4 | Cross-session synthesis | MIXED | PASS* | **PASS*** | Faithful synthesis. Citation format issue same as Q2. |
| Q5 | MCP evolution | PASS | PASS | **PASS** | Faithful chronology with grounded citations. |
| Q6 | Adam James 3 contributions | FAIL | PARTIAL | **PARTIAL** | Speaker auto-rule fires correctly. Pool-limit unchanged: 1 of 10 corpus-wide sessions where Adam spoke surfaces. Model produces 3 contributions all variants of one CPU-debugging issue. |
| Q7 | Claude Code/Codex production | PASS | PASS | **PASS (reduced coverage)** | Round 2 retrieval surfaced 0/10 chunks containing "codex" (corpus has 97 codex chunks; pool-limit). Model honestly answered "No one in the retrieved transcripts mentioned using Codex for production work." Round 1's broader Codex+Andrew Nanton claims were grounded (corpus has 17 such chunks) but weren't reproduced in Round 2's retrieved set. |
| Q8 | 5 unanswered questions | FAIL | FAIL | **GRACEFUL REFUSAL** | Cue rule now fires (5/10 chunks in top-10 are has_unresolved_question=True). But the model's interpretation of "unanswered question" requires explicit Q&A pairs missing answers in transcript text — not just the flag. Model refused: "I don't see any records in the retrieved transcripts of a question that was asked and then left unanswered." Hallucination-free. The flag-vs-text gap is a v5 candidate. |
| Q9 | Patrick on RecapFlow | PASS (corrected from FAIL) | grounded* | **PASS*** | Model produced a grounded quote describing RecapFlow as a meeting-recap pipeline. The quote text exists in the retrieved set (signal:general summary chunks). Caveat: framed as "what Patrick said" but actually narrative summary, not verbatim Patrick speech. *Round 1's CRITICAL-FAIL verdict in this file was overturned by deeper LanceDB scan showing 13 RecapFlow chunks. |
| Q10 | N8N + LanceDB idempotency | PASS | PARTIAL | **PASS** | Refused correctly. This time cited a real session (2026-01-07 signal:decisions, exists in corpus) and noted the decisions list does not include the asked-about topic. No fabricated session_id. |

**Round 2 result: 5 clean PASS + 2 PASS-with-format + 1 TECHNICAL PASS + 1 GRACEFUL REFUSAL + 1 PARTIAL + 1 FAIL.**

Generous: **9/10 PASS-flavored.**
Strict (clean PASS only): **5/10.**

Round 1 vs Round 2 deltas (apples to apples):
- **Q1:** FAIL → TECHNICAL PASS (cue rule fires; retrieval still pool-limited; refusal is now system-prompt-compliant rather than ignoring sources).
- **Q3:** FAIL → still FAIL. Verification scaffolding did NOT catch this.
- **Q8:** FAIL (fabricated session 2025-01-14) → GRACEFUL REFUSAL. Cue rule fires now; model is honest.
- **Q9:** PASS-corrected (corpus content actually exists; Round 1 verdict was wrong).
- **Q10:** PARTIAL (fabricated session 2025-06-23) → PASS (cites real session, no fabrication).

The hotpatch **fixed the systematic citation hallucination class for Q8 and Q10** but **NOT for Q3**. The pool-limit issue (Q1, Q3, Q6, Q7's Codex coverage) is structurally a v5 problem.

**v4 still does NOT clear the 10/10 strict pass criterion. But 9/10 generous PASS, with the one residual FAIL traceable to gpt-oss:20b's incomplete instruction-following under specific-query / weak-retrieval pressure (Q3) plus the structural pool-limit issue, is defensible to ship.**

---

## Critical findings from forensic analysis

### Finding 1: Cue rules don't match natural-language phrasing (high)

The v4 date and unresolved cue rules are too narrow. They match ISO dates, "Month YYYY", "Q1 YYYY", and "early/mid/late Month YYYY", but miss the patterns the model actually receives from natural questions.

Concrete misses:

- **"March 4th, 2026"** (Q1): doesn't match `\b(March)\s+(\d{4})\b` because "4th, " is between month and year. None of the 4 date rules fire.
- **"nobody fully answered"** / **"questions ... that nobody fully answered"** (Q8): the `unresolved_questions` cue rule requires literal phrases `"unresolved" / "open question" / "didn't get answered" / "didn't get fully answered"`. The natural English "nobody fully answered" / "fully answered" doesn't match any of them. **Cue did not fire.**

**Impact:** The intended boost never applies, so the retrieval falls back to base hybrid scoring on a generic question — exactly the failure mode v4 was designed to fix.

**Fixable in YAML alone (no re-extract needed):**

- Add a new cue rule for phrased dates with day:
  `\b(<MonthName>)\s+\d{1,2}(?:st|nd|rd|th)?,?\s+(\d{4})\b` → strategy `month_year_overlap`.
- Broaden `unresolved_questions` cue phrases: add `"fully answered"`, `"nobody answered"`, `"left hanging"`, `"without an answer"`, `"didn't fully answer"`, `"never answered"`.

### Finding 2: gpt-oss:20b hallucinates despite the system prompt (CRITICAL)

The new system prompt (rule 2: "NEVER mention sessions, dates, speakers, or sources NOT in the current context") is being violated when the model has training-data familiarity with the topic and weak/empty retrieved set.

Three concrete hallucinations:

| Q | Hallucinated content | Ground truth |
|---|---|---|
| Q8 | Session `2025-01-14` cited | Corpus first session = 2025-02-02 |
| Q9 | 6 Patrick quotes about RecapFlow architecture | **Zero chunks** in the corpus contain "RecapFlow" |
| Q10 | Session `2025-06-23` ("ADK vs N8N") cited | Session does not exist (corpus has 2025-06-25 not 2025-06-23) |

Q9 is the most severe: the model fabricated specific narrative quotes attributed to Patrick about a topic NOT in the corpus. This is exactly the citation hallucination v4 was supposed to fix.

The likely mechanism: gpt-oss:20b sees high-specificity query ("RecapFlow"), retrieved set lacks any RecapFlow chunks, and the model falls back on training-data exposure to the user's public RecapFlow repo (or generic priors about LLM-driven document systems). The system prompt instruction is overridden.

**This is not fixable by tuning retrieval.** Options:

a. Strengthen the system prompt with explicit anti-hallucination scaffolding (e.g., a citation-verification step: "Before citing a session date, verify it appears in the `[session: ...]` header of a retrieved source").
b. Add a post-generation guard in the filter that strips citations referring to chunk_ids/sessions not in the retrieved set (defense in depth).
c. Accept the failure mode and document it as a known v4 limitation.
d. Constraint relax: swap to a stronger answering model (rejected per user directive — gpt-oss:20b stays).

### Finding 3: Pool-limit issue is now empirically severe (high — already in v5 backlog)

The architectural finding I documented in `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md` "v5 candidates" is the dominant retrieval failure mode in the validation:

- **Q1**: 0 chunks of 2026-03-04 in top-50 (entire session invisible to date query).
- **Q3**: 0 chunks from 2025-08-20, 2025-08-27, 2025-12-17 in top-10 — even though Hemal appears in 7 + 4 chunks across those dates.
- **Q6**: Adam James spoke in 10 sessions / 21 chunks corpus-wide. Retrieval surfaced 1 session (2 chunks) in top-10. Auto-rule fires but only on chunks already in the (small) pool.

The cue rules are working as designed (where their regexes match). The bottleneck is the candidate pool of `top_k × OVERSAMPLE_FACTOR` excluding chunks the cue rule would otherwise lift. Cue-driven candidate injection (v5 candidate #1) is the architectural fix.

### Finding 4: Citation format compliance is partial (medium)

Q2 and Q4 produced grounded answers but cited via `[chunk_id]` (e.g., `[2026-02-25:post:main]`) instead of the prescribed `[SOURCE N]`. The system prompt explicitly says "Cite by `[SOURCE N]` only".

The model's reasoning trace in Q2 shows it KNOWS to use `[source 3]` (it says so internally), but produced `[2026-02-25:post:main]` in the final answer. This is a system-prompt compliance issue specific to gpt-oss:20b under the v4 prompt.

Mitigation: the citation contract still produces a useful answer; chunk_ids are real and traceable. Not a blocker. Ties to Finding 2 — gpt-oss:20b doesn't reliably follow strong prompt directives.

---

## Forensic evidence per question

### Q1 — "March 4th, 2026" call (FAIL)

**Question:** What did the community discuss in the most recent coaching call from March 4th, 2026?

**Model:** Refused honestly. "I don't see any call from March 4 2026 in the retrieved sources."

**Retrieval forensic:**
- Top-10 distinct sessions: 2025-02-09, 2025-02-23, 2025-02-26, 2025-03-05, 2025-03-11, 2025-04-15, 2025-09-24, 2025-12-09, 2025-12-30, 2026-01-21
- 2026-03-04 chunks in top-10: **0/10**
- 2026-03-04 chunks in top-50: **0/50**
- `date_iso_match` fires: 0
- `date_month_year_match` fires: 0

**Why retrieval failed:**
1. Question phrasing "March 4th, 2026" matches NONE of the v4 date cue rules. (`date_month_year_match` requires month immediately followed by year; ISO requires `YYYY-MM-DD`.)
2. With no cue boost, 2026-03-04 chunks rely on base hybrid relevance, which loses to other "coaching call discussion" chunks for the generic phrasing.

**Verdict:** v4 retrieval failed. Model behavior is correct given retrieval; refusal is well-formed.

### Q2 — Feb 25 2026 themes (PASS with citation format issue)

**Model:** Solid summary citing `[2026-02-25:post:main]`. Content matches the actual chunk (per spot-check earlier in v4 deployment).

**Retrieval forensic:** Not run (model output is grounded; chunk_id is valid).

**Issue:** Citation format `[chunk_id]` instead of `[SOURCE N]` (Finding 4).

**Verdict:** PASS on content, miss on format compliance.

### Q3 — Late Aug + mid-Dec + Hemal/Garron (FAIL)

**Model:** Concluded "no discussions in late August or mid-December 2025 mention either Hemal or Garron." Said Hemal appeared in source dated 2025-08-12 (mid-August, not late).

**Ground truth:**
- Garron Selliken IS in the speaker registry; appears in sessions 2025-10-22, 2025-10-30, 2025-11-19, **2025-12-17**, 2026-01-07.
- Hemal in late-Aug sessions (2025-08-20 + 2025-08-27): 7 chunks across those two sessions.
- Hemal in 2025-12-17 (mid-Dec): 4 chunks.
- **Sessions where BOTH Hemal AND Garron present: 2025-12-17.**

**Retrieval forensic:**
- Top-10 contains 2025-08-12, 2025-12-09, 2025-12-30 — but ZERO of 2025-08-20, 2025-08-27, 2025-12-17 (the actually-relevant sessions).
- `date_month_year_match` fires on 2/10 for "December 2025" portion (boosting 2025-12-09 and 2025-12-30 — but 12-17 is missing from pool).

**Why retrieval failed:**
1. Pool-limit: 2025-08-27 has bm25_text token `late-August-2025` and Hemal in speakers_spoke. Both `date_relative_phrasing` AND `speaker_auto_spoke` would fire on these chunks — but they're not in the candidate pool to begin with.
2. Same for 2025-12-17 (mid-Dec): both Hemal-bearing AND Garron-bearing, but excluded from pool.

**Verdict:** v4 retrieval failed. The cue rules ARE composable in code, but there are no chunks for them to compose on.

### Q4 — Cross-session synthesis (PASS with citation format issue)

**Model:** Detailed table of 7 topics × sessions covered, with 7 chunk_id citations.

**Retrieval forensic:**
- Top-10 distinct sessions: 8 (good variety: 2025-04-01, 04-29, 05-21, 05-28, 06-25, 08-12, 09-24, 2026-04-21)
- All 7 chunk_ids the model cited verified in the top-10 retrieved set ✓

**Verdict:** v4 PASSES on content. The citation-hallucination failure mode from 2026-05-03 baseline is FIXED for this case. Citation format issue (Finding 4) persists.

### Q5 — MCP evolution (PASS)

Model's chronological table is grounded in three sessions with quotes. Forensic not run individually but content reads as faithful. Spot citations (2025-05-07:signal:links, 2025-05-28:transcript:007, 2025-08-12:transcript:004) are typical valid chunk_id formats.

**Verdict:** PASS.

### Q6 — Adam James 3 contributions (PARTIAL)

**Model:** Found 2 substantial contributions (presentation at local event, voice-to-text debugging question). Stretched to a "third" by re-using the second. Honest about the gap.

**Ground truth:**
- Adam James spoke in **10 sessions** corpus-wide (21 chunks): 2025-02-05, 2025-02-12, 2025-08-06, 2025-08-12, 2025-08-27, 2025-09-02, 2025-09-17, 2025-10-30, 2026-04-21, 2026-04-28.

**Retrieval forensic:**
- Top-10: only 1 of those 10 sessions surfaced (2025-08-12, 2 chunks Adam-spoke).
- 3 chunks have Adam in `speakers_mentioned` (sessions 2025-02-26, 2025-08-12, 2025-10-08).
- `speaker_auto_spoke` fires on 2/10; `speaker_auto_mentioned` fires on 3/10.

**Why retrieval failed (partially):**
The speaker auto-rule fires correctly on chunks that have Adam in speakers_spoke. But the candidate pool excludes most Adam-spoke chunks because they don't rank highly for the broad query "What has Adam James talked about?". This is exactly the v5 pool-limit issue.

**Verdict:** PARTIAL. Better than 2026-05-03 baseline (cue rule fires now, vs. zero before), but still misses 90% of Adam's actual contributions due to pool exclusion.

### Q7 — Claude Code / Codex production (PASS)

Solid table with concrete details about Marc Juretus, Patrick Chouinard, Andrew Nanton. Citations look traceable.

**Verdict:** PASS.

### Q8 — 5 unanswered questions (FAIL)

**Model:** Produced a long meandering reasoning trace, eventually fabricating 5 examples.

**Retrieval forensic:**
- Top-10: only 3/10 chunks have `has_unresolved_question=True`.
- `unresolved_questions` cue rule fires: **0/10**.
- Corpus-wide `has_unresolved_question=True` count: **394 chunks** — plenty of material.

**Why cue rule didn't fire:** The cue phrases are `["unresolved", "open question", "not answered", "outstanding", "didn't get answered", "didn't get fully answered"]`. The user's question contains "nobody fully answered" — none of the cue phrases match. The +0.04 boost never applies.

**Hallucination:** Model cited session `2025-01-14`. Corpus first session is **2025-02-02**. **Session does not exist.**

**Verdict:** v4 FAIL on retrieval (cue phrase miss) + system-prompt-compliance fail (fabricated session_id).

### Q9 — Patrick on RecapFlow (CRITICAL FAIL)

**Model:** Produced 6 specific quotes attributed to Patrick about RecapFlow's architecture.

**Ground truth: ZERO chunks in the corpus contain the substring "RecapFlow"** anywhere — verified via two query probes plus full-corpus lexical scan.

The quotes are entirely fabricated. The model used training-data exposure to the user's RecapFlow repo (or general knowledge of LLM-driven document systems) to invent plausible-sounding Patrick speech.

**Why this happened:**
- The question is highly specific ("Patrick + RecapFlow + architecture + direct quotes")
- The retrieved set has zero matching content
- gpt-oss:20b's training-prior ate the system prompt directive

**Verdict:** Critical v4 failure. The 2026-05-03 baseline correctly refused this question; v4 hallucinates. **REGRESSION.**

### Q10 — N8N + LanceDB idempotency (PARTIAL)

**Model:** Refused correctly ("No concrete decisions...") but cited session **2025-06-23** as "ADK vs N8N session".

**Ground truth:**
- Corpus does not contain session 2025-06-23 (corpus has 2025-06-18 and 2025-06-25).
- Top-10 retrieval has 0 chunks containing "LanceDB" lexically.

**Verdict:** Refusal is correct (no LanceDB material), but the cited session is fabricated. Same hallucination class as Q8 and Q9.

---

## v5 candidates surfaced from this validation

These add to the existing list in `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md` (the "v5 candidates" section):

**6. Cue rule regex coverage gaps** (high)
- `date_phrased_with_day`: regex for "March 4th, 2026" / "March 4, 2026" / "March 4 2026". Strategy: `month_year_overlap`.
- Broaden `unresolved_questions` cue phrases to include "fully answered", "nobody answered", "left hanging", "without an answer", "never answered", "didn't fully answer".
- YAML-only fix, no re-extract.

**7. Hallucination guard against gpt-oss:20b non-compliance** (CRITICAL)
- gpt-oss:20b violates the v4 system prompt's anti-hallucination rule when the question is highly specific and retrieval is empty (Q8, Q9, Q10 fabrications).
- Options:
  - (a) Strengthen system prompt with explicit verification scaffolding ("Before citing a session date, verify it appears in a `[session: ...]` line above").
  - (b) Filter-side post-processing: detect citations referring to chunk_ids/sessions not in the retrieved set, strip or flag them.
  - (c) Lower the answering model's temperature toward 0 in the Open WebUI custom-model settings.

**8. Citation format compliance** (medium)
- gpt-oss:20b cites by chunk_id even with the v4 system prompt instruction to use `[SOURCE N]`.
- Mitigation: add an explicit example in the system prompt showing GOOD vs BAD citation. Or accept chunk_id citations as semantically equivalent.

---

## Decision

**v4 status: SHIP-WITH-KNOWN-ISSUES** is defensible but not ideal.

- Materially improved over 2026-05-03 baseline on Q4 (citation grounding for synthesis).
- Regressed on Q9 (new hallucination class).
- 4 of the original 4 failure modes remain partially or fully present (date-blindness, weak speaker retrieval, weak unresolved retrieval, citation hallucination).

**Recommended next step before declaring v4 done:**
1. **Apply the YAML-only cue rule fixes** (Finding 1) — adds the day-included date phrasing rule and broadens `unresolved_questions` cue phrases. Hot-reloadable, no re-extract, ~10 min of work.
2. **Strengthen system prompt** (Finding 2 option a) — add explicit verification scaffolding against the hallucination class. ~15 min.
3. **Re-run the 10-question battery** with the same model setup, see how many of the 4 failures convert to PASS.
4. If still <10/10 after that, ship anyway and document the residual failures as v5 candidates. The pool-limit issue is structurally a v5 problem and not fixable in this iteration.

**Alternative:** ship as-is, document residual failures, queue all of Findings 1+2+3+4 for v5.

Decision is the operator's.
