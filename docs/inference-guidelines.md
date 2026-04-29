# Community Brain — Inference Guidelines

This document defines the contract between the Community Brain retrieval server and downstream LLM consumers (Open WebUI filter, query scripts, custom agents). It MUST be prepended to any system prompt that reasons over retrieved chunks.

## Trust hierarchy

- **`ground_truth.full_text` is authoritative.** All direct quotes must come from here.
- **`derived_metadata` fields** (stance, speech_acts, chunk_local_markers, decisions, action_items, entities, topic_label, etc.) are LLM-extracted approximations. Use them to orient your retrieval and frame your response, but verify against `full_text` before citing as fact.
- **`provenance`** tells you which extraction prompt version produced the derived fields. Treat older extractions with appropriate skepticism.

## Rules when generating responses

1. Direct quotes must cite a specific `chunk_id` and be locatable in that chunk's `full_text`.
2. When summarizing what someone said, check `speakers_spoke` against `full_text` attribution — the former is LLM-inferred, the latter shows actual speaker labels.
3. Claims about decisions, outcomes, or action items: verify against `full_text` before stating. The `decisions` and `action_items` fields are hints, not records.
4. When `derived_metadata` fields are null (e.g., on older chunks), reason from `full_text` alone. Do NOT infer "no decisions" from "decisions field is null" — absence means the chunk predates that extraction.
5. If `full_text` contradicts a `derived_metadata` value, state the source-of-truth reading and flag the discrepancy.

## Tolerating mixed generations

Corpus chunks may be from different `schema_version` or `extraction_prompt_version` eras. Missing fields are normal. Field richness varies. Reason from what's present; don't speculate about what's absent.

## Enforcement boundary

The reference compliant consumer is the `community_brain_filter` Open WebUI function. Consumers that bypass these guidelines — direct LanceDB access, custom API clients that ignore the `ground_truth` vs `derived_metadata` distinction, LLM prompts that don't prepend this fragment — are considered **unsupported**. The system's correctness guarantees apply only within the enforcement boundary.

## Presentation tags

When the answering context contains lines like `[flags: <flag_names>]` (per-chunk) or `[corpus summary: <counts>]` (above all chunks), these are presentation conventions exposing structured derived metadata. The `[flags: ...]` line lists boolean derived flags that Stage C marked True for the immediately-following chunk. The `[corpus summary: ...]` line gives authoritative counts of those flags across the retrieved set. Both are derived (the same trust-contract caveats apply — re-derive from `full_text` when in doubt), but they reflect what Stage C and the retrieval layer concluded; they are not invented by you.
