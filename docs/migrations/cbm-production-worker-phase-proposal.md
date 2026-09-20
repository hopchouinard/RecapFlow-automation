# Next phase proposal: bounded production-worker rehearsal

Status: approved by Patrick on September 10, 2026, with a **US$2 total cap**. API staging acceptance is complete for the
recorded cases: real Patrick login, matching preserved-corpus queries, active
monitoring and restored migrated schema. See the post-API management receipt.
This is not readiness for intake cutover or service retirement.

Completion: both synthetic jobs and paired nonempty DB/files recovery passed.
See `cbm-production-bounded-worker-results.md` and
`cbm-production-nonempty-recovery-readiness.md`. Unused allowance authorizes no
additional execution.

## Approved bounded scope

Prepare and verify the production worker's TLS-first NATS connection and scoped
`_INBOX.cbm_prod_worker` replies, using the delivered account. First exercise
transport and worker recovery with simulated providers on disposable development
dependencies; no production model call occurs during implementation.

For the subsequent production rehearsal, use only the existing synthetic fixture,
with at most one weekly and one backfill job, explicitly submitted by the operator.
No Fathom recording, historical corpus text or Mac chat is used. Create a separate
production OpenRouter key with a non-resetting **US$2 total provider-side cap**,
managed by Infisical and delivered only to the bounded worker. This is the approved production limit, not a reuse of the approved US$5 development key. Confirm provider
availability and enforce per-job request bounds before enabling execution.

The concrete worker invocation must accept only the two recorded job IDs, stop
when they finish or encounter an uncertain outcome, and refuse other jobs. Scope
live processing to artifact generation: indexing and publication stay disabled;
keep the preserved corpus/config read-only. No recurring intake, general queue
consumer, external corpus release or Git push is enabled. Preserve frozen v1
prompts and all existing quality findings.

Verify accepted-job persistence, bounded execution, authenticated artifact hashes
and downloads, independent final states, and unchanged preserved corpus/config.
Use separate scoped temporary submit/check identities; Patrick's browser identity
can remain read-only. Then repeat coordinated DB/files backup and disposable
restore with actual rehearsal job/artifact records, checking every reference/hash.
Do not intentionally interrupt paid requests to manufacture unknown outcomes;
recovery fault injection remains on simulated providers.

## Remaining gates and prerequisites

Phase approval permits preparing the scoped credentials/identities and executing
these two bounded synthetic jobs after implementation checks pass. It does not
permit production intake ownership changes, Open WebUI endpoint changes, broader
processing, historical replay, publication or retirement. Those require a later
concrete cutover checkpoint including final source drift and rollback evidence.

Service probes expire September 11, 2026 at 02:05:38 UTC; arrange explicit rotation
and coordinated refresh if the rehearsal crosses that deadline. The API's current
readiness does not extend token lifetime. Production recovery uses daily logical
restore points, not PITR. CBM-09 remains separate and CBM-10/Q-01 through Q-05 must
remain the last step of the whole migration.
