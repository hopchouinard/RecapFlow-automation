# CBM-08 — Git and corpus distribution preparation

2026-09-17. Patrick authorized preparation with remote publication disabled.
This is a proposed activation phase, not an execution request. No production
configuration, credential, job, corpus or remote repository was changed.

## Inspected state and rehearsal evidence

The operator repository has working PublicationHandlers for local Git publication
and validated LanceDB bundles, a draft-first GitHubRelease adapter, durable
publication stages, and a corpus:publish API permission. The production automatic
selector executes only acquisition/processing/indexing; the human identities do
not have corpus:publish. Keep those boundaries intact during preparation.

Read-only inspection cloned the consumer repository into an isolated temporary
checkout, at a192f7832e70d60a10de838aa4136b5f3432f15b. Its download-corpus.sh pins
v1.1.0 and SHA256
157f3981262b2ebadab3004c0431fc760ebfe1ac28597c5167a856c6162ef41b.
The consumer image is pinned independently. A new uploaded release alone cannot
update this installer's pinned version/hash. Repository state must be rechecked
before an activation; these are inspection facts, not future release pins.

Completed credential-free tests:
- 18 existing publication/application tests passed, including local bare Git
  lost-push reconciliation, immutable bundle validation and mocked release retry.
- Six focused publication/release/runtime tests passed after adding an explicit
  handler-level disabled-publication guard. Even an injected release publisher
  cannot run distribution when allow_network_publish is false. This source-only
  change has not been deployed.
- A two-session, three-row, schema1.1/768-dimensional fixture was exported and
  installed using the actual consumer download script. Only its checksum was
  substituted, and gh download was replaced with a local fixture-copy stub.
  The installed LanceDB schema/FTS state and row counts passed. A deliberately
  corrupted download failed its hash check and left the installation unchanged.
  See cbm-publication-consumer-rehearsal.json. No actual corpus was exported or
  model invoked; no GitHub release was created, downloaded or modified in this
  rehearsal. This does not claim a fresh containerized consumer query test.

## Recommended first activation

Use one explicitly selected, reviewed release, separate from weekly processing.
Continue manual Markdown use for community-board posting. Keep automatic weekly
publication disabled until this first release and a clean consumer install pass.
Do not enable the generic worker: it requires model credentials and can consume
other stages. A publisher must be a selected-job/stage oneshot with no Fathom or
model credential and no ingestion authority.

Preserve the established two destinations:
- Recap output Git destination: propose hopchouinard/RecapFlow-automation, consistent
  with the existing output/<date>/ handler. Confirm the exact target branch and
  content list before granting writes; never infer a push of this dirty migration
  checkout. The repository's complete migration-code publication is separate.
- Consumer package: hopchouinard/community-brain-distribution. Its existing public
  distribution model remains the referenced design. Do not alter repository
  visibility or broaden content scope during this work.

The first release candidate should pair one selected successful job's approved
files with a consistent complete current corpus snapshot. Select the job at the
release checkpoint; September15 is an eligible proposal, not a new authorization
to publish it. Preserve schema1.1, nomic-embed-text and 768 dimensions. Record all
88 current sessions/1,924 rows if those counts still hold at capture; otherwise
review the change. Export existing vectors without model calls or re-embedding.

## Required implementation and management work before activation

1. Resolve the release file list below. Record target repository/branch, job UUID,
   file hashes and snapshot identity in a reviewed immutable selection. Reject
   paths, files or jobs outside it. Require completed indexing, verified paired
   backup and no unknown stage effects. Publication must never rerun ingestion.
2. Add a selected publication launcher and independent credentials. Infisical
   should deliver narrowly scoped repository write credentials only to that
   oneshot. Use separate operational scope from acquisition/model workers. No
   provider token, management credential or writable corpus mount. Keep the API
   and routine weekly launcher without publication credentials. home.servers
   provisions only after a concrete scoped management request is authorized.
3. Freeze and validate a local candidate under the established writer/quiet locks.
   Record source row/session counts, hashes, extraction status, schema/embedding
   compatibility, job files and backup identity. Preserve old release and rollback.
   Validate selected assets before any remote creation. Current GitHub adapter
   checks the asset-name set after fetching/possibly creating a draft: move all
   local preflight ahead of remote mutation during publisher implementation.
