# Plan B — n8n Ingestion Integration Design

**Date:** 2026-04-19
**Status:** Design, awaiting user approval before implementation planning.
**Predecessor:** [Plan A](./2026-04-18-community-brain-ingestion-pipeline-design.md) — retrieval server live on VM at 127.0.0.1:8999.
**Spec rollout context:** Covers Phase 3 (Workflow 1 extension) and Phase 4 (Workflow 2 backfill) from Plan A §10. Phase 5 (full backfill execution) and Phase 6 (Open WebUI validation) are explicitly out of scope.

## 1. Goal

Wire the existing n8n automation into the Plan A retrieval server so coaching-call artifacts produced by n8n are ingested into LanceDB automatically. Two workflows result:

- **Workflow 1** — the existing *Merged Call Summarizer* is extended with a prep-prompt step and a final `/ingest` POST. Runs weekly on live calls.
- **Workflow 2** — a new *Transcript-Only Summarizer* that backfills the 65 historical sessions from Fathom exports. Runs once (plus occasional retries of failed sessions).

The design deliberately keeps the existing weekly LLM chain intact. One prompt edits, two new branches, one new server endpoint. No refactor of working live code.

## 2. State before Plan B

- Retrieval server deployed at `http://127.0.0.1:8999` on the VM; healthy; Gemma 4 31b (non-free) for Stages B and C; `nomic-embed-text` via remote Ollama at `10.1.50.219`.
- All schema-inference bugs surfaced during pre-Plan-B validation are fixed (commits `83e9b9e`, `e180337`, `271929a`, `748abae`, `20c0115`). 252 unit tests green.
- Merged Call Summarizer runs live weekly, emits five markdown artifacts to `./output/<YYYY-MM-DD>/`: `transcript.txt`, `extracted-signal.md`, `community-post.md`, `community-post-compressed.md`, `YYYY-MM-DD-weekly-invite.md`.
- 65 historical sessions pre-staged at `./historical/<YYYY-MM-DD>-<slug>-r<recording_id>/` on the Mac Mini, each containing `meta.json`, `summary.md`, `transcript.md`.
- Existing Extract Signal prompt emits non-canonical headings (Summary / Key Insights / Key Q&A / Tools and Concepts Mentioned / Shared Resources / Follow-Ups Worth Revisiting). None of the 5 on-disk `output/` sessions parse through the retrieval server's canonical taxonomy — they were never ingested.

## 3. Decisions (from brainstorming Q&A)

