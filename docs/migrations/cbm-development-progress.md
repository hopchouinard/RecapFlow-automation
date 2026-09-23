# Community Brain application development

Current status: [September 20 live assessment and continuation plan](cbm-current-state-and-continuation.md).
The entries below are chronological history. In particular, September 17's idle
runner observation is superseded by the live pause/attention and renewal findings.

Authorization: on 2026-09-09 Patrick instructed continued development through
CBM-02 and subsequent tickets until intervention is needed. Production deployment,
cutover, secret migration and publication remain separately gated by the handoff.

This is the ongoing implementation record, not a declaration of production readiness.

| Ticket | Implementation and review evidence |
| --- | --- |
| CBM-02 | `processing/` ports weekly line chunks and historical turn blocks, exact versioned prompts/config, validators, three-attempt ladder, two prep/signal halvings, ordered aggregation, filenames and backfill continuation. JS runs only in oracle tests. Unknown transport outcomes stop rather than retry. |
| CBM-03 | `jobs/` adds typed SQLAlchemy models, explicit Alembic migration, scoped FastAPI contracts, immutable files, outbox, claims/heartbeats, model intent/response journal and DB-authoritative recovery. PostgreSQL/API integration tests exercise actual application code. |
| CBM-04 | Backend Fathom adapter verifies identity/time with paginated lookup; acquisition is a durable stage. Restricted Zoom collector provides list/read/upload; uploads bypass model prompts. Manual upload and waiting-input binding are API operations. Tests use mocked Fathom and private local files. |
| CBM-05 | React/Vite/TypeScript, Tailwind and shadcn Base UI source with Lucide. Authentik code/PKCE client and JWT/service authorization boundary. Job list, independent status, manual upload, retries/reruns, literal Markdown preview/copy/download. Component and Playwright fixture tests; live IdP registration remains gated. |
| CBM-06 | Single-writer adapter retains existing ingestion and LanceDB 0.34 retrieval. Existing sessions require review instead of implicit rewrites. Versioned consumer packages carry checksums and are reopened with real LanceDB before release. Git and draft-first GitHub publication adapters have explicit runtime gates. |
| CBM-07 | [Deployment review packet](cbm-07-deployment-packet.md) and isolated image/Compose candidates prepared. Compose configuration validates; image build/boot is blocked on Docker access. Live preflight, secrets and release identities remain required. |

Project implementation decisions:

- The durable processing stage owns deterministic subcalls; each model request
  has an immutable journal keyed by its full versioned request. Re-running an
  interrupted stage reuses completed calls and artifacts. Explicit operator retry
  archives failed call entries so only unsuccessful work is eligible for new spend.
  Successful model responses remain private files; PostgreSQL holds hashes,
  request metadata, usage and paths. Missing provider usage remains unknown.
- Acquisition, processing, indexing, Git and distribution are separate durable
  stages. The existing pipeline's exact per-chunk rules remain inside processing.
  Unknown model/publication outcomes require receipt reconciliation or an audited
  explicit duplicate-effect acknowledgment; broker redelivery alone never grants it.
- A versioned rerun preserves original files. Indexing over a previously populated
  legacy session requires explicit review; the migration does not infer permission
  for destructive `force_reextract` from a rerun request.
- Corpus packages are locally `validated` when no network publisher is configured;
  only a confirmed release receipt permits `released` and advances the release pointer.
- OIDC uses RS256 with issuer/audience/expiry checks. Service tokens have independently
  configured hashes/scopes/permissions and mandatory expiry. The SPA keeps access tokens in memory;
  protocol state uses the OIDC library's session storage. Production serves UI and API
  on the same origin. Raw Markdown is rendered as text, never executable HTML.
- Prompt snapshots were extracted from the current JSON workflows using
  `scripts/extract-processing-prompts.js`. Preserve the workflow hashes in the snapshot;
  regenerate only after reviewing a prompt/version change. Existing model slugs and
  ceilings are compatibility baselines, not fresh provider recommendations.
- Frontend dependencies are locked with npm; Python dependencies with uv. The shadcn
  button source comes from `https://ui.shadcn.com/r/styles/base-nova/button.json` with
  its utility import adapted to the local alias. TypeScript 7 requires relative paths
  without `baseUrl`. These choices are project-specific, not changes to the standards.

Fresh Forge setup adds to CBM-01:

```sh
uv sync --project community-brain --locked --python 3.11.15 --extra dev
./scripts/setup-cbm-test-services.sh
./scripts/setup-cbm-browser-libs.sh
npm --prefix web ci
cd web && npx playwright install chromium
```

Run `./scripts/verify-forge.sh` from the repository root. It includes Node oracle
behavior, Python tests, real disposable PostgreSQL/JetStream tests, Vitest,
TypeScript/build and Playwright. The browser-library script extracts Ubuntu packages
under the user cache, without sudo or host service installation. It follows configured
Ubuntu repository versions, unlike the explicitly pinned PostgreSQL/NATS test versions.

