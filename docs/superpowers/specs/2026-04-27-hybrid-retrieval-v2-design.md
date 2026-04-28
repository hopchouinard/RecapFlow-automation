# Community Brain Hybrid Retrieval v2 — Design

**Status:** Draft
**Date:** 2026-04-27
**Owner:** Solo operator (no other clients in production)
**Supersedes:** Pure-vector ranking in `community_brain.query.search_chunks_v2` (Plan A)

---

## 1. Motivation

Phase 6 validation against the 8-session corpus (see Plan A spec §10 Phase 6, findings 6 and 7) surfaced two retrieval-layer limitations that share a common root cause: **pure vector similarity ignores the structured fields the v1 schema was purpose-built to support.**

Concrete failures observed:

- **Finding 6 — rare-token retrieval fails.** *"What did Adam from Gold Flamingo commit to?"* returned 0 chunks containing "Adam" in top-10. Rephrasing with concrete content keywords ("Adam Gold Flamingo Solutions sales funnel law firms LinkedIn") returned the right chunks at similarity 0.42+. Pure-vector via `nomic-embed-text` favours thematic similarity over proper-noun matching.
- **Finding 7 — metadata-tagged retrieval fails.** *"What questions came up across these calls that didn't get fully answered?"* returned 1 of 38 corpus chunks tagged `has_unresolved_question=True`. The other 37 tagged chunks ranked below `signal:general` overviews that *thematically* mention questions but aren't flagged.

Both findings point at the same gap: the schema's structured fields (`has_unresolved_question`, `decisions`, `action_items`, `entities`, `references_prior`, etc.) and proper-noun-rich `full_text` are not part of the ranking signal. Hybrid Retrieval v2 closes that gap.

## 2. Goals and non-goals

### 2.1 Goals
- Restore retrieval correctness for entity-grounded queries (Finding 6) by adding lexical (BM25) signal alongside vector similarity.
- Restore retrieval correctness for metadata-tagged queries (Finding 7) by injecting lightweight cue-driven boosts on chunks whose structured flags align with the question's lexical intent.
- Keep the existing client-facing `/query` request/response contract (POST shape, structured response, ground_truth/derived_metadata/provenance partitioning).
- Preserve the `extraction_status='success'` guard and the existing `QueryFilters` filter-then-rank semantics.
- Ship as a clean break: no `mode` parameter, no parallel endpoint, no deprecation period. The legacy v0/v1 vector-only helpers are deleted.
- Stay deterministic and offline (no LLM call in the query path).

### 2.2 Non-goals
- LLM intent classification (deferred — would have been Approach B in brainstorming). v3 candidate.
- Cross-encoder reranking (deferred — Approach C). v3 candidate.
- Weighted-sum fusion. RRF only in v2.
- BM25 over a synthesized field (`topic_label + entities + full_text`). Index `full_text` only in v2; revisit if entity coverage stays weak after first validation pass.
- Cue rules in YAML config. Hardcoded Python dict in v2; lift to YAML if the rule set churns.
- Multi-writer FTS index lifecycle. Single-process server only (matches the existing v1 registry constraint).

### 2.3 Explicit semantic break
v2's `/query` is **not** response-equivalent to v1's `/query` for the same `(question, top_k, filters)` inputs. Top-K rankings will differ. This is intentional and acceptable because the only operator-facing client (Open WebUI filter) ships in lockstep and there is no third-party consumer. Documented here so future-you doesn't blame past-you.

## 3. Architecture

### 3.1 Retrieval pipeline

```
question
  │
  ├─ Ollama embed (nomic-embed-text) ─────► vector candidates
  │                                         (top_k * 3, internal)
  │
  └─ tokenize for BM25 (LanceDB FTS) ─────► BM25 candidates
                                            (top_k * 3, internal)
                              │
              LanceDB native hybrid query
                  RRF fusion, k=60
                              │
            filter-then-rank guard applied as WHERE clause:
              extraction_status = 'success'
              + caller's QueryFilters expression
                              │
                  fused candidates (top_k * 3)
                              │
              cue-boost pass (Python, post-LanceDB):
                for each candidate:
                  for each cue rule whose phrase set
                  matches the question (case-insensitive
                  substring) AND whose target predicate
                  matches the chunk's metadata:
                    score += rule.delta
                              │
                  re-sort by boosted score
                              │
                  truncate to top_k
                              │
            structured response (shape unchanged)
```