| # | Decision | Why |
|---|---|---|
| 1 | **Additive, minimal touch** to the weekly workflow | Live workflow; minimum change is lowest risk. Cleanup and rewrites belong in separate iterations. |
| 2 | **Synchronous `/ingest` with 10-min timeout** | Ingestion is I/O-bound on OpenRouter; async hides the bottleneck without fixing it. n8n blocking for 3–4 min per week is a nothing-burger. |
| 3 | **`GET /speaker-aliases-block` on retrieval server** for alias injection | Retrieval server already owns the registries; single source of truth; n8n stays dumb about YAML schemas. |
| 4 | **One retry on `/ingest` failure + continue to disk** | Artifacts must always hit disk (humans read them weekly). Retry once gives OpenRouter's quota window a chance to clear. More clever retry logic bit-rots. |
| 5 | **Use `transcript.md` + `meta.json` from historical/**, ignore `summary.md` for Plan B | Meta improves `session_title` and provides collision-safety via `recording_id`. Summary is Fathom-voiced and high-value (deep-link citation) but wants its own design round — deferred to Plan C. |
| 6 | **Workflow 2 emits prep + signal + community-post (3 pre-ingest LLM calls)** | Community-post is LLM-friendly structured prose, not just human consumption. Maintains corpus consistency when the content is queried. |
| 7 | **Backfill state tracked in a JSON file on an n8n-accessible volume** | Auditable flat file, operator-editable, crash-safe with atomic writes. Skips pre-ingest LLM calls for already-done sessions (the savings that matter). Exact path chosen in the implementation plan. |

## 4. Architecture

```
┌─────────────────────── Mac Mini (dev) ─────────────────────────┐
│  historical/  ─ rsync (one-time setup) ─▶                      │
└────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────── VM ──────────────────────────────────┐
│                                                                 │
│  ~/n8n/historical/               ~/n8n/watch/                  │
│       │                               │                         │
│       ▼                               ▼                         │
│  ┌────────────────────┐    ┌──────────────────────────────┐   │
│  │ Workflow 2:        │    │ Workflow 1 (extended):       │   │
│  │ Transcript-Only    │    │ Merged Call Summarizer       │   │
│  │ Summarizer         │    │                              │   │
│  │                    │    │  existing chain (UNCHANGED): │   │
│  │ reads historical/  │    │  - Extract Signal *          │   │
│  │ iterates sessions  │    │  - Community Post            │   │
│  │ tracks state in    │    │  - Compress Post             │   │
│  │ backfill-state.json│    │  - Weekly Invite             │   │
│  │                    │    │                              │   │
│  │ per session:       │    │  NEW (parallel branches):    │   │
│  │  1. Prep-Prompt    │    │  - Prep-Prompt               │   │
│  │  2. Extract Signal │    │  - POST /ingest              │   │
│  │  3. Community Post │    │                              │   │
│  │  4. POST /ingest   │    │                              │   │
│  └────────────────────┘    └──────────────────────────────┘   │
│         │                          │                            │
│         └─────────┬────────────────┘                            │
│                   ▼                                             │
│           ┌─────────────────┐                                  │
│           │ retrieval-server│  NEW: GET /speaker-aliases-block │
│           │ /ingest         │  (returns pre-rendered markdown  │
│           │ port 8999       │   from speaker-aliases.yaml)     │
│           └─────────────────┘                                  │
└────────────────────────────────────────────────────────────────┘

* Extract Signal prompt gets rewritten to emit canonical headings
  (## general, ## insights, ## qa, ## tools, ## links, ## decisions).
```

## 5. Workflow 1 — Merged Call Summarizer Extension

### 5.1 Topology

```
                   (existing chain — unchanged except Extract Signal prompt text)
Manual Trigger ──▶ Validate ──▶ Merge Content ──▶ Create Output Folder ──▶
                                                          │
                                                          ▼
                                                  Save transcript.txt
                                                          │
                                                          ├──▶ LLM: Extract Signal (PROMPT REWRITTEN) ──▶ Save extracted-signal.md ─┐
                                                          │         │                                                                  │
                                                          │         ├──▶ LLM: Community Post ──▶ Save community-post.md ──────────────┤
                                                          │         ├──▶ LLM: Compress ──▶ Save community-post-compressed.md          │
                                                          │         └──▶ Calc Next Tue ──▶ LLM: Weekly Invite ──▶ Save wi.md         │
                                                          │                                                                            │
                                                          │   NEW (parallel branch):                                                  │
                                                          ├──▶ Code: Read raw transcript from watch/<date>-transcript.txt            │
                                                          │         │                                                                  │
                                                          │         ▼                                                                  │
                                                          │    HTTP GET /speaker-aliases-block                                        │
                                                          │         │                                                                  │
                                                          │         ▼                                                                  │
                                                          │    LLM: Prep-Prompt (raw transcript + alias block)                        │
                                                          │         │                                                                  │
                                                          │         ▼                                                                  │
                                                          │    Save prepared-transcript.md ─────────────────────────────────────────┤
                                                          │                                                                            │
                                                          ▼                                                                            ▼
                                                   (rejoin via Merge node by position) ───────────────────────────────────────────────▶
                                                          │
                                                          ▼
                                                  NEW: HTTP POST /ingest
                                                  (10-min timeout, 1 retry at 60s)
                                                          │
                                                          ├─▶ 2xx: done
                                                          └─▶ non-2xx: Code node writes
                                                              output/<date>/ingest-error.log
                                                              (workflow still reports success)
```

### 5.2 Change surface

| Area | Action |
|---|---|
| **New: Prep-prompt branch** | Runs parallel to the existing Extract Signal chain. Reads the raw transcript file (`./watch/<date>-transcript.txt`, not the merged `./output/<date>/transcript.txt`), fetches alias block via HTTP GET, feeds alias block + raw transcript into the prep LLM, writes `./output/<date>/prepared-transcript.md`. Does NOT feed into any downstream existing step. |
| **Edit: Extract Signal prompt** | System-message text rewritten so output uses canonical headings (`## general`, `## insights`, `## qa`, `## tools`, `## links`, `## decisions`) instead of today's headings. Operates on the raw merged content same as today — not on the prepared transcript. |
| **New: `/ingest` POST** | Runs once after both branches rejoin. Fires with 10-min timeout, one retry at 60s on non-2xx. On ultimate failure: Code node writes `output/<date>/ingest-error.log` with response body + timestamp; workflow reports success (artifacts on disk). |
| **Unchanged** | Every other step: Community Post, Compress, Weekly Invite, all file writes, all credentials, all triggers. |

### 5.3 Design notes

1. **Prep-prompt operates on the raw transcript** in both workflows. The prep-prompt template ([community-brain/config/extraction-prompts/prep-prompt-v1.md](../../community-brain/config/extraction-prompts/prep-prompt-v1.md)) is designed to segment + tag a raw transcript with `HH:MM:SS` / `Speaker Name` structure; feeding it the merged chat-log+transcript content would confuse the speaker/timestamp parsing. Workflow 1 reads from `./watch/<date>-transcript.txt`; Workflow 2 reads from `./historical/<folder>/transcript.md`. Extract Signal continues to use the merged content as before.

2. **Extract Signal prompt is the only existing prompt touched.** Heading names change; semantics stay the same. Proposed mapping (confirmed during brainstorming):
   - Summary → `## general`
   - Key Insights → `## insights`
   - Key Q&A → `## qa`
   - Tools and Concepts Mentioned → `## tools`
   - Shared Resources → `## links`
   - Follow-Ups Worth Revisiting → `## decisions`

3. **Fail-safe on `/ingest` failure: artifacts still hit disk.** All markdown writes happen upstream of the POST. Ingestion failing never breaks the weekly human-facing deliverable.

4. **No async job queue.** One HTTP call, blocks up to 10 min, returns inline. Longer than that is a server-side problem.

### 5.4 `/ingest` request body

```json
{
  "session_id": "<YYYY-MM-DD>",
  "session_date": "<YYYY-MM-DD>",
  "session_title": "<derived from folder or meta — see §6>",
  "artifact_paths": {
    "prepared_transcript": "/data/output/<YYYY-MM-DD>/prepared-transcript.md",
    "extracted_signal":    "/data/output/<YYYY-MM-DD>/extracted-signal.md",
    "community_post":      "/data/output/<YYYY-MM-DD>/community-post.md"
  },
  "force_reextract": false
}
```

`session_id` = `YYYY-MM-DD` from the existing folder-date convention. No recording_id suffix for Workflow 1 (weekly calls don't have the Pro-vs-regular same-date collision the historical corpus has).

## 6. Workflow 2 — Transcript-Only Summarizer (Backfill)

### 6.1 Topology

```
Manual Trigger (operator kicks off in n8n UI)
  │
  ▼
Code: Load state file
  reads the n8n-accessible backfill-state.json (path per §6.2)
  returns { completed: [...], failed: [...] }
  │
  ▼
Code: List historical/ folders
  scans ~/n8n/historical/*/ with a transcript.md
  returns ordered list [{ session_id, folder_path, meta }]
  filters: session_id NOT IN state.completed
  │
  ▼
