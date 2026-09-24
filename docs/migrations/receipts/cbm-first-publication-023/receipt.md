# Request023 completed: first manual publication

Request **CBM-FIRST-PUBLICATION-20260917-023**. Actor **home.servers**.

The exact approved publication completed. All six launcher commands returned zero, in order, once each: preflight/enqueue/execute git, then preflight/enqueue/execute distribution. Both durable publication stages are succeeded, generation1, attempts1. No public effect was retried.

## Published and independently verified

| Target | Verified result |
| --- | --- |
| RecapFlow-automation main | `82167b30b2d72ae8ebb9a64a557991b30be442c3` |
| community-brain-distribution main | `e2eca50575571a23657192163842c02331c85c96` |
| Lightweight tag v1.2.0 | `e2eca50575571a23657192163842c02331c85c96` |
| Published release | ID **390814260**, not draft/prerelease |
| Selected job | `744d0f3f-8da7-4c12-bc15-5ec0a046518d`, git **complete**, distribution **released** |

[Published release](https://github.com/hopchouinard/community-brain-distribution/releases/tag/v1.2.0)

Anonymous GitHub API/raw/download requests independently verified both main SHAs, actual tag commit, all six September15 recap file SHA256 hashes, installer hash/pins and all three release asset hashes. The consumer main update followed verified release creation; no force push or workflow change occurred.

| Asset | Asset ID | SHA256 |
| --- | --- | --- |
| corpus-v1.2.0.tar.gz | 570478167 | `783466593d3077b227d715c0efe8ac9266db7e28a745251d24c0dd2148d0b109` |
| corpus-manifest.json | 570478254 | `f2073718e83eacb27f455cf1151aacb99572311206883bf0d1d8a2f94b259127` |
| sha256sum.txt | 570478272 | `f9e2b2a7431d261a1cd0fbae84952601c0ea8093d06595efc051179b84044420` |

The prior v1.1.0 release remains published, ID380201443. Previous commits remain the parents of the new commits. No public history was rewritten.

## Preflight and execution controls

All six handoff document hashes and 12 packet file hashes matched. Plan canonical SHA256: `a7ac3cf3f0d2ee31c184f956b6c1c2fd61545d8c3d23179ca8506a53ad506759`.

Reviewed commit parents, exact changed paths/modes/content, all candidate assets, job identity/artifact selection, current corpus and approved checkpoint matched. Both repository bases/protections were checked; main branches were unprotected, with no effective rules, and v1.2.0 tag/release/draft was absent. No work, unknown outcome, attention or pending checkpoint blocked the run.

The management scheduler mutex and ordered VM runner/manual-worker/submission/corpus-writer locks remained held continuously across successful preflight, before-capture, all six commands, post-capture, isolated recovery tests and paired-copy verification. Locks were then released; the runner was rechecked idle with no attention markers. No temporary maintenance flags or selectors were changed.

The pinned production-image credential-free probe passed UID10001 mount access, candidate/prepared Git validation, modules, executable askpass and GitHub CA trust. Captured actual launcher arguments/env dicts verified the strict DB/NATS/publisher allowlist; token values were not placed in argv or output.

Fresh App **4978270**, installation **162488086**, exact repositories **1176379254/1249770482**, permissions **contents:write, metadata:read**. Only `/etc/community-brain-production/publication.env` was atomically refreshed as root:root0600. Its repository-ID value uses the JSON array expected by this packet; stored publication flag stayed false. Only the selected oneshots received publication true and model calls false. No signing/bootstrap/provider keys reached workloads.

Token disposition: **allow expiry at 2026-09-17T15:54:38Z (11:54:38 EDT)**. No unattended renewal or background publisher exists. The retained private bundle and recovery archive must not be treated as usable publication authorization after this run.

## Actual installation verification

The actual published `download-corpus.sh` was fetched at the exact consumer commit, hash-checked, and run in a fresh private directory on the Mac host. Its real GitHub CLI downloads and pinned SHA256 validation passed. Separately, all release assets were downloaded anonymously and hashed.

The installed file set was transferred to a fresh isolated VM108 verification directory and rechecked byte-for-byte. The existing pinned consumer image `sha256:ceb3b08de5947b3c0c9e458ce50c8d28111b4df1d818ad1fabb0add5d39765c4` passed health, **88 sessions / 1,924 rows**, a three-result query with fixture zero-vector embeddings, absent ingest/reindex routes, and unchanged corpus hashes. It ran with network disabled, read-only corpus/tokenizer cache, UID10001, and no model/provider credentials.

These checks establish package and retrieval API compatibility, not semantic ranking or a complete Open WebUI user installation. A first disposable smoke probe missed the image's instance-level Ollama client; the fixture was corrected to mock both embedding paths and rerun with network disabled. No model call occurred, and no published content or image was changed.

## Preservation and paired recovery

Source/artifact/model-call table rows and content hashes are identical before/after: **9 sources, 21 artifacts, 42 model-call rows**. Schema/owners/grants/sequences remained unchanged. Only expected publication tables changed: jobs, stages, attempts, operations and outbox. Attempts7→9, operations4→6, outbox10→12.

Production files/config/corpus/archive fingerprint remained `b7cd389b23db9c7fa7baa164cca0d32e15ab471bfaa00d5697145b8342d32446`. Corpus fingerprint remained `d189c3bf5bb018dbb9d39145726ef4bb47ab89b98fec51004c745a13ff354ce9`.

The only changed existing recovery-input file was `publication.env`; the six added files are the two immutable selections, two execution-started markers, operation journal and launcher log. All original credentials/runtime controls were preserved. API identity/image/start time/environment/mounts match; healthy, zero restarts. No publisher credentials remain in a running container. Routine publication and model calls are still false.

Private before-state:
- VM109 `/srv/community-brain/artifacts/request023-before/`
- DB host10.1.10.50 `/var/backups/community-brain/request023-before/`

Private post-publication pair:
- VM109 `/srv/community-brain/artifacts/request023-after/`
- DB capture `/var/backups/community-brain/request023-after/`
- Verified off-host pair `/var/backups/community-brain/request023-after/paired/`

Post paired-manifest SHA256: **`983977e506238d7ec93805faf86cb4d6f86fedf23418b820cb77349542c0ce14`**.

Post dump SHA256: `448a2322747c266636ec7b47f4f626e36fe6d001ee2c9b684aa03081498bebcb`.
Post managed-state archive SHA256: `1a50105aa130e081b30e2ca44245bff2790d374c7e6b2f931d05b60ccee62138`.

A disposable PostgreSQL restore matched schema/owners/grants/rows/sequences and all72 file references; public connect was revoked, connection limit0, and the temporary DB was removed. An isolated file restore verified1,150 input entries, all72 DB file references, and the unchanged88-session corpus; temporary restore removed. All nine paired files match by size/hash on both hosts and have root-owned private permissions. Live data was rechecked against the post-capture state before lock release.

The previous acknowledged checkpoint `df1ce04cd7a15e38cc21e1be5fc3ee1fd931489f7a66a351705a6e248970684e` is preserved as history. This is a separately named publication recovery pair, not an overwrite of the prior automatic checkpoint. No new PBS snapshot was created; verified logical recovery and off-host copy evidence are supplied. Existing PBS history was preserved.

## Remaining gates

No automatic weekly publication, additional meeting, processing/model work, historical replacement/retirement, request016 permission work, CBM-09 or final CBM-10 acceptance was performed. No blocker remains for this approved manual publication.

`verification-receipts.json` contains the safe detailed verification results. `receipt-manifest.json` binds this receipt and evidence with SHA256 hashes. Private archives/dumps/credentials are excluded from HANDOFF.

Reference checked: [GitHub release API](https://docs.github.com/en/rest/releases/releases), including actual tag-commit verification because an existing tag controls the release target.