The cue boost runs *after* RRF fusion and *before* truncation to `top_k`. Boosts are additive deltas on the RRF score; they do not exclude candidates and they do not interact with the WHERE-clause filter. A candidate that wins on RRF score alone still surfaces; the boost only nudges flag-aligned chunks up the list to break near-ties.

### 3.2 Filter / boost interaction (orthogonal layering)

Three layers of selectivity, applied in order:

1. **Hard guard** — `extraction_status='success'`. Always applied. Excludes failed-extraction chunks (which carry zero-vector embeddings by design — see Plan A spec §6).
2. **Caller's `QueryFilters`** — explicit operator-supplied predicates (e.g. `has_unresolved_question=True`, `entities CONTAINS 'Adam'`, `session_date_range`). Hard filter, applied as part of the LanceDB WHERE clause before retrieval.
3. **Cue-driven boost** — soft additive Δ on RRF score, applied after retrieval. Affects ranking only, never selection.

If layer 2 already constrains the set (e.g. caller passed `has_unresolved_question=True` explicitly), layer 3's boost on the same field is redundant but harmless — every candidate already satisfies the predicate, so every candidate gets the same Δ, no ranking change.

### 3.3 Oversampling

Internal candidate pool size is `top_k * 3` (e.g. for `top_k=10`, the LanceDB hybrid query returns 30 candidates internally before cue boosting). This gives the cue-boost pass enough headroom to promote flag-aligned chunks that ranked 11th–30th by RRF alone into the top-10. The factor is a tunable constant (`OVERSAMPLE_FACTOR = 3`) inside `community_brain.query.search`; not exposed in the API.

## 4. Component changes

### 4.1 Code changes

| File | Change |
|---|---|
| `src/community_brain/query/query_local.py` | `search_chunks_v2` renamed to `search_chunks` and reimplemented around LanceDB hybrid query + cue boost. Legacy `search_chunks` (targeting v0 `transcripts` table) deleted. `build_filter_expression` (v1) deleted; `build_filter_expression_v2` renamed to `build_filter_expression`. CLI `main()` reworked to use the new helper or removed entirely if unused. |
| `src/community_brain/query/cue_rules.py` | **New module.** Exports `CUE_RULES: tuple[CueRule, ...]` and `apply_cue_boosts(question, candidates) -> list[dict]`. Pure function over candidate dicts; no LanceDB dependency. |
| `src/community_brain/query/fts_lifecycle.py` | **New module.** Exports `ensure_fts_index(table)` (idempotent: creates if absent) and `optimize_fts_index(table)` (called after each `/ingest` commit). |
| `src/community_brain/query/retrieval_server.py` | `/query` handler unchanged in shape. Startup hook calls `ensure_fts_index()` once before accepting traffic. Internal call sites updated to use renamed helpers. |
| `src/community_brain/ingestion/pipeline.py` | After successful chunk commit, call `optimize_fts_index()` so freshly-written chunks become BM25-searchable on the next `/query`. Failure to optimize logs a warning but does not fail the ingest (chunks are already committed; FTS will catch up on the next call). |
| `src/community_brain/query/__init__.py` | Re-export new public surface. Drop legacy exports. |

### 4.2 Test changes

