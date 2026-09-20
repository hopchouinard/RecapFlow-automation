# Live development validation — 2026-09-09

## Current result

Real Authentik browser login and the bounded live weekly exercise passed.
Patrick confirmed the workspace loads under `pchouinard`; `akadmin` was denied
by the development group policy. A development-only authenticator wrapper then
recorded successful RS256 signature, issuer, audience and expiry verification,
`community-brain-dev` scope and exactly the eight approved permissions from an
actual browser request. No token or token body was logged. The SPA uses its
public authorization-code/PKCE flow; provider discovery advertises S256.

Job `f453deaf-0638-4580-9fe6-2b5a47cb1133`, meeting
`live-development-synthetic-20260909`, processed synthetic transcript/chat using
the unchanged `processing-v1` snapshot. Eight OpenRouter requests succeeded on
their first attempt. All six artifact downloads passed SHA-256 verification:
original transcript, prepared transcript, extracted signal, community post,
compressed post, and September 15 weekly invite. Processing is `succeeded` and
artifacts are `ready`.

Provider usage initially lagged the request receipts, then reconciled exactly:
**US$0.01324578 used; US$4.98675422 remaining** under the original US$5
non-resetting limit. No unresolved model calls or automatic retries occurred.
The one-shot worker exited and its container was removed. The normal API has
no inference credential; no background worker remains. Remote publication stayed
disabled and Git/distribution remain `not_requested`. Indexing subsequently completed; the final section records live retrieval evidence.

A read-only probe from the API container reached the retained Ollama endpoint
`http://10.1.50.219:11434/api/tags` and found `nomic-embed-text:latest`. This proves
reachability/model presence only, not embedding execution or semantic quality.

### Output review and decision

The pipeline's structural validation passed, but manual review found:

- The prepared transcript wrapped the declarative sentence about startup not
  proving recovery in `<Q>` markers, although no question was asked.
- The community post and compressed post changed “keep the original transcript”
  into “keep the original transcript running,” an inaccurate paraphrase.

These are output-quality findings for the unchanged historical prompt snapshot,
not evidence of migration parity failure. Do not mutate the frozen snapshot or
rewrite the immutable outputs. Patrick chose strict prompt parity on 2026-09-09. Track these findings in
[CBM-10, the final quality backlog](cbm-final-quality-backlog.md), to be addressed
as the last step of the whole migration. They do not block continued development
rehearsal or semantic indexing; do not change the frozen prompts now.

Sixteen targeted deployment/spending-guard tests passed. They include rejection
of exhausted/unknown allowance, an incorrect/resetting limit, management keys,
excluded BYOK spending and the request-count ceiling without reaching inference.
Changed helpers passed Ruff and formatting; `git diff --check` passed.

Safe evidence in the VM artifact directory includes `oidc-verification.json`,
`fixture-job.json`, `fixture-result.json`, `bounded-worker.log`, and
`allowance-final.json`. Artifact contents remain in the private project volume.
The explicit one-shot overlay is `compose.bounded-development.yml`; its launcher
requires verified browser-claim evidence, rechecks allowance, selects only the
fixed fixture's queued processing stage, limits requests to 12, and refuses a
repeat execution after model intents have been recorded. It uses the real
JetStream delivery, Worker lease heartbeat and durable model journal. It never
runs downstream indexing/publication handlers.

## Initial login environment and checks

The provisioned [access handoff](cbm-live-development-access.md) was consumed on
VM 108 only. Compose project `cbm-live-development` runs PostgreSQL 18.6,
authenticated NATS 2.10.27 with JetStream, and the standalone API/web image
`sha256:5e234ec55b2bf0f8aa42d39b721fd3e0c219d674860ca0729db2e2c98c1d6259`.
The API is healthy and published only at `127.0.0.1:8090` on the guest.

The project has dedicated database, queue, files, configuration and NATS-config
volumes. PostgreSQL/NATS use the rendered development passwords. Only the API
joins the additional egress network for Authentik; dependencies use an internal
network with no published ports. The API mounts the guest CA bundle read-only.
Initialization has no network, migrations completed, and the durable consumer
was explicitly provisioned. JetStream storage is capped at 64 MiB.

There is no worker in this login-validation Compose file, and no service receives
the OpenRouter key. Model calls and remote publication are explicitly false.
Retrieval remains disabled pending a verified live embedding endpoint. Only a
synthetic speaker alias file was initialized; no historical corpus was copied.

Source: `deploy/community-brain/compose.live-development.yml` and
`deploy/community-brain/live-development/`. VM staging:
`/srv/dev-data/workspaces/cbm-rehearsal-20260909/deploy/community-brain/`.

## Passed checks

