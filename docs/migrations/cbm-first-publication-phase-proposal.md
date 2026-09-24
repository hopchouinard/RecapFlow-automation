# Proposed first manual publication phase — approval required

This proposal is the next major phase after verified Requests021 and022. No
remote publication or live publisher activation has occurred. Approval would
cover preparing and verifying the constrained live publisher, then one selected
publication of the concrete candidate below. This is not approval for automatic
weekly publication or for publishing the dirty Forge development checkout.

## Concrete publication scope

1. Publish exactly six September15 job artifacts into
   hopchouinard/RecapFlow-automation, main, output/2026-09-15/:
   transcript.txt, prepared-transcript.md, extracted-signal.md,
   community-post.md, community-post-compressed.md,
   2026-09-22-weekly-invite.md. Selected job:
   744d0f3f-8da7-4c12-bc15-5ec0a046518d. File hashes are bound to the verified private
   candidate and its matching paired checkpoint. No other files or historical
   dates may be changed. Inspected main base:
   dd29e82aa21f3e52d0ea7a96561f8dec9af28055. That output date is absent there.
2. Publish the three approved corpus assets as consumer release v1.2.0 in
   hopchouinard/community-brain-distribution, using the full88-session/1,924-row
   corpus. Archive SHA256:
   783466593d3077b227d715c0efe8ac9266db7e28a745251d24c0dd2148d0b109.
   Companion manifest: cbm-publication-v1.2.0-manifest.json. No recomputation of
   vectors, extraction, regeneration of Markdown or change of corpus contents.
3. Apply only the reviewed two-line download-corpus.sh version/checksum change
   from cbm-publication-consumer-v1.2.0.patch to the consumer repository's main
   branch. Inspected base: a192f7832e70d60a10de838aa4136b5f3432f15b.
   Pin the release to the exact resulting commit; retain the prior release and
   old installer pins for rollback. Do not substitute the unmodified old commit.
   Treat any unexpected remote changes, branch protections, occupied release
   version or file conflicts as a review boundary, never force-push or overwrite.

## Required work within this phase before any external write

The current Forge worker is offline-only. Build a separate live selected-run
adapter and credential delivery contract, and test it with the same scoped
PostgreSQL/JetStream fixtures plus local Git/mock GitHub. Do not enable the
production generic worker or add publication to the automatic weekly selector.
The adapter must bind selected job/stage/generation, all six artifact hashes,
candidate hashes, target repositories/branches and exact base/target commits.
Only the two publication stage types may run. Model/acquisition work must be
impossible in this worker; no model/provider credentials may be present.

Coordinate management's ordered quiet locks and matching backup/freshness check.
Revalidate candidate files, existing job states, remote bases and permissions.
Prepare an immutable selection and operation journal before enqueueing exactly
the selected publication stages. Capture pre-publication recovery/control state.
Verify the first release's source/pin sequence using isolated local refs before
making a remote branch refer to an unavailable or mismatched package.

Management must mint a fresh installation token from the already provisioned
App and Infisical signing material, explicitly limited to repository IDs
1176379254 and1249770482 with contents:write/metadata:read. Verify expiry/access
and atomically refresh only publication.env. Its previous token expires
2026-09-17T14:33:43Z. Keep signing/bootstrap material out of workloads. Render
publication enablement only into the approved oneshot; existing API and routine
worker publication flags and credentials remain unchanged.

## Execution and acceptance

Publish only the reviewed recap commit and consumer pin commit/assets. Use draft
release staging with local validation before remote creation, verify every remote
asset digest, then explicitly finalize the release and verify its final state.
Record commits, release identity, asset hashes and durable stage outcomes.
Preserve the previous usable release until success. On a lost response, stop and
inspect remote receipts; do not retry unknown effects or infer success.

Verify an installation using the actual public release URLs/pins and its existing
consumer image. The private candidate already passed package/API tests with
mocked embeddings and read-only mounts; these did not certify semantic ranking
or a complete Open WebUI user installation. Do not invoke generative models for
publication checks. Account for the pinned image's cold-start tokenizer cache
requirement without silently changing its image or model configuration.

Capture paired publication/recovery evidence and return a safe receipt. Revoke or
allow the selected short-lived token to expire according to the managed contract;
do not activate a background publisher or unattended renewal as part of this run.

## Continuing gates

No automatic weekly publication, additional meetings, historical replacement,
old-service retirement, request016 permission work, CBM-09 transition or model
spend is included. CBM-10 output-quality review stays last. If a scope change is
necessary, return the concrete difference for approval before that action.
