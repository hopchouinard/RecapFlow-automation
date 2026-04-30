# Community Brain Retrieval v3 + Stage C v2 — Design

**Status:** Draft
**Date:** 2026-04-29
**Owner:** Solo operator (no other clients in production)
**Supersedes:** Stage C extraction prompt v1 (`chunk-extraction-v1`), schema v1.0, and the v2 retrieval pipeline's `full_text`-anchored FTS index.

---

## 1. Motivation

Hybrid Retrieval v2 (deployed 2026-04-28) closed the retrieval-layer gaps identified in Findings 6 and 7 — entity-grounded queries went from 0/10 → 6/10 hits, metadata-tagged queries from 1/10 → 6/10. Live-VM validation surfaced **Finding 8**: the answering LLM under-utilizes Stage C's `has_unresolved_question` flag because the trust contract correctly tells it to re-derive from text, and that flag's textual cue is uniquely subtle (an awkward pause, a `?` mark, a soft topic-change).

A 2026-04-29 audit of the live 9-session corpus, run **before** kicking off Plan C's remaining ~57-session backfill, surfaced gaps that go beyond Finding 8:

- **`entities` array is 100% empty (0/184 chunks).** Not "underpopulated" — never populated. Cross-validation: every proper-noun probe (Adam, Brandon, Claude, Cursor, Gemini, OpenAI, Anthropic, Cursor, etc.) has 100% miss-rate between `full_text` and `entities`. The `entities` filter parameter on `/query` has been functionally dead for the entire life of v1.
- **`speakers_mentioned` is 100% None** (consistent with the schema v1.0 docstring, which explicitly notes the field is reserved for a future Stage C update). Ditto effective deadness.
- **`speakers_spoke` lacks canonicalization.** 47 unique speaker tokens across 9 sessions; visible duplicates (`Adam` + `Adam - Gold Flamingo` + `Adam James`; `delvis` + `Delvis Nunez`; `asako` + `Asako Hayase`; `Bastian` + `Bastian Venegas`; raw Zoom display strings like `David's iPhone`). The `speaker-aliases.yaml` registry has 4 canonicalized aliases and 40+ entries in the `pending:` queue that have never been promoted. Pipeline correctly populates pending; operator-curation step has never been operated.
- **`keywords` extraction skipped for `community_post` and `extracted_signal`.** Empty for all 64 such chunks; only populated for `prepared_transcript` (mean length 11.5 entries).
- **`corpus_derived_markers` and `corpus_markers_computed_at` are 100% empty/null.** No populating pass exists.

The "do this once" pressure of Plan C makes these gaps load-bearing in a way they weren't pre-v2. Re-running 73 sessions through a known-broken Stage C extractor, only to fix it later, is the precise pay-twice anti-pattern Plan C was held to avoid. v3 closes every Bucket-1 (re-extraction-required) gap in a single coordinated release.

This document specifies that release. It bundles the F8 narrow fix (paths (b) and (c) from the Plan A spec §10 v2 validation addendum), Stage C v2 (entities + speakers_mentioned + uniform keywords + enriched embed_text), speaker canonicalization tooling and operational pattern, the v2 §12 secondary candidates that don't introduce new model dependencies (synthesized BM25 field, score breakdown in response, YAML cue rules), and a corpus-lint pass for the recurrent marker.

## 2. Goals and non-goals

### 2.1 Goals
- Close every Bucket-1 audit gap before Plan C: empty `entities`, dead `speakers_mentioned`, asymmetric `keywords`, lacking-canonicalization `speakers_spoke`.
- Resolve Finding 8 at the presentation layer (paths (b) inline-flag rendering and (c) `metadata_summary` response field) without re-litigating the trust contract.
- Move the FTS index from `full_text` to a synthesized `bm25_text` so the lexical path benefits from the newly-populated structured fields.
- Establish a `recanonicalize` operational pattern that decouples name-substitution from extraction so future name additions don't trigger re-extracts.
- Populate `corpus_derived_markers` via a single-marker (`recurrent`) lint pass that auto-fires after `/ingest`.
- Add explainability: per-chunk `score_breakdown` in `/query` responses; cue rules in YAML for hot-reload tuning.
- Preserve the existing `/query` request/response contract structurally — additive fields only (`metadata_summary` top-level; `score_breakdown` per-chunk).
- Preserve the trust partition (`ground_truth` / `derived_metadata` / `provenance`) unchanged at the structural level.

### 2.2 Non-goals
- LLM intent classifier (deferred — would have been v2 §12 item 5f). v4 candidate.
- Cross-encoder reranker (deferred — v2 §12 item 5e). v4 candidate, only motivate if post-v3 retrieval validation shows hybrid + bm25_text + cue boost still misses.
- Weighted-sum fusion (deferred — v2 §12 item 5d). RRF stays.
- Trust-contract revision (Finding 8 fix path (a)). `inference-guidelines.md` gets a 2-3 sentence additive section documenting the new presentation tags; the partition itself does not change.
- Entity-canonicalization registry for non-people entities (companies, products, frameworks). v3 keeps people-only canonicalization. v4 candidate.
- Improvements to `decisions` / `action_items` / `topic_label` / `session_themes` Stage C content. The 2026-04-29 audit confirmed these are good as-is.
- Multi-writer registry support, `/reindex` mutating verbs, deep `/health`, read/write API key split. Pre-existing v2 backlog items unrelated to the F8 / audit motivations.

### 2.3 Explicit semantic break
v3's `/query` response is a **superset** of v2's: existing fields preserved structurally; two additive fields (`metadata_summary` top-level; `score_breakdown` per-chunk). Existing clients (Open WebUI filter, n8n workflows) continue to work without code change. The Open WebUI filter ships in lockstep to gain the new `[flags: ...]` and `[corpus summary: ...]` rendering and the `expose_score_breakdown` valve.

The `/ingest` contract is unchanged. The Stage C internal contract (`extraction_prompt_version`) bumps from `chunk-extraction-v1` to `chunk-extraction-v2`; idempotency is preserved via the existing version anchor.

## 3. Audit-driven scope

This spec was scoped from a 2026-04-29 audit of the live 9-session, 184-chunk corpus on the n8n VM's retrieval-server container. Methodology: pyarrow scan of the LanceDB chunks table; per-field fill rates, distribution analyses, cross-validation of proper-noun mentions in `full_text` vs the `entities` array, and inspection of speaker-token uniqueness against the alias registry. Full results in Appendix A.

