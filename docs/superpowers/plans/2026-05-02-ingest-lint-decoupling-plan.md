# Ingest / Lint Decoupling — Implementation Plan

> **Status:** READY — companion to design spec at `docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md`. Read the spec first.
> **Sub-skill:** Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to drive task-by-task execution.

**Goal:** Make `/ingest` complete in time bounded by session size (not corpus size), eliminate the lint write storm, and move corpus-marker maintenance to a daily cron.

**Architecture:** Two coordinated code changes in `community-brain/`:
- Change A: drop no-op timestamp writes from `lint_corpus_chunks` so it only writes when marker state actually changes
- Change E: remove the lint auto-trigger from `_post_commit_maintenance` so /ingest no longer pays for it

Plus operational change F: a daily host crontab entry on the n8n VM that runs `python -m community_brain.cli.lint_corpus` via `docker exec`.

**Tech stack:** Python 3.11 + LanceDB 0.30.x + pytest. Linux host crontab on the n8n VM.

**Spec:** [docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md](../specs/2026-05-02-ingest-lint-decoupling-design.md)

**Pre-requisite:** Plan C must be in a stopped state. Do NOT run this plan while Workflow 6 is running.

---

## File map

| Action | Path | Purpose |
|---|---|---|
| Modify | `community-brain/src/community_brain/cli/lint_corpus.py` | Drop no-op timestamp writes (Change A) |
| Modify | `community-brain/src/community_brain/ingestion/pipeline.py` | Remove lint_corpus_chunks call from `_post_commit_maintenance` (Change E) |
| Modify | `community-brain/tests/test_lint_corpus.py` | Add write-skipping tests; tighten idempotency test |
| Modify | `community-brain/tests/test_ingestion_pipeline.py` | Remove auto-trigger tests; add "no auto-trigger" assertion test |
| Create | `scripts/cron/community-brain-lint.cron` | Crontab fragment for daily lint (committed to repo for reproducibility) |
| Create | `scripts/cron/install-cron.sh` | Idempotent installer that copies the fragment to `/etc/cron.d/` on the VM |
| Modify | `community-brain/CLAUDE.md` | Update the "Trade-offs" section to reflect the new model |
| Modify | `CLAUDE.md` (root) | Note the cron in the architecture diagram |
| Modify | `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md` | Add this fix to the timeline; mark complete on deploy |
| Create | `docs/migrations/CHANGELOG.md` entry | Record the behavior change for `corpus_markers_computed_at` |

Runtime-only actions (not code changes):
- Apply schema-level state-file cleanup for `2025-12-09` (move from failed → completed; it actually succeeded)
- Deploy the new code to the retrieval-server container (`docker compose up -d --build retrieval-server`)
- Install the crontab on the n8n VM
- Verify a manual lint run completes cleanly post-deploy
- Resume Plan C

---

## Task dependency overview

```
Phase 1 (validate diagnosis with timing test)
        │
        ▼
Phase 2 (Change A — drop no-op writes + tests)
        │
        ▼
Phase 3 (Change E — remove auto-trigger + test refactor)
        │
        ▼
Phase 4 (deploy code to retrieval-server)
        │
        ├──────────────────────────────────┐
        ▼                                  ▼
Phase 5 (install cron F)        Phase 6 (state file cleanup)
        │                                  │
        └─────────────────┬────────────────┘
                          ▼
                  Phase 7 (resume Plan C)
                          │
                          ▼
                  Phase 8 (docs + CHANGELOG)
```

Phases 1–3 are codebase changes (do them in order with tests passing between each). Phase 4 is the deploy. Phases 5 and 6 are independent operational tasks. Phase 7 is the final unblock. Phase 8 wraps up documentation.

---

## Phase 1: Validate diagnosis with timing test

**Purpose:** Lock in a quantitative baseline before changing anything. Confirms we understand the bug and gives us a regression test that proves Change A worked.

### Steps

