# CBM-01: Job and artifact contracts and isolated test harness

Date: 2026-09-09. Status: development contract and executable boundary probes.
Authority: Patrick's instruction to begin CBM-01 after the
[Forge handoff](forge-development-handoff.md). No production action is authorized.

These are project decisions under Backend v0.15, Frontend v0.6 and Hosted
Services v0.5 in `docs/standards/`; the dated standards remain unchanged.
The test-only schema is deliberately smaller than the application contract.
CBM-03 owns production ORM models, reviewed Alembic migrations, API handlers,
outbox dispatcher, worker, recovery loop and their full acceptance tests.
No application startup runs migrations.

## Identity and durable records

PostgreSQL is authoritative. UUIDs identify meetings, source revisions, jobs,
stages, attempts, artifacts and outbox events. Every record belongs to an access
scope. A meeting records provider and provider meeting/recording ID where
available, an offset-aware start instant, validated IANA timezone and local
meeting date. Manual intake allocates a meeting ID and requires these time
fields. Validate local date against instant/timezone. Multiple calls on one day
remain distinct; a filename date alone never establishes a rendezvous.

An immutable source revision records each source kind, byte SHA-256, byte size,
managed storage key, acquisition timestamp and provider receipt. Chat and
transcript must be explicitly associated with the validated meeting. Repeated
uploads with the same identity and hashes reuse the revision. Different bytes
create a new revision, never change an accepted job's inputs. A job waiting for
missing input may bind its first complete revision exactly once under a lock.

Acceptance stores job, initial stages and outbox rows in one transaction. Return
202 only after commit. Scope an idempotency key to authenticated principal,
access scope and operation. Hash a canonical validated request, including source
revision, mode and requested pipeline version; do not include bearer tokens.
Same key/hash returns the original job and status; same key/different hash is
409. Concurrent acceptance must converge on the database uniqueness constraint.
Keys survive as long as their job/audit records; expired keys must not silently
be reused. Also uniquely constrain scope/meeting/revision/pipeline-version/run
number so a different key cannot accidentally repeat paid work. Only explicit
rerun creates a new run number and links the original job.

Persist mode (`weekly` or `transcript_backfill`), parent job, submitter, stage
dependency graph and all versions at acceptance. Attempts record fence token,
worker ID, start/end/heartbeat timestamps, retry decision, provider request ID,
effect intent/outcome, prompt hash/version, model/provider/configuration,
token usage/cost/currency where known and a sanitized error. Unknown usage is
null, never zero. Artifact records include source revision, producing attempt,
logical filename, media type, bytes/hash and relative immutable storage key.
Index records include expected/successful/failed chunk counts and corpus version;
publication records include manifest hash, target and provider/Git receipt.
Secrets and raw transcript content never enter job events or ordinary logs.

## Independent states

Expose the following dimensions; there is no single success bit that hides
partial indexing or failed distribution.

| Dimension | States and transitions |
| --- | --- |
| Processing | `waiting_for_input` → `queued` → `running` → `succeeded`; failures may enter `retry_wait`, `failed`, or `outcome_unknown` |
| Stage | `blocked` → `queued` → `running` → `succeeded`; `running` → `retry_wait` / `failed` / `outcome_unknown`; `retry_wait` → `queued` when due; mode-inapplicable stages are `skipped` |
| Artifacts | `pending`, `partial`, `ready`, `corrupt`; ready means every required artifact for the selected mode is durably recorded and hash-verified |
| Indexing | `not_requested`, `pending`, `running`, `partial`, `complete`, `failed`; any failed expected chunk prevents `complete` |
| Git publication | `not_requested`, `pending`, `running`, `complete`, `failed`, `outcome_unknown` |
| Distribution | `not_requested`, `pending`, `validating`, `validated`, `released`, `failed`, `outcome_unknown` |

Terminal attempts are immutable. Retry creates a new attempt on an eligible
stage, preserving successful upstream artifacts. It cannot reset a succeeded
stage. A versioned rerun creates a new job/revision namespace. Dependents remain
blocked when required predecessors fail; independent stages continue. Backfill
jobs and individual meetings in a batch keep separate durable failure/progress
records so one failure does not erase progress or abort later meetings.