Reference documentation checked during implementation:
[Fathom transcript API](https://developers.fathom.ai/api-reference/recordings/get-transcript),
[PyJWT](https://pyjwt.readthedocs.io/en/stable/usage.html),
[OIDC client](https://authts.github.io/oidc-client-ts/),
[shadcn Base UI Button](https://ui.shadcn.com/docs/components/base/button),
[GitHub releases](https://docs.github.com/en/rest/releases/releases),
[GitHub release assets](https://docs.github.com/en/rest/releases/assets).

## Review and remaining intervention

The actual consumer `download-corpus.sh` at distribution repository commit
`a192f7832e70d60a10de838aa4136b5f3432f15b` successfully installed a locally generated
fixture package in a disposable directory. Only its operator-pinned version/checksum
were replaced; a local `gh` shim supplied the three assets without any release call.
The extracted LanceDB reopened with three expected chunks. Existing OpenWebUI
`X-API-Key` retrieval authentication is retained alongside Bearer authentication.

The dedicated image has **not** been built or booted. Forge has no Docker daemon;
passwordless sudo and rootless user-namespace setup are unavailable to this user.
An isolated Docker-capable development host, or operator-enabled Docker access on
Forge, is the next required input. The user has been asked which environment to use.
No production services, shared databases, streams, secrets, Mac installation or
remote publication were changed. Live OIDC, model/provider, scoped platform ACL,
release and coordinated restore rehearsals remain outside fixture evidence.

Final credential-free verification on 2026-09-09 passed: 150 existing Node tests,
821 Python tests, 23 disposable PostgreSQL/JetStream contract/application tests,
one Vitest component test and one Playwright browser test. TypeScript/Vite build,
new backend Ruff checks, frontend Prettier checks, shell syntax and `git diff --check`
also passed. The browser fixture was visually reviewed. Python's 70 warnings are
reported in the test output; passing tests do not establish live service readiness.
Compose v2 validation is covered by the Python deployment tests and does not start
containers. All changes remain local on the migration branch for review.

## Development VM rehearsal completed

VM 108 is ready under the explicit [VM handoff](cbm-development-vm-handoff.md).
The earlier Docker-access blocker is resolved. The standalone image boot,
disposable database migration, API authentication and JetStream smoke checks
passed on 2026-09-09; see [rehearsal evidence](cbm-development-rehearsal.md).
Packaging fixes were made on Forge and tested on the VM. Disposable containers
and volumes were removed afterward; production services remain unchanged.

## Durable worker, publication and restore rehearsal

The [extended container rehearsal](cbm-development-scenario-results.md) passed
on VM 108: weekly/history processing, real ingestion and hybrid retrieval,
restart idempotency, SIGKILL/unknown-effect reconciliation, coordinated DB/files
restore with a fresh queue and pending job, local Git receipts and a validated
four-session consumer package. Providers/embeddings were simulated; production
and remote publication remain untouched. Disposable scenario state was removed
after saving fixture backups and logs on the VM.

Patrick selected separate development Authentik/Infisical identities and a
US$5 total non-resetting OpenRouter key limit. The exact operator requirements
are in [the live identity handoff](cbm-live-development-identity-handoff.md).
The manual-input worker now permits an absent Fathom adapter; configured
acquisition remains supported. Sixteen targeted runtime/auth/deployment tests
passed. Live login and paid calls await the provisioned development identities;
no production credential is required or authorized for that step.

## Live development identity validation underway

The development identities are now provisioned. The separate live-development
API/PostgreSQL/authenticated-JetStream project is running on VM 108 with guest
loopback access. Service authorization, negative permission checks, container
OIDC TLS/discovery/JWKS, model catalog availability and the untouched $5 allowance
passed. Eight deployment tests passed. No worker or paid call has started.
Actual browser login needs Patrick's Mac tunnel and sign-in before the bounded
exercise; see [live development results](cbm-live-development-results.md).

The live browser gate and first paid weekly fixture are now complete. The actual
browser token passed issuer/audience/signature/expiry/scope/permission verification.
Eight first-attempt requests produced six hash-verified artifacts, costing
US$0.01324578 (provider total reconciled; US$4.98675422 remains). The one-shot
worker is removed; remote publication stayed disabled. Indexing remains pending.
Ollama's retained endpoint is reachable and advertises the expected embedding
model; semantic execution is not yet established. Manual output review found
incorrect question annotation and one inaccurate paraphrase. A decision on strict
prompt parity versus a separately versioned quality improvement is needed before
further live quality work; details are in the live development results. Sixteen
targeted deployment/spending-guard tests passed.

## Final quality-review sequencing decided

Patrick chose to preserve prompt parity and address output-quality findings as
the **last step of the whole migration**. [CBM-10](cbm-final-quality-backlog.md)
tracks Q-01 (false question annotation) and Q-02 (inaccurate preservation
paraphrase), with exact artifact evidence, expected behavior and acceptance
criteria. It remains last after CBM-08/09 and any added migration work. These
findings no longer block development rehearsal; v1 stays unchanged. Overall
migration completion requires explicit disposition of every final-review item.

## Indexing recovery boundary repaired

Live indexing preparation found a retry/uncertainty gap in retained ingestion.
Job indexing now opts into strict uncertain-outcome propagation while legacy
callers and frozen prompts remain unchanged. Full verification passed (150 Node,
843 Python, 23 DB/queue, one component and one browser test). A later additional
guard regression passed with the eight-test spending-guard suite.

A local volume-initialization failure interrupted the first indexing attempt
before any indexing model intent; the expired lease is now `outcome_unknown`.
Initialization, preflight and worker exit reporting are repaired and verified.
All six processing artifacts and the $4.98675422 remaining allowance are intact.
The next step is Patrick's explicit reconciliation acknowledgment for this single
stage; the exact retry action is prepared in the live-development launcher.
See [current evidence](cbm-live-development-results.md). No production or remote
publication changes occurred; CBM-10 remains the final quality-review step.

## Reconciled live indexing and retrieval passed

After Patrick's explicit reconciliation approval, indexing completed on generation
2: nine successful chunks, ten extraction requests, real 768-dimensional Ollama
embeddings and verified BM25 index. Authenticated hybrid retrieval, date exclusion,
legacy read transport and rejection of mutation/unauthenticated routes passed.
The original six artifacts remain unchanged. Total provider-confirmed spend is
US$0.02107203, leaving US$4.97892797. Workers are removed; read-only retrieval/API
remain on guest loopback. A coordinated private development snapshot was saved.
Seventeen targeted deployment/guard checks passed after the final configuration
changes. See the live results for evidence and limits of the one-session sample.

The next live intake check needs an explicitly approved Fathom test recording and
separate development credential delivered through Infisical. The current handoff
provides neither. Await that input or Patrick's choice to defer live acquisition;
no production credential extraction, polling, publication or cutover is authorized.

## Fathom credential reuse authorized; selection pending

Patrick authorized reuse of the n8n Fathom credential through its Infisical-managed
private VM copy. The previous separate-key requirement is superseded. The
acquisition-only Compose overlay validates, confines the credential to a stopped
one-shot worker, and exposes no model/publication capability. Sixteen focused
acquisition tests passed. No provider lookup, transcript fetch or acquisition job
has started. Await Patrick's choice of one recording before execution; see
[the acquisition rehearsal handoff](cbm-fathom-rehearsal.md).

Patrick selected Fathom recording `812746883`. A bounded metadata-only lookup
mode is prepared and tested; its date/time window still needs the recording date
from Patrick. No transcript fetch, job creation or worker startup has occurred.

## Selected Fathom acquisition completed

Patrick's selected call URL `812746883` resolved through exact metadata URL match
to API recording `181075701`, September 8 at 17:54:33 Toronto. The acquisition-only
job `33cc7538-e326-4f74-93ef-f2fcbb5c1624` saved and hash-verified a 112,886-byte
transcript privately. It has zero model calls/generated artifacts; processing
waits for input. The worker is removed and no polling/publication/production
change occurred. Twenty focused tests passed, including call/recording ID mapping
and safe terminal-notification handling. See the Fathom rehearsal document for
output paths and identity evidence. Any model processing now requires Patrick's
explicit approval for this recording, as instructed.

## Approved real transcript-only processing completed

Patrick supplied that explicit approval. Child job
`acd77c69-10d8-4079-9514-35ca5cc0c9fc` completed transcript backfill using the
unchanged acquired source and frozen v1 prompts. All nine requests succeeded on
their first attempt. Three artifacts passed storage and authenticated download
hash checks. The worker is removed; real-recording indexing and publication
remain unexecuted. Run cost was US$0.60421275; provider-confirmed cumulative usage
is US$0.62528478, leaving US$4.37471522. Twenty-four focused checks passed.

See [recording processing evidence](cbm-recording-processing-results.md).
A provider-free preflight counts 29 retrieval chunks and 30 extraction requests
for a potential isolated indexing exercise, which awaits approval. CBM-10 remains
last, with explicit Q-01/Q-02/Q-03 dispositions required before migration closure.

## Approved real-recording indexing completed

Patrick approved the follow-on indexing exercise. The recording produced 29
successful chunks with 30 extraction requests, no failed chunks, and verified
768-dimensional Ollama embeddings. The isolated corpus has 38 chunks including
the nine synthetic originals. Two authenticated hybrid queries, date filters,
legacy read transport and authorization/mutation rejection checks passed.
The worker is removed and remote publication remains disabled.

Indexing cost US$0.03412550; provider-confirmed total usage is US$0.65941028,
leaving US$4.34058972. Twenty-five focused guard/deployment tests passed. See
[recording results](cbm-recording-processing-results.md) for metadata-only evidence
and the unvalidated development speaker-registry limitation. A real weekly
rehearsal now needs a selected matching Zoom chat and explicit combined-input
processing approval; current authorization does not install a recurring collector
or change production intake. The final quality backlog remains deferred to CBM-10.

## Matching Zoom chat staged

Patrick supplied the September 8 chat. Its 6,804 bytes were hash-verified and
staged as development source `23d9780b-513e-4782-96d2-97211e31e855`; raw content
remains private. No job or model work started. The [weekly rehearsal plan](cbm-weekly-recording-rehearsal.md)
specifies a separate weekly child, both selected inputs, unchanged v1 prompts,
six artifact checks and the existing spending cap. Await explicit approval for
combined-input processing. Indexing is excluded because the current development
corpus already contains the same date's backfill session.

## Real weekly processing completed

Patrick approved combined-input processing. Weekly child
`7bce1799-dd0f-40fa-a444-a7797ff38b1b` succeeded with 15 first-attempt requests
and six hash-verified, authenticated downloads. Source hashes are unchanged;
the worker is removed. Indexing and publication remain unexecuted. Cost was
US$0.32885985, bringing provider-confirmed cumulative spend to US$0.98827013
with US$4.01172987 remaining. Twenty-six focused checks passed.

A coordinated private database/files/config/corpus snapshot passed archive-read
checks; the API restarted healthy. See [weekly results](cbm-weekly-recording-rehearsal.md)
for exact hashes and restore limits. Further indexing of these weekly outputs
requires a separate isolated corpus because the existing September 8 session
belongs to the completed backfill job. No production or remote publication
authorization is implied. CBM-10 remains the last migration step.

## Separate weekly corpus and retrieval passed

Patrick approved isolated weekly indexing. Thirty chunks and 31 successful
extraction receipts were verified, with real 768-dimensional embeddings and
authenticated hybrid retrieval through a temporary API. All 27 original-corpus
files remained hash-identical. The temporary API and worker are removed; the main
API is unchanged. Cost was US$0.03618950; reconciled total usage is US$1.02445963,
leaving US$3.97554037. Supplemental weekly corpus/config archives passed read
checks. See [weekly results](cbm-weekly-recording-rehearsal.md).

The remaining live intake integration needs a dedicated Mac collector identity
and an approved HTTPS development endpoint. The existing collector requires HTTPS;
the current localhost HTTP browser tunnel is insufficient for that contract.
See [development collector proposal](cbm-development-collector-proposal.md).
No recurring Mac installation or production intake change is authorized here.

## Approved collector access prepared; management delivery required

Patrick approved development HTTPS and the scoped Mac collector identity. DNS,
VM listeners and UFW were inspected; a digest-pinned VM-local nginx proxy and
hash-bound manual upload runner are prepared. Compose/nginx validation passed
with disposable TLS fixtures. The collector now optionally checks the selected
content hash before transmitting that exact in-memory content. No production
installation or existing collector behavior was changed.

The remaining dependency is the lab-signed certificate and Infisical-provisioned
collector identity described in [the management handoff](cbm-collector-management-handoff.md).
Forge's broker is read-only, and no CA/Infisical bootstrap is installed on VM 108.
No proxy listener, firewall opening, credential substitution or model call was made.

## Collector HTTPS activated; Mac execution pending

Read management's completed-delivery handoff. Verified certificate/key and scoped
identity preservation, recreated only the development API, added the two approved
source-specific TCP 443 rules and started the dedicated proxy. Trusted HTTPS health,
unauthenticated-upload rejection and hidden job routes passed from Forge. No model
calls, job submissions, production or publication changes occurred.

The exact manual runner and collector are staged on VM 108. Direct Mac SSH timed
out; its token remains exclusively on the Mac. The [activation results and manual
exercise](cbm-collector-activation-results.md) identify the required Mac-side path
confirmation and execution. Actual scoped-token allowed upload/denied operations
remain pending that execution; do not claim them from Forge's unauthenticated checks.

## Manual collector and development restore completed

Patrick returned the successful Mac receipt: script hashes, TLS, scoped permission
denials and deduplicated upload all passed. Forge independently confirmed the
selected source hash and unchanged counts (four jobs, 32 processing calls, six
sources). See [collector acceptance](cbm-collector-activation-results.md).

Continued with the authorized development snapshot restore into disposable,
externally isolated dependencies. All six sources, 15 artifacts and 32 model
responses passed restored hash checks, with 38 intact 768-dimensional corpus
chunks. No worker or provider call ran; disposable copies were removed. See
[restore results](cbm-development-restore-results.md).

The next representative-data gate is the [preserved corpus rehearsal proposal](cbm-preserved-corpus-rehearsal-proposal.md).
It requires approval for a data-only copy from the existing preservation archive
to a new isolated VM 108 area; current selected-recording authorization does not
cover that broader dataset. Production and remote publication remain prohibited.

## Preserved corpus rehearsal approved; routine autonomy clarified

Patrick approved the broader data-only preserved-corpus rehearsal and instructed
continued routine implementation/verification without repeated minor approvals.
Only major changes, project phase transitions or genuinely missing input/access
require intervention. Preserve the existing production/publication prohibitions.

VM 108 does not yet contain the approved preservation delivery, and Forge cannot
reach the Mac copy. A management transfer request is pending, with no request for
additional authorization or secrets. Prepared and staged a manifest/path/hash
validator (16 checks passed) and read-only corpus/local-package inspection helpers.
The [approved proposal](cbm-preserved-corpus-rehearsal-proposal.md) records the
delivery format and acceptance boundaries. Continue the restore/retrieval checks
as soon as management supplies the dataset paths and verified manifest.

## Preserved dataset restored; consumer-policy decision identified

Management delivered the approved subset. Verified all 2,627 files (108,764,895
bytes), normalized only their isolated-copy paths and opened the preserved corpus:
87 sessions, 1,914 rows, schema 1.1, FTS and 768-dimensional vectors. All 260 source
references resolve. Authenticated historical/recent hybrid retrieval, filters and
access checks passed; the temporary API was removed and all delivery hashes stayed
unchanged. No generation, re-extraction, re-embedding or publication occurred.

Strict consumer export is blocked by 13 failed rows. Further read-only inspection
proved that every failed row contains only a Markdown divider, not meeting prose.
The [results and recommended export disposition](cbm-preserved-corpus-results.md)
propose a separate 1,901-success-row consumer candidate with explicit exclusion
provenance and an untouched full archive. This dataset-policy decision remains
with Patrick; routine verification needs no further approval. Added Q-04 to the
final quality backlog without changing frozen behavior. CBM-10 remains last.

## Approved consumer candidate verified; production phase remains gated

Patrick approved the divider-only export policy. Built/reopened a private candidate
with 1,901 unchanged successful rows, all 87 sessions and hash-linked provenance for
the exact 13 exclusions. Source data stayed unchanged. Candidate retrieval initially
differed from the preserved corpus; inspection identified zero current-row FTS index
coverage in the original. A fresh full-data index control matched the candidate's
top-five IDs/order for all four queries. Added Q-05 for final coverage-maintenance
review, with explicit coverage verification required now in deployment preflight.

Canonical verification passed: 150 Node, 887 Python, 23 DB/queue, one component and
one browser test plus frontend build. No generation calls or remote publication
occurred; all temporary APIs were removed. See [candidate evidence](cbm-preserved-corpus-results.md).

Prepared the [production phase gate](cbm-production-phase-gate.md) with refreshed
read-only capacity observations and concrete proposed resource boundaries. Opening
production provisioning/staged deployment is a major phase transition and requires
Patrick's explicit authorization; cutover/publication/retirement remain separately
held. No production resource has been created or reserved.

## September 10 — production staging phase approved

Patrick explicitly approved the phase transition to production provisioning and
staged deployment. Cutover, remote publication and retirement remain gated.
Created `cbm-production-management-handoff.md` with the VM 109 / PVE1 candidate,
network/storage, scoped platform resources, Infisical/OIDC delivery and readiness
receipt. Broker nextid remained 109 at 01:07 UTC; no resource was reserved.

Added standalone API-only `compose.production-staging.yml`: no worker or provider
credentials, model/publication flags fixed false, all state mounts read-only,
lab trust bundle, resource limits and no build/pull during startup. Staging claims
are read-only; initial jobs database is empty and legacy attempts are not invented.
The approved 1,901-row candidate and preserved registries are the initial corpus
mapping, with explicit full FTS coverage verification before serving.

Deployment configuration tests: 11 passed, including Compose v2 parsing and
staging boundary checks. No production deployment performed. Management must
create the new target and deliver scoped runtime access; Forge has only read-only
infrastructure access. Source freeze/build and actual production acceptance remain
pending and must not be inferred from configuration validation.

## September 10 — production image delivered; startup held

Completed the independent image preparation authorized by the early guest
receipt. An 83-file source snapshot preserves the uncommitted checkout and
records per-file hashes. Canonical verification passed (150 Node, 889 Python,
23 DB/queue, one component, one browser, frontend build). Built on VM 108 and
passed disposable DB/migration/API/SPA/JetStream smoke checks. Removed the
isolated test stack and transferred/loaded the exact image on VM 109; archive
checksum and image digest matched. No production container exists or API/ingress
was started. See `cbm-production-image-readiness.md` for immutable identifiers,
private evidence paths and pending management integrations. No corpus installation
or production migration was attempted without the remaining prerequisites.

## September 10 — production API staging ready for Mac monitoring preflight

Applied explicit Alembic with the scoped migration identity, verified runtime
DML and denied DDL on all ten migrated objects, installed the pinned 1,901-row /
87-session candidate plus 13 verified config files, and confirmed complete FTS
coverage. Started only the immutable staging API behind the existing restricted
Traefik route. Health/authentication/permissions/SPA checks passed; all four
retrieval queries matched the control's top-five IDs/order. Post-query hashes
were unchanged; jobs and immutable files remain empty. Models/publication remain
disabled and no worker started. Eleven deployment tests and helper lint passed.

See `cbm-production-api-readiness.md` and JSON for evidence and Mac activation
instructions. Pending: Patrick's real browser login, Mac monitoring activation,
and repeat DB backup/restore acceptance with the migrated schema. No cutover,
publication, retirement or final-quality work was performed.

## September 10 — production browser login accepted

Patrick confirmed successful Authentik login and an empty recap workspace without
errors. Recorded this user-confirmed acceptance in both production API readiness
files. Available management receipts still show Kuma paused, the API metrics
target inactive, and only a pre-migration zero-table restore. Mac monitoring
activation and post-migration backup/restore remain the next required handoff.
Cutover, publication and retirement remain gated.

## September 10 — API staging acceptance complete

Read post-API management receipts: HTTPS probes, Kuma and Prometheus UP; actual
ten-table migrated schema restored with matching grants/owners/counts; source
unchanged. Independently verified VM109 dump checksum and healthy API. Recorded
completion of monitoring/restore alongside Patrick's successful real login.
Prepared a bounded synthetic production-worker phase proposal with a proposed
separate US$1 total key limit. This next phase is not approved or activated.
Cutover, publication, retirement and final quality work remain gated/deferred.

## September 10 — bounded worker phase approved at US$2; guards verified

Patrick approved the phase with a US$2 total non-resetting OpenRouter cap, replacing
the proposed US$1. Implemented a separate one-shot runner: exactly two synthetic
job IDs, exact source validation, fresh attempts only, selected-event dispatch,
12 requests per job, quota check before calls, and stop on uncertain outcome.
No indexing/publication/acquisition handlers. All 28 DB/queue tests passed,
including fake-provider execution and failure guards. The installed production
image passed a TLS-first scoped queue connect/bind check without fetch/publish.
No production job or model call was made; the public API remains read-only.

Management prerequisite: deliver a dedicated US$2 key and separate temporary
internal submission identity via the existing Infisical renderer. See
`cbm-production-worker-credential-handoff.md`; no management secrets or further
routine approval needed. Remaining submission/worker/backup work continues after
that delivery. Existing probe expiry remains September 11 at 02:05:38 UTC.

## September 10 — both bounded production synthetic jobs completed

Read delivered credential receipts and verified live US$2 unused allowance plus
frozen model availability. Temporary internal API submitted weekly
f6e9abed-e862-4eb7-a231-e98467adcaba and backfill
91d77409-afed-4625-97cb-748c8b637991, then was removed. The bounded worker processed
both once and exited: 8+6 successful model calls, 6+3 artifacts, total US$0.04381715
confirmed by saved response costs and later provider usage. Remaining US$1.95618285
is not authorization for more work. No indexing/publication/acquisition ran;
preserved corpus/config hashes remain unchanged. All source/artifact/model-response
references verified. Only staging API and Alloy remain running.

Captured and successfully restored all 53 managed files to a disposable directory.
Mac management must pair a new nonempty DB dump with this archive and verify the
restored references without replaying queued indexing. Concrete instructions and
private evidence paths: `cbm-production-bounded-worker-results.md`. Sixteen targeted
tests passed; lint/diff checks passed. Cutover/publication/retirement remain gated.

## September 10 — bounded phase and paired nonempty recovery complete

Read Mac management's nonempty recovery receipt and companions. Both jobs, all
rows and 26 references restored exactly against the 53-file archive; source
unchanged, copies removed, paired PBS checkpoint completed at 03:32:39Z. Forge
rechecked VM109 dump hash and healthy API/Alloy-only state. Approved bounded
worker phase is complete. Prepared `cbm-retrieval-cutover-phase-proposal.md` for
the next major decision; no endpoint, source writer or credential change made.
Cutover/publication/retirement remain gated and final quality backlog remains last.

## September 10 — retrieval-only cutover phase approved; preflight prepared

Patrick approved the retrieval-only phase. Confirmed the repository Open WebUI
filter posts directly to its full `retrieval_url` using X-API-Key, so the exact
new setting is https://community-brain.patchoutech.lab/retrieval/query (not the
base /retrieval path). All 75 filter tests passed. Updated the phase document and
prepared `cbm-retrieval-cutover-management-preflight.md` for the required VM101
source drift/writer inventory, private rollback capture, scoped retrieval identity
and actual-container TLS/auth path checks. The active endpoint remains unchanged.
Source freshness/ownership must be established before switching. Processing,
publication, retirement and final-quality work remain gated/deferred.

## September 10 — retrieval preflight verified; freshness policy decision needed

Read the management results and all referenced receipt descriptions. Verified all
14 receipt hashes and VM109 installed candidate/config hashes. Source matched all
2,627 files at 03:57:11 UTC, before scheduled 04:00 lint, so final source hashes
must be repeated after writer drain. Live filter differs from Forge source:
keep live code and perform valve-only changes; repository tests do not certify it.
Management verified its actual Requests HTTPS/auth path and documented CA handling
on recreation. No endpoint or writer state changed from Forge.

Prepared `cbm-retrieval-freshness-hold-decision.md`: a proposed legacy-writer hold
through no later than September 11 01:30 UTC, with verified rollback before prior
writers resume if ownership is not ready. This extended processing hold requires
Patrick's decision; immediate cutover-window approval did not settle its duration.
Do not switch into a stale-copy arrangement or silently extend an outage.

## September 10 — extended freshness hold approved; execution handoff ready

Patrick approved the legacy-writer hold through September 11 01:30 UTC, with
rollback before writer resumption if ownership is not ready. Recorded approval
and prepared `cbm-retrieval-final-window-handoff.md`: durable deadline recovery,
exact writer controls, post-lint source comparison, conditional valve-only switch,
actual loaded-filter checks and immediate rollback on failure. No further routine
approval is required for management execution. Changed source data stops the
switch and returns for candidate review.

Forge rechecked target package/config hashes, immutable image, read-only mounts
and verified HTTPS health. Legacy writers and the active endpoint have not been
changed from Forge; management access is necessary to execute those operations.

## September 10 — shared conversation handoff installed

Patrick authorized a file-based relay between Forge and home.servers. Installed
root-private `/srv/community-brain/handoff/` on VM109, accessible through both
conversations' existing SSH/sudo access. `HANDOFF.md` points to immutable request
CBM-RETRIEVAL-20260910-001, carrying the approved final window/switch request and
19 hash-verified documents. No management action has been claimed or executed by
this setup. Protocol copy: `docs/migrations/handoff/PROTOCOL.md`.

home.servers owns responses/status and an atomic claim; Forge acknowledges the
receipt before issuing a next request. Both should check the mailbox before asking
Patrick to relay messages. Polling operates only while the respective T3 turn is
active; no idle wake-up, background executor, new credential or listener was added.
The infrastructure rollback deadline must remain independently enforced.

## September 10 — shared relay executed retrieval switch; receipt acknowledged

Monitored request CBM-RETRIEVAL-20260910-001 through claim, preparation, switch and
completion. Management's live cached filter accepted the new HTTPS URL at 04:41:20
UTC after the 04:41:18 valve switch. Final held source comparison matched all 2,627
files; target/FTS/auth/monitoring passed. Verified 14 receipt hashes, imported the
safe receipts and acknowledged directly through the mailbox. No user relay needed.

Legacy writer hold remains active. Independent rollback starts September 11 01:25
UTC for the 01:30 deadline; no cancellation/new processing authorized. Patrick's
real Open WebUI check is pending. See `cbm-retrieval-switch-results.md` and the
retained management receipts for exact controls, recovery paths and limitations.

## September 10 — real retrieval acceptance passed; next phase prepared

Patrick confirmed his familiar Open WebUI query returned context/sources without
errors and directed continued work. Recorded acceptance and sent it directly to
home.servers via request CBM-ACCEPTANCE-20260910-002; no copy/paste needed. Hold and
rollback remain armed. Prepared `cbm-manual-processing-cutover-phase.md` around
explicit job eligibility, synthetic indexing only in disposable copies, manual
intake/writer ownership and paired recovery. Its proposed additional spend is
limited to the existing key's remaining US$1.95618285, within US$2 lifetime, and
requires this new phase's approval. No new model or indexing calls made.

## September10 — manual ownership, UI acceptance and next live indexing gate

Requests003–008 completed. The selected September8 job produced six verified
artifacts; Patrick accepted previews/downloads and the requested dark mode.
Paired recovery, off-host/PBS copies, probe renewal and terminal writer/intake
ownership passed. Legacy writers remain disabled; the temporary deadline is
superseded, not armed. See cbm-manual-production-results.md and cbm-dark-mode-results.md.

Live indexing is still awaiting an eligible selected meeting; September8 already
exists and is protected from replacement. The concrete next acceptance procedure
is cbm-next-manual-indexing-acceptance.md. No new provider work, remote publication,
retirement or later major phase was inferred from UI acceptance.

## September10 — full new-meeting loop approved and rehearsed

Patrick requested automatic processing on save and approved acquisition through
search indexing with “Do the full loop.” New-submission-only eligibility, date
collision protection, selected-stage scheduling, uncertainty stops, progress UI
and generated-meeting catalog integration are implemented. Canonical verification
passed and VM108 completed both fake-provider paths through actual LanceDB/FTS
with16 rows, preserving the first fixture and leaving old queued work untouched.

Request CBM-AUTOMATIC-20260910-011 is claimed/running by home.servers. It owns the
mandatory automatic paired recovery hook, deployment and monitoring integration.
Activation remains held until that work is verified. Current production still has
87 preserved meetings,481 files,one visible real job and automatic_processing=false.
See cbm-automatic-processing-results.md for exact checks and remaining acceptance.
Remote publication, historical replacement, retirement and final quality gates remain.

## September17 — workspace recovery implemented and tested

Request019 is the deployed Fathom URL/time-window baseline. Patrick approved the
next stabilization feature: actionable acquisition failures, same-job transcript
fallback, bounded safe resume and backup progress. Implementation and isolated
verification are complete; production rollout of this new feature is pending.
See `cbm-workspace-recovery-ready.md` and its hashed overlay manifest for behavior,
test results, exact packet and management wiring. Production data was not changed.
The prior September10 entries above are historical snapshots, not current status.

## September17 — publication phase prepared, activation disabled

Request020 browser acceptance is complete. Patrick authorized preparing Git/corpus
distribution with remote publication disabled. Existing publication mechanisms
and the current consumer repository were inspected; local Git/release tests and
an actual-installer fixture rehearsal passed. A handler-level disabled-publication
guard is added and tested locally, not deployed. See
`cbm-publication-phase-proposal.md` and `cbm-publication-consumer-rehearsal.json`.
The first-release file allowlist needs Patrick's decision before candidate
selection; credentials, publication launcher, exact release pins, full consumer
container rehearsal and remote activation remain outstanding. No production or
remote repository mutation was performed.

## September17 — six-file scope accepted; selected publication rehearsal passed

Patrick approved all six canonical files, including transcript.txt. Implemented
an offline publication-only selector/worker, exact artifact and checkpoint
checks, and release preflight/final-state verification. Full verification passed:
150 workflow,968 Python application,66 DB/queue,6 frontend-unit,5 browser tests.
The actual pinned consumer image served the fixture read-only on VM108 with a
mock embedding service; startup required the existing tokenizer cache mounted
read-only. Containers/test network removed; no production changes or model calls.

Request CBM-PUBLICATION-PREP-20260917-021 is posted for a private, consistent
six-file/current-corpus snapshot to VM108. It grants no remote publication,
credentials, deployment or publication-stage mutation. Real candidate validation
and exact release activation remain pending. This supersedes the preceding
file-scope question, which is resolved.

## September17 — first manual publication approved and Request023 posted

Patrick approved cbm-first-publication-phase-proposal.md. Exact local commits
were prepared from inspected remote bases: operator82167b30b2d72ae8ebb9a64a557991b30be442c3
adds only six September15 files; consumere2eca50575571a23657192163842c02331c85c96
changes only installer version/checksum with executable mode preserved. Neither
commit was pushed by Forge. Candidate and Git objects are staged privately on
VM109 with canonical plan hash a7ac3cf3f0d2ee31c184f956b6c1c2fd61545d8c3d23179ca8506a53ad506759.

A separate live publication oneshot now validates exact commits/assets, scoped
fresh credentials, job/checkpoint/generation and live claims before external
writes. It uses existing selected JetStream delivery without broadening weekly
stages. Consumer tag/release precede the main pin update; unknown effects stop.
GitHub target verification uses the actual precreated tag commit, consistent
with GitHub's documented target_commitish behavior for existing tags.

Validation: full suite150 workflow/975 application/68 DB-queue/6 frontend-unit/
5 browser plus build passed; final focused15 checks passed after adding tag
verification. Actual commits and candidate validated in the pinned image on
VM108 without network or credentials. Request023 contains immutable source/hash
packet and explicit management execution/rollback/receipt steps. Execution awaits
home.servers; existing API/weekly publication flags remain false. No provider
calls, production stage transitions or remote publication performed by Forge.

## September17 — Request023 publication verified and acknowledged

home.servers completed the approved first manual publication. Forge independently
verified both public main commits, the v1.2.0 tag, all six September15 file hashes,
all three downloaded release asset hashes, and the installer hash against the
approved plan. Release390814260 is published. An authenticated live API check
confirms git complete/distribution released, each generation1/attempts1. API is
healthy with zero restarts; API and stored publication flags remain false and
no publisher token is injected into the API.

Five management receipt hashes passed. Management evidence records unchanged
9 sources/21 artifacts/42 model-call rows, 88 sessions/1924 rows, actual published
installer/pinned consumer-image compatibility checks, isolated DB/file restores,
and verified off-host paired recovery. These recovery and consumer checks were
performed by management; Forge independently checked public effects and live job
state. Safe evidence: receipts/cbm-first-publication-023/. Shared Request023 is
acknowledged. No automatic weekly publication, retirement, CBM09 or final CBM10
phase was activated. Next decision is whether publication should remain manually
approved per release or enter a separately scoped automatic-publication phase.

## September20 — development-first stabilization implemented

Patrick accepted the live assessment and required every change to pass VM108
validation before production. Source a6766eb adds safe runner/readiness visibility,
truthful queued-save behavior, PostgreSQL-enforced read-only diagnosis, safe
scanner errors and an unprivileged-image build correction discovered on VM108.
Both synthetic intake paths passed real DB/queue/ingestion checks there; the
actual API factory and six VM108-served browser tests passed. Final Forge suite
passed150 workflow/1005 application/70 DB-queue/6 frontend-unit/6 browser tests.
See cbm-stabilization-development-results.md and its bound receipts.

Production holds remain; no deployment, rotation or paid call occurred. Request024
asks home.servers for current management source and read-only OpenWebUI/renewal
diagnosis. The actual renewal repair, renderer/image-pin integration and controlled
resume still require development validation and management execution.

## September20 — Request024 consumed; renewal development candidate

Verified and acknowledged all Request024 artifacts/source. Implemented stopped
WebUI credential delivery without restarting the consumer, retaining overlap and
live-cache checks. Twenty tests and a real Docker/SQLite fixture passed on VM108.
Request025 requests exact-image development acceptance and rollout-source review;
production remains unchanged. See [results](cbm-renewal-development-results.md).

### Scope correction: legacy VM is recovery-only

Patrick explicitly included OpenWebUI in migration off n8n-automation. Request025
was withdrawn with a shared stop notice before any response. Its candidate is
retained only as an unpromoted source/evidence archive; no legacy credential or
runtime was changed. Continue with replacement OpenWebUI acceptance on VM108,
production migration, and removal of legacy serving/renewal dependencies.

## September20 — Request026 posted

Verified home.servers acknowledged Request025 withdrawal before execution; no
development or production action occurred there. Consumed the receipt and posted
[Request026](cbm-openwebui-migration-request.md): read-only OpenWebUI migration
inventory, isolated VM108 acceptance, and coherent rollout/rollback preparation.
The old VM remains recovery-only; production changes are outside this request.

## September20 — Request026 accepted and source reconciled

Verified21 receipt artifacts and7 source files; independently matched6 Python
files to VM108 and confirmed its retained fixture is stopped. Imported the exact
OpenWebUI development harness. Real login/cache/credential changes and restart
persistence passed with synthetic retrieval. Fresh restore, full renewal, actual
backend, capacity and production rollout remain pending. See the
[successor packet](cbm-openwebui-successor-packet.md).

## September20 — real WebUI/backend integration, renewal and restore

Actual VM108 API/LanceDB/filter integration passed. The unchanged five-identity
policy retained overlap after a lost delivery acknowledgment and resumed the same
generation across3 API recreations. Fresh-volume/Chroma restore and316 concurrent
request pairs across the full two-meeting pipeline passed;3 focused recovery tests
passed on Forge and VM108. Integration services are stopped; private fixture and
evidence retained. See [results](cbm-openwebui-integration-results.md). Request027
requests actual development Infisical/consumer/lease and successor-renderer work.
Production and the legacy recovery VM remain unchanged.

## September20 — Request027 accepted; production gates reconciled

Verified 27 artifacts and independently matched all 34 live VM108 packet members.
Imported unchanged management source and passed six local boundary tests. Actual
Infisical/leases/consumer monitoring renewal passed on development. Forge acknowledged
the response. A local rebuild found equivalent descriptor contents but different
serialization order and packet hash; deterministic rendering remains open alongside
production descriptor/worker execution validation and protected restore/browser
acceptance. Preserve the reported r020 extra bytecode file for reconciliation.
See [management results](cbm-management-integration-results.md). No production
runtime, ingress or legacy recovery state was changed by Forge.

## September20 — deterministic packet and selected-worker execution

Fixed packet serialization, passed seven boundary tests locally and on VM108,
and matched packet-v8 manifest hashes across hosts. The selected-worker adapter
completed five stages/two synthetic meetings with 16 indexed rows. Providers,
allowance and queue binding were fixtures. Forty source files matched. Disposable
containers removed; existing development services and production preserved.
Read-only r020 bytecode and production mount/resource inspection identified the
remaining concrete bindings. [Request028](cbm-successor-bindings-request.md) is now
posted with source/evidence for home.servers' full VM108 host/management validation.
See [results](cbm-successor-validation-results.md).

## September21 — Request028 accepted and source reconciled

Verified all 42 artifacts and 50 actual VM108 packet members. Independent Forge
build matched the final v14 manifest; nine local boundary tests passed. Imported
unchanged successor source and acknowledged the handoff. Full synthetic host,
TLS queue, uncertainty/checkpoint, restore and renewal evidence passed with the
recorded revision/equivalence limits. Production loader remains disabled. See
[results and next implementation](cbm-successor-bindings-results.md). No production
or legacy runtime was changed; seven request containers are stopped.

## September21 — serving activation and retained-write rollback

Implemented a plan-pinned, journaled host controller with ordered locks and exact
hold/runtime checks. Ten tests pass on Forge/VM108. The actual image rehearsal
passed API/WebUI handoff, lost acknowledgment without recreation, duplicate calls,
authentication and rollback preserving a replacement WebUI write and incumbent ID.
Docker mount-order drift was fixed and regression-tested. Failed attempts were
preserved and reconciled before the passing plan-v3. See
[results](cbm-activation-development-results.md). Request029 now carries source and
evidence for real Mac/SSH/full-successor integration. Production remains unchanged.

## September21 — Request029 accepted

Verified 72 artifacts, 58 VM108 packet members and 255 bound files in each of
three plans. Independent rebuild matches; all 30 local tests pass. Imported exact
source and acknowledged the handoff. Actual Mac/SSH activation/rollback and monitor/
renewal integration passed within the recorded development limits. All 12 request
containers are stopped. Production template remains disabled with 21 evidence
slots; protected restoration/acceptance preparation and workload checks are next.
See [results](cbm-activation-integration-results.md), including the internal-network
loopback-relay qualification and retained-write rollback limits.

## September21 — protected restore packet prepared; Request030 posted

Prepared authoritative source/destination treatment, phase sequence, private
manifest/safe receipt requirements, restoration/browser/workload acceptance and
rollback limits. Identified fixture restart/checkpoint side effects in existing
recovery helpers and excluded their direct production use. Reconciled the packet
with the 21-slot production template; posted and hash-verified all six Request030
documents. Home.servers will resolve exact private bindings/commands and validate
new mechanics on synthetic VM108 state. This was preparation only; no runtime or
real-data transfer occurred. See [packet](cbm-protected-restore-packet.md).

## September21 — Request030 accepted; capture-wrapper gap explicit

Verified 52 manifest artifacts, 15 live VM108 source files and 39 local tests;
imported source and acknowledged. Fresh synthetic DB/fence, component transfer/
restore, WebUI session and budget-negative evidence passed within recorded limits.
Source/destination bindings and bounded private phase proposal are concrete, but
capture-wrapper interruption/deadline handling and new receipt validation remain.
No protected transfer, resizing or paid test occurred. See
[results](cbm-protected-restore-preparation-results.md), including heartbeat-drift,
capacity, counting and browser/session evidence limits.

## Capture controller development — September21

See [Forge results](cbm-capture-controller-development-results.md):49 tests passed on
VM108 plus retained synthetic recovery. Request031 covers remaining host orchestration
and database evidence validation. Production execution remains disabled.

## Request031 consumed — September21

[Verified integration results](cbm-capture-controller-integration-results.md):32 final
source files independently match VM108; eight recovery scenarios and51 negative
checks passed. Source imported unchanged; Forge49 tests pass. Native Mac fixtures
have five metadata errors. Next is shared scheduler/manual/capture admission and a
production-shaped synthetic database validator, including unresolved recovery.
Production remains disabled; protected transfer is not yet ready for authorization.

## Shared admission increment — September21

[Forge shared admission core](cbm-shared-admission-development-results.md) passed
nine tests on VM108, including actual owner kill and cross-entry-point blocking.
[Request032](cbm-shared-admission-integration-request.md) covers installation into
candidate scheduler/manual/capture paths, authoritative recovery and the remaining
production-shaped synthetic database validator. Production remains disabled.

## Request032 consumed — September21

[Reconciled results](cbm-shared-admission-integration-results.md):49 final source
files independently match VM108. Shared candidate admission, failed-finalizer/startup
handling and expanded PostgreSQL evidence passed. Forge reran58 tests. Mac fixture
errors are resolved. Next is actual helper/catalog/service/private-restore mapping,
then validation of changed bytes on VM108. Production execution remains disabled.

## Actual production mappings — September22

[Mapping closure packet](cbm-production-mappings.md) now binds a fresh read-only
production census and boot/runtime inventory. Actual DB has public/plpgsql, ten
tables,19 indexes and no sequences; Request032 fixture topology is not its profile.
Five mapping checks passed on VM108. Request033 must close real helper/admin catalog/
service/private-restore mappings and return final tested source. Production remains
unchanged and mappings are not complete until that evidence is reconciled.

## Request033 consumed — September22

[Production mappings are closed at candidate level](cbm-production-mapping-integration-results.md):
152 source files independently match VM108, all nine helper proof bindings verified,
and65 Forge tests pass. Next is qualification of the mapped implementation and an
executable bounded production controller. External protocol fixtures are not live
consumer/CA acceptance. Protected transfer, session/vector/capacity acceptance and
persistent enrollment remain unproved; production execution stays disabled.

## Stage 2 opened — September23

Patrick authorized the full development qualification. [Forge VM108 results](cbm-stage2-forge-results.md)
include fresh-volume WebUI/API recovery, rendered Playwright login/retained chat,
persisted disabled signup, a corrected dev healthcheck and350 concurrent request
pairs. [Request034](cbm-stage2-qualification-request.md) covers actual scoped
Infisical/CA/consumer integration, the bounded controller and intended full
capacity. The prior production authority and admission window have expired;
production execution remains disabled.
