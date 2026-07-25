# Community Brain Retrieval v5 — Grounding Under a Pinned 20B Model (Design)

**Date:** 2026-07-01
**Status:** LOCKED — decisions below are normative for the implementation plans in this folder.
**Target repo:** `RecapFlow-automation` (canonical clone on the n8n VM at `~/n8n/`; the Mac clone at `/Volumes/NVMe_2TB_Work/Development/RecapFlow-automation` is a read-only mirror per root `CLAUDE.md` "Development model").
**Companion plans:**
- `2026-07-01-recapflow-v5-grounding-plan.md` (implementation, this folder)
- `2026-07-01-distribution-v1.1-release-plan.md` (follow-up release, this folder)

---

## 1. Verified state of the world (2026-07-01)

Everything below was re-verified against the live repos and the live VM today. Several BRIEF/ROADMAP claims were stale; the corrections matter for scope.

| Claim in BRIEF/ROADMAP (snapshot) | Verified reality |
|---|---|
| Distribution "blocked on a first tagged release", placeholders unfilled | **Shipped.** `community-brain-distribution` released **Corpus v1.0.0 on 2026-05-26** (71 sessions / 1,499 chunks / 26 MB), image `ghcr.io/hopchouinard/community-brain-retrieval:1.0.0` (multi-arch), repo tagged `tier-b-v1.0.0`, CI green. The **local Mac clone of the distribution repo is stale** (still shows placeholders; last local commit 2026-05-11). |
| Track B backfill "~56 of 65 sessions un-ingested" | **Done.** Backfill completed as part of getting to v1.0.0. Live corpus today: **77 sessions / 1,622 chunks** (oldest 2025-02-02, newest 2026-06-30), confirmed via `GET /sessions` on `http://10.1.30.10:8999`. |
| Development on the Mac checkout | **Moved.** Root `CLAUDE.md` (origin/main, commit `61254c7`) declares VM-only development: all edits, commits, Claude sessions happen on the VM at `~/n8n/`. The Mac clone is `git pull`-only and is currently **12 commits behind origin/main** (none touch `community-brain/src` or `tests`). |
| Server "v0.4.0 deployed" | Code-wise true (v4 feature set is on `main`), but **`community-brain/pyproject.toml` still says `version = "0.3.0"`** — the 0.4.0 bump never landed in package metadata. Additionally, the **deployed VM server predates the Tier-B `/health` extension** (live `/health` returns bare `{"status":"ok"}` instead of the version/schema payload on `main`). The v5 deploy will bring the VM current. |
| 512 tests | Matches repo state; suite runs via `./.venv/bin/pytest tests/ -q` from `community-brain/`. |

The two v5 problems themselves were re-confirmed from `docs/superpowers/validation/2026-05-05-retrieval-v4-validation.md`:

1. **Fabrication (Q3 class).** With v4's full verification scaffolding in the system prompt, `gpt-oss:20b` still invented a "2025-12-15" session (real December sessions: 12-02, 12-09, 12-17, 12-30, 12-31) and attributed claims to Garron while its own reasoning trace said *"I don't see the speaker name."* Claude Opus, given the same context and prompt, refused correctly — the failure is model-dependent, and the model is pinned (it is the largest open model that runs on community members' machines). Prompting cannot fix this; only architecture can.
2. **Pool-limit (Q1/Q3/Q6/Q7 class).** Cue boosts re-rank a candidate pool of `top_k × OVERSAMPLE_FACTOR` (default 30); they never recruit. Measured: 0/50 chunks from session 2026-03-04 for a query naming that date; 1 of Adam James's 10 sessions surfaced for a speaker query; 0/10 "codex" chunks retrieved while the corpus holds 97. The boost deltas fire on chunks that were never in the pool to begin with. Model-independent.

**Constraint (load-bearing, from the distribution):** `gpt-oss:20b` stays as the answering model. No fine-tuning, no model swap, no per-query second LLM call.