Loop Over Items (n8n SplitInBatches, size=1)
  │
  │  for each session:
  │    ├─▶ Code: Parse meta.json
  │    │      - extract meeting_title → session_title
  │    │      - extract recording_id → collision disambiguator
  │    │      - derive session_id = YYYY-MM-DD (or YYYY-MM-DD-r<id> on collision)
  │    │
  │    ├─▶ HTTP GET /speaker-aliases-block
  │    │
  │    ├─▶ LLM: Prep-Prompt (transcript.md + alias block)
  │    │      write ./output/<session_id>/prepared-transcript.md
  │    │
  │    ├─▶ LLM: Extract Signal (transcript.md)
  │    │      same canonical-heading prompt as Workflow 1
  │    │      write ./output/<session_id>/extracted-signal.md
  │    │
  │    ├─▶ LLM: Community Post — transcript-only variant
  │    │      write ./output/<session_id>/community-post.md
  │    │
  │    ├─▶ HTTP POST /ingest (10-min timeout, 1 retry at 60s)
  │    │      ├─▶ 2xx: Code appends session_id to completed[]
  │    │      └─▶ fail: Code appends to failed[] with reason
  │    │
  │    ├─▶ Code: Save updated state file (atomic write)
  │    │
  │    └─▶ Wait (30s inter-session delay)
  │
  └──▶ (next session)

