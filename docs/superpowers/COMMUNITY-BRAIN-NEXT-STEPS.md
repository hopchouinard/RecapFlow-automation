# Community Brain — Next Steps Handoff

**Snapshot date:** 2026-04-27
**Purpose:** Single entry-point document for a fresh session that needs to pick up the Community Brain project. Reads in 3 minutes, tells you exactly what's done, what's outstanding, where the canonical artifacts live, and how to start each remaining track.

---

## Where the project is right now

### Plan A — Retrieval server (DONE, deployed)

The Community Brain retrieval server is live on the n8n VM at `http://10.1.30.10:8999` (LAN-reachable). 37-field LanceDB v1.0 schema, trust-partitioned `/query` response, all 252+ unit tests passing on `main`. 8 sessions ingested.

Canonical references:
- Spec: [`docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md`](specs/2026-04-18-community-brain-ingestion-pipeline-design.md)
- Plan: [`docs/superpowers/plans/2026-04-18-community-brain-ingestion-plan-a.md`](plans/2026-04-18-community-brain-ingestion-plan-a.md)

### Plan B — n8n ingestion integration (DONE except Task 17)

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

Validated the 5 query types from Plan A spec §10 against the 8-session subset. 3 query types pass cleanly (evolution, relationships, unresolved-questions when chunks reach the model). 2 query types have documented retrieval-layer caveats that motivate Track C below.