Audit findings drove every scope decision in §2 and the design choices in §6-§12. The audit is not part of v3 itself (it's a pre-design exercise), but its output is the load-bearing rationale for what's in v3 vs what's deferred.

## 4. Architecture

### 4.1 End-to-end flow

```
[ Stage A: parse artifacts ]            ← unchanged
[ Stage B: session-level extraction ]   ← unchanged (session_themes etc.)
[ Stage C v2: per-chunk extraction ]    ← REVISED (entities, speakers_mentioned, keywords uniform)
        ↓
[ Canonicalization pass ]               ← NEW: registry → speakers_spoke / speakers_mentioned / people-entities
        ↓
[ embed_text synthesis ]                ← REVISED (transcripts get enriched format)
[ bm25_text synthesis ]                 ← NEW: topic + entities + speakers + keywords + full_text
        ↓
[ Embed via Ollama nomic ]              ← unchanged
        ↓
[ LanceDB commit ]                      ← unchanged
        ↓
[ FTS auto-update on bm25_text ]        ← MIGRATED (was full_text)
        ↓
[ lint_corpus auto-trigger ]            ← NEW: recurrent marker, K=8 / T=0.65 / cross-session ≥ 2
        ↓
[ ingest_session returns ]
```

### 4.2 Retrieval flow (v3)

```
question
  │
  ├─ Ollama embed → vector candidates (top_k * 3)
  │
  └─ Tokenize → BM25 candidates (top_k * 3)
                         (now indexed over bm25_text)
                              │
              LanceDB native hybrid query
                  RRF fusion, k=60 (unchanged from v2)
                              │
            filter-then-rank guard:
              extraction_status='success' + caller's QueryFilters
                              │
                  fused candidates (top_k * 3)
                              │
              cue-boost pass (cue_rules.yaml-loaded):
                additive Δ on RRF score per matched cue
                              │
              record per-chunk: vector_similarity, bm25_rank, rrf_score,
                                cue_delta, cue_rules_fired
                              │
                  re-sort by boosted score, truncate to top_k
                              │
              compute metadata_summary across top_k:
                of_top_k + has_*_count for each boolean flag
                              │
            structured response
              chunks[] (with score_breakdown), metadata_summary, etc.
```

### 4.3 Operational loop (post-deploy, ongoing)

```
Weekly call ingested (Workflow 1)
  → chunks written with raw extracted names (canonicalized via current registry)
  → new names accumulate in pending: queue
  → lint_corpus auto-fires; corpus_derived_markers refreshed

Periodic (operator-triggered, when pending: queue has accumulated):
  1. propose_canonicalizations          → emits proposals YAML
  2. operator reviews + edits the YAML
  3. apply_canonicalizations            → updates registry; auto-triggers recanonicalize
  4. recanonicalize                     → rewrites affected chunks; re-embeds; re-synthesizes bm25_text

Manual edit to speaker-aliases.yaml:
  → operator runs recanonicalize standalone
```

The recanonicalize pass is **decoupled from Stage C extraction**. Future name additions require only a per-chunk re-embed (~50ms each via local Ollama); they never trigger re-extraction. Realistic per-week cost: 1-5 seconds. One-time post-Plan-C bulk: 15-30 seconds.

### 4.4 Trust-partition layering (unchanged structurally)

```
chunks[].ground_truth        ← authoritative; quotes must resolve here
chunks[].derived_metadata    ← LLM-interpreted; probabilistic; re-derivable
chunks[].provenance          ← tracks what generated it
chunks[].similarity          ← v2 contract: vector cosine, 1 - _distance
chunks[].score_breakdown     ← NEW (v3): retrieval-derived; orthogonal to trust partition
metadata_summary             ← NEW (v3): top-level corpus-aggregate; authoritative count of derived flags across retrieved set
```

`score_breakdown` and `metadata_summary` are **retrieval-derived**, not Stage-C-derived. They sit alongside the trust partition rather than inside it; the answering LLM can use them as authoritative facts about the *retrieval* (e.g. "of the top-10 chunks, 6 are tagged `has_unresolved_question`") without conflict with the contract that derived per-chunk metadata is probabilistic.

## 5. Schema changes (v1.0 → v1.1)

### 5.1 Field addition: `bm25_text`

```python
@dataclass
class Chunk:
    # ... existing 37 fields ...
    bm25_text: str  # NEW (38th field)
```

- Type: `pa.string()` in pyarrow schema.
- Required at write time (every chunk has it; not nullable).
- Synthesized as: `topic_label + "\n" + ", ".join(entities) + "\n" + ", ".join(speakers_spoke) + "\n" + ", ".join(speakers_mentioned) + "\n" + ", ".join(keywords) + "\n" + full_text` (with empty arrays rendered as empty strings).
- Re-synthesized in `recanonicalize` when any constituent field changes.

### 5.2 SCHEMA_VERSION bump

`schema.py`: `SCHEMA_VERSION = "1.1"`. Existing 9-session chunks are written under `schema_version="1.0"`; v3 re-extraction overwrites them with `schema_version="1.1"`. The `schema_version_min` filter in `QueryFilters` lets future callers gate on minimum schema if needed.

### 5.3 Migration entry

Add to `docs/migrations/CHANGELOG.md`:
- §X.1 — schema 1.0 → 1.1: additive `bm25_text` column. FTS index target migrates from `full_text` to `bm25_text` at deploy time.
- §X.2 — Stage C contract change: `chunk-extraction-v1` → `chunk-extraction-v2`. Triggers re-extraction of all v1 chunks. New prompt populates `entities` (typed proper nouns), `speakers_mentioned` (people not in `speakers_spoke`), `keywords` uniformly across content types.
- §X.3 — `embed_text` synthesis change for `prepared_transcript`: prior format `topic + summary` becomes `topic + speakers + mentions + entities + keywords + summary`. Vector embeddings change for transcript chunks; signal/post chunks unaffected (their `embed_text == full_text`).

### 5.4 What does NOT change in the schema

- `speakers_mentioned` field type (`list[str] | None`) — unchanged. Its value goes from "always None" to "deterministic subset of entities-people not in speakers_spoke."
- `entities` field type (`list[str]`) — unchanged. Its value goes from "always empty" to "typed proper nouns across 4 categories."
- `corpus_derived_markers` and `corpus_markers_computed_at` types — unchanged. Values populated by the new `lint_corpus` pass.
- Trust partition assignments (which fields are ground_truth vs derived_metadata vs provenance) — unchanged.

## 6. Stage C v2 prompt revision (item 1)

### 6.1 `entities` extraction

The Stage C prompt extracts `entities` as a typed list of proper nouns spanning four categories:

- **People** — proper-noun human names (e.g. "Adam James", "Andrej Karpathy"). Stored in canonical-full-name form when the speaker registry recognizes them; raw form otherwise.
- **Companies / orgs** — e.g. "OpenAI", "Anthropic", "Gold Flamingo", "Microsoft".
- **Products / tools** — e.g. "Claude Code", "Cursor", "n8n", "LanceDB", "Ollama", "Sonnet 4.6".
- **Frameworks / standards / techniques** — e.g. "RAG", "MCP", "OAuth", "BM25".

Excluded:
- Places (rarely meaningfully part of context for these calls).
- URLs / hashes (already captured in `external_refs`).
- Generic nouns ("the team", "users", "developers").

Normalization rules:
- Case-preserved canonical form ("Claude Code" not "claude code").
- De-duplicated within a chunk (same entity appearing twice in `full_text` produces one entry).
- No internal aliasing for non-people categories — raw extracted strings only. Canonicalization for people-typed entries happens in the canonicalization pass (§7), driven by `speaker-aliases.yaml`.

### 6.2 `speakers_mentioned` population

The Stage C prompt extracts `speakers_mentioned` as the deterministic subset of `entities` that are people AND who are not in this chunk's `speakers_spoke`. Useful for "what did the group say about <name>?" queries — filter on `speakers_mentioned` to find chunks where the person is talked-about rather than present.

The prompt explicitly instructs Stage C to emit two related fields:
- `entities` — broad list across all four categories above.
- `speakers_mentioned` — the people-typed subset of entities, filtered against `speakers_spoke`.

This avoids the schema partition becoming "guess from entities" at write time; Stage C produces both fields directly.

### 6.3 `keywords` uniform extraction

Stage C v2 extracts `keywords` for all three content types: `prepared_transcript`, `extracted_signal`, `community_post`. Prior asymmetry (transcript-only) is corrected.

Keyword extraction guidance in the prompt:
- Topical keywords (tools, techniques, concepts, frameworks).
- 5-15 keywords per chunk (mean target ~10).
- De-duplicated within a chunk.
- Useful for `bm25_text` enrichment + `keywords` filter on `/query`.

### 6.4 `embed_text` enriched synthesis (transcripts only)

Pre-v3 transcript `embed_text` synthesis:
```
topic: <topic_label>
summary: <LLM-written summary>
```
~600 chars; pure thematic distillation. Loses entity-grounding for vector search.

v3 transcript `embed_text` synthesis:
```
topic: <topic_label>
speakers: <speakers_spoke joined with ", ">
mentions: <speakers_mentioned joined with ", ">
entities: <entities joined with ", ">
keywords: <keywords joined with ", ">
summary: <LLM-written summary>
```
~800 chars typical. Vector index now grips on proper nouns, not just thematic content. Both retrieval paths (vector + BM25 over `bm25_text`) become entity-aware after v3.

`community_post` and `extracted_signal` continue to use `embed_text == full_text` (per the v1.0 design — these content types are already structured / themed at write time). The audit confirmed this works; not changing.

### 6.5 What other Stage C fields stay unchanged

The 2026-04-29 audit confirmed quality on:
- `topic_label` — descriptive multi-word labels for transcripts; section labels for signals/posts.
- `session_themes` — Stage B output; 4-5 descriptive themes per session.
- `decisions` — quality good when populated; 47/184 chunks.
- `action_items` — quality good when populated; 80/184 chunks.
- `external_refs` — 77/184 chunks; URLs and references captured cleanly.
- `speech_acts` — clean 12-token vocabulary, well-distributed.
- `stance` — distribution reflects corpus character (positive 96, neutral 51, mixed 25, negative 2 — coaching calls skew constructive).
- `certainty` — distribution reflects corpus (asserted 174, hedged 9, speculative 1 — participants tend to assert).
- `chunk_local_markers` — 4 unique tokens (emphasized, resolved, breakthrough, sustained); sparse but consistent.
- All five `has_*` boolean flags + `references_prior` — accuracy validated against textual cues.

The v2 prompt only changes the four areas above (§6.1-§6.4); everything else carries over.

## 7. Speaker canonicalization (item 2)

### 7.1 Three CLIs

**`community_brain.cli.propose_canonicalizations`** — generates merge proposals from the current `pending:` queue and existing canonicals in `speaker-aliases.yaml`. Writes to `community-brain/canonicalization-proposals.yaml`:

```yaml
generated_at: 2026-04-29T03:00:00Z
proposals:
  - canonical: "Delvis Nunez"
    candidate_aliases:
      - "delvis"
    confidence: high
    reason: "case-insensitive exact match"

  - canonical: "Adam James"
    candidate_aliases:
      - "Adam"
      - "Adam - Gold Flamingo"
    confidence: medium
    reason: "token containment, single canonical candidate; verify whether all 'Adam' instances refer to the same person"

ambiguous:
  - "David's iPhone"
    reason: "Zoom display name; no canonical found"
  - "Tony"
    reason: "first name only; multiple candidate canonicals"
```

Heuristics, in order of confidence:
- **High** — case-insensitive exact match between pending entry and a canonical alias; first-name match where exactly one canonical full-name candidate exists.
- **Medium** — token containment with single canonical candidate; affiliation-suffix patterns ("X - Company Y" → "X" canonical).
- **Low / ambiguous** — first names with multiple canonical candidates; raw Zoom display names without an obvious canonical. Surfaced under `ambiguous:` with no auto-proposal.

The CLI is non-mutating (read-only on the registry; write-only to the proposals file).

**`community_brain.cli.apply_canonicalizations`** — reads an edited proposals YAML, merges accepted proposals into `config/speaker-aliases.yaml` (under `aliases:`, removing applied entries from `pending:`), then auto-triggers `recanonicalize` to rewrite affected chunks. CLI flag `--no-recanonicalize` skips the auto-trigger for dry-run inspection between apply and recanonicalize.

**`community_brain.cli.recanonicalize`** — standalone chunk-rewrite pass. For each chunk in the LanceDB table:
1. Read `speakers_spoke`, `speakers_mentioned`, `entities`.
2. Apply current `speaker-aliases.yaml` map to person-bearing fields (people-typed entries within `entities` are detected by checking the alias map; any string matching a registered alias gets replaced with the canonical form).
3. If any field changed: re-synthesize `embed_text` (transcripts) and `bm25_text` from current Stage C outputs; re-embed `embed_text`; write the row back.
4. If nothing changed: no-op fast scan.

Cost characteristics:
- No Stage C LLM call (the entire point — decoupled from extraction).
- Re-embed via Ollama nomic: ~50ms per chunk.
- BM25 index auto-updates on row writes (verified in v2 spike: lancedb 0.30.2 auto-includes new content without explicit optimize).
- Idempotent (running with no changes = fast scan).

Realistic per-week cost (typical ingest + small pending queue): 1-5 seconds.
One-time post-Plan-C bulk cleanup: 15-30 seconds.
Adversarial worst case (registry-wide rewrite): ~75 seconds.

### 7.2 Ingest-time canonicalization pass

`pipeline.py` adds a canonicalization pass before chunk write. Inputs: Stage C v2 outputs (`speakers_spoke`, `speakers_mentioned`, `entities`). Behavior:
1. For each person-bearing field, replace each entry with its canonical form (looked up in the in-memory registry).
2. For entries not in the registry, append to `pending:` (existing behavior preserved).
3. The unchanged-name case is the common path; only newly-seen names trigger the pending-append flow.

This means new chunks land already-canonicalized for any name the registry has seen; new names accumulate in pending until the operator runs propose+apply (which then triggers recanonicalize for the older chunks containing those names).

### 7.3 Sequencing relative to v3 deploy

```
1. Land v3 code; tests green
2. Deploy container to VM
3. Run propose_canonicalizations
4. Operator reviews canonicalization-proposals.yaml; edits as needed
5. Run apply_canonicalizations (auto-triggers recanonicalize → no-ops since no chunks exist with v2 data yet)
6. Re-extract 9 ingested sessions (force_reextract: true on /ingest, one per session)
   - Each ingest applies the now-curated registry at write time
   - Each ingest auto-triggers lint_corpus
7. Validation suite (criteria 12.1-12.8 of the brainstorming Q12)
8. Plan C kickoff
```

If canonicalization is skipped or done backwards (re-extract before curating), the result is two re-extraction passes (once with raw names, once after registry curation). The sequencing above pays the curation cost first and re-extracts once.

## 8. F8 narrow fix and presentation layer (item 3)

### 8.1 Path (b) — inline-flag rendering in the Open WebUI filter

Filter (`community_brain_filter.py`) renders one tag line per chunk above `full_text` listing every True boolean flag in `derived_metadata`:

```
[flags: unresolved_question, references_prior]
{full_text content}
```

Format rules:
- Only true flags are listed (chunks with no true flags get no tag).
- Flag names match the schema field name without the `has_` prefix where relevant: `unresolved_question` (from `has_unresolved_question`), `question` (from `has_question`), `answer` (from `has_answer`), `insight` (from `has_insight`), and `references_prior` (no prefix to strip).
- Tag is one line above `full_text`, separated by a single newline.
- Compact comma-separated form; no JSON, no all-caps, no escape characters.

The renderer is uniform across all `has_*` flags + `references_prior` (per Q8.2 decision B). No per-flag special-casing in code; the only special thing about `has_unresolved_question` is the corpus-level cue rule's Δ value (which lives in `query-cues.yaml`, not in the filter).

### 8.2 Path (c) — `metadata_summary` field on `/query` response

Top-level field on `QueryResponseV2`, sibling to `chunks` / `total_matched` / `filters_applied`:

```python
class QueryResponseV2(BaseModel):
    query: str
    chunks: list[QueryChunkResult]
    total_matched: int
    filters_applied: dict
    metadata_summary: dict  # NEW
```

Content of `metadata_summary` (per Q8.3 decision B — uniform booleans, no array counts):

```json
{
  "of_top_k": 10,
  "has_question_count": 4,
  "has_answer_count": 3,
  "has_unresolved_question_count": 6,
  "has_insight_count": 5,
  "references_prior_count": 2
}
```

Computed by `search_chunks` over the top-K candidates after cue-boost re-sort and truncation. `of_top_k` reflects the actual candidate count (handles the corner case where fewer than `top_k` results survive filtering).

### 8.3 Filter rendering: corpus summary

The filter prepends a single line at the top of the LLM-facing context, derived from `metadata_summary`:

```
[corpus summary: of the 10 retrieved chunks, 6 are tagged unresolved_question, 5 are tagged insight, 4 are tagged question, 3 are tagged answer, 2 reference prior]

--- chunk 1 ---
[flags: unresolved_question]
{chunk content}
...
```

Format rules:
- Only true counts are listed (counts of zero are omitted to reduce noise).
- Counts ordered by descending value (most-prevalent flag first).
- Singular vs plural ("1 reference prior" vs "2 reference prior") — keep singular form for simplicity; not worth a pluralization library for stylistic polish.

This primes the answering LLM with authoritative aggregate counts before it reads chunks. The trust contract still applies (chunk-level `derived_metadata` is probabilistic), but the corpus-level "X of N retrieved chunks are tagged" is a retrieval-derived fact, not a Stage C derivation, and the model can lean on it.

### 8.4 Inference-guidelines.md additive section

Add a 2-3 sentence section at the end of `docs/inference-guidelines.md`:

> ### Presentation tags
>
> When the answering context contains lines like `[flags: <flag_names>]` (per-chunk) or `[corpus summary: <counts>]` (above all chunks), these are presentation conventions exposing structured derived metadata. The `[flags: ...]` line lists boolean derived flags that Stage C marked True for the immediately-following chunk. The `[corpus summary: ...]` line gives authoritative counts of those flags across the retrieved set. Both are derived (the same trust-contract caveats apply — re-derive from `full_text` when in doubt), but they reflect what Stage C and the retrieval layer concluded; they are not invented by you.

This documents the convention without modifying the trust contract. A test enforces parity between this docs string and the constant embedded in `community_brain_filter.py` (per the existing `test_inference_guidelines_match_docs_file` pattern).

## 9. Corpus-lint pass (item 4)

### 9.1 New CLI: `community_brain.cli.lint_corpus`

Operates on the existing chunks table. For each chunk:
1. Look up the K=8 nearest neighbors of its `embedding` in the chunks table (using LanceDB's vector index).
2. Filter neighbors with cosine similarity above T=0.65.
3. Count how many of those above-threshold neighbors come from a different `session_id` than the chunk itself.
4. If that count is ≥ 2, append `recurrent` to the chunk's `corpus_derived_markers` list (deduplicating if already present from a prior run).
5. Set `corpus_markers_computed_at` to the current UTC timestamp regardless of whether markers changed.
6. Write the row back.

Tunable constants (initial values, hardcoded):
- `K_NEAREST = 8`
- `SIMILARITY_THRESHOLD = 0.65`
- `CROSS_SESSION_COUNT_MIN = 2`

Not exposed as config in v3. If empirical tuning is needed, lift to YAML in v4.

### 9.2 Auto-trigger from `/ingest`

`pipeline.ingest_session` calls `lint_corpus` at the very end of a successful session ingest, after the new chunks are committed to LanceDB. Adds ~5-15 seconds to `/ingest` latency for the current corpus size; remains tractable even at Plan-C-end ~1500 chunks (the K-nearest scan is O(N · K) using the existing vector index, not a full pairwise scan).

If `lint_corpus` fails (logs WARN; does not fail the ingest — chunks are already committed). The next `/ingest` or manual `lint_corpus` run will catch up.

### 9.3 Idempotency

Running `lint_corpus` twice on an unchanged corpus produces identical markers. Running after a new session is added produces markers reflecting the larger corpus (some chunks that were previously unique may flip to `recurrent` once their neighbor count rises). This is the desired behavior.

### 9.4 What `recurrent` means semantically

A chunk is `recurrent` when its embedding sits in a topical cluster that spans 2+ sessions. The threshold T=0.65 is tuned to capture genuine topical alignment without flagging coincidental similarity (e.g., two chunks that both contain timestamp lines and greetings). The `embedding` field is now enriched with entities/keywords/speakers via §6.4, so "topical similarity" reflects entity overlap and keyword alignment in addition to semantic content.

Initial expected fill rate (the 9-session validation corpus): ≥ 30% of chunks marked `recurrent` (most sessions share themes per the audit's `session_themes` inspection — "developer personal branding" appears in multiple sessions; "AI agent architecture" recurs; etc.).

## 10. Synthesized BM25 field (item 5a)

### 10.1 Schema column `bm25_text`

Per §5.1: new required string column on the chunks table, synthesized at chunk write as:

```
{topic_label}\n{entities joined with ", "}\n{speakers_spoke joined with ", "}\n{speakers_mentioned joined with ", "}\n{keywords joined with ", "}\n{full_text}
```

Empty arrays render as empty strings. Newlines are real newlines (BM25 tokenization treats them as whitespace; no semantic effect).

Mean length post-Stage-C-v2: ~3500 chars per chunk (measured against the audit data assuming uniform keyword extraction). Total storage cost across the post-Plan-C ~1500-chunk corpus: ~5MB of raw column data; the FTS index itself is similar order of magnitude. Trivial against the existing LanceDB volume.

### 10.2 FTS index migration

Server startup hook in `retrieval_server.py` calls `ensure_fts_index(table, column="bm25_text")` instead of `column="full_text"`. The pattern:

1. On first boot post-deploy: `ensure_fts_index` detects no FTS index on `bm25_text`, creates one. The old index on `full_text` (built by v2's startup hook) is still present but unused; LanceDB allows multiple FTS indexes on different columns. The unused index gets dropped at the next FTS lifecycle pass — see §10.3.
2. On subsequent boots: the `bm25_text` index exists; idempotent no-op.

### 10.3 Old `full_text` FTS index cleanup

Add a cleanup step to the startup sequence: after `ensure_fts_index(column="bm25_text")` succeeds, drop the FTS index on `full_text` (if present) via `table.drop_index("full_text_fts_idx")` (or whatever LanceDB's drop API is named in version 0.30.2 — verify during implementation). This is a one-time cleanup; subsequent deploys see no `full_text` index and skip the drop.

If LanceDB's drop API is not available in 0.30.2, the design tolerates leaving the old index in place: it's unused, costs disk space but no query latency, and gets cleaned up at the next embedding-model swap or full table rebuild.

### 10.4 Per-ingest update

Per the v2 spike findings (verified 2026-04-28): LanceDB FTS auto-includes new rows on `table.add(...)` after the index has been created. No explicit optimize call is required. v3 reuses the v2 `optimize_fts_index` no-op-with-rationale stub on the new column; the call site exists as a future-proofing seam if a later LanceDB version drops auto-update.

## 11. Score breakdown in `/query` response (item 5b)

### 11.1 Per-chunk field

```python
class QueryChunkResult(BaseModel):
    ground_truth: dict
    derived_metadata: dict
    provenance: dict
    similarity: float
    score_breakdown: dict  # NEW
```

Content:

```json
{
  "vector_similarity": 0.42,
  "bm25_rank": 3,
  "rrf_score": 0.0238,
  "cue_delta": 0.010,
  "cue_rules_fired": ["unresolved_questions"]
}
```

- `vector_similarity` mirrors the top-level `similarity` (kept for unified consumption inside one record).
- `bm25_rank` is the chunk's 1-indexed position in the BM25-only ranking; `null` if the chunk did not appear in the BM25 result set (vector-only contribution).
- `rrf_score` is the post-fusion score before cue boosting.
- `cue_delta` is the additive boost applied (sum of all fired rules' Δ values; `0.0` if no rules fired).
- `cue_rules_fired` is the list of cue rule names that fired on this chunk for this query (empty list if none).

### 11.2 Filter rendering valve

`community_brain_filter.py` adds a valve:

```python
class Valves(BaseModel):
    ...
    expose_score_breakdown: bool = False
```

When False (default): the filter does not render `score_breakdown` in the LLM-facing context. The `[corpus summary: ...]` and per-chunk `[flags: ...]` tags are still rendered.

When True: the filter renders an additional per-chunk `[score: vector=0.42, bm25=3, rrf=0.024, cue=+0.01 (unresolved_questions)]` line above each chunk, exposing the retrieval confidence breakdown for the answering LLM.

Default-off because in normal operation the LLM doesn't need the explainability; default-on is operator-debug mode.

### 11.3 Operator-side use

`/query` always returns `score_breakdown` regardless of filter valve state. Operators inspecting `/query` directly (curl, debug session) see the full breakdown. The valve only gates the LLM-facing rendering.

## 12. YAML cue rules (item 5c)

### 12.1 File location: `config/query-cues.yaml`

Mounted into the container at `/app/config/query-cues.yaml` (existing volume mount pattern for other YAMLs).

### 12.2 File format

```yaml
cue_rules:
  - name: unresolved_questions
    cue_phrases:
      - unresolved
      - open question
      - not answered
      - outstanding
      - didn't get answered
      - didn't get fully answered
    target_predicate:
      field: has_unresolved_question
      value: true
    delta: 0.010

  - name: decisions
    cue_phrases:
      - decision
      - decided
      - resolved
      - concluded
    target_predicate:
      field: decisions
      check: non_empty
    delta: 0.008

  - name: action_items
    cue_phrases:
      - action item
      - commit
      - commitment
      - next step
      - to-do
      - todo
      - homework
    target_predicate:
      field: action_items
      check: non_empty
    delta: 0.008

  - name: insights
    cue_phrases:
      - insight
      - realization
      - aha moment
      - key takeaway
    target_predicate:
      field: has_insight
      value: true
    delta: 0.006

  - name: referenced_prior
    cue_phrases:
      - referenced
      - prior call
      - last week
      - previously
      - discussed before
    target_predicate:
      field: references_prior
      value: true
    delta: 0.006

  - name: questions_general
    cue_phrases:
      - question
      - asked
    target_predicate:
      field: has_question
      value: true
    delta: 0.003
```

### 12.3 Predicate types

Three declarative types supported by the loader:
- **`field: <name>, value: <bool>`** — chunk[field] equals value (used for boolean flags).
- **`field: <name>, check: non_empty`** — chunk[field] is a non-empty list or string (used for array-type fields like `decisions`, `action_items`).
- **`field: <name>, check: contains, value: <string>`** — chunk[field] (list or string) contains value (reserved for v4-tier rules; not used in the initial rule set but supported by the loader for forward compatibility).

The loader translates each rule into a `CueRule` instance equivalent to the v2 hardcoded form. `apply_cue_boosts` is unchanged; only the rule source changes.

### 12.4 Hot reload

`/query` reads `query-cues.yaml` on each call (sub-millisecond cost: file stat + YAML parse + predicate compilation). No container restart required for rule changes; operator can edit the YAML and the next `/query` picks it up.

If the YAML is malformed or missing, `/query` falls back to the previously-loaded rule set (held in module-level state) and logs WARN. If the very first `/query` after server boot encounters a malformed YAML, the rule set is empty and queries proceed with vector + BM25 only (no cue boost). This is the same graceful-degradation pattern the v2 spec uses for FTS index unavailability.

### 12.5 Schema validation

The loader validates each rule's shape before installing it:
- Required keys: `name`, `cue_phrases`, `target_predicate`, `delta`.
- `cue_phrases` is a non-empty list of non-empty strings.
- `target_predicate` is a dict with `field` plus exactly one of `value` or `check`.
- `delta` is a non-negative float.

Failed validation: skip the rule, log ERROR with the rule name and reason. Other rules proceed normally.

## 13. Component changes (file-by-file)

### 13.1 Code

| File | Change |
|---|---|
| `src/community_brain/ingestion/schema.py` | Add `bm25_text: str` field; bump `SCHEMA_VERSION = "1.1"`; update `pyarrow_table_schema()` and `lancedb_table_schema()`. |
| `src/community_brain/ingestion/extraction_prompts/chunk-extraction-v2.md` | **New file.** Stage C v2 prompt: typed entities, speakers_mentioned partition, uniform keywords. |
| `src/community_brain/ingestion/extractor.py` | Update prompt-loading logic to default to v2 (config drives this via `extraction_config.yaml`). |
| `src/community_brain/ingestion/pipeline.py` | Add canonicalization pass before chunk write; add `bm25_text` synthesis; auto-trigger `lint_corpus` at end of `ingest_session`. |
| `src/community_brain/ingestion/embedding.py` | Update transcript `embed_text` synthesis to enriched format (§6.4). |
| `src/community_brain/cli/__init__.py` | (May need creation if not present.) |
| `src/community_brain/cli/propose_canonicalizations.py` | **New module.** Heuristic merge proposals → YAML. |
| `src/community_brain/cli/apply_canonicalizations.py` | **New module.** Merges proposals into registry; auto-triggers `recanonicalize` (with `--no-recanonicalize` escape). |
| `src/community_brain/cli/recanonicalize.py` | **New module.** Standalone chunk-rewrite pass. |
| `src/community_brain/cli/lint_corpus.py` | **New module.** Recurrent marker detection; idempotent. |
| `src/community_brain/query/cue_rules.py` | Loader for `query-cues.yaml`; `CueRule` and `apply_cue_boosts` retained; hardcoded `CUE_RULES` tuple deleted. |
| `src/community_brain/query/query_local.py` | `search_chunks` records per-chunk `vector_similarity`, `bm25_rank`, `rrf_score`, `cue_delta`, `cue_rules_fired`; computes `metadata_summary` over top-K. |
| `src/community_brain/query/retrieval_server.py` | `QueryResponseV2` adds `metadata_summary` top-level field; `QueryChunkResult` adds `score_breakdown`. Startup hook builds FTS on `bm25_text` (and drops old `full_text` index if present). |
| `src/community_brain/query/fts_lifecycle.py` | `ensure_fts_index` accepts column name parameter; default `bm25_text`. |
| `src/community_brain/openwebui/community_brain_filter.py` | Add per-chunk `[flags: ...]` rendering; add top-of-context `[corpus summary: ...]` rendering; add `expose_score_breakdown: bool = False` valve; update embedded `_INFERENCE_GUIDELINES` constant. |

### 13.2 Config

| File | Change |
|---|---|
| `config/extraction-config.yaml` | Bump active prompt version to `chunk-extraction-v2`. |
| `config/query-cues.yaml` | **New file.** Cue rules in declarative YAML format (§12.2). |
| `config/speaker-aliases.yaml` | Operator-curated; updated by `apply_canonicalizations` runs. |

### 13.3 Tests

| File | Change |
|---|---|
| `tests/ingestion/test_schema.py` | `bm25_text` field present; `SCHEMA_VERSION == "1.1"`; pyarrow schema parity. |
| `tests/ingestion/test_extractor.py` | Stage C v2 prompt loaded; mock LLM returns expected typed entities, speakers_mentioned subset, keywords across all content types. |
| `tests/ingestion/test_pipeline.py` | Canonicalization pass applied at chunk write; `bm25_text` synthesized; `lint_corpus` auto-triggered. |
| `tests/ingestion/test_embedding.py` | Transcript `embed_text` synthesis includes new fields. |
| `tests/cli/test_propose_canonicalizations.py` | **New.** Heuristics produce expected proposals; ambiguous entries surfaced; idempotent (running twice = same output). |
| `tests/cli/test_apply_canonicalizations.py` | **New.** YAML merges into registry; auto-triggers recanonicalize; `--no-recanonicalize` flag respected. |
| `tests/cli/test_recanonicalize.py` | **New.** Affected chunks rewritten; unchanged chunks no-op; re-embed triggered only when needed. |
| `tests/cli/test_lint_corpus.py` | **New.** Synthetic corpus → recurrent markers applied to expected chunks; idempotent; cross-session count threshold respected. |
| `tests/query/test_cue_rules.py` | Update for YAML-loaded rules; predicate type dispatch; malformed YAML graceful degradation. |
| `tests/query/test_search_chunks.py` | Per-chunk score_breakdown surfaced; metadata_summary computed correctly across top-K; FTS over bm25_text. |
| `tests/query/test_retrieval_server.py` | `/query` response includes `metadata_summary`; chunks include `score_breakdown`. |
| `tests/query/test_hybrid_search.py` | Golden queries updated for v3 corpus shape (entities populated; FTS over bm25_text). |
| `tests/openwebui/test_filter.py` | `[flags: ...]` rendering for true-flagged chunks; `[corpus summary: ...]` rendering at top; `expose_score_breakdown` valve gates rendering. |
| `tests/fixtures/golden_queries.yaml` | Updated expectations against the v3 corpus. |

### 13.4 Docs

| File | Change |
|---|---|
| `docs/inference-guidelines.md` | Add §X "Presentation tags" with the 2-3 sentence convention documentation (§8.4). |
| `docs/migrations/CHANGELOG.md` | New entries for schema 1.0 → 1.1; Stage C v1 → v2; FTS column migration; embed_text synthesis change. |
| `community-brain/CLAUDE.md` | Remove v2 backlog items closed by v3 (`entities` underpopulation, `speakers_mentioned` always None, `corpus_derived_markers` unimplemented). Update "Trade-offs we've deliberately kept" with the recanonicalize separability and bm25_text indexing notes. |
| `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md` | Mark v3 as complete after deploy; update the "v3 design (when warranted)" subsection to reflect what shipped vs what got deferred to v4. |
| `docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md` | New §10.x addendum referencing this v3 spec; close out Finding 8 with the deployed-and-validated outcome. |
| `docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md` | Cross-reference v3 from §12 "Future work (v3 candidates)" — note which items shipped, which deferred. |

## 14. API contract

### 14.1 Request — unchanged

`QueryRequestV2` fields are byte-identical to v2. The Open WebUI filter sends `{"question": ..., "top_k": ...}`; the n8n workflows POST `{"question": ..., "filters": ...}`; both continue to work.

### 14.2 Response — additive only

```python
class QueryChunkResult(BaseModel):
    ground_truth: dict
    derived_metadata: dict
    provenance: dict
    similarity: float
    score_breakdown: dict     # NEW (v3)


class QueryResponseV2(BaseModel):
    query: str
    chunks: list[QueryChunkResult]
    total_matched: int
    filters_applied: dict
    metadata_summary: dict    # NEW (v3)
```

Existing fields and their semantics: unchanged. Existing clients ignore the new fields by default (Pydantic clients with strict-extra would need to accept them; both Open WebUI filter and n8n use loose JSON parsing).

### 14.3 `/ingest`, `/sessions`, `/health`, `/speaker-aliases-block` — unchanged

`/ingest` accepts the same body shape (`session_id`, `session_date`, artifacts, `force_reextract`). Internal behavior changes (Stage C v2; canonicalization pass; bm25_text; lint_corpus auto-trigger) but the contract is unchanged.

`/sessions` response shape unchanged. `unresolved_question_count` continues to be derived from chunks tagged `has_unresolved_question=True`; v3 doesn't change this aggregate.

`/health`, `/speaker-aliases-block`: untouched.

## 15. Performance budget

| Stage | v2 p50 | v3 p50 (estimated) |
|---|---|---|
| `/query` Embed (Ollama nomic) | ~150-400 ms | unchanged |
| `/query` LanceDB hybrid (167-184 chunks) | ~10-30 ms | ~10-30 ms (FTS over bm25_text similar tokenization cost) |
| `/query` Cue boost over 30 candidates | < 1 ms | < 1 ms (YAML loaded once per call, sub-ms parse) |
| `/query` Score breakdown computation | n/a | < 1 ms |
| `/query` Metadata summary | n/a | < 1 ms |
| **`/query` total p50** | ~250-550 ms | ~250-550 ms |
| `/ingest` Stage A+B+C (per session, 16-20 chunks) | ~30-60 sec | unchanged for B/C; Stage C v2 prompt is similar size → similar latency |
| `/ingest` Canonicalization pass | n/a | < 100 ms total per session (in-memory map lookups) |
| `/ingest` bm25_text synthesis | n/a | < 50 ms total per session (string concatenation) |
| `/ingest` lint_corpus auto-trigger | n/a | ~5-15 sec at post-Plan-C corpus size; ~1-3 sec at current 9-session size |
| **`/ingest` total** | ~30-60 sec | ~35-75 sec |

Per-session Stage C cost (LLM): ~$0.05-0.08 unchanged (same prompt size class; v2 prompt model mix per Plan B retains).

`recanonicalize` per-pass cost: see §7.1.

`lint_corpus` standalone manual run: ~5-15 sec at post-Plan-C corpus size.

Plan C total wall: ~12 hours (unchanged from prior estimate; v3's per-session adders are < 30 seconds total against ~12 minute per-session backfill latency).

No latency budget concern justifies any opt-out. v3 is unconditionally on.

## 16. Validation plan

### 16.1 Pre-Plan-C validation gate

All eight criteria below must hold before kicking off Plan C. Tune and re-validate if any fail.

| # | Criterion | Pass threshold | Source |
|---|---|---|---|
| 16.1.1 | F8 fix — answering LLM count accuracy | Query "What unresolved questions came up across these calls?" via Open WebUI (GPT-oss 20B) → model cites ≥ 5 of the 6+ chunks tagged `has_unresolved_question=True`. (v2 baseline: 1.) | Open WebUI cross-check |
| 16.1.2 | Entities populated and indexed | Direct `/query` for "Adam Gold Flamingo" returns ≥ 5/10 chunks where at least one `entities` entry contains the substring "Adam" (case-insensitive) — captures both raw "Adam" and canonical "Adam James" forms (was 0/10 in v2) | `/query` inspection |
| 16.1.3 | Canonicalization applied | `/query` with `filters.speakers_spoke=["<canonical Adam name>"]` returns all chunks the operator merged into that canonical | `/query` inspection |
| 16.1.4 | `recurrent` marker populated | `corpus_derived_markers` non-empty for ≥ 30% of chunks across 9 sessions | `/sessions` + sample inspection |
| 16.1.5 | Score breakdown surfaced | Every chunk in a sample `/query` response has `score_breakdown` with all 5 sub-fields | `/query` inspection |
| 16.1.6 | `[flags: ...]` and `[corpus summary: ...]` rendered | Filter unit tests + manual Open WebUI check; chunks with True flags get inline tags; corpus summary appears at top of LLM context | Filter tests + manual |
| 16.1.7 | Test suite green | All existing tests pass; new tests added for v3 components also pass | `pytest` on the v3 branch |
| 16.1.8 | No regression on Findings 6 & 7 | The two v2 validation queries still pass at v2 thresholds (Adam: ≥ 5/10 in `full_text`; unresolved: ≥ 5/10 tagged) | Re-run from v2 spec addendum |

### 16.2 Golden query set (CI regression protection)

Update `tests/fixtures/golden_queries.yaml` to reflect the v3 corpus shape:
- Existing v2 entity-grounded queries continue to assert `full_text` containment.
- New assertions: entity-grounded queries should also find the entity in `entities` (now populated).
- New queries targeting the canonicalization fix: filter by canonical speaker name, expect chunks merged from raw aliases.
- New queries targeting `recurrent` marker: filter by `corpus_derived_markers`, expect chunks from cross-session topical clusters.
- New queries targeting `metadata_summary`: assert top-level field present with expected shape.

`tests/query/test_hybrid_search.py::test_golden_queries` continues to enforce; new test functions cover the v3-specific assertions.

### 16.3 Lift validation (proves v3 is actually better than v2)

For at least 3 of the new entity-canonicalization queries, the test asserts that v2-style (raw extracted speakers, no canonicalization) does NOT satisfy the criterion. Assertion enforces that the lift comes from the new pipeline, not from corpus drift.

### 16.4 Operator-side validation (post-deploy)

After v3 ships, run the validation gate (§16.1) against the live Open WebUI filter + retrieval server. Document outcomes as a §10.x addendum in the Plan A spec. Use the same format as the v2 validation addendum (Plan A spec §10 "v2 hybrid retrieval validation").

If any criterion fails: tune (Stage C prompt, alias map, cue Δ values, recurrent threshold, etc.) and re-validate. Plan C is gated on all 8.

## 17. Rollout

### 17.1 Sequence

1. Land this spec → plan → implementation across feature branch (`feat/retrieval-v3-stage-c-v2` or similar). All tests green.
2. Build container; deploy to VM via `community-brain/docs/DEPLOYMENT.md` runbook (containers restart with v3 image).
3. **Drop the existing v1.0 chunks table.** This is the schema-migration step — v1.0 chunks lack the new `bm25_text` column, and adding the column in-place is an extra LanceDB-version-dependent code path we can avoid by re-extracting from scratch. The 9 ingested sessions are cheap to re-create (~9 minutes wall, ~$0.50 LLM cost) and the source artifacts at `/data/output/<date>/` are intact:
   ```bash
   ssh n8n-automation 'docker exec community_brain_retrieval python -c "
   import lancedb
   db = lancedb.connect(\"/data/lancedb/nomic-v1\")
   db.drop_table(\"chunks\")
   print(\"chunks table dropped; will be recreated with v1.1 schema on first /ingest\")
   "'
   ```
   Server startup hook detects empty table and defers FTS index creation until the first ingest creates the v1.1 schema. `/health` continues to return ok; `/query` returns an empty result set until step 7 completes.
4. Run `python -m community_brain.cli.propose_canonicalizations`. Operator reviews `community-brain/canonicalization-proposals.yaml`, edits as needed.
5. Run `python -m community_brain.cli.apply_canonicalizations canonicalization-proposals.yaml --no-recanonicalize`. Registry updated; the `--no-recanonicalize` flag skips the auto-trigger because the chunks table is currently empty after step 3 — running recanonicalize would be a no-op scan, and explicit suppression makes the operator's intent unambiguous.
6. (Skipped — recanonicalize is unnecessary when the chunks table is empty; re-extraction in step 7 applies the now-curated registry at write time.)
7. Re-extract the 9 ingested sessions. The first ingest creates the v1.1 table with `bm25_text` column; subsequent ingests append:
   ```bash
   for date in 2025-02-02 2025-02-05 2025-02-09 2025-02-12 2025-02-16 2025-02-19 2026-04-14 2026-04-21 2026-04-28; do
     curl -X POST http://10.1.30.10:8999/ingest \
       -H "Content-Type: application/json" \
       -d "{\"session_id\":\"$date\",\"session_date\":\"$date\",\"artifacts\":{\"prepared_transcript\":\"/data/output/$date/prepared-transcript.md\",\"extracted_signal\":\"/data/output/$date/extracted-signal.md\",\"community_post\":\"/data/output/$date/community-post.md\"},\"force_reextract\":true}"
     sleep 30
   done
   ```
   Each ingest runs Stage C v2 + canonicalization + bm25_text synthesis + lint_corpus auto-trigger. Total ~9 minutes wall, ~$0.50 LLM cost.
8. Run validation gate (§16.1). Document outcomes in Plan A spec §10.x.
9. Kick off Plan C against the validated v3 retrieval pipeline.

### 17.2 Rollback

If validation surfaces a regression that can't be tuned out:

- **Hard rollback (post-deploy, post-re-extract):** redeploy the prior v2 container image. The v1.1 LanceDB schema (with `bm25_text` column) is mostly forward-compatible — v2 code reads from the table and ignores extra columns. v2's `full_text` FTS index needs to be rebuilt (the table currently has the `bm25_text` index instead); the v2 startup hook handles this idempotently on first boot post-rollback. Stage C v2-extracted chunks remain in the table; v2 code reads them as 37-field rows and ignores the extra column. If the operator wants a *clean* v2 state (Stage C v1 outputs), drop the chunks table and re-extract the 9 sessions under v2 — cost is the same ~9 minutes / ~$0.50 as the v3 forward-migration.

- **Soft rollback (during validation, before deploy):** branch reverts cleanly. v3 changes are confined to:
  - `src/community_brain/ingestion/{schema,pipeline,embedding}.py`
  - `src/community_brain/ingestion/extraction_prompts/chunk-extraction-v2.md` (delete)
  - `src/community_brain/cli/*.py` (delete new files)
  - `src/community_brain/query/{cue_rules,query_local,retrieval_server,fts_lifecycle}.py`
  - `src/community_brain/openwebui/community_brain_filter.py`
  - `config/{extraction-config,query-cues}.yaml`

- **Partial rollback:** If only one v3 component regresses (say, the cue-boost YAML loader), the surface area is small enough that a targeted fix-forward is faster than full rollback. Preserve the rollback option as a backstop.

### 17.3 Observability

- Each `/query` logs at DEBUG: candidate count after RRF, count of cue rules that fired, top-K final IDs, `metadata_summary`.
- Each `/ingest` logs at INFO: session_id, chunks committed, canonicalization mappings applied, `lint_corpus` outcome.
- WARN: cue YAML reload failure (falls back to held rules); FTS index missing (vector-only fallback); canonicalization pass exception (chunk written with raw names).
- ERROR: malformed cue rule (skipped, others proceed); embedding dimension mismatch (fail-loud per existing schema.py guarantee).

## 18. Open questions for implementation

1. **LanceDB FTS index drop API in 0.30.2.** §10.3 assumes `table.drop_index("<name>")` or equivalent. Verify the exact API call name and arguments during implementation. If the API doesn't exist in 0.30.2, leave the old `full_text` index in place (unused, harmless) and document as known cosmetic noise; cleanup rides with the next embedding-model swap or full table rebuild.

2. **`recanonicalize` performance on the post-Plan-C corpus.** The §7.1 cost characteristics assume ~50ms per chunk re-embed. Measure empirically once Plan C completes; if ≥ 100ms, consider parallelizing the embed step (currently sequential in the design for simplicity).

3. **Stage C v2 prompt token budget.** v1 prompt + per-chunk text fits comfortably in Gemma 4 31B's context. v2 prompt is longer (typed entities + speakers_mentioned partition + uniform keywords instructions). Benchmark prompt-size and per-chunk latency on the model mix during implementation; if it exceeds previous timing by > 30%, tune the prompt for token compactness without changing the contract.

4. **Canonicalization heuristic precision/recall.** The propose_canonicalizations heuristics (§7.1) target high precision on the "high confidence" tier. Empirical precision unknown until run on the live `pending:` queue. If false-positive rate > 5%, tighten heuristics (e.g. require both first-name match AND single canonical candidate AND no other candidates within edit-distance 2). Tune during implementation; document the final heuristic set.

5. **`lint_corpus` initial K/T calibration.** §9.1 sets K=8, T=0.65, count ≥ 2 by reasoning. Actual marker fill rate at the 9-session validation point should land in the 30-60% range per the §9.4 expectation. If radically off (< 10% or > 80%), re-tune the constants before validation gate sign-off.

6. **`metadata_summary` rendering pluralization.** §8.3 uses singular form across counts ("1 reference prior", "2 reference prior") to skip a pluralization library. Confirm this is acceptable during filter implementation; if stylistic polish matters, lift to a small inline helper.

7. **Filter unit-test corpus.** Tests for `[flags: ...]` and `[corpus summary: ...]` rendering need a representative chunk fixture. Decide between inline-constructed test data and a small committed JSON fixture during implementation.

## 19. Future work (v4 candidates)

Captured here so they don't get lost; none are blockers for v3 sign-off.

- **LLM intent classifier** (v2 §12 item 5f). If post-v3 retrieval validation shows compositional queries ("What unresolved questions did Adam raise about sales funnels?") still missing, add an upstream LLM that emits structured filter dict + ranking weights.
- **Cross-encoder reranker** (v2 §12 item 5e). For high-stakes queries where latency is acceptable, opt-in `rerank: true` flag runs `bge-reranker-large` (or similar) over top-30 hybrid candidates. Only motivate if hybrid + bm25_text + cue boost still misses post-v3.
- **Weighted-sum fusion** (v2 §12 item 5d). RRF stays unless a calibration story emerges.
- **Entity-canonicalization registry for non-people entities.** Companies, products, frameworks. Same registry+propose+apply+recanonicalize pattern as people; separate YAML; separate operational surface.
- **Synthesized BM25 field iteration.** If post-v3 retrieval shows `bm25_text` is over-indexed on a particular constituent (e.g., `keywords` dominating), tune the constituent set or weighting.
- **Additional `corpus_derived_markers` types.** `cross_session_thread`, `unresolved_followup`, `controversial`, `evolving_topic`, `unique`. Each adds a new lint_corpus pass; no re-extraction required.
- **Metadata summary array counts.** Extend `metadata_summary` with `decisions_count`, `action_items_count`, `external_refs_count` (Q8.3 option C). Motivate only if validation shows the answering LLM struggling to count these from chunk text.
- **Multi-writer registry support.** flock-based file lock or dedicated writer process to support multi-worker uvicorn.
- **Read/write API key split.** Separate `RETRIEVAL_API_KEY_READ` and `RETRIEVAL_API_KEY_WRITE` for finer-grained access control.
- **Deep `/health`.** Check config presence, LanceDB readability, Ollama reachability, FTS index existence.

---

## Appendix A — 2026-04-29 audit findings (full data)

Methodology: `community_brain_retrieval` container, `pyarrow.to_pylist()` over the entire `chunks` table at `/data/lancedb/nomic-v1`. 184 chunks across 9 sessions. Per-field fill rate, distribution analyses, cross-validation of proper-noun mentions, inspection of speaker-token uniqueness against the alias registry.

### A.1 Per-field fill rate

| Field | Empty/null/False | Mean length (lists) |
|---|---|---|
| `entities` | 184/184 (100%) | 0.00 |
| `speakers_mentioned` | 184/184 (100%) | 0.00 |
| `corpus_derived_markers` | 184/184 (100%) | 0.00 |
| `corpus_markers_computed_at` | 184/184 null (100%) | n/a |
| `keywords` (community_post) | 10/10 (100%) | 0.00 |
| `keywords` (extracted_signal) | 54/54 (100%) | 0.00 |
| `keywords` (prepared_transcript) | 0/120 (0%) | 11.53 |
| `speakers_spoke` (prepared_transcript) | 0/120 (0%) | 3.00 |
| `decisions` (whole corpus) | 137/184 (74%) | 0.52 |
| `action_items` (whole corpus) | 104/184 (57%) | 1.30 |
| `external_refs` (whole corpus) | 107/184 (58%) | 1.11 |
| `has_question` True | 53/184 (29%) | n/a |
| `has_answer` True | 56/184 (30%) | n/a |
| `has_unresolved_question` True | 39/184 (21%) | n/a |
| `has_insight` True | 86/184 (47%) | n/a |
| `references_prior` True | 26/184 (14%) | n/a |

### A.2 Cross-validation: proper-noun mentions in `full_text` vs `entities` array

| Probe | In `full_text` | In `entities` | Miss-rate |
|---|---:|---:|---:|
| Adam | 30 | 0 | 100% |
| Brandon | 145 | 0 | 100% |
| Gold Flamingo | 6 | 0 | 100% |
| OpenRouter | 14 | 0 | 100% |
| Claude | 66 | 0 | 100% |
| Sonnet | 19 | 0 | 100% |
| Gemini | 58 | 0 | 100% |
| n8n | 32 | 0 | 100% |
| LanceDB | 13 | 0 | 100% |
| Ollama | 10 | 0 | 100% |
| Anthropic | 15 | 0 | 100% |
| OpenAI | 34 | 0 | 100% |
| Cursor | 35 | 0 | 100% |
| Copilot | 11 | 0 | 100% |

(All 21 probes had 100% miss-rate. The `entities` array is functionally dead in v1.)

### A.3 `speakers_spoke` uniqueness

47 unique speaker tokens across 9 sessions and 120 transcript chunks. Visible duplicates indicating canonicalization gaps:

- `Adam` (5) + `Adam - Gold Flamingo` (5) + `Adam James` (1) — likely all the same person; verify during proposal review.
- `delvis` (2) + `Delvis Nunez` (4) — same person, lowercase first-name variant.
- `asako` (1) + `Asako Hayase` (1) — same person, lowercase first-name variant.
- `Bastian` (1) + `Bastian Venegas` (6) — short-form vs full.
- `Vlad`, `Mitch`, `Tony`, `Victor`, `Miguel`, `Richard` — first names only; canonical candidates may exist.
- `David's iPhone` (1) — raw Zoom display name.

The `speaker-aliases.yaml` registry has 4 canonicalized aliases (Alex Rojas, Alex Wilson, Sam, Shakur) and 40+ entries in the `pending:` queue. Operator-curation step has never run.

### A.4 `has_unresolved_question` cue-textual-cue alignment

38 of 39 chunks tagged `has_unresolved_question=True` contain either a `?` mark or a subtle uncertainty regex match (e.g. "don't know", "not sure", "haven't decided", "still figuring", "open question") in `full_text`. Only 1 of 39 has neither. Stage C's flag is empirically reliable — this corroborates Finding 8's framing: the answering LLM's under-utilization is a presentation problem, not a Stage C accuracy problem.

### A.5 Quality fields confirmed good (no v3 action)

- `topic_label` — descriptive multi-word labels for transcripts; section labels for signals/posts; no quality issues.
- `session_themes` — 4-5 themes per session; descriptive; no quality issues.
- `decisions` content quality — generally good when populated; one weak example noted (`"The video is a how-to"`) but mostly clean.
- `action_items` content quality — clean; concrete and actionable.
- `external_refs` content quality — URLs and references captured cleanly.
- `speech_acts` — clean 12-token vocabulary; well-distributed.
- `extraction_status` — 100% success across all 184 chunks; no failed extractions.
- `embed_text` synthesis — design works as intended; transcripts get summarized form, signals/posts get full content; v3 enriches transcripts only.

## Appendix B — Glossary additions

- **Canonicalization pass:** ingest-time substitution of speaker / mentioned / people-entity raw extracted strings with their canonical form per `speaker-aliases.yaml`. Distinct from extraction (which is the LLM-driven Stage C). Idempotent.
- **`recanonicalize`:** standalone CLI / pass that rewrites already-committed chunks by re-applying the current canonicalization map. Triggers per-chunk re-embed if any name changed; otherwise a fast no-op scan. Decoupled from extraction so name additions don't cost a Stage C re-run.
- **Synthesized BM25 field (`bm25_text`):** new schema column populated as the concatenation of structured fields and `full_text`. The FTS index targets this column rather than `full_text` directly, so lexical retrieval benefits from entities, keywords, speaker names, and topic labels in addition to the conversational text.
- **`metadata_summary`:** top-level field on `/query` response; corpus-level aggregate counts of derived boolean flags across the retrieved chunks. Authoritative count (retrieval-derived); orthogonal to the per-chunk trust partition.
- **`score_breakdown`:** per-chunk field on `/query` response; retrieval-derived breakdown of the chunk's vector similarity, BM25 rank, RRF score, and cue boost. For explainability and operator-side debugging; not rendered to LLMs by default.
- **`recurrent` marker:** corpus-derived marker assigned to chunks whose embedding sits in a topical cluster spanning 2+ sessions. Detected by the `lint_corpus` pass. Filterable via `QueryFilters.require_corpus_markers` / `exclude_corpus_markers`.

## Appendix C — Accepted-by-design behaviors (post-deploy notes)

After implementation, ten rounds of adversarial review (per-phase + holistic) surfaced ~13 findings. Twelve were structural and got fixed in-branch (culminating in the convergent root-cause refactor at commit `7e0622a`). The remaining one is documented here as accepted-by-design with explicit rationale rather than fixed.

### C.1 Empty cue-rules YAML (all rules malformed) leaves cue boost disabled

**Behavior:** if an operator edits `config/query-cues.yaml` such that the file is syntactically valid YAML and has the top-level `cue_rules:` key, but EVERY individual rule entry fails per-rule validation (e.g., missing `target_predicate`, malformed `cue_phrases`), the loader returns an empty rule tuple. `apply_cue_boosts` is a no-op on empty rules. Hybrid retrieval (vector + BM25) continues to serve, but the metadata-aware boost layer (Finding 7 / Finding 8 patterns) is silently dropped until the operator fixes the YAML.

**Per-rule WARN logs identify which rules were rejected.** The fix-forward path is: operator notices in logs or query-quality dip → re-edits YAML → next `/query` picks up the corrected rules via hot-reload.

**Why not "fall back to last-known-good rules" instead?** The proposed alternative would mask the operator's broken edit: their new cue rule appears active because cached old rules continue firing, but the fix isn't taking effect. That trades a quiet downgrade for a subtler "your edits aren't working but you can't tell" failure mode — the same silent-degradation class the v3 refactor was eliminating.

**Trigger frequency:** rare. Requires an operator edit that breaks all rules simultaneously (typically: global rename of a field name during refactor, or a copy-paste accident). Sub-monthly cadence at solo-operator usage.

**Blast radius if it occurs:** narrow. Per-query degradation only on cue-eligible queries (those whose lexical cues match a rule). Vector + BM25 still serve every query. Not a corpus-state corruption; not a /query failure; just temporary loss of ranking refinement.

**Recovery cost:** seconds. Operator fixes the YAML; hot-reload picks it up on the next query. No data loss, no schema impact.

**Accepted by design.** The current behavior is operator-honest (loud per-rule WARNs; visible cue-boost behavior change in query results) and avoids introducing a stale-cached-rules silent-confusion mode.

If this assumption changes (e.g., automated config sync where operator-WARN logs aren't read; multi-operator environments where one's edits affect another's queries), revisit and add fall-back-to-last-known-good with `allow_empty: true` opt-in marker.