End: summary report node (succeeded / failed / skipped counts)
```

### 6.2 State file format

Location: a new n8n-accessible host-bind-mounted path, exact location deferred to the implementation plan. Candidates include (a) adding a dedicated `./n8n-state/` host dir bind-mounted into the n8n container at `/home/node/n8n-state/`, or (b) placing it inside the existing `./watch/` or `./output/` mount with a clear name like `.backfill-state.json`. Option (a) is cleaner; the implementation plan will choose. The `community-brain/config/` directory is NOT suitable — that mount belongs to the retrieval-server container, not n8n.

```json
{
  "schema_version": "1",
  "last_updated": "2026-04-19T12:34:56Z",
  "completed": [
    {
      "session_id": "2025-02-02-r45179632",
      "completed_at": "2026-04-19T10:12:34Z",
      "chunks_written": 12
    }
  ],
  "failed": [
    {
      "session_id": "2025-08-12-r80154690",
      "failed_at": "2026-04-19T10:15:01Z",
      "reason": "HTTP 500: commit_torn_state"
    }
  ]
}
```

**State file discipline:**

- Atomic write after each session (`write to tmp, rename`).
- `completed` entries NEVER re-run automatically.
- `failed` entries re-run on the next invocation (optimistic — transient failures retry, persistent failures repeat into the log for operator review).
- Operator can manually edit: remove a session from `completed` to force re-run; hand-add a `skipped` array (not honored by the workflow, preserved as intent documentation).

### 6.3 `session_id` derivation for historical

- Primary: `YYYY-MM-DD` parsed from the folder name's leading segment.
- Collision avoidance: if the same `YYYY-MM-DD` already exists in `completed`, append `-r<recording_id>` from `meta.json`. Observed in the current 65-session corpus: Pro and regular calls alternate dates, no same-date collisions today, but the guard is cheap.

### 6.4 Pacing

Static 30-second `Wait` node between sessions. Combined with per-session retry (one retry at 60s), a sustained OpenRouter 429 condition propagates as failures into the state file rather than blasting the API. Operator re-runs later when quota resets.

### 6.5 Idempotency

Belt-and-suspenders with the state file: even if the state file lies (marks "completed" when a session was actually torn), the server-side idempotency check on `(chunk_id, extraction_prompt_version)` prevents duplicates. The retrieval server returns `chunks_skipped_idempotent: N, chunks_written: 0` in that case.

## 7. Server-Side Addition — `GET /speaker-aliases-block`

Read-only endpoint; no LanceDB dependency; auth behavior matches the existing endpoint pattern (gated by `RETRIEVAL_API_KEY` when set; open when unset).

### 7.1 Contract

```
GET /speaker-aliases-block
Response 200, Content-Type: text/plain
Body: a pre-rendered markdown block ready for {{SPEAKER_ALIASES_BLOCK}} substitution.
```

### 7.2 Example response body

```markdown
## SPEAKER_ALIASES

