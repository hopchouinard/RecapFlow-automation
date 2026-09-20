# Next major phase: manual processing and indexing ownership

Status: **approved by Patrick on September 10, 2026**. Retrieval is switched and Patrick
accepted his real Open WebUI experience. Legacy writers remain held; independent
rollback begins September 11 at 01:25 UTC for the 01:30 hard deadline. This proposal
does not cancel that deadline. Patrick approved the bounded additional provider
calls below using only the existing key's remaining allowance.

## Intended operational result

Community Brain on VM109 becomes the sole writer for explicitly selected manual
meeting jobs, producing downloadable Markdown artifacts and indexing into the
canonical local corpus. No recurring Fathom polling, automatic queue-wide replay,
remote Git/distribution publication or board posting is enabled. The existing
retrieval and offline consumer contracts remain unchanged. Service retirement,
CBM-09 and final CBM-10 quality work remain separate.

## Execution boundaries

1. Implement and test explicit eligible-job/stage selection before any ordinary
   worker starts. The two synthetic jobs and their unsent indexing events remain
   excluded from live indexing. Do not delete their evidence or dispatch a broad
   outbox sweep. Verify unrelated work cannot execute, retries preserve successful
   outcomes, and uncertain effects stop without blind replay. Use the tested
   TLS-first/scoped-inbox transport and preserve single-writer locking.
2. Exercise indexing with the existing synthetic artifacts only in a disposable
   copy of database/files/config/corpus, never against the live 87-session corpus.
   Record the copy's identity and retain all production hashes for comparison.
   Validate partial/failure behavior, full FTS coverage, hashes and retrieval after
   indexing. Test failure/recovery with fake providers first. Indexing this copy
   must not mark the actual production synthetic jobs indexed.
3. Additional real model work in this phase is authorized to use the **remaining
   US$1.95618285** on the existing dedicated key, retaining its **US$2 lifetime cap**
   and non-resetting policy. No top-up, reset or new key limit is inferred. Check
   current allowance before each bounded exercise; define a request ceiling before
   dispatch. Stop on uncertainty/exhaustion. No historical transcript is reprocessed
   and no new recording is acquired without Patrick explicitly selecting it.
4. Prepare the scoped production manual collector/API identities through Infisical.
   Grant only required upload/submit/read operations to the intended callers;
   preserve independent human, collector, retrieval, worker and monitoring scopes.
   Production Fathom delivery, if needed for a selected job, is acquisition-worker
   only. No migration or management credential reaches workers/clients.
5. Verify the concrete image/helpers on development first; record exact manifests,
   ownership/limits, immutable file behavior, backup and rollback. Stage production
   processing/indexing only after that evidence passes. Allow job creation solely
   through manual operator action; preserve explicit recording choice and no
   background polling. Review each transition from artifacts to live indexing.
6. Cut over the manual Mac intake destination through its existing restricted
   collector, with a live scoped upload check and deduplication/hash receipt.
   Preserve the old sync configuration privately, but do not resume it alongside
   the new owner. Do not indiscriminately enable Folder Actions or load the old
   unloaded LaunchAgent. Select exactly one intake owner and one corpus writer.
7. After writer ownership and manual path verification, prepare a new paired
   DB/files checkpoint and test recovery without replaying queued work. Record
   scheduled maintenance ownership; legacy lint/artifact-push/snapshot jobs cannot
   resume as competing writers. Keep remote publication disabled.

## Superseding the current hold

Only after this approved phase's concrete writer/intake/backup checks pass may
management retire the temporary *hold mechanism* and cancel its rollback timer.
This is not permission to retire the old services/data/backups. Record the new
steady-state controls that keep old writers and intake disabled, preserve their
restoration procedure, then remove temporary immutable flags only where needed.
Do not restore old schedules accidentally while releasing the guard.

If readiness cannot be established before September 11 01:25 UTC, let the existing
verified rollback run and retain all progress/evidence for a later controlled
window. Do not extend the hold or disable its deadline merely to finish this phase.
Explicit probe renewal remains necessary before September 11 02:05:38 UTC if
monitoring the staged system continues; the WebUI identity has its separate expiry.

## Acceptance and remaining migration work

This phase must leave a recoverable manual processing path with no competing
writers. The first future user-selected real meeting remains an observed live
acceptance event, not something inferred from synthetic tests. Two successful
weekly cycles and recovery evidence are still required before retirement. Do not
claim complete CBM-08 stabilization before those cycles. Remote publication has
its own destination/identity approval. Preserve frozen v1 prompts and Q-01 through
Q-05 for the final migration quality step; do not mix those semantic changes into
this operational cutover.
