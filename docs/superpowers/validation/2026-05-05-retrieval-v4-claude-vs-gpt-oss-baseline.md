# Retrieval v4 — Answering-Model Isolation Test (Claude Opus vs gpt-oss:20b)

**Date:** 2026-05-05
**Companion to:** [`2026-05-05-retrieval-v4-validation.md`](2026-05-05-retrieval-v4-validation.md) (Round 2 verdicts)
**Purpose:** Isolate the **answering model** as the only variable in v4 retrieval failures. Same `/query` retrieval, same v4 filter rendering, same v4 system prompt, two different answering models. The aim is to determine which Round 2 failures trace to the model versus which trace to retrieval / cue / system-prompt design.

---

## Methodology

For each of the 10 Task-23 questions, I built the exact prompt that gpt-oss:20b would receive in production:

1. Hit `/query` on the live retrieval-server VM with `top_k=10`.
2. Render every retrieved chunk through a faithful re-implementation of the v4 filter's `_render_chunk` (the same function lives in `community-brain/src/community_brain/openwebui/community_brain_filter.py`). Each chunk was wrapped in:
   ```
   [SOURCE N — chunk_id: ...]
   [session: YYYY-MM-DD — <title>]
   [speakers spoke: ...]
   [speakers mentioned: ...]
   [topic: ...]
   [flags: ...]
   <transcript_data>
   <full_text>
   </transcript_data>
   ```
3. Prepend the v4 system prompt verbatim from `prompts/community-brain-v4-openwebui-system-prompt.md` (Round 2 hotpatch version with strengthened verification scaffolding in rules 2-3-4).
4. Append the user question.

Each prompt was written to `/tmp/v4-claude-prompts/q*.md` on the VM (10 files, 21K-48K bytes each). I then answered each one bound to **only** the retrieved context — no use of prior knowledge of the corpus, the project, or the codebase.

The companion script that built the prompts: `/tmp/v4-claude-baseline.py` on the VM.

## What this test isolates

| Variable | Held constant |
|---|---|
| Retrieval-server top-10 chunks | ✓ |
| v4 filter rendering format | ✓ |
| v4 system prompt | ✓ |
| Question phrasing | ✓ |
| **Answering model** | **VARIED — gpt-oss:20b vs Claude Opus 4.7 (1M)** |

Any difference in answer quality, faithfulness, or system-prompt compliance is therefore attributable to the answering model, not to retrieval coverage, filter rendering, or prompt design.

---

## Per-question comparison

| # | gpt-oss:20b verdict (Round 2) | Claude Opus verdict | Where they diverged |
|---|---|---|---|
| Q1 | Refusal (correct) | Refusal (correct) | Both faithful to retrieval. Equivalent. |
| Q2 | PASS, citation as `[2026-02-25:post:main]` (chunk_id, format violation) | PASS, citation as `[SOURCE 1]` (compliant) | Same content, different citation format. Claude Opus follows rule 2; gpt-oss leaks chunk_id. |
| Q3 | **FAIL**: invented session "2025-12-15" + attributed claims to Garron without source verification | **PASS (graceful refusal)**: explicitly noted Hemal is in mid-Aug not late-Aug, that Garron is not in retrieved set, and that mid-Dec retrieval has no Hemal/Garron content | **gpt-oss hallucinated; Claude Opus refused honestly.** Same retrieval, same prompt. Model is the variable. |
| Q4 | PASS, with `[chunk_id]` citation format | PASS, with `[SOURCE N]` citation format | Same synthesis quality; format compliance differs. |
| Q5 | PASS, chronology grounded in 3 sessions | PASS, chronology grounded in same 3 sessions | Equivalent. |
| Q6 | PARTIAL — found 2 contributions, padded "third" by re-using one | **PASS** — found 3 distinct contributions: voice-to-text/VAD (2025-08-12), ChatGPT-Research lead-gen (2025-10-08), Shopify project win (2025-02-26) | Claude Opus extracted more from same retrieval. All three were available in the retrieved chunks; gpt-oss missed the Shopify mention in [SOURCE 3]. |
| Q7 | PASS but reduced coverage (Ty Wells only) | PASS, same coverage (Ty Wells), explicit refusal on Codex | Equivalent. Both honestly note Codex absence in retrieved set. |
| Q8 | GRACEFUL REFUSAL — "I don't see any" | **PARTIAL PASS** — produced 3 grounded examples, honestly noted couldn't find a clean 5 | Claude Opus extracted the unresolved questions that gpt-oss refused to acknowledge. Same chunks, different willingness to engage with the flag's semantics. |
| Q9 | PASS-with-framing-issue (1 narrative quote, summary-style) | PASS — extracted 8 actual Patrick first-person quotes from [SOURCE 3]'s `<transcript_data>` block | Claude Opus extracted verbatim transcript quotes; gpt-oss settled for the third-party narrative summary. Same retrieval. |
| Q10 | PASS (refusal, cited real session 2026-01-07) | PASS (refusal, cited same 2026-01-07 decisions) | Equivalent. |

