# Community Brain — Next Steps Handoff

**Snapshot date:** 2026-05-05
**Purpose:** Single entry-point document for a fresh session that needs to pick up the Community Brain project. Reads in 3 minutes, tells you exactly what's done, what's outstanding, where the canonical artifacts live, and how to start each remaining track.

---

## Where the project is right now

### Plan A — Retrieval server (DONE, deployed)

The Community Brain retrieval server is live on the n8n VM at `http://10.1.30.10:8999` (LAN-reachable). 37-field LanceDB v1.0 schema, trust-partitioned `/query` response, all 252+ unit tests passing on `main`. 8 sessions ingested.

Canonical references:
- Spec: [`docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md`](specs/2026-04-18-community-brain-ingestion-pipeline-design.md)
- Plan: [`docs/superpowers/plans/2026-04-18-community-brain-ingestion-plan-a.md`](plans/2026-04-18-community-brain-ingestion-plan-a.md)

### Plan B — n8n ingestion integration (DONE)

Two workflows wired into the retrieval server:
- **Workflow 1** (Merged Call Summarizer, n8n id 5): live weekly with prep-prompt + `/ingest` POST appended.
- **Workflow 2** (Transcript-Only Summarizer, n8n id 6): backfill workflow for historical corpus.

State after this session:
- 8 sessions in LanceDB (~167 chunks): 6 consecutive Feb 2025 + `2026-04-14` + `2026-04-21`
- `~/n8n/n8n-state/backfill-state.json` has 6 real `completed` entries
- Operator-tuned model mix: Sonnet 4.6 for Prep + Signal, Kimi K2.5 for Community Post; Gemma 4 31b for Stage B/C inside `/ingest`
- All `/ingest` and Chat Model timeouts at 30 min

Canonical references:
- Spec: [`docs/superpowers/specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md`](specs/2026-04-19-plan-b-n8n-ingestion-integration-design.md)
- Plan: [`docs/superpowers/plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md`](plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md)

### Phase 6 — Open WebUI validation (PARTIAL — 8-session corpus)

Validated the 5 query types from Plan A spec §10 against the 8-session subset. 3 query types pass cleanly (evolution, relationships, unresolved-questions when chunks reach the model). 2 query types had retrieval-layer caveats (Findings 6 and 7) — both addressed in Hybrid Retrieval v2 below.

