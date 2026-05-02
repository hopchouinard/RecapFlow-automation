# Community Brain — Schema and Extraction Migration Log

Every schema version bump or extraction-breaking change is recorded here.

## Entry template

```
## YYYY-MM-DD — vX.Y {short description}
- Change: {what changed}
- Rationale: {why}
- Migration: {automatic | reindex required | full re-ingest}
- Affected chunks: {scope}
- Rollback: {plan if this goes wrong}
```

## 2026-04-18 — v1.0 initial release

- Change: First release of the 37-field LanceDB schema and v1 extraction prompts.
- Rationale: Replaces the prior Open WebUI native RAG path and the old chunk schema. Adds the dual-field embedding architecture and structured metadata layer required by the query types in the spec.
- Migration: N/A — greenfield deployment.
- Affected chunks: None (empty corpus at release).
- Rollback: N/A for initial release.

## 2026-04-18 (addendum) — Env-var model and prompt overrides

- Added: `COMMUNITY_BRAIN_CHUNK_EXTRACTION_MODEL`, `COMMUNITY_BRAIN_SESSION_THEMES_MODEL`,
  `COMMUNITY_BRAIN_CHUNK_EXTRACTION_PROMPT`, `COMMUNITY_BRAIN_SESSION_THEMES_PROMPT`,
  `COMMUNITY_BRAIN_EMBED_MODEL` as deployment-time overrides for
  extraction-config.yaml and embedding.py defaults.
- Precedence: env var > YAML > built-in default. Empty env = use YAML.
- No schema change. No migration required for existing chunks.
- Known trade-off: switching `CHUNK_EXTRACTION_MODEL` or `SESSION_THEMES_MODEL`
  does not bump `extraction_prompt_version`. Re-ingesting existing sessions
  under a new model requires `force_reextract: true` on POST /ingest. This is
  intentional — the prompt file is the versioning anchor; model swaps with
  the same prompt produce broadly comparable output.

## v1.0 known limitations

- `speakers_mentioned` is not populated in v1 (always None). The field is
  reserved for a future Stage C extractor update that distinguishes
  "spoke in this chunk" from "was referenced/mentioned without speaking."
  v1 consumers should read `speakers_spoke` only.

## 2026-05-02 — `lint_corpus` decoupled from `/ingest` (no schema migration)

- Type: Architectural fix — corpus-lint integration. No schema change.
- Affected chunks: None directly. `corpus_markers_computed_at` semantic tightened
  (see below).
- Migration: Automatic. Operator must install daily cron after deploy
  (`/etc/cron.d/community-brain-lint` via `scripts/cron/install-cron.sh`).

### Why
`lint_corpus_chunks` was doing one `table.update()` per chunk per ingest, even
when the chunk's marker state didn't change (timestamp-bump only). At ~1500
chunks, that saturated LanceDB's manifest writer and surfaced as a
"Too many concurrent writers" retry storm. `/ingest` calls began exceeding
n8n's 30-minute HTTP timeout (observed 2026-05-02 04:11 UTC on session
`2025-12-09` — chunks committed, but `/ingest` never returned in time).

### Changes
- **`lint_corpus_chunks`:** drop the two no-op timestamp-bump branches.
  Function now writes only when a chunk's `corpus_derived_markers` actually
  changes. Stable corpus (no marker transitions) → 0 writes.
- **`_post_commit_maintenance`:** remove the `lint_corpus_chunks` call.
  Post-commit work is now just `verify_corpus_v3_state`. Unused `db_path`
  parameter dropped from signature; both call sites updated.
- **Operational:** lint runs via daily host cron at 04:00 UTC instead of
  inline after every `/ingest`. Files added: `scripts/cron/community-brain-lint.cron`,
  `scripts/cron/install-cron.sh`. System cron (`/etc/cron.d/`) is preferred;
  user crontab works as a fallback.

### Behavior change (deliberate)
- `corpus_markers_computed_at` semantics: was "timestamp of last lint pass that
  scanned this chunk." Now "timestamp of last meaningful marker change." Chunks
  that never qualify as recurrent retain `None` indefinitely. Operators can
  force a refresh of all chunks by running `lint_corpus_chunks(rebuild=True)`
  via the CLI, which rewrites markers from scratch.

### Tests
- 4 obsolete tests removed from `test_ingestion_pipeline.py` (3 were using
  "timestamp present" as an indirect proxy for "lint auto-fired" — broken by
  Change A semantics; 1 verified ingest survives lint failure — no longer a
  reachable scenario).
- 5 new/updated tests:
  - `test_lint_corpus_write_count_scales_with_state_changes_not_corpus_size`
    (parametrized 10/25/50 chunks; second-pass write count must be 0)
  - `test_lint_corpus_skips_writes_when_marker_state_unchanged`
  - `test_lint_corpus_writes_only_when_state_changes`
  - `test_post_commit_maintenance_does_not_call_lint_corpus`
  - `test_post_commit_maintenance_still_verifies_corpus_state`