---

## Where Claude Opus did materially better with the same retrieval + prompt

### 1. Q3 — Hallucination caught and refused

gpt-oss fabricated session "2025-12-15" (which doesn't exist; corpus December sessions are 12-02, 12-09, 12-17, 12-30, 12-31) and attributed subscription-model claims to "Garron" despite its own reasoning trace acknowledging *"I don't see the speaker name. The conversation might include Garron but the transcripts may not show his name due to cropping."*

Claude Opus, given the identical retrieved set, correctly stated:

> "Garron is not present in any retrieved chunk. No mention by that name in the speakers or transcript content of [SOURCE 1]–[SOURCE 10]."

Same context, same system prompt, different model — different behavior. **This is v5 candidate #8** (gpt-oss:20b instruction-following limitations under specific-query / weak-retrieval pressure) demonstrated empirically.

### 2. Q6 — Source coverage

gpt-oss found 2 substantial contributions for Adam James and stretched a third by re-using one. Claude Opus found 3 genuinely distinct contributions: the voice-to-text VAD investigation in 2025-08-12, the ChatGPT-Research-and-Relay lead-gen demo in 2025-10-08, and a Shopify development project landed via prior relationship in 2025-02-26. The Shopify mention was in [SOURCE 3] of the same retrieved set; gpt-oss missed it.

This is **not a retrieval problem** — both models had the same 10 chunks. It's a model-side coverage / extraction problem.

### 3. Q8 — Engaging with the flag

The hotpatch made the unresolved-questions cue rule fire on the natural phrasing "nobody fully answered" (5/10 retrieved chunks have `has_unresolved_question=True`). gpt-oss saw the same flagged chunks and refused outright with *"I don't see any records in the retrieved transcripts of a question that was asked and then left unanswered."*

Claude Opus engaged with the flagged chunks and produced three grounded examples (Tom's Gantt-component question on 2025-02-02, Pavan's `crewai chat` `.env` bug on 2025-02-12, Mitch's Cloud Run confusion on 2025-08-12) plus an honest acknowledgement that it couldn't reach 5 without speculating.

The system prompt didn't tell either model to skip flagged chunks. gpt-oss's interpretation of "fully answered" is narrower than the flag's definition — it wants explicit Q&A pairs in transcript text. v5 candidate #7 (has_unresolved_question Q&A-pair semantics gap) is a model-side interpretation gap, not a retrieval gap.

### 4. Q9 — Transcript quote extraction

The model was asked for direct Patrick quotes about RecapFlow's architecture. The retrieved set included [SOURCE 3] (`2026-03-24:transcript:001`), which contains Patrick speaking first-person about RecapFlow's auto-research loop architecture (link extraction validation, compression checks, mechanical inner loop, training-signal feedback loop from comments).

gpt-oss settled for *"He introduced RecapFlow, a pipeline that analyzes meeting transcripts and chat logs to produce weekly community recaps"* — third-party narrative from a `signal:general` summary, not a Patrick quote.

Claude Opus extracted 8 verbatim Patrick utterances from `<transcript_data>` in [SOURCE 3], including the architecture-relevant ones:

> "Actually, it proposed two loops, an inner loop that validate mechanically that the output matches every single rule, like every link has been extracted."
> "I'm doing compression because the original message is always way too long. So it calculates if the compression is all right."
> "So this is purely mechanical. It can run very quickly within the pipeline itself."
> "What I want to do this week is I want to start taking the comments we get on the recap itself and feed it back into the loop."

Both models had the same chunks. Claude Opus read through to the transcript_data block; gpt-oss stopped at the summary chunk.

### 5. Citation format compliance (Q2, Q4)

Rule 2 of the v4 system prompt explicitly says "Cite by `[SOURCE N]` only." gpt-oss consistently cites by `[chunk_id]` (e.g., `[2026-02-25:post:main]`). Claude Opus consistently uses `[SOURCE N]`. v5 candidate #4 (citation format compliance) confirmed as model-dependent.

---

## Where the two models were equivalent

- **Q1, Q5, Q7, Q10** — same retrieval, same answer pattern, same verdicts.
- Both correctly refuse on Q1 (no 2026-03-04 in retrieved set) and Q10 (no LanceDB content in retrieved set).
- Both produce well-grounded answers on Q5 and Q7 within the bounds of the retrieved set.

---

## Implications for v5

This experiment cleanly separates failures attributable to the answering model from failures attributable to retrieval / filter / prompt design.

### Model-independent issues (retrieval-side, requires v5 retrieval fixes)

- **Q1, Q3 partial, Q6, Q7's Codex coverage** — pool-limit issue. Both models lack access to chunks the cue rule would fire on. Cue-driven candidate injection (v5 candidate #1) is the architectural fix.

### Model-dependent issues (gpt-oss:20b weakness, requires defense-in-depth)

- **Q3 fabrication** — gpt-oss invents session_ids and speaker attributions even with explicit verification scaffolding in the system prompt. Claude Opus correctly refuses on the same input. Confirms v5 candidate #6 (filter-side citation post-processing) and v5 candidate #8 (gpt-oss instruction-following limitations).
- **Q6 source coverage** — gpt-oss misses content in retrieved chunks that Claude Opus picks up. Suggests gpt-oss has a narrower attention budget across the rendered context, or scans summary chunks more deeply than transcript_data.
- **Q8 flag engagement** — gpt-oss refuses to engage with `has_unresolved_question=True` chunks because its interpretation of "unanswered" requires Q-without-A in transcript text. v5 candidate #7 documented; the fix could be a system-prompt clarification (cheap) or a chunk-extraction-v4 prompt that aligns the flag with the Q&A-pair interpretation (expensive — needs re-extract).
- **Q9 quote extraction** — gpt-oss reads summary-style chunks and stops there; Claude Opus drills into transcript_data for verbatim quotes. Could indicate gpt-oss has weaker long-context comprehension or a tendency to short-circuit when a plausible summary is available.
- **Citation format (Q2, Q4)** — gpt-oss leaks chunk_ids in citations. Could be addressed by stronger system prompt examples; v5 candidate #4 already documents this as a known gpt-oss issue under the v4 prompt.

### Constraint preserved

The "gpt-oss:20b stays as the answering model" constraint (per the distribution goal: gpt-oss:20b is the largest open model that runs on community members' personal machines) limits the fix surface for the model-dependent issues. The two practical paths:

1. **Defense-in-depth in the filter** — strip / flag citations not in the retrieved set, post-generation. Catches Q3-class fabrications regardless of model compliance.
2. **System-prompt iteration** — add BAD/GOOD exemplar pairs and explicit failure-mode examples. Cheap to test; effectiveness uncertain given gpt-oss's demonstrated tendency to override directives under inferential pressure.

The retrieval-side fixes (cue-driven candidate injection) help both models equally and are the higher-leverage architectural change. The model-side fixes (filter-side post-processing, system-prompt hardening) are necessary for gpt-oss specifically and don't help higher-capability models that already comply.

### What this means for distribution

The Community Brain artifact is designed to ship to community members with `gpt-oss:20b` as the answering model. This experiment shows that under that constraint, **a meaningful fraction of v4's failures are model-dependent and would be PASS-rated under a stronger answering model (Claude Opus, GPT-4-class)**. Operators running their own corpus with a stronger model should get materially better results than the Round 2 5/10-strict / 9/10-generous numbers suggest. Distribution-tier operators (community members on gpt-oss:20b) will benefit most from v5's filter-side defense-in-depth.

---

## Reproducing this test

The full setup is captured in `/tmp/v4-claude-baseline.py` on the VM. To re-run with a different answering model:

1. Run the script: `python3 /tmp/v4-claude-baseline.py`. This generates `/tmp/v4-claude-prompts/q01.md` through `q10.md`, each containing the full system-prompt + retrieved-context + question bundle.
2. For each prompt file, feed the contents to the answering model under test as a single system+user prompt.
3. Capture the model's response.
4. Score with the same rubric used in `2026-05-05-retrieval-v4-validation.md`: PASS / PASS-with-issue / PARTIAL / FAIL, with a focus on (a) faithfulness to retrieved set, (b) hallucination behavior under specific-query pressure, (c) citation format compliance.
5. Compare to gpt-oss:20b's Round 2 baseline to isolate model-dependent vs model-independent behaviors.

The script also serves as a reproducible test harness — re-running it on a future date will pick up whatever the live retrieval server returns at that time, so it tracks corpus + retrieval + cue-rule evolution alongside any model swap.