All findings are captured in [Plan A spec §10 Phase 6 Validation findings (2026-04-27)](specs/2026-04-18-community-brain-ingestion-pipeline-design.md#phase-6--open-webui-integration-and-validation). Read that section before doing any v2 retrieval work.

---

## Three outstanding tracks

### Track A — Plan B Task 17 (CLAUDE.md doc update)

Last task in [Plan B's plan](plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md). 15-minute job. Status: not done.

Self-contained scope. Either knock it out as the first task in your next session OR fold it into Track B's kickoff (since you'll be touching CLAUDE.md anyway when Plan C completes).

### Track B — Plan C: Full historical backfill (operational, ~12 hr overnight run)

Run Workflow 2 across the remaining 59 of 65 historical sessions. Total cost ~$3, total wall time ~12 hours.

**No formal plan document exists** because the operational steps already live in Plan B Tasks 11–15 (the workflow itself). Only thing missing is the "kick off the full run" trigger and post-run state cleanup.

#### Starter prompt for Track B (paste into new session)

```
I'm continuing the Community Brain project. Plan A and Plan B are
complete (retrieval server + n8n workflows deployed and validated).
Read /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md
first for current status.

The work for this session: execute Plan C — full historical backfill.
The retrieval server is deployed at http://10.1.30.10:8999. 6 of 65
historical sessions are already ingested (verify via /sessions). The
remaining 59 are pre-staged at ~/n8n/historical/ on the VM. Workflow
2 (n8n id 6) handles the per-session pipeline. State tracked in
~/n8n/n8n-state/backfill-state.json.

Steps:
1. Pre-flight: verify retrieval server health, Ollama nomic-embed-text
   is installed, Workflow 2 is in good state in n8n UI.
2. Trigger Workflow 2 to run all remaining sessions (it will iterate
   automatically; expected ~12 hr wall time).
3. While it runs, optionally execute Plan B Task 17 (CLAUDE.md doc
   update) since you'll touch that file at the end anyway.
4. Post-run: review state file's failed[] entries, decide retry vs
   accept, clean up any partial output dirs, update CLAUDE.md "Current
   status" section to mark Plan C complete.

Reference docs (read in this order):
- docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md (this handoff)
- docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md §10 Phase 5
- docs/superpowers/plans/2026-04-19-plan-b-n8n-ingestion-integration-plan.md Tasks 11-15 (workflow internals)

Don't introduce new spec or plan documents — Plan C is execution-only.
```

**Notes:**
- The backfill is not strictly required before Track C (v2 hybrid retrieval) — you can do them in parallel or in either order. Backfill increases the corpus from 8 → 65 sessions, which strengthens v2 design tests but isn't a blocker.
- If 429 rate-limit cascades become a problem during the run, the workflow's per-session retry + state file design tolerates partial failure cleanly. Failed entries stay in `failed[]` and re-run on next invocation.

### Track C — Hybrid Retrieval v2 (substantial, needs full design cycle)

Phase 6 validation surfaced two retrieval-layer limitations (findings 6 and 7 in the spec) that share a common root cause: **pure vector similarity ignores the structured fields the schema was built to support.**

Concrete impacts observed:
- **Entity-grounded queries fail.** Asking "What did Adam from Gold Flamingo commit to?" returned 0 chunks containing Adam in top-10. Rephrasing with concrete keywords ("Adam Gold Flamingo Solutions sales funnel law firms LinkedIn") returned the right chunks at sim 0.42+.
- **Metadata-tagged chunk queries fail.** Asking "What questions came up that didn't get fully answered?" returned 1 of 38 `has_unresolved_question=True` tagged chunks.

The schema already has the rich structured fields (`has_unresolved_question`, `decisions`, `action_items`, `entities`, `speakers_spoke`, etc.) — they're just not part of the ranking signal. v2 fixes this.

#### Design space (do NOT pre-decide; brainstorm in the new session)

Possible approaches, each with tradeoffs:

1. **Hybrid: vector + BM25 reranking** — classic. LanceDB has full-text search support. Re-rank top-K vector candidates by BM25 over a configurable text field.
2. **Metadata-aware filtering** — let `/query` accept structured filters (`where has_unresolved_question = true`, `where entities CONTAINS 'Adam'`, etc.) that combine with vector similarity.
3. **Query intent classification** — small LLM upstream classifies the user's question (entity-grounded? metadata-tagged? thematic?) and routes to the appropriate retrieval strategy.
4. **Reranker model** — embedding-based or cross-encoder reranker as a second-stage pass over a wider top-K candidate pool.
5. **Some combination of the above.**

Don't pick before brainstorming. Each has implementation cost, latency, and explainability tradeoffs.

#### Starter prompt for Track C (paste into new session)

```
I'm continuing the Community Brain project. Plan A and Plan B are
complete. Plan C (full backfill) is [either: also complete / pending
- adjust as appropriate].

The work for this session: design and implement Hybrid Retrieval v2
for the Community Brain retrieval server. Read /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md
first for current status, THEN read docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md §10 Phase 6 Validation findings —
particularly findings 6 (entity tokens) and 7 (structured metadata).
Those findings are the seed for this work.

The current retrieval server uses pure vector similarity via
nomic-embed-text. The schema has rich structured fields that are not
leveraged by ranking. v2 should fix that.

Use superpowers:brainstorming to explore the design space (vector +
BM25 reranking? metadata filters? query intent classification?
cross-encoder reranker? combination?). Don't pre-decide. Then write
a spec via superpowers:writing-plans → an implementation plan.
Ship via superpowers:subagent-driven-development.

Don't break the existing /query contract — clients (n8n workflows,
Open WebUI filter) MUST continue to work unchanged. v2 should be
either an opt-in parameter on /query or a new endpoint.

Reference docs (read in this order):
- docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md (this handoff)
- docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md §10 Phase 6 (ESPECIALLY findings 6 and 7)
- community-brain/CLAUDE.md (architectural discipline + non-negotiables)
- community-brain/src/community_brain/query/retrieval_server.py (current /query implementation)
- community-brain/src/community_brain/ingestion/schema.py (37-field schema with structured fields)
```

#### Why this needs a fresh session

The current session has 250k+ tokens of context. Fresh session = clean head, follows the natural brainstorming → spec → plan → implement flow. Don't try to continue v2 work in this session.

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
