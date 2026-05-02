# Ingest / Lint Decoupling — Design Spec

**Status:** Proposed (2026-05-02)
**Type:** Architectural fix — corpus-derived markers / `/ingest` reliability
**Affects:** `community-brain/src/community_brain/ingestion/pipeline.py`, `community-brain/src/community_brain/cli/lint_corpus.py`, related tests, deployment cron

---

## 1. Problem statement

`/ingest` is timing out on the n8n side (30-minute HTTP timeout) on certain sessions, and the retrieval-server periodically enters a "Too many concurrent writers" retry storm that monopolizes CPU and makes `/sessions` and `/query` return wrong/stale data while the storm is active.

Concrete observation (2026-05-02 04:11 UTC, run #4549, session `2025-12-09`):
- LLM phase completed in normal ~14 minutes
- `/ingest` POST sent
- n8n received `ECONNABORTED` after exactly 1,800,000ms (30 min)
- Retrieval-server logs show `lint_corpus auto-trigger failed: lance error: Too many concurrent writers` repeating throughout the window
- The chunks for `2025-12-09` actually committed successfully (visible in `/sessions` after retrieval-server restart) — the timeout was caused by the post-commit lint phase, not by the commit itself

This was not a one-off. The same pattern (lint storm after /ingest) has been visible in retrieval-server logs since at least 2026-04-30 and was masked because most sessions completed lint within the timeout window. As corpus size has grown from ~167 chunks at v2 deploy to ~1,500 chunks today, the storm has gotten progressively worse.

## 2. Root cause

`lint_corpus_chunks()` (`community-brain/src/community_brain/cli/lint_corpus.py`) does **one `table.update()` per chunk in the entire corpus, every time it runs.** Of the four code branches that decide what to write, two are pure no-op timestamp bumps:

```python
elif should_be_recurrent:                              # already correct, no marker change
    table.update(values={"corpus_markers_computed_at": now_iso})

else:                                                   # already correct, no marker change
    table.update(values={"corpus_markers_computed_at": now_iso})
```

These two branches account for ~95% of the writes during a typical lint pass — most chunks don't need their markers changed; the code rewrites them anyway just to bump the timestamp.

Because LanceDB is copy-on-write at the manifest level, each `table.update()` call creates a new manifest version. Firing 1,500 of them in a tight loop saturates the manifest commit pipeline. Lance's optimistic-concurrency retry mechanism interprets self-contention as "concurrent writers" and starts retrying with `retry_timeout=30s`, which doesn't help because the contention is the writer fighting its own backlog.

The auto-trigger from `_post_commit_maintenance` (`pipeline.py:514`) makes this part of every `/ingest`. So:

- Per-session ingest cost ≈ N write operations on the corpus
- N grows linearly with corpus size
- /ingest is currently O(N) on **total corpus size**, not session size
- At ~1,500 chunks, that's already exceeding n8n's 30-min timeout under contention
- At ~10,000 chunks, /ingest would be unusable

The current design has the right algorithmic core (K-NN to find recurrent topics) bolted onto the wrong execution model (synchronous, in the hot path of /ingest, rewriting every row every time).

## 3. Goals

1. **Make `/ingest` complete in time bounded by session size, not corpus size.** No more 30-minute timeouts.
2. **Eliminate the "concurrent writers" storm** by removing the saturating-write pattern.
3. **Keep the corpus-derived markers feature** — recurrent flagging still works, just on a different schedule.
4. **Maintain test coverage** — the post-commit invariant guarantees that matter (FTS index, schema validity) stay enforced.

## 4. Non-goals

- Not redesigning `lint_corpus_chunks`'s K-NN algorithm. The algorithm is fine; the integration is broken.
- Not adding parallel write support to LanceDB. Out of scope.
- Not building a new background-task framework inside the retrieval-server. Cron + manual invocation is sufficient for personal-tier scale.
- Not changing the trust model, ranking, or query-side behavior. Markers are derived metadata; their freshness affects ranking quality slightly but not correctness.
- Not fixing the n8n state file inconsistency for `2025-12-09` (handled separately as operational cleanup).
- Not addressing the n8n Workflow 6 build-ingest-payload Code node bug (separate issue, blocking only `2025-08-27` and `2025-12-17` which are already reserved).

## 5. Proposed solution

Two coordinated changes:

### Change A — Drop the no-op timestamp writes

In `lint_corpus_chunks()`, the two no-op branches (lines ~169–185 of `lint_corpus.py`) are removed. The function now only writes when a chunk's marker state actually changes:

```python
if should_be_recurrent and not currently_recurrent:    # ADD recurrent → write
    table.update(...)
elif not should_be_recurrent and currently_recurrent:  # REMOVE recurrent (rebuild only) → write
    if rebuild: table.update(...)
# No write for "already correct" branches.
```

The `corpus_markers_computed_at` field becomes a record of **last meaningful change**, not "last lint pass." This is a documented behavior change — see §7 backward compatibility.

After Change A:
- Writes per lint pass = number of chunks whose marker state flipped (typically 0–30 per ingest, often 0 once the corpus stabilizes)
- Reads per lint pass = unchanged (still K-NN search per chunk)

### Change E — Remove the auto-trigger from `/ingest`

In `_post_commit_maintenance` (`pipeline.py`), remove the call to `lint_corpus_chunks(db_path)`. Keep the `verify_corpus_v3_state` invariant check — that's fast (one read pass over schema/FTS state) and load-bearing.

`/ingest` post-commit work becomes:
1. Open the freshly-committed table
2. Run `verify_corpus_v3_state` (invariant: schema + FTS index)
3. Return

Lint becomes operator-scheduled — daily host cron, manual invocation, or a separately-scheduled n8n workflow.

After Change E:
- /ingest cost = O(session chunks) for commit + O(1) for verify
- Lint cost = O(corpus chunks) but runs once per day, not once per ingest
- /ingest becomes architecturally immune to lint-related slowdowns and storms

### Change F (operational) — Schedule lint as a daily cron

Add a host crontab entry (or compose-managed scheduled job) on the n8n VM:

```
# /etc/cron.d/community-brain-lint
0 4 * * * pchouinard docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus >> /home/pchouinard/n8n/logs/lint-corpus.log 2>&1
```

Runs at 04:00 UTC daily (after the LanceDB snapshot at 03:30 UTC, so snapshots capture pre-lint state). Logs to a rotating log file. Failure is non-fatal — markers stay where they are.

After Change F:
- Markers stay fresh within a 24-hour window
- Lint is observable independently of /ingest
- Failure modes are isolated: a busted lint run doesn't break ingestion

### Why A + E together?

A alone solves the immediate write-storm bug but leaves the auto-trigger pattern in place. The K-NN reads are still O(N) per ingest — at 10k+ chunks they'd still slow ingest noticeably even without writes.

E alone removes the auto-trigger but leaves the no-op-write bug in `lint_corpus`. A daily lint pass would still hammer the manifest writer with 1,500 unnecessary writes.

Together: ingest is fast and reliable forever, lint is correct and proportional to actual change.

## 6. Architecture

### Before

```
n8n /ingest POST
   │
   ▼
ingest_session()
   ├─ Stage A-D (parse, chunk, extract, embed)
   ├─ Stage E: _commit_chunks                        ← O(session chunks)
   └─ _post_commit_maintenance
       ├─ verify_corpus_v3_state                     ← O(1)
       └─ lint_corpus_chunks(db_path)                ← O(corpus chunks) writes ⚠️
           └─ for chunk in entire_corpus:
                table.update(...)  # every chunk     ← The bug
```

### After

```
n8n /ingest POST
   │
   ▼
ingest_session()
   ├─ Stage A-D
   ├─ Stage E: _commit_chunks                        ← O(session chunks)
   └─ _post_commit_maintenance
       └─ verify_corpus_v3_state                     ← O(1)

(separately)

cron 04:00 UTC daily
   │
   ▼
docker exec community_brain_retrieval python -m community_brain.cli.lint_corpus
   └─ lint_corpus_chunks(db_path)
       └─ for chunk in entire_corpus:
            if marker state would change:           ← Change A
                table.update(...)
            # else: no write
```

## 7. Backward compatibility

### Behavior changes (deliberate)

| Field / behavior | Before | After |
|---|---|---|
| `corpus_markers_computed_at` semantics | "Timestamp of last lint pass that scanned this chunk" | "Timestamp of last meaningful marker change" |
| `corpus_markers_computed_at` freshness | Updated every /ingest | Updated only when marker state changes; otherwise unchanged |
| Lint trigger | Synchronous after every /ingest | Cron at 04:00 UTC daily, plus manual |
| Marker freshness lag | ~immediate | Up to 24h |

### What does not change

- `corpus_derived_markers` semantics (the actual `recurrent` flag) — unchanged
- Marker-aware ranking in `/query` — unchanged
- Schema (`schema_version`) — unchanged; the `corpus_markers_computed_at` column stays nullable string, no migration needed
- `/ingest`, `/query`, `/sessions`, `/reindex` API surface — unchanged

### Migration

No data migration required. Existing chunks keep whatever `corpus_markers_computed_at` they currently have. The first cron run after deployment will refresh stale markers as it would have under the old auto-trigger.

### Failure modes preserved

- Operator can still run `python -m community_brain.cli.lint_corpus` manually whenever they want to refresh markers (same CLI as before)
- `--rebuild` flag still works for full marker recomputation after big corpus changes
- The `lint_corpus_chunks(rebuild=True)` row-rewrite path for stale-marker removal is unchanged

## 8. Test strategy

### Tests to remove or repurpose

| Test | Action | Reason |
|---|---|---|
| `test_ingest_session_auto_triggers_lint_corpus` | Remove | Auto-trigger no longer exists |
| `test_idempotent_retry_runs_lint_corpus` | Remove | Same as above |
| `test_post_commit_maintenance_lint_uses_explicit_db_path_not_env_var` | Remove | Lint is no longer called from post-commit |
| `test_ingest_session_does_not_fail_when_lint_raises` | Remove | Lint not in /ingest path; can't fail it |

### Tests to add

| Test | Asserts |
|---|---|
| `test_post_commit_maintenance_does_not_call_lint_corpus` | The auto-trigger is gone — `lint_corpus_chunks` is not invoked by `_post_commit_maintenance` |
| `test_post_commit_maintenance_still_verifies_corpus_state` | `verify_corpus_v3_state` is still called (the invariant check stays) |
| `test_lint_corpus_skips_writes_when_marker_state_unchanged` | Build a 100-chunk corpus where most chunks are non-recurrent and marked correctly. Run lint. Assert: write-call count ≪ 100 |
| `test_lint_corpus_writes_only_state_transitions` | Build a corpus, run lint, then run lint again. Second run produces 0 writes (idempotency at the write layer) |
| `test_lint_corpus_still_adds_recurrent_when_qualifies` | Build a corpus with cross-session similarity. Run lint. Assert: recurrent marker added correctly |
| `test_lint_corpus_rebuild_still_removes_stale` | Pre-populate a stale recurrent marker. Run with `rebuild=True`. Assert: marker removed |

### Tests to keep unchanged

- `test_lint_corpus_idempotent` (existing) — should still pass; behavior tightens (now true write-level idempotency, not just marker-state idempotency)
- All tests of `lint_corpus_chunks` core algorithm (KNN search, similarity threshold, cross-session counting)

### Performance regression test (new)

Add a timing test that times `lint_corpus_chunks(db_path)` against tmp_path corpora at N=100, N=500, N=1500 chunks where no marker state changes. Assert: total write calls ≪ N. This locks in Change A and prevents regression.

### Smoke test for cron command

The cron command runs `python -m community_brain.cli.lint_corpus`. The CLI's `main()` already has tests; the cron wrapper just invokes it. No new test needed beyond a one-time manual smoke run after deploy.

## 9. Risks & mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Removing the auto-trigger leaves new sessions un-marked for up to 24h | Certain | Low | Markers are derived metadata; ranking still works, just slightly less optimally for that 24h window. Operator can manually run lint anytime to refresh sooner. |
| Cron job fails silently | Medium | Medium | Log to `~/n8n/logs/lint-corpus.log`. Add a Grafana panel monitoring last-successful-run timestamp (Phase 5+ — optional follow-up). |
| Tests break in unexpected ways during refactor | Medium | Low | Phased implementation: Change A first (small, isolated), then Change E. Run full pytest suite between phases. |
| First post-deploy lint run is slow/disruptive | Low | Low | Cron runs at 04:00 UTC, low-traffic window. First run after deploy will rewrite chunks whose state was stale; subsequent runs are near-zero-write. |
| Operator forgets to set up cron after deploy | Medium | Low | Plan calls out cron setup as an explicit step with a verify command. Markers stale forever ≠ broken; just stale. |
| Existing tests reference `_post_commit_maintenance` lint behavior in ways the refactor breaks | Medium | Low | §8 enumerates exactly which tests to remove and which to add. |

## 10. Open questions

1. **Should we add a `/lint` HTTP endpoint** so the cron can use HTTP instead of `docker exec`? Slightly cleaner but adds API surface. Default: no — `docker exec` is simpler and there's no good reason to expose lint over HTTP. Revisit if we ever want to trigger lint from another system.

2. **Should the cron schedule be configurable?** For now, hardcoded to 04:00 UTC. If we ever distribute the retrieval-server publicly, this becomes a config knob. Personal tier: hardcode it.

3. **Is there value in periodically running `lint_corpus_chunks(rebuild=True)`?** The auto-trigger uses `rebuild=False` (skips stale-marker removal). After Change E, if we want stale removals to ever happen, we'd need either a weekly `--rebuild` cron or operator action. Default: weekly `--rebuild` cron, separate from the daily light pass. **Open for decision.**

## 11. Out of scope

- The lint algorithm itself (K-NN + similarity threshold) — unchanged
- Performance optimization of the K-NN reads — current O(N) per-chunk reads are tolerable at <10k chunks; revisit if/when we hit that
- Replacing LanceDB's optimistic concurrency with explicit locking — not needed; the bug was in the caller, not the DB
- The `/ingest` API contract — unchanged
- Workflow 6 (Plan C) state file cleanup for `2025-12-09` — operational task, separate
- Workflow 6 build-ingest-payload Code node bug — separate issue
- Adding cost/usage tracking to lint runs — out of scope for this fix; covered separately by the 2026-05-02 OpenRouter usage-tracking plan

## 12. Implementation reference

See companion plan: `docs/superpowers/plans/2026-05-02-ingest-lint-decoupling-plan.md`