Initial project retry policy: at most three automatic attempts per stage,
30-second then 120-second backoff, respecting a larger provider Retry-After up
to one hour. Validation, permission and immutable-conflict failures are terminal.
Only failures known to have caused no external effect may retry automatically.
An operator may authorize a fresh bounded retry cycle with a reason; preserve
all earlier attempts and the total spend history. Pipeline-specific inner LLM
retry/budget caps remain those extracted from the JS oracle in CBM-02 and must
fit the outer budget, not multiply it invisibly.

## Claims, events and external effects

Use version 1 events on project subject `cbm.<environment>.jobs.stage.ready.v1`.
Envelope: `schema_version`, `event_id`, `job_id`, `stage_id`, `generation`,
`occurred_at` (UTC), `trace_id`. IDs reference PostgreSQL state; no transcript,
credentials, arbitrary paths or caller-selected executable actions. Consumers
validate the envelope and look up authoritative state before acting. Reject and
record unsupported/poison events with a sanitized reason before terminating
delivery. Subject authorization and final stream provisioning belong to CBM-07.

The outbox publisher marks an event sent only after JetStream publish ACK.
Use event ID as `Nats-Msg-Id` for best-effort broker deduplication. A lost publish
ACK or crash before marking sent causes republish of that same ID. Business
correctness never relies on the broker's finite deduplication window.

Use a durable pull consumer with explicit ACK. Proposed application defaults:
60-second DB lease, heartbeat every 15 seconds, 90-second consumer AckWait,
max delivery 10. The worker renews the lease and sends in-progress acknowledgments
while work runs. DB time governs eligibility. Claim atomically increments a
monotonic fence token and records owner/expiry only if prerequisites are met,
retry is due and there is no valid claim. Every renewal, outcome and artifact
pointer update must compare owner/token/state and unexpired lease. No transaction
stays open during model calls. A completed stage yields a durable no-op and ACK;
a busy stage is delayed without starting another attempt. ACK only after a
durable outcome, retry intent/outbox, or quarantine decision commits.

Lease expiry is not permission to repeat an external effect. Persist effect
intent and attempt/provider idempotency key before starting model spend or
publication. A crashed/expired attempt with unresolved intent moves to
`outcome_unknown`; reconcile using provider status, saved response or Git/release
receipt. If the provider cannot resolve it, require explicit operator disposition
before retrying with acknowledged duplicate-spend risk. Calls have bounded
timeouts and total stage budgets pinned with the pipeline version. A worker that
loses its lease stops new effects; a late response can be preserved privately
for reconciliation but cannot promote itself to the canonical artifact.

Initially one corpus writer owns ingestion, lint and publication coordination.
An expired lease alone cannot make LanceDB writes safe: stop/fence the previous
writer process before starting its replacement. Process-local registry locks
cannot arbitrate multiple worker processes.

## Files and both output contracts

Managed storage keys use server-generated IDs:
`jobs/<job-id>/stages/<stage-id>/attempts/<fence>/<logical-filename>`.
Clients address artifact IDs, never filesystem paths. Storage is private to the
application; enforce containment and reject symlink traversal in CBM-03/04.
Publish the same legacy logical names on download and in the compatibility export:

| Artifact | Required mode/semantics |
| --- | --- |
| `transcript.txt` | Weekly formatted raw output; backfill retains its original transcript input without requiring a new copied output |
| `prepared-transcript.md` | Both modes; preserve preparation semantics |
| `extracted-signal.md` | Both modes; six canonical sections below |
| `community-post.md` | Both modes; backfill preserves the historical archive framing |
| `community-post-compressed.md` | Weekly; compressed community-board copy |
| `YYYY-MM-DD-weekly-invite.md` | Weekly; next Tuesday strictly after meeting local date |

Signal headings remain `## general`, `## insights`, `## qa`, `## tools`,
`## links`, `## decisions`, in that order, as enforced by `Code: Aggregate Signal`
in workflows 5/6 and the ingestion parser. The older human-readable headings in
`prompts/MergeCallSummary-ExtractSignal.md` are not the current signal wire format.
Community posts preserve the assembled plain-text presentation. Exact generation and backfill
behavior will be checked against workflows 5/6 in CBM-02; these contracts do not
authorize rewriting existing output. Legacy date-directory collisions from
multiple same-day meetings must stop export for explicit disambiguation, never
overwrite a previous session.