| File | Change |
|---|---|
| `tests/fixtures/golden_queries.yaml` | **New.** 5 entity-grounded queries (Finding 6 coverage) + 5 metadata-tagged queries (Finding 7 coverage), each with expected `chunk_id` signatures derived from the current 8-session corpus. |
| `tests/query/test_hybrid_search.py` | **New.** End-to-end test: small corpus fixture → ingest → `/query` → assert top-K contains target chunks. Also asserts pure-vector baseline (computed by disabling cue boost + dropping FTS) does NOT contain the target chunks for at least 3 of the golden queries — proves the lift is real, not coincidental. |
| `tests/query/test_cue_boost.py` | **New.** Unit tests over `apply_cue_boosts`: cue match → Δ added; no cue match → no change; cue match but flag false → no Δ; multi-cue accumulates; fault injection (rule with bad regex / missing field) → caught and skipped. |
| `tests/query/test_fts_lifecycle.py` | **New.** `ensure_fts_index` is idempotent; `optimize_fts_index` no-ops on absent index; missing index at query time degrades gracefully (logged WARN, vector-only path runs). |
| `tests/query/test_search_chunks.py` (existing or new) | Updated for renamed `search_chunks` symbol; covers the new pipeline order. |
| Existing tests touching `search_chunks_v2` symbol | Renamed call sites; behavior preserved at the API-shape level. Behavior at the ranking level may shift — accept and update assertions. |

### 4.3 Doc changes

| File | Change |
|---|---|
| `docs/migrations/CHANGELOG.md` | New §X entry: "v2 — FTS index added on `chunks.full_text`; legacy v0/v1 query helpers removed; ranking is hybrid (vector + BM25) with cue-driven metadata boost." Schema fields and field count unchanged (still 37). Index addition is index-level metadata, not a schema migration. |
| `community-brain/CLAUDE.md` | Update "Trade-offs we've deliberately kept" section. Remove the "Failed-extraction chunks are intentionally unsearchable" note's stale framing (still true, just rephrase to mention hybrid). Remove items from "Known v2 backlog" that v2 actually addresses. |
| `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` | New §10.x addendum after Phase 6 validation findings: "v2 hybrid retrieval — see `2026-04-27-hybrid-retrieval-v2-design.md`." Update findings 6 and 7 from "v2 backlog" to "addressed in v2 (link)." |
| `docs/inference-guidelines.md` | **No change.** The trust contract is independent of ranking strategy. |
| Open WebUI filter (`src/community_brain/openwebui/community_brain_filter.py`) | **No change.** Same POST body, same response shape. |

## 5. Cue rule design

### 5.1 Rule shape

```python
@dataclass(frozen=True)
class CueRule:
    """A single cue → metadata-boost mapping.

    The rule fires when ANY phrase in `cue_phrases` is found
    (case-insensitive substring) in the question, AND the chunk
    satisfies `target_predicate(chunk)`. When it fires, `delta` is
    added to the chunk's RRF score.
    """
    name: str                                   # for logging / debugging
    cue_phrases: tuple[str, ...]                # case-insensitive substrings
    target_predicate: Callable[[dict], bool]    # over chunk row dict
    delta: float                                # additive Δ on RRF score
```

### 5.2 Initial rule set

| Rule name | Cue phrases | Target predicate | Δ |
|---|---|---|---|
| `unresolved_questions` | `unresolved`, `open question`, `not answered`, `outstanding`, `didn't get answered`, `didn't get fully answered` | `chunk["has_unresolved_question"] is True` | 0.010 |
| `decisions` | `decision`, `decided`, `resolved`, `concluded` | `chunk["decisions"]` is non-empty list | 0.008 |
| `action_items` | `action item`, `commit`, `commitment`, `next step`, `to-do`, `todo`, `homework` | `chunk["action_items"]` is non-empty list | 0.008 |
| `insights` | `insight`, `realization`, `aha moment`, `key takeaway` | `chunk["has_insight"] is True` | 0.006 |
| `referenced_prior` | `referenced`, `prior call`, `last week`, `previously`, `discussed before` | `chunk["references_prior"] is True` | 0.006 |
| `questions_general` | `question`, `asked` | `chunk["has_question"] is True` | 0.003 |

Δ values are calibrated against the typical RRF score range for `k=60` and `top_k=10` (per-item scores hover around 0.01–0.03). Δ is large enough to break near-ties on flag-aligned chunks, small enough to avoid surfacing genuinely-irrelevant flagged chunks over relevant unflagged ones.

### 5.3 Maintenance model

Hardcoded Python tuple in `cue_rules.py`. The schema only has so many flag fields and structured arrays; the universe of useful rules is bounded. If the rule set churns weekly in operations, lift to YAML at `config/query-cues.yaml` and load on each `/query` call (cheap). Until then: keep it typed and version-controlled.