- [ ] **1.1 — Add `test_lint_corpus_write_count_scales_with_state_changes_not_corpus_size`** in `tests/test_lint_corpus.py`.

  This test should:
  1. Build three corpora at sizes N=100, N=500, N=1500 chunks, all with stable marker state (no chunks should flip recurrent / non-recurrent on a re-run)
  2. Run `lint_corpus_chunks(db_path)` once on each corpus to apply initial markers
  3. Patch `table.update` to count call invocations
  4. Run `lint_corpus_chunks(db_path)` a second time on each corpus
  5. **Currently expected:** call count ~= N (the bug)
  6. **Post-Change-A expected:** call count == 0 or close to it

  Mark the assertion as `pytest.xfail` with reason `"Change A not yet applied — see spec 2026-05-02-ingest-lint-decoupling-design.md"`. After Change A lands, remove the xfail.

- [ ] **1.2 — Run the test.** Confirm it currently fails (xfailed) with high write counts. This is the proof-of-bug.

**Phase 1 exit criteria:** xfailed test exists; running pytest shows `XFAIL` for this test with the expected high write counts.

---

## Phase 2: Change A — drop no-op timestamp writes

**Purpose:** Implement the core fix. Skip writes for chunks whose marker state doesn't change.

### 2.1 Code change

In `community-brain/src/community_brain/cli/lint_corpus.py`, modify `lint_corpus_chunks()`:

**Branch 3 (currently lines ~169–176):**
```python
# REMOVE THIS BRANCH ENTIRELY:
elif should_be_recurrent:
    recurrent_count += 1
    table.update(
        where=f"chunk_id = '{safe_id}'",
        values={"corpus_markers_computed_at": now_iso},
    )

# REPLACE WITH:
elif should_be_recurrent:
    # Already correctly marked — count it but don't write.
    # corpus_markers_computed_at is "last meaningful change", not "last lint pass"
    # (see spec 2026-05-02-ingest-lint-decoupling-design.md §7).
    recurrent_count += 1
```

**Branch 4 (currently lines ~178–185):**
```python
# REMOVE THIS BRANCH ENTIRELY:
else:
    table.update(
        where=f"chunk_id = '{safe_id}'",
        values={"corpus_markers_computed_at": now_iso},
    )

# REPLACE WITH:
else:
    # Doesn't qualify and isn't currently marked — no write needed.
    pass
```

The two write-skipping branches together also obviate the surrounding try/except for those branches, but keep the try/except wrapping the whole if/elif chain since the ADD-marker branch still writes and can still fail.

### 2.2 Test changes

- [ ] **2.1 — Apply Change A** in `lint_corpus.py` exactly as described.
- [ ] **2.2 — Remove the xfail** from `test_lint_corpus_write_count_scales_with_state_changes_not_corpus_size`. Now it must pass: write count == 0 on the second pass.
- [ ] **2.3 — Add `test_lint_corpus_skips_writes_when_marker_state_unchanged`:** explicitly small (10 chunks), assert `table.update` not called when no chunks need flipping.
- [ ] **2.4 — Add `test_lint_corpus_writes_only_when_state_changes`:** small corpus with 1 chunk that should flip recurrent. Assert: exactly 1 `table.update` call, on that one chunk.
- [ ] **2.5 — Verify existing tests still pass:** `test_lint_corpus_idempotent`, the rebuild path tests, the K-NN algorithm tests. Run `pytest tests/test_lint_corpus.py -v`.

**Phase 2 exit criteria:** all of `tests/test_lint_corpus.py` passes; the previously xfailed test now passes assertively; new write-skipping tests pass.

---

## Phase 3: Change E — remove auto-trigger from /ingest

**Purpose:** Decouple lint from /ingest entirely. After this phase, /ingest's post-commit work is just the invariant check.

### 3.1 Code change

In `community-brain/src/community_brain/ingestion/pipeline.py`, modify `_post_commit_maintenance()` (currently lines ~495–524):

