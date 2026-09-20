# Manual processing staging readiness — September 10, 2026

Patrick approved `cbm-manual-processing-cutover-phase.md` and selected Fathom call
`812746883` again as the first production manual meeting. The previously verified
API recording is `181075701`, started `2026-09-08T21:54:33Z`, local date September 8,
zone `America/Toronto` (17:54:33 EDT). Matching previously approved Zoom chat:
`2026-09-08 19.41.15 AI Developer Accelerator Coaching Call/2026-09-08-zoom-chat.txt`,
6,804 bytes, SHA256 `5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084`.

This date already exists in the canonical corpus. New manual recap artifacts may
be acquired/processed under the approved phase and remaining budget; **replacement
of the existing indexed session is held for a separate explicit decision**.
The production adapter rejects that collision before dispatch. It also rejects
both earlier production synthetic jobs by ID. No ordinary queue worker is enabled.

## Verified disposable exercise

VM108 private copy: `/srv/dev-data/workspaces/cbm-manual-index-20260910`.
Restored the verified nonempty production DB dump into its own PostgreSQL18.6
container, with a fresh JetStream2.10.27 queue and no host ports. Its 53 copied
files match the paired checkpoint; all original DB/file references verified.
No production database, queue, submission or monitoring credential entered this
copy. Only the existing Infisical-rendered bounded model key reached its single
indexing worker, and that temporary delivery was removed after execution.

- Indexed only the copied weekly synthetic job: 8 successful chunks, 9 requests,
  9 durable response receipts, **US$0.00768625**, maximum 32 requests.
- All 1,901 original rows remain byte-value identical; 87 preserved sessions remain.
- Explicit copy-only FTS rebuild: 8 unindexed new rows became full 1,909-row coverage.
- Exact candidate image/helper checks: five authenticated hybrid retrieval hits,
  nine artifact-download hashes, collector chat-only enforcement, unauthenticated
  denial, upload deduplication, and zero-call idempotent skip of all 8 new chunks.
- Production's original 53 files are unchanged; both synthetic jobs retain zero
  indexing attempts and two unsent indexing events. No live synthetic indexing.
- Provider-side allowance reconciled after billing settlement: **US$0.0515034
  lifetime used, US$1.9484966 remaining**, US$2 non-resetting limit unchanged.

Public manifests/results: `cbm-manual-phase-receipts-20260910/`.
Final canonical verification passed **150 Node, 899 Python, 35 PostgreSQL/JetStream,
one component and one browser test**, including the selected-Fathom, date-collision
and selected API-client guards. Ruff and diff checks passed.

## Exact production staging packet

Base image remains `sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`.
VM109 candidate: `/srv/community-brain/workspaces/manual-20260910/`.
`runtime-manifest.json` binds all 14 public source/config assets to the VM108-tested
packet. The companion public receipt records the archive SHA256. Helpers are
read-only mounted; private runtime files are root0600 under root0700 parents.

`production-staging/manual_host.py api-up` merges only the manual Compose overlay:
API managed files writable for scoped uploads; config/corpus stay read-only;
no model/Fathom/queue keys or workers enter the API. It refuses any broad collector
permission. Production API restart requires the management activation handoff
after fresh Infisical identity merge; do not copy a stale pending API environment.

The overlay also explicitly maps the preserved cue-rules and speaker-aliases paths
to `/state/config`. Inspection found the prior runtime used absent `/app/config`
defaults for these two query features. The corrected candidate loads 13 cue rules.
No prompt, splitter, corpus row or retrieval algorithm changed. Q-06 records the
final quality-validation obligation; Q-05 remains open for final lifecycle review.

`manual_host.py inspect JOB STAGE GENERATION` creates a private review manifest.
`manual_host.py execute /srv/community-brain/manual-approvals/SELECTION.json`
executes exactly that stage once. Selection binds job/stage/event/generation,
identity/config and source/artifact hashes; a durable start marker prevents blind
restart. The in-container file lock serializes manual workers, independently of
the Forge connection. Existing corpus locking also covers explicit FTS maintenance.
The first packet has a 12-request processing ceiling. The separately staged and
VM108-verified V2 packet at `/srv/community-brain/workspaces/manual-20260910-v2/`
has the reviewed **20-request ceiling** for Patrick's selected weekly meeting
(the same meeting previously required 15 requests). V2 also includes the selected
API submission client. Its 15 assets and exact-image receipt are recorded in
`runtime-manifest-v2.json` and `image-checks-v2.json`. Use V2 for the future manual
worker after request005 completes; the active request's original packet is unchanged.
Indexing has 32 requests; both paths check the unchanged US$2
key before requests. Uncertain outcomes stop for reconciliation. Acquisition has
only its Fathom key, at most five metadata pages with all content inclusion disabled,
then at most one selected transcript GET. No scheduler, broad outbox sweep, automatic
retry, network publication, Git/distribution handler or service retirement.

## Gates retained

Management must verify fresh identities, TLS and allowed/denied upload checks before
the selected manual Mac upload. Forge then submits/acquires/processes the selected
job and reviews artifacts; no existing session is overwritten. A new paired
DB/files checkpoint and disposable recovery are still required after ownership
checks. Only a separately verified superseding ownership receipt may retire the
temporary hold mechanism. The September 11 **01:25 UTC rollback start /01:30 UTC hard
deadline remain armed**. Probe renewal remains due before 02:05:38 UTC. Publication,
service retirement, two-cycle stabilization and final quality closure stay gated.

## Subsequent activation and recovery status

Request **CBM-MANUAL-ACTIVATE-20260910-005** was completed, independently verified
and acknowledged. The selected real production job completed acquisition and
processing; see [the production result](cbm-manual-production-results.md).

Request **CBM-MANUAL-RECOVERY-20260910-006** completed and was independently
verified and acknowledged. The fresh paired restore, off-host/PBS checkpoint,
probe renewal and manual API recreation checks passed. Follow-up
**CBM-MANUAL-OWNERSHIP-20260910-007** covers maintenance gaps and conditional
steady-state ownership supersession. The rollback deadline remains armed until
that final receipt passes. The relay is active; no message copying is needed.

The disposable rehearsal containers, networks and PostgreSQL/JetStream volumes
have been removed. Original development services are unchanged. Private final copy
evidence remains on VM108: `final-copy.dump`, `final-copy-state.tar.gz` and
`final-copy-manifest.json` under the rehearsal workspace (87 files); the temporary
model key is absent. This is explicitly a disposable synthetic copy, never a
production replacement corpus or production recovery checkpoint.
