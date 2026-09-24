# CBM-MEETING-ARCHIVE-20260910-009

Patrick requested exposing all preserved Markdown files from the existing87
meetings in the workspace and removing the synthetic September10 entries. This
request deploys that read-only history view and hides the exact two rehearsal
jobs from workspace APIs, preserving their DB/file/queue/recovery evidence.
No historical content is reprocessed, no new jobs/embeddings are created and no
LanceDB modification is authorized. Request008 is acknowledged; dark mode was
accepted. Existing ownership/retirement/publication gates remain unchanged.

## Prepared and tested

VM109 private dataset: `/srv/community-brain/meeting-archive-20260910/`.
It contains manifest.json and files/<64hex-id>. Manifest SHA256:
3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00.
87 dates exactly match live canonical session IDs.481 files were copied directly
from VM108's verified preserved delivery, never from model regeneration. Each
file matches its manifest hash/size; original preservation manifest hash is
4f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7.
All87 dates have prepared-transcript.md, extracted-signal.md, community-post.md.
Additional original transcripts, summaries, compressed posts, invites and legacy
versions remain individually identifiable. Original historical folder2026-03-25
maps to2026-03-24 using its explicit recording_start_time, matching the indexed
session; every original relative path is retained in the private manifest.

VM109 tested source/static packet:
`/srv/community-brain/workspaces/cbm-archive-ui-20260910/`.
Contains api.py,runtime.py,archive.py,check.py,dist/ and runtime-manifest.json.
Attached cbm-archive-ui-manifest.json binds all7 files. These are reviewed read-only
API modules plus frontend, not a new worker image or dependency. api.py adds the
scoped archive routes and hidden-job filtering before cursor pagination and direct
job/artifact reads. runtime.py loads the pinned archive and configured hidden IDs.
archive.py never touches PostgreSQL, queue, model provider or corpus. Auth uses
existing jobs:read for catalog and artifacts:read for bytes, matching scope; keys
must exist in the manifest and content hashes must pass before downloads.

Canonical verification passed150 Node tests,904 Python tests,36 isolated PG/NATS
tests,1 component test and2 browser tests. Tests cover hidden-job pagination and
preserved DB/outbox, wrong-scope/collector/unauthenticated denial, missing/tampered
files and symlink denial, Markdown text safety, date search, dark mode/mobile and
downloads. Exact existing image on VM108 with read-only candidate modules and
network disabled verified all87 dates and481 authenticated file hashes. No DB,
queue or provider entered that rehearsal. Disposable container removed.

## Activate using existing management recipe

Verify complete dataset and packet hashes before deployment. Retain private
before-state of overlay/runtime manifest/Mac recreation helper and API image/env,
current database fingerprints, stored files and corpus/config hashes.
Keep backend image sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449.
Use current-authority Infisical rendering, existing two-file manual Compose recipe,
and only recreate API after these reviewed additions to its overlay:

- Read-only dataset bind to /state/meeting-archive.
- Read-only candidate api.py,runtime.py,archive.py binds to the respective
  /app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs/*.py.
- Point the API-only /app/web/dist bind at candidate dist. Retain previous hashed
  static assets (all current URLs) without collisions; pin their supplemental
  hashes too so existing sessions continue working.
- CB_MEETING_ARCHIVE_ROOT=/state/meeting-archive
- CB_MEETING_ARCHIVE_SHA256=3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00
- CB_HIDDEN_JOB_IDS must be exactly JSON array:
  ["f6e9abed-e862-4eb7-a231-e98467adcaba","91d77409-afed-4625-97cb-748c8b637991"]

Reconcile the active runtime packet and Mac helper validation with these reviewed
module/static/dataset manifests; do not weaken hash pinning. Preserve historical
manifests/checkpoints unchanged and record the new chain. No changes to worker
packets, identity values/scopes, prompts, NATS, model budget, corpus or databases.
The static source/data directories must be readable by container UID10001 under
protected host parent /srv/community-brain; all API mounts remain read-only except
existing managed files. No new host port/listener/public route without auth.

## Acceptance and recovery checks

Through verified HTTPS and current private read/operator tokens:
- GET /api/v1/meetings gives87 dates exactly matching canonical session IDs.
- All481 manifest URLs return exact preserved hashes/bytes as text/plain with
  nosniff, private/no-store and original download filename. Unauthenticated401,
  collector403; wrong-scope refusal is covered by isolated tests.
- /api/v1/jobs now returns only real job48550d00-9ad8-4b77-9f05-00ef5e929a5e;
  hidden synthetic direct job/artifact routes404. Their database rows,14 response
  receipts and two indexing events remain intact; no DB delete/update.
- Real job previews/downloads and all existing15 scope checks still pass (update
  the jobs-list expectation for the intentional hide, not the DB totals).
- New index/callback/assets match expected bytes. Healthy API+Alloy only,13 cue
  rules, existing corpus/config read-only, provider/queue absent. Actual cached
  WebUI context and monitoring unchanged. Terminal legacy guards remain effective.
- All10 DB fingerprints and original files/corpus/config hashes unchanged.

Back up the new archive, source/static packet and effective recreation controls
privately/off-host with exact481-file manifest/hash coverage. Explicitly add the
archive root and its pin to the existing POST-MANUAL-JOB/recovery inventory so it
cannot disappear during a later restore. This is read-only additional history,
not changed job state; existing paired application checkpoint remains valid for
its recorded scope. Verify an isolated extraction of the archive backup matches
all481 files; no provider, live queue, DB restore or model call is needed.

Rollback if verification fails: restore saved overlay/runtime manifest and the
prior pinned Mac recreation helper, render current authority and recreate only
API. Verify old dark-mode assets, real job access, scopes and health; hidden jobs
would reappear under that old API, so report this honestly. Retain all new files
and backups for investigation. Never restore old api.env or legacy writer controls.

Return safe receipt/hashes and exact verification results in responses/this-ID.
No raw Markdown, secret values or DB dumps in relay. Do not move to publication,
CBM-09, corpus replacement or retirement. Forge will verify and request user
acceptance once live. Continue monitoring the shared relay.
