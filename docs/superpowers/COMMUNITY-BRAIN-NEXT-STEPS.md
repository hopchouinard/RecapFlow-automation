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

Validated the 5 query types from Plan A spec §10 against the 8-session subset. 3 query types pass cleanly (evolution, relationships, unresolved-questions when chunks reach the model). 2 query types had retrieval-layer caveats (Findings 6 and 7) — both addressed in Hybrid Retrieval v2 below.

All findings are captured in [Plan A spec §10 Phase 6 Validation findings](specs/2026-04-18-community-brain-ingestion-pipeline-design.md#phase-6--open-webui-integration-and-validation). Findings 6 and 7 cross-reference the v2 spec.

### Hybrid Retrieval v2 — DONE in code; live-VM validation pending

Replaces pure-vector ranking with hybrid (vector + BM25 RRF, k=60) plus cue-driven metadata-aware boosting. Oversamples top_k by 3× internally; applies additive RRF-score deltas when question-side lexical cues align with chunks' structured-metadata flags. Public `similarity` field continues to expose vector cosine (spec-faithful). Vector-only path retained as internal graceful-degradation fallback only — no `mode` parameter, no parallel endpoint, legacy v0 helpers and `_v2` suffix archaeology removed.

302 tests passing. Server bumped to `0.2.0`. Open WebUI filter and n8n workflows continue to work without change.

Canonical references:
- Spec: [`docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md`](specs/2026-04-27-hybrid-retrieval-v2-design.md)
- Plan: [`docs/superpowers/plans/2026-04-27-hybrid-retrieval-v2-plan.md`](plans/2026-04-27-hybrid-retrieval-v2-plan.md)
- CHANGELOG entry: [`docs/migrations/CHANGELOG.md`](../../docs/migrations/CHANGELOG.md) (2026-04-28 — Hybrid Retrieval v2)

Only outstanding piece: **v2 Task 16 — operator-side validation against the live VM.** Deploy the `0.2.0` container, re-run the Phase 6 query types via Open WebUI, append a §10.x addendum to the Plan A spec confirming Findings 6 and 7 are empirically resolved.

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

### Track C — Hybrid Retrieval v2 (DONE; only T16 remains)

Designed, planned, implemented, and merged on 2026-04-28. 16 commits on `feat/hybrid-retrieval-v2` (now in `main`). 302 tests passing.

Findings 6 (rare-token retrieval) and 7 (metadata-tagged retrieval) addressed by:
1. **Hybrid LanceDB query** — RRF (k=60) over native FTS index on `chunks.full_text` + the existing vector column. Oversampled 3× internally before truncation to `top_k`.
2. **Cue-driven metadata boost layer** — Python post-RRF pass that adds small additive deltas (0.003–0.010) to chunks whose structured flags align with question-side lexical cues. Six cue rules covering `has_unresolved_question`, non-empty `decisions`/`action_items`, `has_insight`, `references_prior`, `has_question`.
3. **Filter-then-rank guards preserved** — `extraction_status='success'` and caller's `QueryFilters` continue to apply as a WHERE clause before retrieval.
4. **Graceful degradation** — hybrid query exception → vector-only fallback with WARN log; cue rule exception → log and skip rule, others continue; FTS index missing on boot → log and continue.
5. **No API contract change** — request/response shapes identical; the public `similarity` field continues to reflect vector cosine similarity (spec-faithful).

The only remaining piece is **T16: operator-side validation against the live VM.** Deploy the `0.2.0` container, re-run Phase 6 query types via Open WebUI, append a §10.x addendum to the Plan A spec confirming Findings 6 and 7 are empirically resolved.

#### Starter prompt for T16 (paste into new session)

```
I'm continuing the Community Brain project. Hybrid Retrieval v2 is
implemented and merged to main on 2026-04-28; the only remaining
piece is operator-side validation against the live VM.

Read /Volumes/NVMe_2TB_Work/Development/RecapFlow-automation/docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md
first for current status, then community-brain/docs/DEPLOYMENT.md
for the canonical SSH-driven deploy runbook (it encodes the
permission model — 🟢 auto / 🟡 confirm / 🔴 gated — that you must
respect when acting as operator).

Steps:
1. Pre-flight: confirm SSH access to n8n-automation (LAN IP
   10.1.30.10), retrieval-server health, Ollama nomic-embed-text
   pinned.
2. Deploy: pull/rebuild the retrieval-server container from main;
   confirm `INFO: FTS index on column 'full_text' built in N.NNs`
   appears in startup logs.
3. Validate via Open WebUI: re-run the five Phase 6 query types
   from Plan A spec §10. Specifically retest the failing cases that
   motivated v2:
     - Finding 6: "What did Adam from Gold Flamingo commit to?"
       (top-10 must contain ≥5 chunks with Adam in entities or
       full_text)
     - Finding 7: "What unresolved questions came up?"
       (top-10 must contain ≥5 of 38 corpus chunks with
       has_unresolved_question=True)
4. Document outcomes: append a §10.x addendum to
   docs/superpowers/specs/2026-04-18-community-brain-ingestion-pipeline-design.md
   capturing the validated/failing query results.
5. If validation fails, tune cue rule deltas in
   community_brain/query/cue_rules.py or OVERSAMPLE_FACTOR in
   community_brain/query/query_local.py, then re-validate.

Reference docs:
- docs/superpowers/specs/2026-04-27-hybrid-retrieval-v2-design.md
  (especially §9 Validation plan)
- docs/superpowers/plans/2026-04-27-hybrid-retrieval-v2-plan.md
  (Task 16 has the operator runbook)
- community-brain/docs/DEPLOYMENT.md (deploy steps + permission model)
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