- `test_lint_corpus_writes_corpus_markers_computed_at` and
  `test_lint_corpus_marker_update_non_destructive_on_failure` updated to use
  multi-session aligned corpora that trigger real state changes.

### Files changed
- Modified: `community-brain/src/community_brain/cli/lint_corpus.py`,
  `community-brain/src/community_brain/ingestion/pipeline.py`,
  `community-brain/tests/test_lint_corpus.py`,
  `community-brain/tests/test_ingestion_pipeline.py`,
  `community-brain/CLAUDE.md`.
- New: `scripts/cron/community-brain-lint.cron`,
  `scripts/cron/install-cron.sh`.
- Spec: `docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md`.
- Plan: `docs/superpowers/plans/2026-05-02-ingest-lint-decoupling-plan.md`.

### Rollback
`git revert <commit-hash> && docker compose up -d --build retrieval-server`
plus `sudo rm /etc/cron.d/community-brain-lint`. Behavior reverts to inline
auto-trigger; the storm returns at /ingest scale, but no data is at risk.

## 2026-04-29 — Schema 1.0 → 1.1 + Stage C v2 + FTS column migration (Retrieval v3)

### Schema changes
- Additive: new `bm25_text` string column on chunks. Synthesized at chunk write as the concatenation of `topic_label`, `entities`, `speakers_spoke`, `speakers_mentioned`, `keywords`, and `full_text`. Required at write time (every chunk has it).
- `SCHEMA_VERSION` bumps `1.0` → `1.1`.
- Field types and existing field semantics unchanged.

### Stage C contract change
- Active extraction prompt: `chunk-extraction-v1` → `chunk-extraction-v2`.
- v2 prompts the LLM to emit `entities` as a flat `list[str]` covering four conceptual categories (people, companies/orgs, products/tools, frameworks/standards/techniques) — no type discriminator is persisted; the categorization lives in the prompt's extraction guidance. Populates `speakers_mentioned` (deterministic subset of entities that are people not in `speakers_spoke`), populates `keywords` uniformly across all content types, drops `new_entities_seen` and `new_speakers_seen` from the JSON output schema.
- Stage C prompt accepts `SPEAKERS_SPOKE` as input context so `speakers_mentioned` partition is computed against an explicit speaker list.
- Pipeline applies a canonicalization pass at chunk write time, mapping `speakers_spoke` / `speakers_mentioned` / `entities` through `config/speaker-aliases.yaml`. Because the alias map only contains people, non-people entities (companies, products, frameworks) pass through unchanged. v3 has no analogous registry for non-people entities; they're stored raw.

### embed_text synthesis change (transcripts only)
- Prior: `topic: <X>\nsummary: <Y>` (~600 chars).
- v3: `topic + speakers + mentions + entities + keywords + summary` (~800 chars).
- Vector embeddings change for `prepared_transcript` chunks; `extracted_signal` and `community_post` chunks unaffected (their `embed_text == full_text`).

### Retrieval / index
- FTS index target column migrates from `full_text` to `bm25_text`. Server startup hook builds the new index; legacy index dropped on best-effort basis (LanceDB 0.30.x lacks a working `drop_index` API; helper graceful-degrades).
- All FTS-side queries pin `fts_columns="bm25_text"` to prevent silent fallback to a lingering legacy index.
- `cue_rules` data moves from hardcoded Python tuple to `config/query-cues.yaml`. Hot-reload on each `/query` call. Per-path last-known-good cache rescues transient YAML read errors.
- `/query` response gains `metadata_summary` top-level field (per-flag counts across retrieved chunks) and per-chunk `score_breakdown` (vector_similarity, bm25_rank, rrf_score, cue_delta, cue_rules_fired). Existing fields unchanged.

### Filter (Open WebUI) rendering
- Per-chunk `[flags: <names>]` line lists True boolean derived flags (uniform across `has_question`, `has_answer`, `has_unresolved_question`, `has_insight`, `references_prior`).
- Top-of-context `[corpus summary: of the N retrieved chunks, ...]` line carries authoritative aggregate counts.
- `expose_score_breakdown` valve (default off) opts in to per-chunk `[score: vector=X, bm25=Y, rrf=Z, cue=+W (rules)]` line for operator-side debug.
- Trusted tags structurally separated from raw transcript content: `[flags:]` / `[corpus summary:]` / `[score:]` rendered OUTSIDE `<transcript_data>...</transcript_data>` wrapper; transcript content inside. Position contract documented in `docs/inference-guidelines.md`.
- Corpus summary recomputed post-`min_score` filter so it reflects only chunks the LLM sees.

### Corpus-lint
- New `recurrent` marker populated by the `lint_corpus` pass. K=8 nearest neighbors over the embedding column; chunks whose neighbors span 2+ distinct sessions at similarity ≥ 0.65 receive the marker.
- Auto-triggered at end of `/ingest` (WARN-on-failure; chunks already committed).
- Atomic marker writes via `table.update()` (not delete+add) so failures don't risk row loss.

