# Preserved meeting archive — September10,2026

Patrick requested all existing87 meetings' Markdown files in the workspace and
removal of synthetic September10 entries. Implementation and isolated verification
are complete; production request CBM-MEETING-ARCHIVE-20260910-009 deployed and
was independently verified and acknowledged.

## Catalog and provenance

All87 canonical session IDs have matching preserved output folders. The archive
contains481 exact original files:351 output files plus130 historical recording
Markdown files. All87 have prepared-transcript.md, extracted-signal.md and
community-post.md; other existing transcripts, summaries, compressed posts,
weekly invites and six legacy versions are included without regeneration.
Each artifact retains original relative path, origin, size and SHA256. All481
are valid UTF-8 without BOM. One historical folder dated2026-03-25 maps to the
indexed2026-03-24 date using its explicit recording_start_time; no time was invented.

Built from the VM108 approved data-only preservation delivery, verified against
manifest SHA2564f41f14043a718e28e06aeb5707310408103e7dcc2602d9b5bfb7ddb3c78d3d7.
Catalog manifest SHA2563ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00.
Private catalog/files staged directly to VM109 /srv/community-brain/meeting-archive-20260910/.
No raw Markdown copied to Forge. No model/embedding call or LanceDB/DB mutation.

## Interface and API

Meetings is the default view, with date search, file groups, literal Markdown
preview, copy/download and dark mode. Recent runs retains actual new processing
history. A meeting with a new run links to it without overwriting preserved files.
Historical entries are not fake jobs and do not fabricate processing/stage status.

GET /api/v1/meetings uses existing jobs:read; file content uses artifacts:read.
Both enforce the archive scope. Manifest pinning, allowlisted opaque IDs, safe
paths and hash/size verification protect downloads. Missing/corrupt files fail
closed; no automatic repair or reprocessing. API mounts the archive read-only.

Configured synthetic IDs f6e9abed-e862-4eb7-a231-e98467adcaba and
91d77409-afed-4625-97cb-748c8b637991 are filtered before job-list pagination and
denied by direct job/artifact routes. Their durable evidence and inert queue
records remain intact privately. Real September8 job48550d00-9ad8-4b77-9f05-00ef5e929a5e
remains accessible. No broad deletion of historical or test evidence.

## Validation and deployment

Canonical check passed150 Node,904 Python,36 isolated PG/NATS,1 component and2
browser tests. New tests cover archive access boundaries, tamper/missing/symlink
failures, manifest pinning, synthetic filtering/pagination with durable evidence
preserved, search, literal Markdown, downloads and mobile dark-mode layout.
Forge visually inspected the mobile fixture screenshot. New archive module lint
passes with the existing FastAPI Depends convention exempted (B008); broad existing
API/runtime lint debt was not rewritten as part of this change.

The exact production base image with read-only candidate modules on VM108 served
all87 dates and481 authenticated file hashes in a network-disabled disposable
container with no database, queue or provider access. The container was removed.
Tested source/static packet is cbm-archive-ui-20260910 on both VMs; the safe source
manifest is cbm-archive-ui-manifest.json. Management owns current-authority API
recreation, pinned effective manifests and private off-host recovery coverage.

Request009 completed at17:08:17UTC. Forge verified all22 response files and
independently fetched the three new static assets over verified HTTPS. Production
catalog matches all87 canonical dates, all481 authenticated file hashes passed,
and the two synthetic job/details/artifact routes return404. Six real September8
artifacts remain valid. All DB fingerprints and original files/corpus/config
hashes are unchanged; only API/Alloy run, auth scopes and monitoring passed.

Two private off-host recovery archives include the full history and effective
source/static/recreation controls. Isolated extraction validated481 file hashes
and11 effective packet files, and was removed afterward. POST-MANUAL-JOB.md now
requires this archive and manifest pin in future recovery inventories. Historical
paired checkpoints remain unchanged. See cbm-meeting-archive-receipts-20260910/.
User visual acceptance remains pending. Count clarification:481 total files
includes447 .md,28 .txt and6 .md.legacy files; no content was regenerated.
Publication, reindex/replacement, recurring polling and retirement remain gated.

Patrick subsequently confirmed historical file viewing and downloads work perfectly.
User acceptance is complete; the follow-up request is expandable date navigation
and an accessible manual new-meeting form. No reprocessing was requested.