- API health and PostgreSQL migration.
- Operator and reader service identities: exact development scope/permissions,
  authenticated identity and job-list reads.
- Missing, malformed and expired credentials rejected (401); reader source
  writes rejected (403); metrics and publication denied to both roles (403).
- Test bearer values delivered over stdin only to a disposable scoped test
  process, never to application containers or the browser. Docker `--env-file`
  preserves dotenv quotes; the checked-in launcher parses the rendered quoted
  values before delivery. An initial quoted-value test failed without granting
  access; the corrected test passed.
- Container HTTPS verification: Authentik discovery issuer matches, PKCE S256
  is advertised, and JWKS contains an RSA signing key.
- Public OpenRouter catalog contains the existing model IDs
  `z-ai/glm-5.3-flash`, `anthropic/claude-sonnet-5`, and
  `google/gemini-3.1-flash-lite-preview`. No model substitution was made.
- Authenticated read-only OpenRouter allowance check: limit $5, reset null,
  remaining $5, usage $0, management-key false, BYOK included in limit.
  Recheck immediately before any paid request.
- Eight deployment tests passed, including Compose v2 parsing and live-stack
  isolation/credential checks. Changed helpers passed Ruff and formatting checks;
  `git diff --check` passed.

## Initial browser gate (subsequently completed above)

A Forge SSH tunnel successfully reached API health. The collaborative browser
could not reach its own localhost endpoint before the Mac tunnel was established;
this is not evidence of an OIDC login failure. Patrick has been asked to run:

```sh
ssh -N -L 127.0.0.1:8090:127.0.0.1:8090 pchouinard@10.1.30.20
```

Open `http://localhost:8090`, sign in, and keep the browser/tunnel open. Actual
code exchange and signed access-token authorization remain unverified. The SPA
requests `/api/v1/me` and the jobs list using its access token; successful backend
responses must establish the expected scope and permissions, including absence
of `corpus:publish`, before enabling a bounded worker exercise.

At that initial checkpoint, no inference request, job submission, live ingestion,
remote publication, production deployment or cutover had occurred. The development stack is left running
for login. Service test tokens expire 2026-09-10 at 19:43:21 UTC; expired values
must be renewed through Infisical, never replaced with timeless fixtures.

## Repeat checks on the VM

From the staging `deploy/community-brain/live-development` directory:

```sh
sudo -n python3 compose.py config --quiet
sudo -n python3 run_auth_checks.py
sudo -n python3 check_allowance.py
```

The Compose launcher constructs percent-encoded private connection URLs in
process memory and passes the private runtime path via `--env-file`. Never run
plain resolved `docker compose config`, dump container environments, or print
private runtime files. Safe evidence is under
`/srv/dev-data/artifacts/cbm-live-development-20260909/`.

## Indexing follow-on: initialization repaired, reconciliation pending

The next indexing attempt exposed a local initializer permission failure: its
root process had CHOWN but could not populate the runtime-owned private config
directory. The shell driver then proceeded despite that initializer failure.
Indexing was claimed but could not load its configuration. The one-shot worker
exited without completing the stage; the existing recovery sweep classified its
expired indexing lease as `outcome_unknown`, conservatively, as designed.

Current indexing stage: `66cabad3-bf3e-4ae0-a7e3-a09f21b5e9c0`, generation 1,
attempts 1, error `lease_expired`. Processing and all six artifacts remain intact.
No indexing model intent journal exists, and provider usage remains exactly
US$0.01324578 / US$4.98675422 remaining. No additional model call or live embedding
has been established. No indexing retry or reconciliation was performed.

Repairs prepared and verified:

- Initializer has DAC_OVERRIDE in addition to CHOWN, confined to its isolated
  project volumes with no network. Canonical extraction configs/prompts plus
  synthetic registries are now installed and readable by UID 10001.
- The launcher now requires initialization success before running indexing.
  The worker validates configuration before consuming/claiming queued work and
  exits nonzero unless its selected stage completes.
- The application ingestion client now has a context-local, opt-in strict outcome
  policy. Job indexing uses it: uncertain HTTP/response outcomes propagate through
  both extractors into `outcome_unknown`, without automatic provider retry. Legacy
  callers retain their retry behavior; prompts and model choices are unchanged.
- The development indexing wrapper checks allowance before each paid request,
  caps requests at 16, persists private intent/response receipts, and propagates
  receipt or malformed-response uncertainty instead of continuing extraction.
- Image built successfully:
  `sha256:b3a1284201f42ef7cb603ff9866c999ba084350a9ae9e65a122f5a36ad95aedc`.
  The running API still uses its earlier healthy image; the new image was used
  for indexing and the repaired configuration preflight.