```python
def _post_commit_maintenance(table, db_path: str | Path) -> None:
    """Run the post-commit invariant: corpus validity check.

    verify_corpus_v3_state is invariant-enforcing: it checks schema + FTS
    index in one call and raises CorpusInvalidError if either is broken.
    Translated to CommitError here so callers see consistent failure signal.

    Lint is NO LONGER called here — see spec 2026-05-02-ingest-lint-decoupling-design.md.
    Operators run lint via the daily cron at 04:00 UTC, or manually via
    `docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus`.
    """
    try:
        verify_corpus_v3_state(table)
    except CorpusInvalidError as exc:
        raise CommitError(f"Corpus invalid post-commit: {exc}") from exc
```

The `lint_corpus_chunks` import in `pipeline.py` becomes unused — remove it too.

### 3.2 Test refactor

Existing tests that exercise the auto-trigger need to go or change. The spec §8 lists them:

- [ ] **3.1 — Apply Change E.** Remove the lint call and import in `pipeline.py`.
- [ ] **3.2 — Remove `test_ingest_session_auto_triggers_lint_corpus`** from `test_ingestion_pipeline.py`. Auto-trigger no longer exists.
- [ ] **3.3 — Remove `test_idempotent_retry_runs_lint_corpus`** from `test_ingestion_pipeline.py`. Same reason.
- [ ] **3.4 — Remove `test_post_commit_maintenance_lint_uses_explicit_db_path_not_env_var`.** Lint is no longer called from this function.
- [ ] **3.5 — Remove any test asserting "ingest still succeeds when lint raises"** — that scenario can no longer occur.
- [ ] **3.6 — Add `test_post_commit_maintenance_does_not_call_lint_corpus`:** mock both `verify_corpus_v3_state` and `lint_corpus_chunks`. Run `_post_commit_maintenance`. Assert: `verify_corpus_v3_state` called, `lint_corpus_chunks` not called.
- [ ] **3.7 — Add `test_post_commit_maintenance_still_verifies_corpus_state`:** affirmative test that `verify_corpus_v3_state` is still invoked. Important to lock in the surviving invariant.
- [ ] **3.8 — Run full test suite:** `pytest tests/ -v`. Expected outcome: all pass except whatever else is broken pre-existing (verify clean baseline first).

**Phase 3 exit criteria:** full test suite passes; the four removed tests no longer exist; the two new tests pass; `lint_corpus_chunks` import is no longer referenced from `pipeline.py`.

---

## Phase 4: Deploy code to retrieval-server

**Purpose:** Get the fix onto the live VM. This is the moment Plan C becomes safe to resume.

### Steps

- [ ] **4.1 — Commit the changes** with a clear message:
  ```
  fix(retrieval): decouple lint_corpus from /ingest auto-trigger

  Remove O(N)-per-ingest write storm. lint_corpus_chunks now skips
  no-op writes (only writes when marker state changes), and the
  /ingest auto-trigger is removed entirely. Lint runs as a daily
  cron at 04:00 UTC instead.

  Spec: docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md

  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
  ```
- [ ] **4.2 — Push to main** (after running pytest one final time locally).
- [ ] **4.3 — On the VM:** `cd ~/n8n && git pull origin main`
- [ ] **4.4 — Rebuild and restart retrieval-server:** `docker compose up -d --build retrieval-server`
- [ ] **4.5 — Verify health:** `curl http://10.1.30.10:8999/sessions | jq '.total'` returns the expected count (~67), retrieval-server logs show clean startup with no lint-related errors.
- [ ] **4.6 — Smoke-test ingest:** run a tiny test ingest (or wait for the next legit one). Confirm logs show only `verify_corpus_v3_state` post-commit, no `lint_corpus auto-trigger` mentions.

**Phase 4 exit criteria:** new code is live; /sessions returns correct data; logs are clean; a /ingest call (real or test) completes without any lint-related log lines.