**Invariants v5 MUST NOT break** (carried over from v4 handoff; each was hard-won through adversarial review):
- Trust partition (`ground_truth` / `derived_metadata` / `provenance`) structure of `/query`.
- `verify_corpus_v3_state` fail-closed semantics on startup, `/query`, post-commit.
- `lint_corpus` auto-path is additive-only; destructive cleanup only behind `--rebuild`.
- Speaker partition (`speakers_mentioned` excludes `speakers_spoke`) in both `pipeline.py` and `recanonicalize.py`.
- Filter trusted tags (`[flags:]`, `[corpus summary:]`, `[score:]`, `[SOURCE N — ...]`) structurally outside `<transcript_data>`; anything tag-shaped inside is unverified speech.
- Cue-rules YAML loader last-known-good semantics (never silently serve stale rules when a current load returns valid-but-empty).
- No `/query` request/response contract break: no `mode` parameter, no parallel endpoint. Additive response fields are allowed.

---

## 2. v5 scope in one paragraph

v5 is an **anti-fabrication architecture** with three layers plus housekeeping: (a) **cue-driven candidate injection** so date/rare-entity/quiet-session queries actually retrieve the chunks the cue rules were built to boost; (b) a **deterministic filter-side citation guard** that verifies every session date, `[SOURCE N]` reference, and chunk_id in the model's answer against the retrieved context and annotates (or strips) what cannot be verified; (c) a **fabrication-rate evaluation harness** with a fixed adversarial query set so before/after is a number, not an anecdote. Housekeeping: speaker auto-rule last-known-good cache, `has_unresolved_question` over-permissiveness alarm, `RetryConfig` wiring (closing the documented v2 TODO), prompt/docs updates, version bump to 0.5.0. No schema change, no corpus re-extract, no new services.

---

## 3. Decisions

### D1 — v5 bundle: injection + citation guard + eval harness + three small items; nothing requiring re-extract

**Decision.** v5 MUST ship: cue-driven candidate injection, filter-side citation verification, fabrication evaluation harness, speaker auto-rule LKG cache, `has_unresolved_question` corpus alarm, `RetryConfig` wiring, prompt/docs updates (D15), version bump 0.3.0 → 0.5.0 (D16). v5 MUST NOT change the LanceDB schema (`schema_version` stays `1.1`) and MUST NOT change `chunk-extraction-v3` (no re-extract).