The following canonical speaker names are known. When normalizing speakers
in the transcript, map any of the listed raw variants to the canonical form.
If a speaker is NOT in this list, pass the raw name through unchanged AND
list them under "=== UNRESOLVED SPEAKERS ===" at the end of your output.

- Brandon Hancock — aliases: brandonhancock, Brandon
- Alexandra Spalato — aliases: alexandra_spalato, Alex S
- Patrick Chouinard — aliases: patrick, pchouinard, Patrick C
- ...
```

### 7.3 Implementation sketch

```python
# community-brain/src/community_brain/query/retrieval_server.py
from fastapi.responses import PlainTextResponse

@app.get("/speaker-aliases-block", response_class=PlainTextResponse)
def speaker_aliases_block(_key: str | None = Depends(_verify_api_key)):
    """Return the current speaker alias map as a pre-rendered markdown block
    for prompt-template substitution. Reads config/speaker-aliases.yaml on
    every call (~1 ms) so operators can edit the yaml and see changes on
    the next call without restarting the server."""
    registry = load_speaker_registry(CONFIG_DIR / "speaker-aliases.yaml")
    return render_alias_block(registry)
```

`render_alias_block(registry)` is a new pure function in `community_brain.ingestion.registries` (or adjacent). Deterministic text formatting, testable with one unit test per input shape (empty, populated, with pending entries ignored).

### 7.4 Edge cases

- **Empty registry:** response is well-formed with an empty alias list; prep-prompt's "pass unknown through" instruction still works.
- **File missing:** 500 with clear error; flags config drift. Not expected in normal operation.

### 7.5 Explicitly out of scope

- No entity-registry endpoint in Plan B. Parallel endpoint to add when a prompt starts needing entity aliases.
- No mutation endpoints (e.g., "promote this pending speaker"). Promotion stays manual: operator edits YAML, server picks up on next call.

## 8. Prompt Changes

### 8.1 Extract Signal — rewrite (Workflow 1 only)

Rewritten system message uses canonical headings per the mapping in §5.3. Body semantics unchanged. The `extraction_prompt_version` in LanceDB (`chunk-extraction-v1`) is NOT affected — that version anchors the server-side chunk-extraction prompt, not n8n's prompt layer. Idempotency keys do not shift.

### 8.2 Prep-Prompt — reuse existing

[community-brain/config/extraction-prompts/prep-prompt-v1.md](../../community-brain/config/extraction-prompts/prep-prompt-v1.md) already exists and is used verbatim in both workflows. Only the `{{SPEAKER_ALIASES_BLOCK}}` placeholder needs runtime substitution — handled natively by n8n's chainLlm template support.

### 8.3 Community-Post Transcript-Only — new prompt (Workflow 2 only)

New system message, transcript-only variant. Stylistic anchor: match the live community-post voice. Cues removed: chat-specific references ("based on member questions in chat", "emoji reactions"), replaced with transcript-derived cues ("moments when multiple members engaged with X topic", "recurring themes across the call"). Length target: match live.

### 8.4 Prompt storage convention

Current workflow JSONs embed prompts inline as system messages. Plan B stays consistent — new prompts ship inline in their respective workflow JSONs. Extracting prompts to standalone files is a separate cleanup concern.

### 8.5 Model selection

Workflow 1 and Workflow 2 both use the same model already configured in the existing live chain — `anthropic/claude-sonnet-4.6`, set per-LLM in the workflow JSONs' OpenRouter Chat Model nodes. This is independent from the retrieval server's Stage B/C extraction model (currently `google/gemma-4-31b-it`, configured via env vars). No per-prompt overrides in Plan B; if later tuning is wanted, it's a per-node edit in the workflow JSON.

## 9. Testing & Rollout

### 9.1 Rollout order (strict)

Each step depends on the prior.

| Step | Deliverable | Exit criterion |
|---|---|---|
| 1 | `GET /speaker-aliases-block` endpoint on retrieval server | `curl` from VM returns well-formed alias block; existing 252 tests still pass + new unit test for `render_alias_block` |
| 2 | `rsync ./historical/ n8n-automation:~/n8n/historical/` (one-shot setup) | `ls ~/n8n/historical/ \| wc -l` = 65 |
| 3 | Workflow 1 extension (rewrite Extract Signal prompt, add prep-prompt branch, add `/ingest` POST) | One live weekly run produces all current artifacts plus `prepared-transcript.md`, and the session appears in `/sessions` and returns meaningful `/query` results |
| 4 | Workflow 2 + state file + loop | Single historical session processes end-to-end; 5 sequential sessions process with state file correctly tracking completions; simulated interruption resumes correctly |

Steps 1–4 are Plan B. Step 5 (full 65-session backfill run) is Plan C scope.

### 9.2 Testing strategy per step

- **Step 1:** unit test `render_alias_block(registry)` with empty and populated registries; FastAPI TestClient integration test for 200 + expected body shape. No LanceDB dependency.
- **Step 3:** manual verification on one live weekly session. Smoke-test pre-live: drop a known `YYYY-MM-DD-zoom-chat.txt` + `YYYY-MM-DD-transcript.txt` pair into `watch/`, trigger workflow, verify all 6 output files plus `/sessions` entry plus `/query` relevance.
- **Step 4:** manual verification on one historical session first; then 5 sequential sessions; then resume test (kill n8n mid-run, restart, confirm state file and skip logic work correctly).

No automated n8n workflow tests exist in this repo; not introducing a test harness for workflow JSON in Plan B.

## 10. Out of Scope (Explicit)

To keep Plan B disciplined, the following explicitly do **NOT** ship in this plan:

1. **Fathom summary.md ingestion or deep-link citation.** Deferred to Plan C.
2. **Entity-registry block endpoint.** Parallel to speaker-aliases; add when a prompt needs it.
3. **`/ingest` async / job queue.** Not needed at weekly cadence or overnight backfill.
4. **`RETRIEVAL_API_KEY` enforcement.** Currently disabled; can be flipped independently via `.env` + restart, documented in DEPLOYMENT.md §6.3.
5. **Prompt extraction from workflow JSON into standalone files.** Separate cleanup.
6. **Stage B/C registry promotion UI.** Manual YAML edit remains the promotion mechanism.
7. **Open WebUI filter changes.** Already handles the trust-partitioned response; unchanged in Plan B.
8. **Full backfill execution across all 65 sessions.** Plan C (Phase 5 per Plan A §10).
9. **Re-extraction of the existing `2026-04-14-FULLTEST` smoke-test session.** Can be force-reextracted or deleted after Plan B ships; not a Plan B deliverable.

## 11. Implementation plan generation

After user approval of this spec, the next step is invoking `superpowers:writing-plans` to produce a detailed, task-decomposed implementation plan covering the four rollout steps in §9.1.

## References

- [Plan A design spec](./2026-04-18-community-brain-ingestion-pipeline-design.md) §10 — rollout phases.
- [Plan A implementation plan](../plans/2026-04-18-community-brain-ingestion-plan-a.md) — prior reference shape.
- [community-brain/CLAUDE.md](../../community-brain/CLAUDE.md) — non-negotiable architectural discipline for the retrieval server.
- [community-brain/docs/DEPLOYMENT.md](../../community-brain/docs/DEPLOYMENT.md) — SSH-driven VM deployment runbook.
- [community-brain/config/extraction-prompts/prep-prompt-v1.md](../../community-brain/config/extraction-prompts/prep-prompt-v1.md) — prep-prompt template with `{{SPEAKER_ALIASES_BLOCK}}` placeholder.
- [workflows/merged-call-summarizer.json](../../workflows/merged-call-summarizer.json) — current live Workflow 1.