### 5.4 Boost composition

Multiple rules can fire on a single (question, chunk) pair. They compose additively: a chunk that satisfies both `unresolved_questions` (Δ=0.010) and `references_prior` (Δ=0.006) on a question that contains both cues gets a combined Δ=0.016. No cap, no diminishing returns — composition follows the underlying RRF score additivity.

### 5.5 Failure mode

If `apply_cue_boosts` raises (rule has a programming error, target predicate accesses a field that doesn't exist, etc.), the call site catches the exception, logs an `ERROR` with the rule name and question, and returns the **un-boosted RRF candidates**. Hybrid retrieval still works; just no metadata smarts on that one query. Subsequent queries are unaffected. This is "graceful degradation" applied to the boost layer.

## 6. FTS index lifecycle

### 6.1 Initial creation

- Server startup hook in `retrieval_server.py` calls `ensure_fts_index(table)` before binding the port.
- `ensure_fts_index` opens the `chunks` table, checks for an FTS index on `full_text`, and creates one if absent: `table.create_fts_index("full_text")`.
- Idempotent: repeated calls (e.g. on container restart) are no-ops.
- One-time cost: seconds for the current 167-chunk corpus, minutes after Plan C's ~2000-chunk full backfill. Cost paid in the `docker compose up` window, not in user-facing query latency.

### 6.2 Per-ingest update

- After `pipeline.ingest_session` successfully commits new chunk rows, it calls `optimize_fts_index(table)`.
- The exact mechanics of LanceDB FTS update-on-write will be **verified during the implementation phase** (whether new rows are auto-indexed or require explicit optimize). The design accommodates either: `optimize_fts_index` is a no-op if LanceDB auto-includes, an explicit rebuild call otherwise.
- Failure to optimize logs a warning but does not fail the ingest. The chunks are already committed; the FTS index will catch up on the next ingest's optimize call or the next server boot.

### 6.3 Missing index at query time

- If the FTS index disappears between server boot and a query (manual deletion, disk corruption, etc.), the LanceDB hybrid query raises an exception.
- `search_chunks` catches the exception, logs `WARN: FTS index unavailable, falling back to vector-only ranking`, and re-runs the query in vector-only mode. Cue boosts still apply over vector candidates.
- This is the same graceful-degradation pattern as §5.5: the retrieval server stays up; users get *some* ranked result; operator sees the WARN and rebuilds.

### 6.4 Embedding-model swap interaction

Out of scope for v2 but worth flagging: if a future operator swaps `nomic-embed-text` for a different embedding model (different vector dimension), the table is rebuilt anyway (vectors from different models are incompatible — see CHANGELOG.md §8.4). FTS index rebuild rides along with that rebuild for free. v2 doesn't add new constraints here.

## 7. API contract

### 7.1 Request — unchanged

```python
class QueryFilters(BaseModel):
    session_date_range: list[str] | None = None
    content_type: list[str] | None = None
    speakers_spoke: list[str] | None = None
    speakers_spoke_match: str = "any"
    speakers_mentioned: list[str] | None = None
    speakers_mentioned_match: str = "any"
    entities: list[str] | None = None
    entities_match: str = "any"
    keywords: list[str] | None = None
    keywords_match: str = "any"
    schema_version_min: str | None = None
    require_chunk_markers: list[str] | None = None
    exclude_chunk_markers: list[str] | None = None
    require_corpus_markers: list[str] | None = None
    exclude_corpus_markers: list[str] | None = None
    has_question: bool | None = None
    has_answer: bool | None = None
    has_unresolved_question: bool | None = None
    has_insight: bool | None = None
    references_prior: bool | None = None


class QueryRequestV2(BaseModel):
    question: str
    top_k: int = 10
    filters: QueryFilters | None = None
    response_shape: Literal["structured"] = "structured"
```

No field added, no field removed, no field semantically changed. The request body the Open WebUI filter sends today (`{"question": ..., "top_k": ...}`) continues to work.

### 7.2 Response — unchanged shape, different rankings

```python
class QueryResponseV2(BaseModel):
    query: str
    chunks: list[QueryChunkResult]
    total_matched: int
    filters_applied: dict
```

`QueryChunkResult` continues to carry `ground_truth` / `derived_metadata` / `provenance` / `similarity`. The `similarity` field continues to expose `1 - _distance` from the underlying vector ranking for backward-comprehensible interpretation by the answering LLM. The hybrid RRF score is internal; not surfaced in the response.

(Future v3 may introduce `score_breakdown: {vector_sim: float, bm25_rank: int, cue_delta: float}` for explainability. v2 keeps the response field-identical.)

### 7.3 Type-system rename

The class names `QueryRequestV2` and `QueryResponseV2` keep their `V2` suffix — those refer to the *response shape* contract (introduced in Plan A as the migration from v0's flat shape), not to retrieval ranking. Renaming would be a wider rippling refactor without operator value. v2 retrieval lives inside `search_chunks`, not in the request/response classes.

## 8. Performance budget

| Stage | Current p50 | v2 p50 (estimated) |
|---|---|---|
| Embed (Ollama nomic) | ~150–400 ms | unchanged |
| LanceDB query (vector-only, 167 chunks) | ~5–20 ms | n/a |
| LanceDB query (hybrid, 167 chunks) | n/a | ~10–30 ms |
| Cue boost pass (Python over 30 candidates) | n/a | < 1 ms |
| Total `/query` p50 | ~200–500 ms | ~250–550 ms |

p50 estimates assume corpus growth to Plan C's ~2000 chunks. At that scale LanceDB's FTS query is still sub-100ms range (it indexes once, queries against the index). The Open WebUI filter's 30s timeout has 50× headroom.

No latency budget concern justifies an opt-out. Hybrid is unconditionally on.

## 9. Validation plan

### 9.1 Golden query set (CI regression protection)

Ten queries in `tests/fixtures/golden_queries.yaml`, each with:
- `question`: free-form natural-language string
- `expected_chunk_ids`: list of `chunk_id` values that MUST appear in top-10
- `min_match_count`: minimum number from `expected_chunk_ids` that must be present (e.g. `≥3 of 5` for a query targeting 5 known-relevant chunks)
- `target_finding`: `"6"` (entity-grounded) or `"7"` (metadata-tagged)

The five Finding-6 queries cover the cases that motivated the spec (Adam from Gold Flamingo, etc.) and three other entity-grounded queries chosen to stress the lexical-match path.

The five Finding-7 queries cover each of the six cue rules at least once (decisions, action items, unresolved questions, insights, references_prior, questions general).

`tests/query/test_hybrid_search.py::test_golden_queries` runs the full `/query` path against an ephemeral test corpus seeded from the 8-session validation set (or a representative subset committed as a fixture). Any commit that breaks the golden assertions fails CI.

### 9.2 Lift validation (proves v2 is actually better)

For at least 3 of the 10 golden queries, the test asserts that **pure-vector baseline does NOT** satisfy `min_match_count`. This is computed by calling an internal helper (`_search_vector_only` — exposed for tests, not for HTTP) against the same corpus. The assertion enforces that the lift comes from hybrid + cue boosts, not from fixture luck.

### 9.3 Operator-side validation (post-deploy)

After the spec → plan → implementation cycle ships, run the five Phase 6 spec query types against the live Open WebUI filter (per Plan A spec §10 Phase 6). Document outcomes as a §10.x addendum in the Plan A spec. Success criteria:

- Finding 6 case: entity-grounded query returns ≥5 of the 8-session corpus's tagged chunks for `Adam` / `Gold Flamingo` in top-10. (Pure vector returned 0.)
- Finding 7 case: *"What unresolved questions came up?"* returns ≥5 of 38 corpus chunks tagged `has_unresolved_question=True` in top-10. (Pure vector returned 1.)
- All five spec query types continue to satisfy their original criteria.

If any criterion fails, tune Δ values in cue rules or `OVERSAMPLE_FACTOR` and re-validate. Do NOT merge until all pass.

## 10. Rollout

### 10.1 Sequence
1. Land the spec (this document) → plan → implementation across feature branch.
2. Run unit + integration tests; golden queries pass.
3. Build container, deploy to VM via `community-brain/docs/DEPLOYMENT.md` runbook.
4. Server's startup hook builds the FTS index on first boot. Logs `INFO: FTS index built on chunks.full_text in N.NNs`.
5. Operator validation: Phase 6 query types from the Open WebUI; document outcomes.
6. Update CLAUDE.md "Current status" and CHANGELOG.md with the deployed version.

### 10.2 Rollback

If validation surfaces a regression (some currently-good query degrades) and we can't tune it out:

- Hard rollback: redeploy the prior container image. The FTS index on disk is forward-compatible (old code ignores it; LanceDB doesn't fail on its presence). No data migration needed for rollback.
- Soft rollback (during validation, before merging to main): branch reverts cleanly because v2 changes are confined to `query/` and `ingestion/pipeline.py`'s post-commit hook.

### 10.3 Observability

- Each `/query` logs at DEBUG level: candidate count after RRF, count of cue rules that fired, top-K final IDs.
- `/query` continues to log at WARN/ERROR for degraded paths (FTS missing, cue exception).
- Existing `/health`, `/sessions`, `/speaker-aliases-block` endpoints unchanged.

## 11. Open questions for the implementation phase

1. **LanceDB FTS update-on-write semantics.** Verify whether new rows are auto-included in the FTS index after `table.add(...)` or whether `optimize_fts_index` must call `create_fts_index` again with `replace=True`. Both options accommodated by the design; just need to pick the right call.
2. **CLI `query_local.main()` fate.** Is the click-based CLI still used in practice? If yes, it gets reworked against v1 chunks schema + hybrid path. If unused (likely — the legacy `transcripts` table is gone), it gets deleted as part of the cleanup.
3. **`ensure_fts_index` and concurrent boots.** v1's registries-are-single-writer constraint means we don't run multi-worker uvicorn. But two-process boot (e.g. blue/green deploy) calling `create_fts_index` concurrently is theoretically possible. Confirm idempotency or wrap in a file-level lock if needed. Low-risk; flag for implementation.
4. **Test corpus fixture location and size.** The golden test needs a real (not synthetic) chunk corpus to exercise lexical+vector ranking. Either commit a subset of 8-session output as a small fixture (~167 chunks of artifact text), or generate a synthetic one. Decide during implementation.
5. **Rollback compatibility of the FTS index file.** §10.2 assumes a pre-v2 binary can open a post-v2 LanceDB directory (one that has an FTS index built) without failing. This is consistent with LanceDB's auxiliary-index design but worth verifying empirically before the operator-side validation cutover. If it turns out pre-v2 chokes on the index presence, rollback requires deleting the index directory before redeploying the prior image — still tractable, just a documented step.

### 11.1 Resolution

LanceDB FTS update-on-write behavior verified via `community-brain/scripts/spike_lancedb_fts.py` on 2026-04-28 (lancedb 0.30.2, the version pinned in `community-brain/.venv`):

- **Observed behavior:** auto-update. New rows added via `table.add(...)` after `create_fts_index("full_text")` are visible to subsequent `query_type="fts"` searches with no explicit refresh call.
- **Production hook:** `optimize_fts_index` is a no-op (returns immediately). Document the rationale inline so a future reader does not assume the function is dead code waiting to be removed; it exists as the seam where a future LanceDB version that drops auto-update can be patched without changing call sites in `pipeline.py` and the boot path.
- **Cost on current corpus:** initial `create_fts_index` on a 170-row stand-in took ~3.6ms; post-index `table.add(1 row)` took ~1.1ms; a follow-up FTS search returning the freshly-added row took ~2.4ms. Expect comparable numbers on the 167-chunk live corpus and sub-second numbers even at 10× growth.
- **Spike script output (relevant lines):**
  ```
  [ok] create_fts_index built
  [ok] FTS query returned 1 rows: ['a']
  [ok] hybrid query returned 2 rows: ['a', 'b']
  [after add, no optimize] FTS query for 'Adam LinkedIn' returned 2 rows: ['c', 'a']
  [ok] table.optimize() succeeded
  [after optimize] FTS query for 'Adam LinkedIn' returned 2 rows: ['c', 'a']
  [ok] create_fts_index(replace=True) succeeded
  [after replace] FTS query for 'Adam LinkedIn' returned 2 rows: ['c', 'a']
  ```
  The `[after add, no optimize]` line returning chunk `c` (inserted *after* the FTS index was built) is the decisive evidence: no optimize/replace required.
- **Side note for implementation (LanceDB 0.30.x):** the hybrid query API requires the explicit `table.search(query_type="hybrid").vector(...).text(...)` builder form. Passing the vector positionally to `search()` while also calling `.text(...)` raises `ValueError: You can either provide a string query in search() method or set vector() and text() explicitly for hybrid search. But not both.` Use the explicit-builder form in `pipeline.py` and the operator CLI, not the positional shortcut some older docs/snippets show.

## 12. Future work (v3 candidates)

Not part of v2; capturing here so they don't get lost:

- **LLM intent classifier.** If cue rules prove too brittle for compositional queries ("What unresolved questions did Adam raise about sales funnels?"), add an upstream LLM that emits a structured filter dict + ranking weights.
- **Cross-encoder reranker.** For high-stakes operator-driven queries where latency is acceptable, add an opt-in `rerank: true` flag that runs a `bge-reranker-large`-class model over the top-30 hybrid candidates.
- **Score breakdown in response.** Surface `{vector_sim, bm25_rank, cue_delta}` per chunk for UI debugging and answering-LLM citation hygiene.
- **Cue rules in YAML config.** Once the rule set churns weekly.
- **Synthesized BM25 field** (`topic_label + entities + speakers_spoke + full_text`). If entity coverage stays weak with `full_text`-only.
- **Weighted-sum fusion** as alternative to RRF, with operator-tunable `vector_weight` / `bm25_weight`.

---

## Appendix A — Why pure vector failed

Pure vector ranking via `nomic-embed-text` (768-dim cosine similarity over a structured `embed_text` representation per chunk) optimizes for **semantic-thematic similarity**: two chunks discussing the same concept space rank close even when they share zero proper-noun tokens. This is the *right* behavior for thematic queries (*"how do we approach onboarding?"*) and the *wrong* behavior for two distinct query patterns:

1. **Entity-grounded queries** want chunks where a specific proper noun appears in `full_text`. Vector similarity dilutes a single "Adam" mention against the broader thematic content of the chunk, ranking it below thematically-related chunks that don't mention Adam at all. BM25's IDF weighting flips the priority: rare tokens get high weight by definition, so "Adam" pulls a chunk to the top.

2. **Metadata-tagged queries** want chunks where a structured flag is set. Pure vector knows nothing about the schema's `has_unresolved_question` field — it embeds `embed_text` content. The cue-boost layer compensates by mapping question-side lexical cues to flag predicates and adding a small Δ that breaks ties in favor of flag-aligned chunks.

Hybrid (vector + BM25 + cue boost) preserves vector's strength on thematic queries while restoring the missing signals.

## Appendix B — Glossary

- **RRF (Reciprocal Rank Fusion):** Score-combining function for multi-source ranking. `score(item) = Σ 1/(k + rank_i(item))` across each source. Robust to score-scale differences between sources. `k=60` is the canonical constant.
- **BM25 (Best Match 25):** Lexical ranking function; the de-facto standard for keyword search. Weights tokens by inverse document frequency × term frequency × document length normalization. Captures rare-token importance that vector embeddings dilute.
- **FTS (Full-Text Search):** LanceDB's native lexical index, built on Tantivy. Per-column index; persistent on disk; queryable alongside vector via `query_type="hybrid"`.
- **Cue rule:** A 3-tuple of (question phrase set, chunk predicate, score delta). Fires when the question contains any cue phrase AND the chunk satisfies the predicate.
- **Oversample factor:** Internal multiplier on `top_k` for the candidate pool size before cue boosting. v2 uses 3 (i.e. 30 candidates for `top_k=10`).
- **Filter-then-rank:** Existing v1 contract — caller's `QueryFilters` apply as a WHERE clause before the ranker sees candidates. v2 preserves this and stacks hybrid scoring + cue boost on top.