**Rationale.** The two high-priority v5 candidates (#1 injection, #6 citation post-processing) are the architectural answers to the two confirmed failure classes; the eval harness is what makes "fixed" falsifiable. The three small items are cheap, code-only, and already documented as debt. Re-extract-class changes (tightening `has_unresolved_question` semantics via prompt, candidate #7 option a) cost ~$5 and 12–15 h wall at 77 sessions and re-open extraction drift — rejected in favor of the prompt-side clarification (D15).

**Rejected.** Splitting into v5 (injection) and v6 (guard): the eval harness needs both layers in place to measure the system-level fabrication rate the BRIEF asks about, and the two changes touch disjoint code (retrieval server vs filter) with no interleaving risk.

### D2 — Injection is a recruitment pass inside `search_chunks`, merged into the pool BEFORE the cue-boost step

**Decision.** `community_brain.query.query_local.search_chunks` gains one step: after the hybrid candidate list is built and before the BM25-rank annotation / boost snapshot, a recruitment pass pulls targeted chunks for every firing recruit-enabled cue rule and merges them (dedup by `chunk_id`) into the candidate list. The existing boost pass then ranks everything as today. Injection runs only on the hybrid path (`_use_hybrid=True`); the vector-only graceful-degradation fallback and the `_use_hybrid=False` test knob stay pure.

**Rationale.** Boosts already encode "this chunk answers this cue"; the only missing piece is membership in the pool. Injecting pre-boost means injected chunks are scored by the identical delta machinery — one ranking model, no special-case scoring path. Keeping the vector-only path pure preserves the golden-suite lift-validation semantics (`test_golden_query_vector_only_baseline_misses`) and keeps degradation behavior unchanged.

**Rejected.**
- *Raise `OVERSAMPLE_FACTOR`.* Wasteful for every query, and provably insufficient: 2026-03-04 chunks were absent from the top-50 (top_k=10 would need OVERSAMPLE > 5 just for that one case, with no guarantee for quieter sessions).
- *Separate `/query` mode or endpoint.* Contract break; violates the standing no-mode-parameter stance.
- *Post-boost merge.* Injected chunks would need a synthetic final score; pre-boost merge lets the real rules price them.
- *Cross-encoder reranker.* Reranks the same broken pool; doesn't recruit. Also adds a model dependency to a system whose constraint is "no new models."

### D3 — Recruitment is opt-in per rule via `recruit: true`; speaker auto-rules recruit by default

**Decision.** `CueRule` gains `recruit: bool = False` and `predicate_spec: dict | None = None` (the raw YAML `target_predicate` mapping, preserved for recruitment derivation). `load_cue_rules_from_yaml` MUST parse an optional `recruit` key on both rule shapes. `build_speaker_auto_rule` MUST set `recruit=True` on both synthesized rules. `config/query-cues.yaml` enables `recruit: true` on exactly: `unresolved_questions`, `date_iso_match`, `date_month_year_match`, `date_phrased_with_day`, `date_relative_phrasing`, `date_quarter_match`. Generic rules (`questions_general`, `decisions`, `action_items`, `insights`, `referenced_prior`) stay boost-only.

**Rationale.** `questions_general` fires on the word "question" — recruiting on it would inject near-arbitrary chunks into most queries. The pool-limit evidence is specifically about dates, speakers, and the unresolved-question flag; recruitment stays surgical and, because it lives in the hot-reloaded YAML, an operator can widen or narrow it without a deploy.

**Rejected.** Recruit-on-every-rule (pool inflation, latency, and semantic noise on generic cues); a separate recruitment-rules file (two files to keep in sync for one concept).

### D4 — Per-strategy recruitment queries, derived from the rule that fired

**Decision.** A new module `community_brain/query/candidate_injection.py` owns recruitment. For a firing rule, `build_recruitment_query(rule, question)` derives a `RecruitmentSpec(where, fts_text)`:

| Rule shape / strategy | Recruitment predicate |
|---|---|
| `iso_date_equals` | `WHERE session_date = '<captured>'` |
| `month_year_overlap` (incl. `date_phrased_with_day`) | `WHERE session_date >= 'YYYY-MM-01' AND session_date <= 'YYYY-MM-31'` |
| `token_overlap` | no WHERE; FTS search with the joined capture token (e.g. `Q1-2026`, `late-December-2025`) as the query text against `bm25_text` |
| `name_resolve_then_check` | `WHERE (array_has(<match_field>, '<name1>') OR array_has(<match_field>, '<name2>') …)` over every registry name mapping to the resolved canonical |
| legacy `{field, value}` predicate (bool or str) | `WHERE <field> = true/false` or `= '<value>'` |
| legacy `check: non_empty` / `check: contains` | **no recruitment** (no portable LanceDB SQL for list-column emptiness/membership across versions); rule stays boost-only |

Execution per rule: FTS query (`query_type="fts"`, `fts_columns="bm25_text"`, text = `fts_text or question`) with `(<rule_where>) AND <where_expr>` and `limit(INJECT_PER_RULE)`; if the FTS leg errors or returns zero rows and the rule has a hard WHERE, fall back to a plain filtered scan with the same WHERE and limit. All string values pass through SQL-standard quote-doubling.

**Rationale.** Each strategy already defines what "this chunk matches the cue" means; the recruitment predicate is that same definition expressed as a WHERE clause instead of a per-chunk Python check. Ranking recruits by FTS relevance to the question picks the best N when a predicate matches many chunks (e.g. a speaker with 21 chunks); the plain-scan fallback covers the pathological case that motivated this whole feature — a quiet session with zero lexical overlap with the question.

**Rejected.** Vector-ranked recruitment (a second ANN query per rule; the vector leg is exactly the signal that failed for these queries); implementing `non_empty` recruitment via `array_length()` (DataFusion function availability varies across LanceDB releases; the only recruit-enabled legacy rule is a bool-equality predicate anyway).

### D5 — Budgets: `INJECT_PER_RULE = 10`, `MAX_INJECTED_TOTAL = 30`, module constants

**Decision.** Constants in `candidate_injection.py`, mirroring how `OVERSAMPLE_FACTOR` is a module constant in `query_local.py`. Rules are processed in resolution order (YAML order, then the two speaker auto-rules); recruitment stops with a WARN log when the total cap is hit. A chunk recruited by multiple rules is stored once with all recruiting rule names accumulated.

**Rationale.** 10 per rule covers whole quiet sessions (2025-12-30 has ~10 chunks) and a speaker's plausible per-query slice. The 30 cap bounds worst-case pool growth to `top_k×3 + 30` and worst-case added latency to ~3 recruitment queries at ~10–20 ms each (same cost class as the existing BM25 rank annotation query). Env-var tunables are NOT added: v3 established "one tunable" discipline, and hot-reloaded YAML already controls *which* rules recruit.

**Rejected.** Per-rule YAML budgets (config surface without evidence of need); unbounded recruitment (a broad month query against a busy month could inject hundreds of rows).

### D6 — Injected chunks enter at `_rrf_score = 0.0` and are priced by the normal boost pass; `score_breakdown` gains `injected_by`

**Decision.** Injected rows get `_rrf_score = 0.0`, real `_distance`/`_vector_similarity` computed as cosine against the query vector (so the public `similarity` field keeps spec §7.2 semantics), `_bm25_rank` from the same rank-annotation map as pool rows, and `_injected_by: [rule names]`. The `ScoreBreakdown` response model gains `injected_by: list[str] = []` (additive field; empty for pool-native chunks). No other `/query` contract change.

**Rationale.** An injected chunk that then fails to fire any boost sorts to the bottom — harmless by construction. Deltas (0.04) sit at the same magnitude as top RRF scores (max ≈ 2/(60+1) ≈ 0.033), so a recruited exact-date chunk lands above generic pool members but below pool members that match the same cue *and* have base relevance — exactly the intended ordering. `injected_by` gives the operator (and the eval harness) provenance for every rescue at zero cost.

**Operational note (documented, not code):** the Open WebUI filter's `min_score` valve (default 0.2) filters on cosine `similarity`; recruited chunks from semantically distant sessions can carry low cosine similarity and be dropped client-side. At nomic's observed 0.3–0.8 range the default is safe; operators raising `min_score` past ~0.3 are trading away injection rescues, and `community-brain/CLAUDE.md` MUST say so.

### D7 — Injection respects the caller's WHERE (success guard + user filters)

**Decision.** Every recruitment query ANDs the rule predicate with the exact `where_expr` used by the main hybrid query — `extraction_status = 'success'` plus the caller's filter expression. Injection can therefore never surface a chunk the caller's filters excluded, and never a failed-extraction chunk.

**Rationale / rejected.** Anything else silently violates the `/query` filter contract and the failed-chunks-are-unsearchable invariant. No alternative was considered viable.

### D8 — Citation guard lives in the filter's `outlet`; context re-parse first, bounded per-chat stash as fallback; fail-open

**Decision.** `community_brain_filter.py` gains an `outlet(body, __user__)` hook (Open WebUI's post-generation callback). Grounding facts are obtained by, in order: (1) parsing the `[COMMUNITY_BRAIN_CONTEXT]` system message found in `body["messages"]`; (2) if **no** context message is present at all, a per-chat stash `self._grounding_by_chat` (an `OrderedDict` capped at 32 chats, written on every `inlet`: facts on `ok`, `None` on `no_results`/`error` so stale facts can't leak across turns). If a context message is present but is a no-sources/unavailable notice, the guard MUST skip (the model was explicitly told to answer from general knowledge or refuse). If no facts are available, the guard MUST fail open with a logged warning.

**Rationale.** Re-parsing the context out of the same message list the model saw is stateless, concurrency-safe, and immune to Open WebUI's habit of resetting filter state on re-upload. The stash exists only because some Open WebUI versions do not replay injected system messages into `outlet`. Fail-open is deliberate: the guard is defense-in-depth behind retrieval and the system prompt; a guard that blocks answers when its own state is missing would convert a safety net into an outage.

**Rejected.** Fail-closed (see above); storing facts keyed by message hash (fragile); a server-side verification endpoint (adds a network hop and couples the filter to a new API; the filter already possesses everything it needs).

### D9 — What the guard verifies, and against what

**Decision.** From the answer text, three token classes are extracted and checked:

1. `[SOURCE N]` references (case-insensitive) — N must be one of the rendered source indices.
2. chunk_id-shaped citations `[YYYY-MM-DD:<type>:<suffix>]` — must be one of the retrieved chunk_ids.
3. Bare ISO dates `\bYYYY-MM-DD\b` — must appear somewhere in the retrieved context.

The **source-index and chunk_id sets** are parsed from `[SOURCE N — chunk_id: …]` header lines with all `<transcript_data>…</transcript_data>` bodies removed first (a transcript containing a tag-shaped line must not be able to whitelist a fake source — this preserves the v3/v4 format-injection defense). The **grounded-dates set** is parsed from the FULL context including transcript bodies (a date a speaker actually said is legitimate for the model to repeat).

**Rationale.** These three classes cover the entire observed fabrication surface (Q3: fabricated session date + fabricated chunk-attribution; Q2/Q4: chunk_id-style citations, which remain *verifiable* and are only flagged when they don't resolve). Dates inside real chunk_ids are grounded automatically because chunk_ids embed their session date.

**Rejected — speaker-attribution verification.** Detecting "attributed claims to Garron" requires NLP over free prose (name detection, claim-attribution parsing) inside a single-file filter with a stdlib+httpx dependency budget; false positives would flag legitimate paraphrase. The speaker fabrication class is instead attacked upstream (injection makes the *right* speaker chunks present) and by the strengthened prompt exemplar (D15). This is the one BRIEF-named fabrication class v5 addresses indirectly; the eval harness (D11) still measures it via refusal-correctness probes on fictitious speakers.

### D10 — Failure policy: `annotate` by default; `strip` and `off` as valve options; never auto-refuse

**Decision.** New valve `citation_guard: str = "annotate"` with values `annotate | strip | off`.
- `annotate`: append a clearly-delimited **"Grounding check (automated)"** block listing unverified dates / source refs / chunk_ids, instructing the reader to treat those specific claims as unverified.
- `strip`: additionally replace each unverified token in place (`[unverified date]` / `[unverified source]`) before appending the block. Chunk_id citations are replaced before bare dates so a fabricated date inside a fabricated citation is handled once.
- `off`: guard disabled.
The guard MUST NOT replace the whole answer with a refusal.

**Rationale.** The guard is a regex-level verifier; it knows a token is ungrounded but not whether the sentence around it still carries grounded value. Annotation preserves everything and makes the fabrication visible — which is the actual requirement ("catch Q3-style fabrications regardless of how well the model follows the prompt"). Strip is offered because the distribution audience includes operators who prefer hard redaction over reader judgment. Auto-refuse discards grounded content on the strength of a regex and would turn every minor date slip into a dead answer.

**Rejected.** LLM-based re-ask/self-correction loop (adds latency and a second inference per answer, and the re-ask runs on the same model that fabricated); refusing when *any* check fails (see above).

### D11 — Fabrication-rate evaluation harness: deterministic verifier + fixed adversarial set, two phases

**Decision.** Two tiers, sharing the verifier functions from the filter module (single source of truth for "what counts as fabricated"):

1. **CI tier (deterministic, no LLM, runs in pytest).** Golden-corpus fixtures gain a quiet session (`2025-12-30`, two chunks engineered to be invisible to both hybrid legs); integration tests prove injection recruits them, that the no-recruit configuration misses them (the pool-limit reproduced in miniature), that `injected_by` is reported, and that user filters are honored.
2. **Operator tier (`scripts/eval-fabrication.py` + `scripts/eval/fabrication-queries.yaml`).** A fixed adversarial query set (12 queries) spanning the classes: quiet-session ISO date, phrased date, relative date, quarter, **non-existent session date** (expects refusal), rare-entity+date conjunction (Hemal/Garron mid-Dec 2025), speaker enumeration (Adam James), topic coverage (codex), unresolved-question survey, fictitious speaker (expects refusal), verbatim-quote trap, cross-month synthesis. Phases: `RETRIEVAL` (POST `/query`, measure target-session recall@top_k — no LLM needed), `ANSWER` (render the context with the real filter code, call the answering model via Ollama chat with the canonical system prompt, run the verifier over the answer), `REPORT` (JSON out; `--compare baseline.json` prints deltas).

**Metrics (locked).** Per query: `retrieved_target_recall` (|target sessions ∩ retrieved sessions| / |targets|), `fabricated_dates`, `unverified_source_refs`, `unverified_chunk_ids`, `refused` (heuristic phrase match), `refusal_correct` (for expect-refusal probes). Aggregate: **fabrication_rate** = fraction of answered queries containing ≥1 unverified date/citation; **refusal_correctness** over expect-refusal probes; **mean target recall**. Before/after = run once on the deployed v4 VM before merging v5, once after.

**Rationale.** Using the filter's own verifier for measurement means the metric and the guard can't drift apart. Splitting phases keeps the expensive, nondeterministic part (a 20B model answering) out of CI while the retrieval-side regression surface is pinned forever in pytest. The adversarial set is built from *verified corpus facts* (real December session list, Adam James's 10 sessions, the 97 codex chunks, the 2025-12-17 Hemal+Garron session) so recall numbers are ground-truthed.

**Rejected.** LLM-as-judge scoring (adds a judge model to a system whose defining constraint is a pinned model and a solo operator; the deterministic verifier covers the fabrication classes that matter); embedding the ANSWER phase in pytest behind a marker (Ollama + 20B model on CI runners is not a thing this project has).

### D12 — Speaker auto-rule last-known-good cache (with resolver snapshot)

**Decision.** `build_speaker_auto_rule` gains a per-path last-known-good cache symmetrical to `_LAST_GOOD_RULES`, storing the rule pair **and** snapshots of the two resolver dicts (`_SPEAKER_NAME_TO_CANONICAL`, `_SPEAKER_CASEFOLD_LOOKUP`). On a load that yields an empty registry for a path that previously loaded non-empty, return the cached pair and restore the resolver dicts, logging a WARNING. First-time-empty behavior (fresh install, genuinely empty registry) is unchanged: never-match sentinel rules, nothing cached.

**Rationale.** The v4 asymmetry: a transient partial write to `speaker-aliases.yaml` during `/query` silently degrades speaker boosts to never-match for that request. Caching only the rules without the resolver dicts would be a bug — `name_resolve_then_check` (and D4's recruitment) resolve through the module-level dicts, which `_refresh_speaker_resolver` rebinds to `{}` on failure.

**Rejected.** Treating empty-after-non-empty as an error (an operator legitimately emptying the registry would need a server restart to be believed; WARN-and-serve-stale matches the cue-rules loader's accepted semantics, Appendix C of the v3 spec).

### D13 — `has_unresolved_question` over-permissiveness alarm in `lint_corpus`

**Decision.** `lint_corpus_chunks` computes the corpus-wide rate of `has_unresolved_question=True` and logs a WARNING (and returns `unresolved_rate` / `unresolved_alarm` in its stats dict; the CLI prints an alarm line) when the rate exceeds `UNRESOLVED_RATE_ALARM_THRESHOLD = 0.50`. Additive stats keys only; existing `scanned`/`recurrent` semantics untouched; alarm never changes markers or exit code.

**Rationale.** chunk-extraction-v3 deliberately defaults the flag toward `true`; current corpus rate is ~27% (394/1,434 at v4 deploy). 50% is far above any observed healthy rate and clearly below "the flag has stopped discriminating." The alarm rides the existing daily 04:00 UTC cron for free.

**Rejected.** Alarming inside `/ingest` (per-session rates on small sessions are noisy; the lint pass sees the whole corpus); failing the lint run (an alarm that blocks the cron's real work punishes the operator for a prompt-tuning question).

### D14 — `RetryConfig` wiring: thread the config, keep the mock boundary intact

**Decision.** `community_brain.llm.call_llm` gains `backoff_schedule: list[int] | None = None` (used as `backoff_schedule[attempt]` when provided; `2 ** attempt` otherwise — the loader already guarantees `len(schedule) >= retry_attempts`). `extractor._call_llm` and `session_extractor._call_llm` gain optional `retries` / `backoff_schedule` parameters (defaults preserving today's behavior). `extract_chunk_metadata` and `extract_session_themes` gain `retry_config: RetryConfig | None = None`; when provided they call `_call_llm` with the configured values, when absent the call site is byte-identical to today. `pipeline.ingest_session` passes the already-loaded `retry_cfg` (renamed from `_retry_cfg`) to both stages and the module-docstring TODO is removed. Exactly nine test mock functions with `(model, prompt)` signatures gain `**_kwargs` (enumerated in the plan).

**Rationale.** Honors `chunking.yaml`'s `retry_attempts: 3` / `retry_backoff_seconds: [2, 8, 32]` as documented, without moving the retry loop (it stays in `call_llm`, the single place that understands HTTP-vs-parse failure classes) and without breaking the CLAUDE.md-blessed mock boundary (`extractor._call_llm` / `session_extractor._call_llm` keep positional compatibility).

**Rejected.** A retry wrapper around `_call_llm` in the extractors (duplicates the retry loop that `call_llm` already implements, and double-retries: 3 outer × 3 inner = 9 attempts); changing `call_llm`'s default retries source to read YAML itself (couples the generic LLM client to the ingestion config).

### D15 — Prompt and docs updates: flag-survey rule + citation exemplar; paired-file discipline; v5 custom model at temperature 0

**Decision.**
- `docs/inference-guidelines.md` gains **rule 8** (flag-survey semantics — candidate #7 option b): flagged-unresolved chunks may be enumerated from the `[flags:]` line for survey-style questions without locating an explicit unanswered Q&A pair verbatim.
- Rule 2 gains a **BAD/GOOD exemplar** (candidate #8 option c) built from the real Q3 fabrication, plus an explicit "never cite by raw chunk_id" line.
- `prompts/community-brain-v4-openwebui-system-prompt.md` is updated in the same commit (the two files share content by contract), and a new test locks the containment relation so they cannot drift again.
- Operator deploy step (gated): create Open WebUI custom model **`community-brain-v5-gpt-oss:20b`** with the updated prompt and **temperature 0** (candidate #8 option b — reduces gap-filling; never tried in v4).

**Rationale.** Option (b) for the flag-semantics gap costs one prompt paragraph versus a $5/12-15 h re-extract with drift risk for option (a); option (c) documents-and-accepts a refusal that users experience as a bug. The exemplar is the cheapest known lever on gpt-oss's citation-format compliance; temperature 0 is free and orthogonal.

**Rejected.** Re-extract under a tightened prompt (option a — cost, drift, and it *narrows* the flag exactly when D13 exists to watch it); renaming `docs/inference-guidelines.md` (referenced from too many docs).

### D16 — Version 0.5.0; CHANGELOG; docs currency

**Decision.** `community-brain/pyproject.toml` bumps `0.3.0 → 0.5.0` (0.4.x is skipped in metadata; the CHANGELOG entry records that "0.4.0" existed only as a docs/deploy label — package metadata was never bumped). `docs/migrations/CHANGELOG.md` gains a v5 entry (no schema migration; additive `/query` response field `score_breakdown.injected_by`). `community-brain/CLAUDE.md` is updated: pool-limit note replaced with injection + `recruit:` documentation, citation-guard valve documentation, `min_score` interaction note (D6), RetryConfig removed from the "Known v2 backlog." Re-run `pip install -e ".[dev]"` after the bump so `importlib.metadata` (and `/health`) report 0.5.0.

**Rationale / rejected.** `test_version_source.py` derives `app.version` from package metadata; leaving 0.3.0 in place while shipping v5 makes `/health` lie to `verify-install.sh` in the next distribution release. Bumping to "0.4.0 then 0.5.0" in two commits is ceremony with no consumer.

---

## 4. Architecture (data flow)

### 4.1 Injection

```
/query → verify_corpus_v3_state → search_chunks(question, top_k, filters)
  1. embed question (Ollama)
  2. hybrid query: RRF(vector, BM25 on bm25_text), limit top_k×3, WHERE success+filters
  3. rules = _resolve_cue_rules()                        ← moved up (was after step 5)
  4. inject_candidates(question, table, rules,           ← NEW (candidate_injection.py)
        where_expr, existing_ids, query_vector)
       for each firing rule with recruit=True:
         spec = build_recruitment_query(rule, question)  # D4 table
         rows = FTS(fts_text or question) WHERE (spec.where AND where_expr) LIMIT 10
         if none and spec.where: plain scan WHERE ... LIMIT 10
       normalize: _rrf_score=0.0, cosine _distance, _injected_by=[rules]
       dedup vs pool and among rules; cap total at 30
  5. BM25 rank annotation (existing; injected rows get ranks from the same map)
  6. snapshot _rrf_score_pre_boost; apply_cue_boosts (existing, unchanged)
  7. sort, truncate top_k; score_breakdown += injected_by
```

### 4.2 Citation guard

```
inlet:  retrieve → build context → stash grounding facts per chat (ok→facts, else→None)
model:  generates answer (system prompt = inference-guidelines v5, temperature 0)
outlet: facts = parse [COMMUNITY_BRAIN_CONTEXT] system message from body
          (source indices + chunk_ids from headers, transcript bodies removed;
           grounded dates from full context)
        if context present but not a sources context → skip
        if no context message at all → stash fallback → else fail open (log)
        verdict = verify_answer_grounding(answer, facts)
        annotate / strip per valve; append "Grounding check (automated)" block
```

### 4.3 Evaluation

```
pytest (CI, deterministic)          scripts/eval-fabrication.py (operator)
  golden corpus + quiet session       RETRIEVAL: /query recall vs target_sessions
  injection recruits / no-recruit     ANSWER: filter-rendered context → Ollama chat
  misses / filters honored            → verifier (same functions as the guard)
                                      REPORT: fabrication_rate, refusal correctness,
                                              recall; JSON + --compare deltas
```

---

## 5. Rejected scope (v5 will not do)

| Item | Why rejected |
|---|---|
| LLM intent classifier (pre-retrieval) | Second LLM call per query; speculative in v3 §19, still speculative; injection addresses the measured failure directly. |
| Cross-encoder reranker | Re-ranks the same pool it can't grow; new model dependency against the project's core constraint. |
| Weighted-sum fusion replacing RRF | v3 §19's "anti-feature without a calibration story" verdict stands. |
| Stage C prompt re-extract (candidate #7a) | $5 / 12–15 h; drift risk; D15's prompt rule + D13's alarm cover both directions cheaply. |
| Speaker-attribution NLP verification in the guard | Free-prose claim attribution is beyond a deterministic single-file filter; handled upstream (injection) + prompt exemplar; measured by the harness regardless. |
| Deep `/health`, read/write API-key split, `/sessions` pagination, multi-writer registries, `/reindex` mutations | Real backlog, zero coupling to fabrication; would dilute the plan. Stay in the known-backlog list. |
| Open WebUI SHA bump | Known alembic data-loss hazard; nothing in v5 requires it. The distribution release plan treats it as an explicitly separate, manually-verified operator flow (unchanged from v1.0.0). |

---

## 6. Risks and mitigations

- **Recruitment query performance.** Each firing rule adds one FTS query (~10–20 ms at 1.6 k chunks). Worst realistic case is 3 rules ≈ +60 ms on a path that already spends ~1 s embedding. Budgets (D5) cap the blast radius; `injected_by` + server log line make recruitment observable.
- **LanceDB `.where()` on FTS queries.** Already exercised in production by the BM25 rank-annotation query with the same builder shape; the fallback plain scan covers per-release quirks.
- **Open WebUI `outlet` body shape variance.** Primary path parses the message list; stash fallback covers versions that don't replay system messages; fail-open guarantees no outage. Valve `off` is the escape hatch.
- **Golden-corpus perturbation.** New fixture rows use vocabulary chosen to be disjoint from existing golden queries; the plan runs the full suite immediately after seeding and treats any golden regression as a fixture-vocabulary bug, not a retrieval bug.
- **Filter re-upload resets valves.** Known v4 hazard; deployment checklist re-states it (`retrieval_url`, `api_key`, and now `citation_guard` must be re-set after upload).

---

## 7. Deliverable map

| BRIEF deliverable | Where |
|---|---|
| Design doc (injection, verification, harness, small-items scope) | This document |
| Implementation plan (RecapFlow, TDD, complete code) | `2026-07-01-recapflow-v5-grounding-plan.md` |
| Optional distribution release plan | `2026-07-01-distribution-v1.1-release-plan.md` — **re-scoped**: v1.0.0 already shipped (2026-05-26), so the plan cuts **v1.1.0** (post-v5 corpus + image + curated-file sync), following the proven v1.0.0 release flow |
| Track B interaction note | Moot — backfill complete; the eval harness runs against the full 77-session corpus, which strengthens (not weakens) fabrication measurement |