Publication order:

1. Write an exclusive staging file inside the attempt directory on the same
   filesystem; flush, fsync and hash complete bytes.
2. Atomically publish without overwriting an existing immutable file (the Linux
   probe uses a hard link), remove staging and fsync affected directories.
3. Commit artifact metadata and successful stage outcome together under the
   valid claim. Enqueue dependent work in the same transaction.
4. Only committed artifact IDs can be listed, previewed or downloaded.

An identical existing file may be reused after hash verification; different
bytes at the same key are an immutable conflict. Fencing must include the file
namespace so a stale worker cannot overwrite a new worker's bytes. A crash before
DB commit leaves an unreferenced file, not a ready artifact. Recovery can adopt
a verified matching result under a new valid claim and preserve its original
attempt provenance. Reconcile missing/corrupt recorded files into `corrupt` and
block downstream release. Never serve them as ready.

Orphan cleanup considers only managed staging/attempt directories, checks DB
references and active claims, and holds the same job lock while selecting work.
Use a 24-hour grace period for closed attempts; quarantine before deletion and
recheck references. Do not delete unresolved external-effect evidence. General
backup retention and quarantine purge policy remain CBM-07 decisions.

Artifact readiness enables the authenticated web preview/copy/download path
independently of indexing or publishing. Separately, Git/corpus distribution
builds an immutable candidate manifest with file hashes, canonical source IDs,
schema/embedding/prompt/registry versions and corpus version. Validate the
LanceDB consumer package before advancing the release pointer. Persist Git
commit/release receipts. Failure leaves the previous valid release intact.
Release retries reconcile the candidate hash and receipt before another push.
There is no board auto-posting. Tests never push or publish real releases.

## HTTP and authorization contract (implementation in CBM-03/05)

All routes use `/api/v1`. People authenticate through Authentik/OIDC; services
have independent scoped identities. Validate issuer, audience and expiry.
Authorization checks the access scope and resource on every route; knowing a
job/artifact UUID grants nothing. An inaccessible resource returns 404.

| Route | Permission / result |
| --- | --- |
| `POST /jobs` | `jobs:submit`; Idempotency-Key required; meeting/revision/mode/pipeline version → 202 job/status URL (200 for replay) |
| `GET /jobs` | `jobs:read`; stable `(created_at,id)` cursor, default limit 50, max 100; filter by independent dimensions |
| `GET /jobs/{id}` | `jobs:read`; all dimensions, stage attempts, safe errors, retry eligibility, missing inputs and version/provenance summaries |
| `GET /jobs/{id}/artifacts` | `artifacts:read`; committed records with filename/media type/hash/bytes and download URL |
| `GET /artifacts/{id}/content` | `artifacts:read`; plain UTF-8 Markdown/text with safe Content-Disposition and ETag; never executable HTML |
| `POST /jobs/{id}/stages/{stage_id}/retry` | `jobs:retry`; idempotency key and reason; expected stage generation prevents stale concurrent retries; 202 or 409 |
| `POST /jobs/{id}/reruns` | `jobs:rerun`; explicit pipeline/source revision and reason, idempotency key; 202 new linked job |

Human reader maps to read permissions; operator adds submit/retry/rerun. Hermes
receives submit/status permissions by default, artifact read only when separately
granted. Collector gets source-upload capabilities only (CBM-04). Worker/publisher
identities cannot impersonate people. Unknown-outcome disposition requires a
separate `jobs:reconcile` operator permission and audited reason; API details for
that administrative action must be finalized alongside reconciliation in CBM-03.

Errors are `application/problem+json` with `type`, `title`, `status`, stable
`code`, sanitized `detail`, `instance`, `trace_id`, `retryable` and optional
`retry_after_seconds`. Codes include `invalid_request` (422),
`unauthenticated` (401), `forbidden` (403), `not_found` (404),
`idempotency_conflict`, `stage_not_retryable`, `stale_generation` (409),
`rate_limited` (429), `dependency_unavailable` (503). Durable stage errors also
include `claim_lost`, `artifact_corrupt`, `immutable_artifact_conflict`,
`indexing_partial`, `outcome_unknown`, `retry_exhausted`. No provider body, token,
raw transcript or absolute host path belongs in error detail. Unknown outcomes
always report retryable=false until disposition. Additive API changes retain v1;
breaking semantics require a new version and compatibility review.