### Operator pattern (canonicalization)
- Three new CLIs: `propose_canonicalizations` (heuristic merge proposals from pending queue), `apply_canonicalizations` (merges proposals into registry; auto-triggers recanonicalize; `--no-recanonicalize` escape), `recanonicalize` (standalone chunk-rewrite pass; re-applies registry; re-embeds when needed).
- Validates proposals before write to refuse alias-canonical conflicts (raises `ProposalConflictError`).
- Snapshot+restore on failure to minimize data loss in the rare double-failure case.

### Migration sequence (one-time, see spec §17.1)
1. Drop existing v1.0 chunks table.
2. Run `propose_canonicalizations` → operator reviews YAML → run `apply_canonicalizations --no-recanonicalize` (chunks table is empty after step 1).
3. Re-extract 9 ingested sessions via `/ingest` with `force_reextract: true`. First ingest creates v1.1 schema with `bm25_text`; subsequent ingests append.
4. Run validation gate (8 criteria — see spec §16.1).
5. Plan C kickoff.

### Files changed (high-level)
- New modules: `community_brain.ingestion.bm25_synthesis`, `.canonicalize`, `.cli.propose_canonicalizations`, `.cli.apply_canonicalizations`, `.cli.recanonicalize`, `.cli.lint_corpus`.
- Modified: schema (38 fields), pipeline (canonicalization + bm25_text + lint auto-trigger), extractor (v2 prompt parsing), embedding (build_transcript_embed_text), query_local (score_breakdown + metadata_summary + YAML cue rules + fts_columns binding), retrieval_server (response shape + FTS migration), cue_rules (YAML loader + last-known-good cache), fts_lifecycle (column param + drop helper), openwebui filter (rendering + valves + parity).
- Tests: 100+ new tests across the surface; 4 pre-existing infrastructure failures unchanged.

## 2026-04-28 — Hybrid Retrieval v2 (no schema migration)

- Type: Retrieval-layer change (additive index, no schema migration).
- Scope: `community_brain.query` package, `community_brain.ingestion.pipeline`.
  No change to chunks-table schema (still 37 fields, schema_version
  unchanged at "1.0").

What changed:

- LanceDB FTS index added on `chunks.full_text` (Tantivy-based, native to
  LanceDB 0.30.x).
- `/query` ranker is now hybrid (vector + BM25, RRF k=60) with oversampling
  3× and a Python cue-boost post-processing layer that promotes chunks
  whose metadata flags align with question-side lexical cues. See
  `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`.
- Legacy v0 (`transcripts`-table) helpers removed:
  `query.__init__.build_filter_expression`, `query_local.search_chunks`
  (v0), `query_local.format_results`, `query_local.build_answer_prompt`,
  `query_local`'s click CLI, and the entire `query_openai.py` (an
  OpenAI-targeted CLI sibling, also dead).
- `query_local.build_filter_expression_v2` renamed to
  `build_filter_expression`. `query_local.search_chunks_v2` renamed to
  `search_chunks`. Test file `tests/test_query_local_v2.py` renamed to
  `tests/test_query_local.py`.
- New modules: `community_brain.query.cue_rules` (CueRule dataclass,
  6-rule initial set, `apply_cue_boosts` with graceful rule-failure
  handling) and `community_brain.query.fts_lifecycle`
  (`ensure_fts_index` idempotent boot helper, `optimize_fts_index`
  no-op refresh seam).
- FastAPI startup lifespan ensures the FTS index on boot.
  `pipeline.ingest_session` calls `optimize_fts_index` after each
  successful chunk commit (no-op under LanceDB 0.30.x auto-update path;
  kept as a future-proofing seam).
- `retrieval_server` version bumped from `0.1.0` to `0.2.0`.

Operator action required:

- None. First boot of the new container builds the FTS index automatically.
- Open WebUI filter and n8n workflows continue to work without change.

Rollback:

- Redeploy prior container image. The on-disk FTS index is auxiliary
  metadata that pre-v2 binaries ignore (consistent with LanceDB's
  auxiliary-index design; spec §11.5 flagged for empirical verification
  at operator-side cutover, T16).
- If pre-v2 chokes on the index presence, recovery is to delete the FTS
  index directory under the LanceDB store before redeploying. Tractable,
  just a documented step.

Validation:

- 296 unit + integration tests pass on the feature branch.
- Golden query suite (`tests/test_golden_queries.py`) covers Findings 6
  (entity-grounded) and 7 (metadata-tagged) with lift-validation
  assertions that prove the hybrid+cue layers — not corpus luck —
  surface the target chunks.
- Operator-side validation against the live VM (Phase 6 query types per
  Plan A spec §10) is task T16 of the plan, post-merge.
