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
