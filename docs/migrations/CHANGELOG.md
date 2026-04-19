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