All findings are captured in [Plan A spec §10 Phase 6 Validation findings](specs/2026-04-18-community-brain-ingestion-pipeline-design.md#phase-6--open-webui-integration-and-validation). Findings 6 and 7 cross-reference the v2 spec.

### Hybrid Retrieval v2 — DONE and DEPLOYED

Replaces pure-vector ranking with hybrid (vector + BM25 RRF, k=60) plus cue-driven metadata-aware boosting. Oversamples top_k by 3× internally; applies additive RRF-score deltas when question-side lexical cues align with chunks' structured-metadata flags. Public `similarity` field continues to expose vector cosine (spec-faithful). Vector-only path retained as internal graceful-degradation fallback only — no `mode` parameter, no parallel endpoint, legacy v0 helpers and `_v2` suffix archaeology removed.

302 tests passing. Server `0.2.0` deployed to live VM on 2026-04-28. Open WebUI filter and n8n workflows continue to work without change.

Live-VM validation outcomes (full addendum in Plan A spec §10):
- **Finding 6 (entity-grounded retrieval):** v1 0/10 → v2 6/10 chunks containing the target entity in `full_text`. PASS.
- **Finding 7 (metadata-tagged retrieval):** v1 1/10 → v2 6/10 chunks tagged `has_unresolved_question=True`. PASS at retrieval layer.
- **Finding 8 (NEW, surfaced by v2 validation):** Answering LLM under-utilizes Stage C metadata flags because the trust contract correctly tells it to re-derive. Pre-v2 invisible (retrieval was the bottleneck). v3 candidate; not a v2 regression.

Canonical references:
- Spec: [`docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`](specs/2026-04-27-hybrid-retrieval-v2-design.md)
- Plan: [`docs/superpowers/plans/2026-04-27-hybrid-retrieval-v2-plan.md`](plans/2026-04-27-hybrid-retrieval-v2-plan.md)
- CHANGELOG entry: [`docs/migrations/CHANGELOG.md`](../../docs/migrations/CHANGELOG.md) (2026-04-28 — Hybrid Retrieval v2)
- Validation addendum: Plan A spec §10, "v2 hybrid retrieval validation (2026-04-28 — against live VM)"

### Ingest / Lint Decoupling — DONE and DEPLOYED (2026-05-02)

Discovered during Plan C re-attempt: `lint_corpus_chunks` was doing one `table.update()` per chunk in the entire corpus on every `/ingest`, ~95% as no-op timestamp bumps. At ~1500 chunks this saturated LanceDB's manifest writer and surfaced as "Too many concurrent writers" retry storms. `/ingest` calls began exceeding n8n's 30-min HTTP timeout (observed on `2025-12-09` — chunks committed, but the response never came back).

Fix: two coordinated changes plus one operational change.
- **Change A:** drop the no-op timestamp-bump branches in `lint_corpus_chunks`. Function writes only when marker state actually changes.
- **Change E:** remove the `lint_corpus_chunks` call from `_post_commit_maintenance`. `/ingest`'s post-commit work is now just `verify_corpus_v3_state`.
- **Change F (operational):** lint runs via daily cron at 04:00 UTC (`/etc/cron.d/community-brain-lint`) instead of inline after every `/ingest`.

Behavior change (deliberate): `corpus_markers_computed_at` now records "last meaningful marker change," not "last lint pass." No schema migration required.

471 tests passing. Deployed to live VM on 2026-05-02. Cron installed via `scripts/cron/install-cron.sh`. State file fix: `2025-12-09` moved from `failed[]` → `completed[]` (it actually succeeded; the timeout was on the lint, not the commit).

Canonical references:
- Spec: [`docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md`](specs/2026-05-02-ingest-lint-decoupling-design.md)
- Plan: [`docs/superpowers/plans/2026-05-02-ingest-lint-decoupling-plan.md`](plans/2026-05-02-ingest-lint-decoupling-plan.md)
- CHANGELOG entry: [`docs/migrations/CHANGELOG.md`](../../docs/migrations/CHANGELOG.md) (2026-05-02)

### Hybrid Retrieval v3 + Stage C v2 — DONE and DEPLOYED

Schema bumped to v1.1 (38 fields; synthesized `bm25_text` FTS column). Stage C extraction prompt updated to chunk-extraction-v2. All 9 sessions re-extracted under the new prompt. Speaker-aliases.yaml curated (39 canonicals, 49 alias entries). Canonicalization applied at chunk write. `recurrent` corpus marker populated via `lint_corpus` (157/184 chunks). `score_breakdown` + `metadata_summary` on every `/query` response. `[flags:]` and `[corpus summary:]` presentation tags structurally separated from transcript content. F8 partial fix: filter now renders the structured presentation tags so the answering LLM sees them.

466 tests passing. Server `0.3.0` deployed to live VM on 2026-04-30. Track B (Plan C) is now unblocked.

Validation gate outcomes (full addendum in Plan A spec §10 "v3 retrieval + Stage C v2 validation"):
- **16.1.3 (canonicalization):** 10/10. PASS.
- **16.1.4 (recurrent marker):** 157/184 (85.3%). PASS.
- **16.1.5 (score_breakdown):** all chunks have all 5 sub-fields. PASS.
- **16.1.7 (test suite):** 466 pass, 0 fail. PASS.
- **16.1.8 F6 (Adam in full_text regression):** 5/10. PASS.
- **16.1.2 (Adam in entities, top-10):** 4/10. Soft miss (off by 1); v4 candidate.
- **16.1.8 F7 (has_unresolved_question, top-10):** 4/10. Soft miss (off by 1); v4 candidate.
- **16.1.1 + 16.1.6:** pending manual Open WebUI operator check.

Canonical references:
- Spec: [`docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md`](specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md)
- Plan: [`docs/superpowers/plans/2026-04-29-retrieval-v3-and-stage-c-v2-plan.md`](plans/2026-04-29-retrieval-v3-and-stage-c-v2-plan.md)
- Validation addendum: Plan A spec §10, "v3 retrieval + Stage C v2 validation (2026-04-30 — against live VM)"

### Retrieval v4 — Quality Improvements — DONE and DEPLOYED (2026-05-05)

Surfaced via 2026-05-03 10-question test battery against `gpt-oss:20b` in Open WebUI. 4 hard-fails clustered on date-blindness, weak speaker retrieval, weak `has_unresolved_question` retrieval, and citation hallucination. v4 addresses all four with a five-layer change set, with `gpt-oss:20b` preserved as the answering model per the distribution constraint.

- **Layer 1 (data, +9 tokens/chunk):** `bm25_text` Level-3 date variants (ISO date, year-month, month name, month-year, phrased form, `Q1-Q4`, `H1`/`H2`, `early/mid/late`-prefixed month-year). `chunk-extraction-v3` prompt: more permissive `has_unresolved_question` criterion (defaults to `true` when in doubt; flags partial answers, deferred answers, and unresolved-on-pivot).
- **Layer 2 (retrieval, hot-reload):** 4 date-aware cue rules (`date_iso_match`, `date_month_year_match`, `date_phrased_with_day` added in hotpatch, `date_relative_phrasing`, `date_quarter_match`). Speaker auto-rule synthesized at server startup from `speaker-aliases.yaml`, longest-first alternation, casefold-normalized for case-insensitive matching. `unresolved_questions` cue delta bumped from 0.010 → 0.040 with broadened cue phrases ("nobody fully answered", "left hanging", "without an answer", etc.).
- **Layer 3 (filter):** new metadata block above `<transcript_data>` — `[SOURCE N — chunk_id: ...]`, `[session: YYYY-MM-DD — title]`, `[speakers spoke: ...]`, `[speakers mentioned: ...]`, `[topic: ...]`. Filter no longer prepends `inference-guidelines.md` content.
- **Layer 4 (system prompt):** `docs/inference-guidelines.md` refactored to V1 system prompt (~440 words) with explicit verification scaffolding (rules 2-3-4: literal source verification before citation, anti-hallucination directive against training-data familiarity). Deployed manually as Open WebUI custom model `community-brain-v4-gpt-oss:20b`. Operator paste artifact at `prompts/community-brain-v4-openwebui-system-prompt.md`.
- **Layer 5 (tooling):** `scripts/reextract-all-sessions.py` orchestrates corpus re-extract with SMOKE / BULK / REPORT phases.

Corpus state after Plan-G deployment: **1,434 / 1,434 chunks at `chunk-extraction-v3` + `success`**, 68 sessions. `has_unresolved_question` corpus-wide tagged count: **394** (target ≥35; v1 was 39, v3 was 20). entities/chunk avg: 12.55. Cost of full re-extract: **$0.751** in Gemma calls (4× cheaper than the plan's $3 estimate).

512 tests passing. Server `0.4.0` deployed to live VM on 2026-05-05.

10-question validation outcomes (Round 2, after a YAML-only cue-rule + system-prompt hotpatch on 2026-05-05; full forensic in [`docs/superpowers/validation/2026-05-05-retrieval-v4-validation.md`](validation/2026-05-05-retrieval-v4-validation.md)):

- 5 clean PASS + 2 PASS-with-citation-format + 1 TECHNICAL PASS + 1 GRACEFUL REFUSAL + 1 PARTIAL + 1 FAIL.
- Generous: **9/10 PASS-flavored**. Strict: **5/10 clean PASS**.
- Q3 still hallucinates ("2025-12-15 meeting" — session doesn't exist; subscription model attributed to Garron without source verification). System-prompt verification scaffolding insufficient against `gpt-oss:20b`'s inferential narrative tendency under specific-query / weak-retrieval pressure. Queued as v5 candidate.
- Pool-limit issue (Q1, Q3, Q6 partial coverage; Q7's Codex coverage absent despite 97 chunks corpus-wide containing "codex") is a structural retrieval architecture concern. Queued as v5 candidate.

Canonical references:
- Spec: [`docs/superpowers/specs/2026-05-03-retrieval-v4-quality-improvements-design.md`](specs/2026-05-03-retrieval-v4-quality-improvements-design.md)
- Plan: [`docs/superpowers/plans/2026-05-03-retrieval-v4-quality-improvements-plan.md`](plans/2026-05-03-retrieval-v4-quality-improvements-plan.md)
- CHANGELOG: [`docs/migrations/CHANGELOG.md`](../../docs/migrations/CHANGELOG.md) (2026-05-03)
- Validation: [`docs/superpowers/validation/2026-05-05-retrieval-v4-validation.md`](validation/2026-05-05-retrieval-v4-validation.md)

---

## One outstanding track

### Track B — Plan C: Full historical backfill (UNBLOCKED — ready to run)

Run Workflow 2 across the remaining ~57 of 65 historical sessions. Total cost ~$3, total wall time ~12 hours.

**Status (2026-04-30):** v3 is deployed and validated. Track B is now unblocked. The 9 sessions already in LanceDB are under v1.1 schema with chunk-extraction-v2. Running the full backfill now means all sessions land cleanly under the same extraction contract.

**No formal plan document exists** because the operational steps already live in Plan B Tasks 11–15 (the workflow itself). Only thing missing is the "kick off the full run" trigger and post-run state cleanup.

#### Starter prompt for Track B (paste into new session, when ready to run)

```
I'm continuing the Community Brain project. Plan A, Plan B,
Hybrid Retrieval v2, and Hybrid Retrieval v3 + Stage C v2 are
all complete and deployed. Track B (Plan C full backfill) is
now unblocked.

Read /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md
first for current status.

The work for this session: execute Plan C — full historical backfill.
The retrieval server is deployed at http://10.1.30.10:8999 running
v0.3.0 (v1.1 schema, chunk-extraction-v2). 9 of 65 historical
sessions are already ingested (verify via /sessions). The remaining
~56 are pre-staged at ~/n8n/historical/ on the VM. Workflow 2
(n8n id 6) handles the per-session pipeline. State tracked in
~/n8n/n8n-state/backfill-state.json.

Steps:
1. Pre-flight: verify retrieval server health, Ollama
   nomic-embed-text pinned, Workflow 2 in good state in n8n UI.
2. Trigger Workflow 2 to run all remaining sessions (~12 hr wall).
3. Post-run: review state file's failed[] entries, decide retry
   vs accept, clean up any partial output dirs, update CLAUDE.md
   "Current status" to mark Plan C complete.

Reference docs (read in this order):
- docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md (this handoff)
- docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md §10 Phase 5
- docs/superpowers/plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md Tasks 11-15 (workflow internals)

Don't introduce new spec or plan documents — Plan C is execution-only.
```

**Notes:**
- If 429 rate-limit cascades become a problem during the run, the workflow's per-session retry + state file design tolerates partial failure cleanly. Failed entries stay in `failed[]` and re-run on next invocation.
- All sessions will ingest under v1.1 schema + chunk-extraction-v2, consistent with the 9 already-ingested sessions.

### v4 design (when warranted)

v3 shipped on 2026-04-30 with three soft-misses on retrieval-side validation criteria, all tracing to the same root cause: Stage C v2 + Gemma 4 31B is more conservative than v1 was on entity-of-speakers and `has_unresolved_question` extraction. Corpus state is excellent (entities populated, canonicalization clean, recurrent + score_breakdown working); retrieval-side edge cases fall slightly short of spec targets.

**Two validation-driven v4 candidates (high priority):**

1. **entities-in-top-10 (closes 16.1.2):** deterministic post-Stage-C step that always merges `speakers_spoke` + `speakers_mentioned` into `entities`. Prevents the case where a speaker appears in `full_text` and `speakers_spoke` but not `entities`, causing a miss on entity-grounded queries. **Code change only — no re-extract required.** Implementable as a `recanonicalize`-style pass that updates `entities` from existing fields.
2. **`has_unresolved_question` sensitivity (closes 16.1.8 F7 + 16.1.1):** prompt tuning to lift the flag's detection sensitivity. Corpus-wide tagged count dropped 39 (v1) → 20 (v3) on the same model with a different prompt. Direction: more permissive trigger in `chunk-extraction-v3` prompt. **Stage C prompt change — full re-extract required.** This is the main candidate that affects Plan C re-ingest risk.

**Other v4 candidates from `2026-04-29-retrieval-v3-and-stage-c-v2-design.md` §19:**

- LLM intent classifier (pre-retrieval LLM call → structured filter dict + ranking weights). Speculative.
- Cross-encoder reranker (`bge-reranker-large` or similar over top-30 hybrid candidates). Only motivate if hybrid + bm25_text + cue boost still misses.
- Weighted-sum fusion (alternative to RRF). Anti-feature without calibration story.
- Entity-canonicalization registry for non-people entities (companies, products, frameworks).
- Synthesized BM25 field iteration if entity coverage stays weak.
- Additional `corpus_derived_markers` types (`cross_session_thread`, `unresolved_followup`, etc.). New lint pass; no re-extract.
- Metadata summary array counts (extend with `decisions_count`, `action_items_count`).
- Multi-writer registry support (flock).
- Read/write API key split.
- Deep `/health` endpoint (config presence, LanceDB readability, Ollama reachability).

**Operational invariants v4 MUST NOT break** (surfaced through 19 rounds of v3 adversarial review):

- Trust partition (`ground_truth` / `derived_metadata` / `provenance`) structure
- `verify_corpus_v3_state` fail-closed semantics on startup, post-commit, and `/query`
- `lint_corpus` auto-trigger is additive-only (UPDATE); destructive cleanup only behind `--rebuild`
- Speaker partition (`speakers_mentioned` excludes `speakers_spoke`) enforced post-canonicalization in BOTH `pipeline.py` and `recanonicalize.py`
- Filter trusted tags (`[flags:]`, `[corpus summary:]`, `[score:]`) structurally separated from `<transcript_data>` (format-injection defense)
- Cue rules YAML loader: never silently use stale cached rules when current load returns valid-but-empty (Appendix C accepted-by-design)

### v5 candidates (surfaced during v4 deployment)

These do NOT block v4. They're observations from the 2026-05-04 SMOKE + sentinel validation pass on Track A and the Codex adversarial review.

**1. Cue-driven candidate injection (high priority — pool-limit finding)**

v4 cue boosts are **additive within the candidate pool** of `top_k × OVERSAMPLE_FACTOR` (default 30) — they re-rank, they don't recruit. Concrete observation from the 2026-05-04 sentinel validation: querying "What was discussed in late December 2025?" returned zero `2025-12-30` chunks in the top-50 even though `date_relative_phrasing` AND `date_month_year_match` would both fire on that session's chunks (combined +0.08 boost waiting). The session's base hybrid RRF was too low to crack the 150-candidate pool, so the boost never saw it.

Speaker queries don't suffer this because frequent speakers have many high-base-relevance chunks already in the pool. Date queries against quiet/short sessions (10 chunks for 2025-12-30) suffer it most.

**Direction:** add a "cue-driven candidate injection" pass to `query_local.search_chunks` BEFORE the cue boost step. For each cue rule that fires, also pull a small slice of top-N chunks (e.g., 5-10) ranked purely by that rule's strategy (not the base hybrid), and merge them into the candidate pool. Then apply the boost as today. Scope: code-only, no schema/data change, no re-extract. v3 already has the OVERSAMPLE_FACTOR=3 architecture as the single tunable; this would add a parallel cue-driven injection alongside it.

**Why not just raise OVERSAMPLE_FACTOR:** wasteful (most queries don't need 300 candidates) and still doesn't help the pathological case where a session has uniformly weak base relevance to a date-only query.

**2. Speaker auto-rule resilience asymmetry (medium)**

`load_cue_rules_from_yaml` has a per-path `_LAST_GOOD_RULES` cache that returns the last-known-good rules during a transient YAML edit window. `build_speaker_auto_rule` does NOT — if `speaker-aliases.yaml` is in a partial-write state during `/query`, the speaker auto-rule silently degrades to the never-match `(?!x)x` sentinels for that one request. The boost is additive so the request still returns; but for ~ms windows during a registry edit, speaker queries lose their boost without any signal in the response.

**Direction:** mirror the YAML loader's last-known-good cache pattern in `build_speaker_auto_rule`. One dict keyed by path, populated on successful load, returned on parse error. Code-only.

**3. has_unresolved_question prompt over-permissive guard (medium)**

The chunk-extraction-v3 prompt is more permissive than v2 ("default to true when in doubt"). The 2026-05-04 SMOKE phase showed unresolved-rate increases of 0.15→0.30, 0.00→0.10, 0.06→0.25 on the 3 sentinels — healthy. But a prompt change at this scale can drift in the opposite direction over time as the model learns. Add a corpus-wide alarm in `lint_corpus` that flags if `has_unresolved_question_rate` exceeds e.g. 50% across the corpus (over-triggering) so we catch a subsequent prompt regression before it skews retrieval.

**4. /query top_k vs pool-limit documentation (low)**

The pool-limit finding above is non-obvious to operators. Document in `community-brain/CLAUDE.md` that cue boosts are pool-limited and that operator-facing tuning options are: raise `top_k`, raise `OVERSAMPLE_FACTOR`, or wait for v5's cue-driven injection. Until v5 ships, the workaround is to raise `top_k` to 30+ for date-query-heavy use cases.

**5. Codex adversarial review surfaced in v4 (already fixed, kept here as v5 watch-items)**

These were caught and fixed in v4 commit `91c3cb1` but are worth keeping in mind for v5 testing:

- Case-sensitive cue lookup (speaker resolver + token_overlap) — fixed via casefold normalization. v5 should add property-based tests covering case permutations across rule types.
- Filter runtime prompt vs system-prompt citation contract conflict — fixed by aligning filter on `[SOURCE N]`. v5 should add a parity test asserting the filter and `docs/inference-guidelines.md` don't carry contradicting citation directives.

### v5 candidates added from v4 Round-2 validation (2026-05-05)

The 10-question Round 2 validation against the live v4 deploy (after the YAML+system-prompt hotpatch) surfaced three additional candidates:

**6. Filter-side citation post-processing (high — Q3 hallucination class)**

Round 2 Q3 demonstrated that even with explicit verification scaffolding in the system prompt ("Before naming any session date, verify it appears literally in one of those headers"), `gpt-oss:20b` still fabricated session "2025-12-15" and attributed claims to "Garron" without speaker verification. The model's own reasoning trace acknowledged "I don't see the speaker name" yet committed to the attribution in the final answer. System-prompt scaffolding alone cannot guarantee `gpt-oss:20b` compliance under specific-query / weak-retrieval pressure.

**Direction:** defense-in-depth in the Open WebUI filter. After the model produces an answer, post-process to:

- Strip or flag any `[SOURCE N]` / `[chunk_id]` references whose values don't appear in the headers of the retrieved set.
- Strip or flag any session-date strings (regex: `\b\d{4}-\d{2}-\d{2}\b`) not present in the `[session: ...]` lines of the retrieved set.

This catches Q3-style fabrications regardless of how well the model follows the prompt. Implementation: add a post-render guard in `community_brain_filter.py:Filter.outlet` (or wherever the filter receives the model's response). Code-only, no schema or data change.

**7. has_unresolved_question Q&A-pair semantics gap (medium)**

Round 2 Q8 showed that `unresolved_questions` cue rule fires correctly post-hotpatch (5/10 retrieved chunks tagged True), but `gpt-oss:20b` refused to enumerate examples. Reasoning: the model's interpretation of "questions nobody fully answered" is "explicit Q&A pairs in the transcript where the answer is missing." But the `has_unresolved_question` flag captures a broader semantics ("a question raised that doesn't get a clear, definitive answer in the same chunk", per chunk-extraction-v3.md) — which includes deferred answers, pivots, and partial responses.

When the model verifies in transcript text it only finds answers that look complete enough; it doesn't trust the flag.

**Direction (one of):**
- (a) Tighten the chunk-extraction-v3 prompt's `has_unresolved_question` definition to align with the Q&A-pair-missing-answer interpretation. Requires a corpus re-extract.
- (b) Add a sentence to the system prompt clarifying that flagged-unresolved chunks indicate Q's the chunk didn't fully resolve, and the LLM can trust the flag for surveying purposes (skip transcript re-verification for this specific case).
- (c) Document the gap and accept that "list 5 unanswered questions" will return a refusal even when retrieval is correct.

**8. gpt-oss:20b instruction-following limitations (high — affects v4's hallucination guarantees)**

Round 2 Q3 confirmed that strong system-prompt directives are not reliably followed by `gpt-oss:20b` when the question is highly specific and retrieval is weak. The constraint "gpt-oss:20b stays as the answering model" (per distribution goal) limits the fix surface. Options:

- (a) Filter-side post-processing (candidate #6 above) — most direct.
- (b) Lower the model's `temperature` to 0 in the Open WebUI custom model — reduces the model's tendency to "fill gaps" with plausible-sounding content. Not yet tried.
- (c) Add explicit failure-mode examples in the system prompt ("BAD: 'Garron discussed subscription model in the 2025-12-15 meeting' (no source verification). GOOD: 'I don't see Garron mentioned in the retrieved sources.'"). Worth trying as a low-risk tweak.

**Read in this order before brainstorming:**

1. `docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md` (full v3 spec, especially §2.2 non-goals, §19 future work, Appendix C accepted-by-design)
2. `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` §10 v3 validation addendum (the per-criterion table + soft-miss analysis)
3. `community-brain/CLAUDE.md` "Trade-offs we've deliberately kept" + "Known v2 backlog" — what's intentional vs follow-up
4. This handoff document

#### Starter prompt for v4 (paste into a new session)

```
I'm continuing the Community Brain project. Plan A (retrieval server),
Plan B (n8n ingestion), Hybrid Retrieval v2, and Retrieval v3 + Stage C
v2 are all DEPLOYED.

v3 shipped to the live VM on 2026-04-30 (commit e484ea4 on main).
Validation gate: 5 PASS, 3 soft-miss (each off by 1-2 chunks), 1
manual filter visual check still pending. The 3 soft-misses share
one root cause: Stage C v2 + Gemma 4 31B is more conservative than
v1 was on entity-of-speakers and has_unresolved_question
extraction. Corpus state is excellent; retrieval-side edge cases
fall slightly short of spec targets.

The work for this session: design Retrieval v4.

Read in this order before brainstorming:
1. docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md (this handoff;
   "v4 design (when warranted)" subsection)
2. docs/superpowers/specs/2026-04-29-retrieval-v3-and-stage-c-v2-design.md
   (full v3 spec — focus §2.2 non-goals, §19 future work,
   Appendix C accepted-by-design)
3. docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md
   §10 v3 validation addendum (per-criterion table + soft-miss
   analysis)
4. community-brain/CLAUDE.md "Trade-offs we've deliberately kept"
   + "Known v2 backlog"

Plan C status (verify before brainstorming):
- If Plan C has run since v3 deploy, the corpus has ~65 sessions
  ingested under chunk-extraction-v2. Soft-miss numbers may have
  shifted. Re-run validation gate against new corpus before
  scoping v4.
- If Plan C has NOT run, the corpus is the 9-session post-v3-deploy
  state. The soft-miss numbers in §10 v3 addendum still apply.
- Check via: curl http://10.1.30.10:8999/sessions

Two validation-driven v4 candidates (high priority):
1. entities-in-top-10 (16.1.2) — deterministic post-Stage-C merge
   of speakers_spoke + speakers_mentioned into entities.
   CODE-ONLY; no re-extract.
2. has_unresolved_question sensitivity (16.1.8 F7 + 16.1.1) —
   prompt tuning in chunk-extraction-v3 to lift detection sensitivity.
   STAGE C PROMPT CHANGE; full re-extract required (~$5 cost,
   ~12-15 hr wall at 65 sessions).

Other v4 candidates listed in v3 spec §19. Operational invariants
v4 must not break listed in this handoff above.

Use superpowers:brainstorming to explore the design space (which
candidates to bundle into v4, scope, whether to include Stage C
prompt revision given re-extract cost). Don't pre-decide. Then
spec via superpowers:writing-plans, then implementation plan,
then ship via superpowers:subagent-driven-development.

Constraints:
- Don't break the existing /query request/response contract (same
  clean-break stance as v2 + v3 — no `mode` parameter, no parallel
  endpoint, no backwards-compat shims for a single-operator
  deployment).
- Preserve the trust partition (ground_truth / derived_metadata /
  provenance) at the structural level.
- Preserve verify_corpus_v3_state fail-closed semantics, the
  speaker partition contract, and the filter format-injection
  defense (these were 19 rounds of adversarial review to
  establish; do not relitigate them).
- Solo operator, no real users. Same operational reality as v2/v3.
- If v4 includes Stage C prompt revision, the re-extract cost is
  ~$5 / ~12-15 hr at the post-Plan-C corpus size; budget
  accordingly.
```

---

## Operational reference card (carry across sessions)

| Resource | Where |
|---|---|
| VM SSH alias | `n8n-automation` (resolves via `~/.ssh/config`) |
| VM LAN IP | `10.1.30.10` |
| Mac LAN IP (Open WebUI + Ollama) | `10.1.50.219` |
| Retrieval server URL (LAN) | `http://10.1.30.10:8999` |
| Retrieval server URL (VM-local) | `http://127.0.0.1:8999` |
| Ollama URL | `http://10.1.50.219:11434` |
| n8n UI | `http://10.1.30.10:5678` |
| Workflow 1 id | `5` (Merged Call Summarizer — live weekly) |
| Workflow 2 id | `6` (Transcript-Only Summarizer — backfill) |
| Backfill state file | `~/n8n/n8n-state/backfill-state.json` |
| Historical corpus on VM | `~/n8n/historical/` (65 folders) |
| Ingested artifact output | `~/n8n/output/<session_id>/` |
| Validated answering models | GPT-oss 20B (A-grade), Qwen3-coder 30B (B+); avoid Gemma family |
| Required Ollama embedding model | `nomic-embed-text` (pin it; eviction silently breaks `/query`) |

## Memory entries (will load automatically in new session)

The auto-memory system has these records that future sessions will surface as relevant:
- Plan A status (deployed, with Plan B artifact-heading gap noted)
- Pre-Plan-B test findings (chain integrity bugs catalog)
- Env file changes require container restart
- Architectural decisions (Open WebUI RAG limitations, LanceDB pivot)
- Development environment notes

These are at `/Users/pchouinard/.claude/projects/-Volumes-NVMe-2TB-Work-Development-RecapFlow-automation/memory/`.

---

## Retrospective — things to watch in the new session

**What went well:**
- Aggressive bug-finding via real-corpus validation surfaced 5 chain bugs + 2 retrieval limitations in days, not weeks
- The trust-partitioned response shape + inference guidelines design held up under model A/B testing
- Schema's structured fields (has_unresolved_question, decisions, etc.) are sound — they just need to be plumbed into ranking
- Sonnet+Sonnet+Kimi prompt mix produces high-quality artifacts at ~$0.05-0.08 per session

**Watch out for:**
- **Open WebUI valve resets on filter re-upload.** Always re-set `retrieval_url` after every filter change.
- **Ollama embedding model eviction.** Pulling large LLMs to test can silently evict `nomic-embed-text`. `/query` returns 500 with no obvious cause; `/health` and `/sessions` keep working. Pin nomic-embed-text.
- **Vector-search-on-rare-tokens problem.** Entity-grounded queries fail unless rephrased with concrete content keywords. v2 fixes this; until then, operator workaround.
- **n8n workflow exports lose credential links** unless you preserve them by export-patch-import (see Plan B Tasks 7-8 for the pattern with the `1YRALvHjmQ3E6pqd` substitution).
- **`docker-compose.yml` drift** — VM had 2 ad-hoc env-var changes that weren't upstreamed for weeks. Always export-and-diff after operator-side changes.

**Things explicitly NOT to redo:**
- Don't rewrite the inference guidelines (test enforces parity with the constant in the filter — update both in the same commit if you need to change them).
- Don't change `extraction_prompt_version` casually (idempotency is anchored on it; bumping forces full corpus re-extraction).
- Don't drop the schema's `has_unresolved_question` / `decisions` / `action_items` fields under the assumption they're unused — v2 will heavily depend on them.