---

## Phase 5: Install daily cron (Change F)

**Purpose:** Replace the auto-trigger with a scheduled lint run.

### 5.1 Cron fragment (`scripts/cron/community-brain-lint.cron`)

```cron
# Community Brain — daily lint run
# Spec: docs/superpowers/specs/2026-05-02-ingest-lint-decoupling-design.md
# Runs at 04:00 UTC daily. Logs to ~pchouinard/n8n/logs/lint-corpus.log.
# Failure is non-fatal — markers stay where they are, retry next day.

SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

0 4 * * * pchouinard docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus >> /home/pchouinard/n8n/logs/lint-corpus.log 2>&1
```

### 5.2 Installer (`scripts/cron/install-cron.sh`)

```bash
#!/bin/bash
# Idempotent installer for the community-brain lint cron.
# Run with sudo on the n8n VM.
set -euo pipefail

SOURCE="$(dirname "$0")/community-brain-lint.cron"
DEST="/etc/cron.d/community-brain-lint"

if [ ! -f "$SOURCE" ]; then
    echo "ERROR: $SOURCE not found"
    exit 1
fi

sudo install -m 644 -o root -g root "$SOURCE" "$DEST"
sudo systemctl reload cron 2>/dev/null || sudo service cron reload || true

echo "Installed: $DEST"
echo "Verify: cat $DEST"
echo "Next run at 04:00 UTC. Manual run: docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus"
```

### Steps

- [ ] **5.1 — Create both files** in the repo, committed to main.
- [ ] **5.2 — On the VM, pull and run the installer:** `cd ~/n8n && git pull && sudo bash scripts/cron/install-cron.sh`.
- [ ] **5.3 — Verify cron entry exists:** `cat /etc/cron.d/community-brain-lint`.
- [ ] **5.4 — Manual smoke run:** `docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus`. Expected output: `[ok] lint_corpus: scanned 1500ish, recurrent <some-count>`. Verify it completes in <60 seconds (since most chunks now skip writes).
- [ ] **5.5 — Tail the log file:** `tail -f ~/n8n/logs/lint-corpus.log`. Confirm the smoke run appended a line.
- [ ] **5.6 — Wait for the first scheduled run** (next 04:00 UTC). Verify in the log file the morning after.

**Phase 5 exit criteria:** cron is installed and verified; manual lint run succeeds in <60s; log file is being written; first scheduled run lands in the log.

---

## Phase 6: State file cleanup

**Purpose:** Fix `backfill-state.json` so `2025-12-09` reflects reality (it succeeded, not failed).

### Steps

- [ ] **6.1 — Backup the state file:** `cp ~/n8n/n8n-state/backfill-state.json ~/n8n/n8n-state/backfill-state.json.bak-$(date +%Y%m%dT%H%M%SZ)`
- [ ] **6.2 — Move `2025-12-09` from failed → completed** with a note explaining the n8n-side timeout vs corpus reality:
  ```python
  {
    "session_id": "2025-12-09",
    "completed_at": "<now>",
    "chunks_written": 24,
    "note": "ingested successfully on 2026-05-02 04:11 UTC; n8n recorded as failed due to /ingest HTTP 30-min timeout caused by lint storm (since fixed). Corpus contains the chunks. Verified via /sessions."
  }
  ```
- [ ] **6.3 — Remove `2025-12-09` from the failed array** (now 0 entries in failed).
- [ ] **6.4 — Verify:** `total completed should now be 65, total failed 0`.

**Phase 6 exit criteria:** state file accurately reflects corpus state; no surprises remaining.

---

## Phase 7: Resume Plan C

**Purpose:** Run the remaining sessions now that /ingest is fast.

### Remaining work for Plan C after this fix

| Session | Status |
|---|---|
| `2026-02-25` | New, never ingested |
| `2026-03-04` | New, never ingested |