4. Reconcile release naming with the consumer version axis. Current handler uses
   v<job-UUID>; consumer installer uses version/hash pins. Choose a reviewed
   distribution version and exact consumer source commit; do not automatically
   mark a UUID release latest. Prepare the consumer pin changes in an isolated
   checkout for review, not a push from this project's dirty tree.
5. Rehearse the exact launcher with fixture Git and mocked HTTP: disabled flags,
   scope denial, immutable conflicts, partial upload, lost push/create/upload/
   publish responses and recovery. Confirm old release stays usable and no retry
   changes an approved artifact. Verify release identity/assets after final remote
   publication before recording a complete receipt or moving current.json.
6. Run a fresh consumer container from its existing pinned image against the local
   candidate: read-only routes, representative retrieval/sources, expected counts,
   install/update and rollback. No generative calls. This remains outstanding;
   the completed installer fixture check is narrower.
7. Only after reviewing the exact candidate/pins authorize remote activation.
   Publish the selected recap commit and verified draft assets, finish the
   reviewed consumer version/commit sequence, and record remote receipts in
   durable stages. Consumer install must use that pinned release; indexing alone
   cannot be reported as release success. No force push or destructive repair.
8. Capture paired publication receipts/config/export state with existing recovery
   tooling. On uncertain remote outcome, inspect receipts first; do not blindly
   repeat. On failure retain the previous consumer release and all evidence.

## Approved file scope and preparation progress

Patrick selected **all six files** on 2026-09-17. The Git allowlist is exactly
transcript.txt, prepared-transcript.md, extracted-signal.md, community-post.md,
community-post-compressed.md and the correctly dated next-Tuesday weekly invite.
A different/missing/extra artifact fails the selected-publication preflight.
This approval fixes content scope; remote activation remains separately gated.

Implemented and tested locally:
- Separate publication selection requires a completed root weekly job, completed
  indexing, exact artifact hashes, correct scope, queued/unattempted generation,
  no running/partial/unknown stages and a matching verified checkpoint identity.
- The offline selected worker reuses exact-event JetStream execution with a
  publication-only selector. Existing manual selection and weekly scheduling
  retain their original stage restrictions. The rehearsal refuses remote
  enablement or any injected release publisher. It never creates model work.
- GitHub adapter validates local asset names/types before any request and reads
  the final release back to verify identity and all asset hashes before success.
- Real disposable PostgreSQL/JetStream plus local bare Git test published all six
  fixture files without adding ModelCall rows or selecting other work.
- Full verification: 150 workflow, 968 application Python, 66 DB/queue, 6 frontend
  unit and 5 browser tests passed, plus TypeScript/Vite build. The focused
  publication/selection/manual checks passed 22 tests (overlapping those suites).

Fresh consumer container rehearsal on VM108 now passes with the actual published
image digest, two fixture sessions and three retrieval results, read-only corpus
and absent ingest/reindex routes. All corpus hashes were unchanged. Network was
internal-only, embedding vectors came from a mock and no generative calls ran.
The pinned image attempted a first-start tokenizer download; supplying the
existing tokenizer cache read-only allowed isolated startup. Before final release,
make this cold-start dependency explicit or include the cache in a reviewed image.
This proves package/routes compatibility, not real retrieval quality or a full
Open WebUI user installation. Containers and their private test network removed.
See cbm-publication-consumer-container-receipt.json.

Next is a private consistent data-only snapshot for candidate preparation: the
September15 job's six files and current complete corpus, delivered to VM108 under
management's existing quiet-lock/checkpoint procedure. This is a proposed first
release candidate for review, not permission to publish it. No publishing
credential is requested yet. Remote launcher, destination/branch/version pins,
real candidate validation and final activation approval remain outstanding.

## Remaining migration gates

Two successful weekly cycles and verified recovery are still CBM-08 stabilization
requirements before retirement proposals. This preparation does not retire old
services, resolve request016's stopped permission work, authorize historical
replacement, or start CBM-09. CBM-10 output-quality review remains the final step.