## Recovery and acceptance evidence

PostgreSQL + immutable files + corpus/export versions define recovery. Queue
state is delivery state. After restore, verify file hashes and publication
receipts, classify expired claims with unresolved effect intent as unknown,
then reconstruct eligible work from DB state using new recorded dispatch
generations. Reconstruct unsent outbox work and due retries even if JetStream
lost all messages or exhausted MaxDeliver; never blindly replay publications.
The recovery scanner uses row locks/unique event generations to avoid duplicate
dispatch storms. Missing files block readiness and require repair/rerun; a
snapshot of the future VM alone cannot restore the shared external database.

`tests/cbm/` contains an executable, deliberately test-only SQLAlchemy Core
probe over Psycopg 3 and PostgreSQL, plus real file-backed JetStream. It covers:

- acceptance/outbox rollback and commit, conflicting and concurrent submissions;
- concurrent claims, heartbeat, expiry and rejected stale completion;
- crashes before file publication, after publication and before DB commit;
- no-clobber bytes, corruption rejection, and durable artifact pointers;
- duplicate publication after lost publisher progress and actual broker
  redelivery after a worker reconnects without acknowledging its completed work.

Injected exceptions model worker crash boundaries; these are not OS power-loss
or full restore rehearsals. The reduced probe has one stage per job, and does
not establish full API/auth/retry/recovery behavior. CBM-03 must port these
scenarios to the application store/worker and add unknown-effect reconciliation,
retry exhaustion, server restart/queue loss, orphan cleanup and authorization
acceptance. CBM-06 adds consumer compatibility and release failure tests.

## Running verification on Forge

```sh
uv sync --project community-brain --locked --python 3.11.15 --extra dev
./scripts/setup-cbm-test-services.sh
./scripts/verify-forge.sh
```

The canonical verification command includes the existing Node/Python baseline
and the new mandatory integration tests; missing dependencies fail, never skip.
For focused development only: `community-brain/.venv/bin/python -m pytest tests/cbm -q`.

Verified on Forge on 2026-09-09: **150 Node + 771 existing Python + 8 new
durability tests passed**. The existing Python suite retained its 70 LanceDB
FTS deprecation warnings. Shell syntax and `git diff --check` passed. No existing
locked package version changed. These results cover the probes listed above,
not an implemented job API, production restore or consumer cutover.

Docker is absent on this Forge environment. As a bounded project choice for
BE-36, the setup script extracts pinned Ubuntu 26.04 PostgreSQL 18.6 and NATS
2.10.27 packages under the runtime user's cache, without sudo, package installation
or service registration. These are test versions, not production upgrade choices.
The package manager's configured repository metadata supplies integrity checks.
Python clients are locked in `community-brain/uv.lock` as development extras.
Cached distro packages may eventually disappear from mirrors; update the
explicit pins deliberately and rerun the baseline. On another Linux host,
install compatible binaries and expose `initdb`, `postgres`, `pg_isready` and
`nats-server` on PATH; the Forge bootstrap is not portable across distributions.
Docker/Compose remains the deployment standard. CI workflow publication is
outside this change; future CI must invoke this same canonical command with
disposable binaries available, without access to the lab.

Each run initializes a fresh mode-0700 temporary cluster and JetStream directory,
uses a private PostgreSQL Unix socket (no TCP) and a loopback-only random NATS
port, and terminates/reaps its own child processes before removing state.
It accepts no external connection URLs and reads no `.env`. Hard-killing pytest
can bypass finalizers; if that happens, identify only the abandoned `cbm-*`
processes/directories before cleanup. No shared-platform resources, production
credentials, model calls, workflow imports or corpus releases are involved.

Primary implementation references:
[PostgreSQL initdb](https://www.postgresql.org/docs/18/app-initdb.html),
[JetStream consumers](https://docs.nats.io/nats-concepts/jetstream/consumers),
[NATS configuration](https://docs.nats.io/running-a-nats-service/configuration).
