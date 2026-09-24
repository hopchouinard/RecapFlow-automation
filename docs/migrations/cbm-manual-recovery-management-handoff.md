# CBM-MANUAL-RECOVERY-20260910-006

Target: home.servers. Patrick approved the manual processing phase and has now
asked Forge to launch its remaining work. Request 005 was verified and acknowledged.
This request completes recovery and prepares steady-state ownership within that
phase. No new recording, provider request, publication or service retirement.

## Verified production result

Read attached cbm-manual-production-results.md and production-job receipts.
Job 48550d00-9ad8-4b77-9f05-00ef5e929a5e completed acquisition and processing.
All six authenticated downloads passed; 15 requests cost US$0.340603766.
Existing US$2 lifetime key now has US$1.607892834 remaining. Do not rotate/top up.
Only API and Alloy containers are running. Existing September 8 indexed session
remains unchanged: indexing selection refused replacement before dispatch.
There are three inert unsent indexing events; never replay the queue.

## Execute recovery

Private VM109 directory:
`/srv/community-brain/artifacts/cbm-manual-production-20260910/`.

- managed-state.tar.gz: 79 files, SHA256
  28c782fe46711eae3bf4132a7df37ff0e963abddefb1259438c4d7b2e39cd824.
- manual-runtime-state.tar.gz: 42 files, SHA256
  b8a9c65a18f52f9e9b34371f177592a89196878087db10d3e9a260152582e3ba.
- Matching *-manifest.json files record each file hash/size. Runtime archive is
  private operational recovery data, including manual approval/start markers.

Capture a fresh logical production DB dump using existing management access.
Verify the file manifests against current sources before and after capture;
manual intake is idle, workers stopped, API still serving. If drift occurs,
stop pairing and report it; do not claim these are simultaneous snapshots.
Create an explicit paired manifest, retaining the previous checkpoint.

Restore the fresh dump and both archives into disposable isolated copies with
no worker, publication handler, provider credentials or live queue connection.
Compare exact nonempty records across all application tables and required grants,
not just totals. Expected jobs3/sources6/artifacts15/model_calls29/stages15/outbox7;
validate all 50 database-to-file references and 79 managed file hashes, plus
42 runtime/approval files. Verify 1901 canonical rows, 87 sessions, full FTS,
and unchanged canonical configuration/corpus. Never restore over production.
Remove disposable restore resources after receipt capture. Copy the paired set
and private runtime state off-host through the established backup path and take
an associated PBS checkpoint. Report paths, hashes, coverage and consistency
limits; no secret values, raw transcript, dumps or provider responses in relay.

## Reconcile ongoing operations

Inspect and update the effective management API recreation/renewal recipe so it
preserves the manual overlay and identities. Active API uses
`/srv/community-brain/workspaces/manual-20260910/production-staging/manual_host.py api-up`
with compose.production-staging.yml plus compose.production-manual.yml.
The V2 selected worker is in workspaces/manual-20260910-v2. Preserve both packets.
The old staging launcher rejects write scopes; do not invoke it to recreate API.
Keep image sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449,
13 loaded cue rules, config/corpus read-only, files writable, and all five scoped
identities. API must have no provider/Fathom/queue credentials or publication.
A controlled API recreation and subsequent TLS/auth/health/cue checks are within
the approved manual activation phase if needed to prove the recipe.

Explicitly renew the expiring read/metrics probe credentials through existing
Infisical management and update their consumers atomically, verifying monitoring
and negative scope checks. Existing expiry September 11 02:05:38 UTC would break
ongoing monitoring. Preserve human, retrieval, collector, operator, Fathom and
bounded model identities; no additional privileges or unrelated key rotation.
Report new probe expiry and renewal ownership without values. If existing scope
or access cannot support renewal, report the concrete blocker.

## Prepare ownership decision; keep deadline armed in this request

Inspect and document concrete steady-state controls keeping old n8n/retrieval
writers, lint/snapshot/artifact-push schedules and Mac legacy intake disabled.
Include safe supersession of BOTH VM101 rollback/boot controller and Mac resume
hook, preserving old restoration state and preventing stale automatic rollback
from resuming competing writers. Record future backup/maintenance owner and any
remaining maintenance gap. Do not enable a new corpus-mutating schedule here.

Do NOT disarm/extend September 11 01:25 UTC rollback (01:30 hard deadline) yet.
Return the verified recovery receipt and concrete supersession procedure to Forge
for the approved phase's final readiness check. Existing corpus replacement,
remote publication, CBM-09, service/data retirement and final CBM-10 remain gated.
Two real weekly cycles have not completed. Continue monitoring for the follow-up.