(`2025-08-27` and `2025-12-17` remain reserved with the build-ingest-payload Code node bug; addressing them is a separate follow-up.)

### Steps

- [ ] **7.1 — Trigger Workflow 6 in n8n.** Watch first session's /ingest in retrieval-server logs — should complete in seconds, not 30 minutes.
- [ ] **7.2 — Verify each session lands:** state file gets a new entry with `chunks_written > 0`; `/sessions` shows the new session.
- [ ] **7.3 — Estimated runtime:** ~10–20 minutes for the 2 sessions (no more lint hang).

**Phase 7 exit criteria:** both new sessions in corpus; state file shows them as completed; total session count = 67 (existing) + 1 (`2026-02-25`) + 1 (`2026-03-04`) − the 8 reservations that were already in completed = whatever the math works out to. Verify against `/sessions` count.

---

## Phase 8: Documentation

- [ ] **8.1 — Update `community-brain/CLAUDE.md`** "Trade-offs we've deliberately kept" section: change "Auto-triggered at end of `/ingest`" to "Run on a daily cron at 04:00 UTC; manual invocation supported."
- [ ] **8.2 — Update root `CLAUDE.md`** architecture section: note the lint cron alongside the existing daily LanceDB snapshot cron on the Mac Mini.
- [ ] **8.3 — Add CHANGELOG entry** in `docs/migrations/CHANGELOG.md`:
  ```
  ## 2026-05-02 — Lint decoupled from /ingest

  `corpus_markers_computed_at` semantics tightened: now records "last
  meaningful marker change" rather than "last lint pass." Lint runs daily
  via cron instead of synchronously after /ingest. No schema or data
  migration required.
  ```
- [ ] **8.4 — Update `docs/superpowers/COMMUNITY-BRAIN-NEXT-STEPS.md`** to reflect this fix is deployed.
- [ ] **8.5 — Mark this plan as DEPLOYED** at the top of the plan doc.

**Phase 8 exit criteria:** all docs reflect new architecture; CHANGELOG entry added; status doc updated.

---

## Risks & mitigations (operational, plan-specific)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Tests pass locally but break in container due to env-var differences | Low | Low | Phase 4.6 includes a smoke /ingest after deploy to catch container-only issues |
| Cron doesn't fire because of timezone confusion | Medium | Low | Cron runs at 04:00 UTC explicitly. Verify VM timezone with `timedatectl` first; the cron daemon respects system timezone unless overridden. |
| Manual lint smoke run reveals an unrelated bug | Low | Medium | Phase 5.4 catches this. If lint fails for any reason post-deploy, Phase 7 (Plan C resume) is blocked until it's understood. |
| Plan C resume hits a different bug (unrelated to lint) | Low | Medium | Phases 4 and 5 must be solid before Plan C resumes. Don't conflate validation. |
| Someone runs lint with `--rebuild` accidentally and rewrites the corpus | Low | Medium | The CLI already requires `--rebuild` explicitly; cron uses default. Document in CLAUDE.md that `--rebuild` is operator-only. |

---

## Notes for the implementer

- **TDD where it makes sense.** Phase 1's xfail-then-fix pattern is the cleanest demonstration. For Phase 3's test removals/additions, the order is: remove old tests → apply code change → add new tests → verify all pass.
- **Don't combine phases.** Each phase has independent verification criteria. Skipping verification to "save time" is how a deploy ends up half-broken.
- **Phase 6 (state file cleanup) is independent** and can happen any time after Phase 4. It's listed before Phase 7 to ensure Plan C's accounting is correct when it resumes.
- **The cron schedule (04:00 UTC) is deliberate:** runs after the LanceDB snapshot at 03:30 UTC, so snapshots capture the pre-lint state and nightly lint changes are visible the next day.
- **If anything fails post-deploy that wasn't anticipated:** revert is `git revert <hash> && docker compose up -d --build retrieval-server` — the change is small enough that revert is safe.