Full canonical verification passed: 150 Node tests, 843 Python tests, 23
PostgreSQL/JetStream application tests, one Vitest and one Playwright test, plus
the frontend build. An additional malformed-indexing-response guard regression
was added afterward and the eight spending-guard tests passed. Config/runtime
preflight passed with network disabled. Existing Python warnings remain 70.

The next concrete action requires explicit operator reconciliation under the
[recovery contract](cbm-01-job-artifact-contracts.md), with an audited reason and
`Acknowledge-Duplicate-Effect: true`. The prepared `run_fixture.py reconcile-index`
action uses the scoped operator token to reconcile this exact stage/generation;
then `run_fixture.py index` runs only that queued indexing stage. The worker
accepts the second attempt only with the corresponding durable authorization,
the exact audited repair reason, and no previous indexing model-intent journal.
No direct database reset or silent replay is used. Await Patrick's acknowledgment
before executing those actions. Publication remains disabled.

## Reconciled indexing and live retrieval completed

Patrick explicitly authorized reconciliation and retry. The scoped operator API
reconciled generation 1; the one-shot worker consumed generation 2 and completed
indexing on its second attempt. The original processing stage was not rerun.

- Nine chunks written: two prepared-transcript, six extracted-signal and one
  community-post chunk. Zero failed chunks; no ingestion warnings.
- Ten live extraction requests using the unchanged
  `google/gemini-3.1-flash-lite-preview` / `chunk-extraction-v3` configuration.
  Every private intent has a corresponding response receipt.
- All nine chunks have successful extraction and 768-dimensional embeddings from
  retained Ollama `nomic-embed-text` at `10.1.50.219:11434`. Real FTS verification
  passed. This is live embedding execution, not the earlier simulated fixture.
- Authenticated read-only retrieval passed for “How should restored meeting notes
  be verified?” and “file hashes backup restoration.” Both returned relevant
  source content with vector similarity and BM25 contributions. The first query's
  top chunk describes comparing file hashes after restoration.
- An unmatched date range returns no chunks. Legacy `X-API-Key` read transport
  works; unauthenticated query is rejected and ingestion/reindex routes are hidden.
- API corpus and configuration mounts are read-only; distribution serving mode
  is enabled. API still has no inference key or model execution permission.
  Only the read-only retrieval interface uses Ollama for query embeddings.
- Indexing cost US$0.00782625; aggregate processing plus indexing cost
  **US$0.02107203**, provider-confirmed **US$4.97892797 remaining**. No further
  OpenRouter worker is running. Remote Git/release/board publication remains off.

This validates plumbing and basic relevance for one synthetic session, not
production-corpus retrieval equivalence. The known Q-01/Q-02 content issues remain
visible in retrieved source material and stay deferred to CBM-10; no frozen prompt
or immutable processing artifact was changed.

The current API runs image
`sha256:b3a1284201f42ef7cb603ff9866c999ba084350a9ae9e65a122f5a36ad95aedc`.
Seventeen targeted deployment/spending-guard tests passed after enabling the
read-only retrieval mount. Ruff and `git diff --check` passed. Earlier full-suite
results remain recorded above; the entire suite was not unnecessarily repeated.
Post-run memory observations: API 174.3 MiB, PostgreSQL 34.25 MiB, NATS 4.871 MiB
(not peak measurements).

Safe query evidence: `retrieval-result.json` and `retrieval-check-output.json` in
the VM artifact directory. The development API was briefly stopped with no workers
running to take a coordinated database/files/config/corpus snapshot, then resumed:

- `completed-snapshot/database.dump` SHA-256
  `41de2df1392f7cfc267c6c4d482d346467216fd744e8f1e61b4ccefa94dc25b7`.
- `completed-snapshot/state.tar.gz` SHA-256
  `d139e53fed3d94339c982dbfb6013b08886e2b9db41ebd2b44373253d81029ed`.

Snapshot directory mode 0700, files 0600. No runtime credentials or NATS auth
configuration were exported. Queue reconstruction uses durable records. This
snapshot has not had a full restore rehearsal; the earlier simulated restore
evidence is separate.

### Next input: live acquisition

Manual upload, live processing, indexing and basic retrieval have been exercised.
The next live acquisition rehearsal needs a development-only Fathom credential
rendered through the approved Infisical development path, plus one explicitly
approved test recording ID/date. The current access handoff deliberately supplies
no Fathom key. Do not extract a production credential or start broad polling to
fill this gap. Patrick must identify the permitted recording/account and arrange
private delivery, or choose to defer live Fathom acquisition. No raw credential
belongs in chat. Production deployment/cutover and remote publication stay gated.
