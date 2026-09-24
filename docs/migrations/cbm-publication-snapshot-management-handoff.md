# Request021 — private publication-candidate snapshot only

Target: home.servers. Patrick authorized preparation of Git/corpus distribution
with remote publication disabled, then selected all six weekly artifact files.
Request020 is completed and acknowledged. No further approval is needed for this
read-only data preparation. This request does NOT authorize remote publication,
new credentials, production code deployment or publication-stage transitions.

Prepare an internally consistent, private, data-only copy for Forge rehearsal:
- Proposed candidate job: September15,
  744d0f3f-8da7-4c12-bc15-5ec0a046518d. Copy its six verified Artifact records'
  files only: transcript.txt, prepared-transcript.md, extracted-signal.md,
  community-post.md, community-post-compressed.md, 2026-09-22-weekly-invite.md.
  Verify the immutable storage hashes and published file names against DB.
- Copy the complete current lancedb/nomic-v1 corpus, preserving existing vector
  files. Last verified baseline is 88 sessions,1,924 rows,zero unindexed. Report
  current counts instead of forcing them; stop for review if any new failed or
  partial state or unexplained drift is present. No reindex or embedding calls.
- Include selected nonsecret metadata only: job identity/date/mode, stage states
  and generations, six artifact names/hashes/bytes, corpus schema/embedding model,
  row/session/FTS counts and file hashes, current backup acknowledgement job ID /
  manifest hash, capture timestamp and matching checkpoint provenance. Do not
  copy the full database, runtime environment, Infisical data or credentials.

Use existing ordered management/runner/manual/submission/corpus quiet locks and
checkpoint procedures to get consistency without altering source data. Inspect
for active work, outstanding backup or uncertainty first; defer/report if busy.
Do not clear markers, replay stages, arm a publisher or change intake settings.
If the available checkpoint cannot identify the same stable files/corpus, report
that mismatch; do not claim a consistent snapshot from unrelated captures.

Deliver under VM108:
/srv/dev-data/artifacts/cbm-publication-candidate-20260917/
with data-only.tar.gz, manifest.json and SHA256SUMS (directory0700, files0600,
existing Forge cbmdev/sudo access). Suggested archive layout:
artifacts/<six exact names>, corpus/lancedb/nomic-v1/<existing files>,
selected-job.json. Reject symlinks and unexpected file names; preserve originals.
Never print file contents or private data in a receipt.

Verify destination checksums, archive listing and before/after source data/DB
fingerprints. Return receipt.md plus safe JSON listing destination paths, file
counts, bytes, manifest/archive SHA256 values, selected job/stage status,
checkpoint match and whether source/DB stayed unchanged. Do not include content.
Candidate copying is not an approval to publish the job or corpus: Forge must
validate the candidate and return exact destination/version/content for Patrick's
activation approval. No real processing, model calls, remote Git pushes/releases,
retirement, historical replacement or request016 permission work.
