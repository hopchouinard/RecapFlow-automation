# Request021 completed — private publication-candidate snapshot

Request: CBM-PUBLICATION-PREP-20260917-021
Actor: home.servers
Capture timestamp: 2026-09-17T03:37:27.968056+00:00

## Delivered

VM108: /srv/dev-data/artifacts/cbm-publication-candidate-20260917/

- data-only.tar.gz: 13,363,566 bytes,
  SHA256 e57da389e18a5a7bb87fdc75222273c4e8b3f87612dddce63d6097637380908f
- manifest.json: 11,325 bytes,
  SHA256 7cc9963032cb7d13bb922a98582ae323b4f6292612b1bc2996c479ff036a3ad4
- SHA256SUMS: checksums for the archive and manifest.

The directory is root-owned 0700 and all three files are root-owned 0600.
Existing Forge cbmdev/sudo access applies. Destination file checksums, archive
listing, every member's bytes/hash/type, and selected metadata were verified.
The archive has 31 regular files: six artifacts, 24 existing corpus files and
selected-job.json, totaling 22,070,017 uncompressed bytes.
No symlinks, special files, unexpected artifact names, credentials, runtime
environment, full database or private checkpoint payloads were copied to VM108.
File contents were not printed or included in this receipt.

The six approved files are:
transcript.txt, prepared-transcript.md, extracted-signal.md, community-post.md,
community-post-compressed.md, 2026-09-22-weekly-invite.md.

## Consistency and provenance

Selected September15 job: 744d0f3f-8da7-4c12-bc15-5ec0a046518d.
Processing succeeded, artifacts ready and indexing complete. Acquisition,
processing and indexing are succeeded at generation1/attempt1. Git and
 distribution remain blocked at generation0/attempt0, with job status
not_requested. No stage transition was performed.

Current database fingerprints exactly match the acknowledged paired checkpoint.
Each selected Artifact record matches its immutable storage bytes and checkpoint
reference. The entire corpus file set and bytes match the same checkpoint's
files-capture, and current row/session fingerprints match its corpus receipt.
The private paired checkpoint and its off-host copy were hash-verified, including
its existing restore and PBS evidence. No new PBS operation was started.

Checkpoint manifest SHA256:
df1ce04cd7a15e38cc21e1be5fc3ee1fd931489f7a66a351705a6e248970684e
Checkpoint created: 2026-09-15T23:49:22.318559+00:00
Acknowledged: 2026-09-17T00:36:42.985634+00:00

Corpus: schema1.1, nomic-embed-text contract, 768 dimensions, LanceDB0.34.0,
88 sessions, 1,924 rows, all1,924 FTS indexed and zero unindexed. Existing vectors
were copied unchanged. No embedding, reindexing or generative model call occurred.
Schema and selected nonsecret metadata accompany file hashes in manifest.json.

The Mac management scheduler mutex and VM109 runner, manual-worker, submission
and corpus-writer locks were held continuously through inspection, capture,
transfer and final verification. No active/eligible work, pending checkpoint or
uncertainty marker was present. Existing lock procedures were used with the
corpus writer lock added to the transient capture process; no installed launcher
or locking code was changed.

Source data before: b7cd389b23db9c7fa7baa164cca0d32e15ab471bfaa00d5697145b8342d32446
Source data after delivery: b7cd389b23db9c7fa7baa164cca0d32e15ab471bfaa00d5697145b8342d32446
Database before: 1ba32dd2d2b405c0bbfa7697c4ad4678a2cee370dc3b58c40855da6b669eae4c
Database after: 1ba32dd2d2b405c0bbfa7697c4ad4678a2cee370dc3b58c40855da6b669eae4c

All match. Source originals and historical checkpoint evidence are preserved.
The database evidence consists of fingerprints plus the allowlisted selected-job
metadata, not a new database dump. Private source capture and delivery evidence:
/srv/community-brain/artifacts/cbm-publication-prep-20260917-021/
Mac evidence: /Users/pchouinard/.local/state/community-brain-management/request021/

## Remaining boundary

This is private candidate preparation only. Forge must validate the candidate
and return exact destination/branch/version/content for Patrick's activation
approval. No Git push/release/publication, publishing credential, production code
deployment, intake change, stage mutation, replay, retirement or historical
replacement occurred. Request016 permission work remains stopped. No production
rollback is needed because production data and settings were unchanged.
