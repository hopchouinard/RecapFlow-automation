# Publication candidate v1.2.0 — private preparation verified

2026-09-17. Request021 completed and independently verified. This document
supersedes its pending-delivery status. Nothing has been published, no publishing
credential created, and no production stage or data changed.

## Exact candidate

- Selected job: September15,744d0f3f-8da7-4c12-bc15-5ec0a046518d.
- Git content: all six canonical files approved by Patrick, under the proposed
  output/2026-09-15/ path, including transcript.txt and the September22 invite.
  Each private staged file matches its selected immutable Artifact record.
- Proposed Git destination: hopchouinard/RecapFlow-automation, main. Inspected
  base dd29e82aa21f3e52d0ea7a96561f8dec9af28055 has no files in this date's target
  directory. No local project changes are included; no Git commit/push performed.
- Proposed consumer release: v1.2.0 in
  hopchouinard/community-brain-distribution. Version was absent from inspected
  remote refs. Consumer main was a192f7832e70d60a10de838aa4136b5f3432f15b.
  The reviewed two-line installer change is
  cbm-publication-consumer-v1.2.0.patch. The future release must target the exact
  approved commit containing these pins, not silently use an old base commit.
- Complete corpus: 88 sessions,1,924 successful rows, all FTS indexed; schema1.1,
  nomic-embed-text,768 dimensions,LanceDB0.34.0. No re-embedding or extraction.
- Corpus archive SHA256:
  783466593d3077b227d715c0efe8ac9266db7e28a745251d24c0dd2148d0b109.
- Existing paired checkpoint manifest:
  df1ce04cd7a15e38cc21e1be5fc3ee1fd931489f7a66a351705a6e248970684e.

Private VM108 root:
/srv/dev-data/artifacts/cbm-publication-build-20260917/

candidate/ contains only corpus-v1.2.0.tar.gz,corpus-manifest.json,sha256sum.txt.
git-output/2026-09-15/ contains the six approved files. snapshot/ preserves the
verified incoming data copy; consumer-install/ holds the isolated installation.
The management delivery remains untouched in cbm-publication-candidate-20260917/.
All data is under private directories; no raw text appears in checked-in receipts.

## Verified evidence

Forge verified both management receipt hashes and both delivered file hashes,
then all31 archive members' identities/types/sizes/hashes before safe extraction.
The Git files match selected Artifact record hashes. Management's evidence
matches the selected files and entire corpus to the acknowledged checkpoint and
confirms unchanged source/database fingerprints after delivery.

The local build validated the full candidate in a network-disabled, read-only
container and confirmed the snapshot's corpus hashes did not change. The actual
consumer installer was used with the proposed v1.2.0 pins and a local gh-download
stub; every installed corpus member matched the candidate manifest. No GitHub
upload/download was performed by this rehearsal.

The consumer's published image digest
ceb3b08de5947b3c0c9e458ce50c8d28111b4df1d818ad1fabb0add5d39765c4
then loaded that installation: health and88 sessions passed, a query returned3
results, ingest/reindex were404 and all corpus hashes remained unchanged. It used
an internal Docker network, mock zero-vector embeddings and the existing
read-only tokenizer cache. No real model call occurred. This verifies package
and API compatibility, not semantic retrieval quality or a complete Open WebUI
user installation. Disposable containers and network were removed.

Safe evidence: cbm-publication-real-candidate-verification.json,
cbm-publication-v1.2.0-manifest.json and receipts/cbm-publication-prep-021/.

## Next authorization boundary

Publishing credentials and production publication controls are not provisioned.
The locally tested selected-publication worker is deliberately offline-only;
live operational wiring, exact consumer commit/branch approvals and scoped
credentials must be prepared before activation. Do not enable the generic worker,
which has model/ingestion authority, or broaden the weekly automatic selector.

Recommended next management scope, still without publication:
- Provision repository-scoped write credentials managed in Infisical for only
  hopchouinard/RecapFlow-automation and hopchouinard/community-brain-distribution.
  Prefer existing management credential mechanisms. Minimum repository metadata
  read and contents write; no administration, organization-wide access, unrelated
  repositories, workflow write or model/provider credentials. Report if branch
  protection requires a different reviewed delivery flow before adding grants.
- Render them solely for a separately gated publication oneshot, never API,
  ordinary processing/acquisition workers, browser, logs or handoff documents.
- Keep remote publication false; no remote draft/tag/branch/asset creation, Git
  push, PR, production stage enqueue or application deployment during provisioning.
- Return safe identity/scope/storage-path/expiry evidence, never secret values.

This next credential authorization does not approve publication. The subsequent
activation review must include exact destination branches, consumer commit,
file/bundle hashes, live selected-worker controls and recovery receipts. Recheck
all remote refs and source freshness at that point. Preserve the candidate if a
new weekly meeting arrives; do not silently change its approved content/version.
Remote publication, retirement, historical replacement and later migration phases
remain gated. CBM-10 quality review remains last.
