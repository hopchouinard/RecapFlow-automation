# Community Brain — Next Steps Handoff

**Snapshot date:** 2026-04-28
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

---

## One outstanding track

### Track B — Plan C: Full historical backfill (operational, holding for v3)

Run Workflow 2 across the remaining ~57 of 65 historical sessions. Total cost ~$3, total wall time ~12 hours.

**Operator decision (2026-04-28):** holding this track until v3 retrieval design lands. Reasoning: backfilling 57 sessions through a retrieval pipeline that may be revised in v3 (to address Finding 8) means paying the cost twice — once to ingest under v2 prompts, again to re-extract if v3 changes the extraction contract or `extraction_prompt_version`. Better to wait until the retrieval layer is settled, then run the backfill once cleanly.

**No formal plan document exists** because the operational steps already live in Plan B Tasks 11–15 (the workflow itself). Only thing missing is the "kick off the full run" trigger and post-run state cleanup.

#### Starter prompt for Track B (paste into new session, when ready to run)

```
I'm continuing the Community Brain project. Plan A, Plan B, and
Hybrid Retrieval v2 are all complete (retrieval server + n8n
workflows deployed; v2 ranking validated 2026-04-28). Track B
(Plan C full backfill) was held pending v3 retrieval design.

Read /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md
first for current status.

The work for this session: execute Plan C — full historical backfill.
The retrieval server is deployed at http://10.1.30.10:8999. 9 of 65
historical sessions are already ingested (verify via /sessions). The
remaining ~56 are pre-staged at ~/n8n/historical/ on the VM.
Workflow 2 (n8n id 6) handles the per-session pipeline. State
tracked in ~/n8n/n8n-state/backfill-state.json.

Before kicking off the backfill, confirm the retrieval pipeline
is on the v2-or-later code you intend to ingest under (a re-run is
expensive). Check git log + retrieval_server version 0.2.0 (or
later if v3 has shipped).

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
- If v3 lands BEFORE this backfill runs, re-read the v3 spec for any changes to `extraction_prompt_version` or per-session behavior that might affect idempotency.

### v3 design (when warranted)

Finding 8 (answering LLM under-utilizes Stage C metadata flags) is the leading v3 candidate. Three concrete fix paths captured in the Plan A spec §10 v2 validation addendum:

1. Tighten `inference-guidelines.md` so models treat strong metadata flags (e.g. `has_unresolved_question=True`) as authoritative even when textual cues are subtle. Trade-off: weakens the "derived is probabilistic" partition.
2. Filter-side: format chunks in the LLM prompt with metadata flags inline (e.g. `[FLAG: unresolved_question]`).
3. Add a `metadata_summary` field to `/query` responses giving authoritative per-flag counts.

Plus secondary v3 candidates from the v2 spec §12: LLM intent classifier, cross-encoder reranker, weighted-sum fusion, BM25 over a synthesized `topic_label + entities + full_text` field, cue rules in YAML config.

When you're ready to design v3, fresh session + `superpowers:brainstorming` is the right starting point.

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
