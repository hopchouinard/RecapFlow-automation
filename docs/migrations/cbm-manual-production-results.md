# Selected production manual run — September 10, 2026

Patrick's approved manual phase and selection of Fathom call `812746883` produced
six downloadable weekly recap artifacts in production. Acquisition and processing
each succeeded on their first attempt. **No live indexing or publication occurred.**

Job: `48550d00-9ad8-4b77-9f05-00ef5e929a5e`, scope `community-brain`, frozen
`processing-v1`, weekly mode. API recording `181075701`, September 8 at
`21:54:33 UTC` / `17:54:33 America/Toronto` (EDT). The matching selected chat and
newly acquired transcript exactly match the earlier approved hashes and sizes.

## Execution and integrity

- Production manual API/collector activation receipt: shared request
  `CBM-MANUAL-ACTIVATE-20260910-005`, independently verified and acknowledged.
  Fifteen TLS/auth checks passed; existing three identities stayed unchanged.
  The actual cached WebUI filter returned ten sources with its original URL,
  key and source hash. The API now loads all 13 preserved cue rules.
- Selected chat: source `dcba207e-92be-4661-995f-c48194a8f9af`, 6,804 bytes,
  SHA256 `5300e1d44b776254042f955493de9a88545e64b10a05cf014d0123a4224d6084`.
  The restricted Mac collector uploaded only this selected file; the explicit
  deduplication check returned the identical receipt. No automatic intake.
- Transcript: source `15e29d83-4e4a-443a-ac1a-097757c30646`, 112,886 bytes,
  SHA256 `79540c3f3f08a09dee48d5784026e0f980ec8a9fb85414091fdffba61fe18f75`.
  Only the acquisition worker received Fathom credentials; its selected GET guard
  limits metadata to five pages with content inclusion disabled and one transcript.
- Processing used the VM108-verified V2 worker packet and 20-request ceiling:
  **15 requests, all successful; US$0.340603766** in durable response receipts.
  No retries or unresolved intents. The six authenticated downloads matched
  their stored sizes and SHA256 hashes. Prompts/config snapshot remained unchanged.
- Provider usage reconciled exactly: **US$0.392107166 lifetime used,
  US$1.607892834 remaining**, unchanged US$2 non-resetting cap. This includes
  the earlier synthetic processing and disposable indexing exercise. No top-up.

Artifacts: `transcript.txt`, `prepared-transcript.md`, `extracted-signal.md`,
`community-post.md`, `community-post-compressed.md`, and
`2026-09-15-weekly-invite.md`. Their complete metadata is in
`cbm-manual-phase-receipts-20260910/production-job/api-artifact-verification.json`.
Review/download them through the authenticated recap workspace. Structural and
integrity checks do not constitute final semantic quality acceptance; CBM-10 remains
the final migration step, with Q-01 through Q-06 retained explicitly.

## Existing corpus is protected

The canonical corpus already includes September 8. A real production invocation
of the indexing-selection check rejected this job with
`existing session requires a separate replacement decision`, before dispatch or
model/embedding access. No indexing approval manifest was produced.

All original 53 checkpoint files remain unchanged, including all 13 corpus and
13 configuration files. The corpus remains 1,901 rows / 87 sessions with full FTS
coverage. The two synthetic production jobs retain zero indexing attempts.

Database state after this run: 3 jobs, 6 sources, 15 artifacts, 29 processing model
records, 15 stages and 7 outbox records. All **50 database-to-file references**
verified. Three unsent indexing events remain inert: the two excluded synthetic
jobs and this real job awaiting the existing-session decision. No general worker,
queue sweep, Git/distribution handler or scheduler has been enabled.

## Recovery and ownership follow-up

Private VM109 evidence: `/srv/community-brain/artifacts/cbm-manual-production-20260910/`.
After both workers exited, Forge captured and verified:

- `managed-state.tar.gz`: 79 files, SHA256
  `28c782fe46711eae3bf4132a7df37ff0e963abddefb1259438c4d7b2e39cd824`.
- `manual-runtime-state.tar.gz`: 42 runtime/approval/evidence files, SHA256
  `b8a9c65a18f52f9e9b34371f177592a89196878087db10d3e9a260152582e3ba`.
- Corresponding per-file manifests, verified archive members and unchanged-source
  checks. Runtime archive includes both active API and V2 worker recipes plus
  the durable manual selection/start markers. It is private, not a public package.

Management request **CBM-MANUAL-RECOVERY-20260910-006** completed at06:35:36 UTC
and Forge independently verified all17 response-file hashes before acknowledging.
Exact rows across all10 tables, schema/owners/grants,50 file references,79 managed
files and42 runtime files matched the disposable restore. Canonical coverage
remains1901 rows/87 sessions/768 dimensions/full FTS. Disposable copies were removed.

Fresh dump: platform-db `/var/backups/community-brain/20260910T061730Z.dump`,
56,658 bytes, SHA256
`3937db5e4f88b3c508bbbac5feac84f0443071b0d7d5709fa490397b53d973cd`.
Paired copies were verified off-host under
`/var/backups/community-brain/manual-20260910-006/`; PBS checkpoint
`pbs:backup/vm/109/2026-09-10T06:28:34Z` completed with both disks and guest freeze/thaw.
This is a verified quiescent logical pair, not simultaneous snapshots or PITR.

Read/metrics probes were renewed through Infisical to September17 06:22:56 UTC.
Both consumer updates and old-token rejection passed; other identities are unchanged.
The fresh-authority manual API recreation recipe passed twice, with15 TLS/auth
checks,13 cue rules and all required mount/credential boundaries. Kuma and both
Prometheus targets are healthy; actual WebUI retrieval still returned10 sources.
Full receipts: `cbm-manual-phase-receipts-20260910/management-006/`.

Follow-up **CBM-MANUAL-OWNERSHIP-20260910-007** addresses backup ordering and expiry
visibility, then conditionally executes the tested server/Mac ownership controls
under the already approved phase. See [the concrete ownership handoff](cbm-manual-ownership-management-handoff.md).
The September11 01:25 UTC rollback/01:30 hard deadline remains armed until that
supersession is verified. User artifact-preview/download acceptance is pending.
Existing indexed-session replacement, publication, service retirement, live
indexing acceptance and two-cycle stabilization remain separate gates. Final
CBM-10 quality work stays last.

## Subsequent acceptance and ownership

Patrick confirmed on September10 that the actual workspace previews and downloads
all work. This is functional user acceptance, not CBM-10 semantic closure.
Request007 completed and Forge verified all25 receipt files. At06:55:45UTC the
terminal manual ownership state committed; timer and service were masked at06:56:50.
Legacy writers/intake remain held; all2867 inodes remain immutable.19 controller
tests,16 maintenance cases and15 API checks passed. Backup timing and identity
expiry alerts are installed; the first actual evening schedule is still unobserved.
The old deadline is superseded, not extended. See management-007 receipts.
Patrick requested dark mode before further migration work; request008 covers only
that tested frontend update. All later phase gates remain intact.
