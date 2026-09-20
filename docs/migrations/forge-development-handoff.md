# Community Brain: Forge development handoff

Current continuation entry point: [September 20 live assessment and plan](cbm-current-state-and-continuation.md).
The preparation status and restrictions below describe the original September 9
phase; later authorized work and today's runtime findings are recorded there.

Date: 2026-09-09. Owner: Patrick Chouinard.
Status: preservation and development preparation complete; application implementation and production cutover are not authorized by this preparation phase.

## Start here in a new T3 thread

Open the **Forge** environment and add `/home/t3code/projects/RecapFlow-automation` as a project. Use branch `migration/community-brain-forge-handoff`. Read this document, then the scoped instructions in `community-brain/CLAUDE.md` when working on retrieval/ingestion. The current checkout is on Forge; `/home/pchouinard/n8n` on the old VM remains the unchanged production checkout. Home.servers describes infrastructure and is not the application development repository.

Suggested next-thread instruction, when Patrick authorizes development:

> Read docs/migrations/forge-development-handoff.md and the three documents in docs/standards/. Implement CBM-01 in this Forge checkout, using isolated development dependencies. Preserve the production installation and both output contracts. Do not deploy, rotate production secrets, publish corpus releases, or cut over intake.

The handoff does not itself authorize that next ticket. Keep preparation, development, deployment, and cutover distinct.

## Authority and settled decisions

Patrick authorized this phase to preserve the installation, reconcile live/repository differences, and establish the Forge development handoff. No production service restart, workflow import/activation, secret extraction into a new operational store, secret rotation, provisioning of the future application VM, or cutover was performed.

Accepted target:

- Move **processing and retrieval first**; keep Open WebUI on the old VM temporarily and later change only its retrieval endpoint/credential at the authorized cutover.
- Develop in the independent `hopchouinard/RecapFlow-automation` repository on Forge. Keep its identity during migration. `hopchouinard/community-brain-distribution` remains the consumer distribution repository.
- Deploy to a **small Ubuntu VM on PVE1 with Docker Compose**, not LXC. Proposal: 2 vCPU, 4 GiB RAM, 32 GiB system disk plus 64 GiB data disk. Capacity, IP/DNS, storage, OS version, and VM ID need live preflight before provisioning. No address or VM ID has been reserved.
- Use the existing shared PostgreSQL server on `platform-db.patchoutech.lab` (`10.1.10.50`, inventory records PostgreSQL 18). Separate application/environment databases and credentials; proposed names `community_brain_prod` and `community_brain_dev`. No cross-application table access. No database was created.
- Use existing `platform-events.patchoutech.lab` (`10.1.10.54`) NATS/JetStream for durable job delivery. Validate service configuration, authorization, limits, and subjects before use. No streams/consumers were created.
- Store and manage **all migrated application secrets in Infisical**, with scoped identities and runtime delivery. This includes n8n-derived credentials, Fathom/model keys, database credentials, publisher credentials, collector identity, and recovery encryption material. No decrypted credentials belong in Git, transcripts, CI artifacts, logs, job payloads, or browser bundles.
- Authorize a restricted Mac collector callable by Hermes for Zoom chat intake. Its implementation is pending: list/read/upload within the designated Zoom root; no general shell, arbitrary paths, deletion, or symlink escape. Direct upload to the backend avoids routing raw content through an agent prompt. Manual upload remains available.
- Preserve **both outputs**: existing Git/corpus distribution for LanceDB consumers AND an authenticated web interface for preview/copy/download of individual Markdown files used for manual community-board publication. Board auto-posting is not in scope.
- Hermes submits and checks jobs. Durable execution survives Hermes/session restarts. Fathom fetch belongs to the backend; its credential is not needed by the Mac collector.

## Stack and exceptions

The attached standards are preserved byte-for-byte as dated user-supplied references:

- [Backend v0.15](../standards/backend-tech-stack.md)
- [Frontend v0.6](../standards/frontend-tech-stack.md)
- [Hosted services v0.5](../standards/hosted-services-tech-stack.md)

They are considered defaults with justified project exceptions, as Patrick instructed. Do not treat a deferred tooling choice as a new universal standard.

| Area | Project direction |
| --- | --- |
| Internal logic/API | Python + FastAPI. Port working JS transformations with behavior tests; retain the current n8n JS as an oracle during extraction. |
| Relational persistence | PostgreSQL + SQLAlchemy 2 + Alembic + Psycopg 3. No authoritative SQLite job store. Migrations are explicit deployment operations. |
| Jobs | PostgreSQL job/stage records plus transactional outbox; JetStream delivery. Explicit claims, idempotency, heartbeats, bounded retry and terminal failure handling. Start with one corpus writer. |
| UI | React + Vite + TypeScript, Tailwind, shadcn/ui **Base UI** variant, Lucide. No Next.js/hosted platform required. |
| Identity | Authentik/OIDC for people; independently scoped service/agent authorization. |
| Operations | Infisical; Traefik/step-ca; Kuma, Prometheus, Grafana, Alertmanager, Loki; Docker/Compose. |
| Testing | pytest; Vitest/React Testing Library/Playwright when frontend is introduced; real disposable PostgreSQL/JetStream dependencies. |
| Delivery | GitHub Actions for credential-free verification. Trusted internal publishing/deployment obtains internal secrets from Infisical; untrusted PR jobs do not reach the lab. No new CI workflow has been deployed. |
| Retrieval transition | Retain LanceDB 0.34.0 internally for the first cutover as a bounded migration exception. A separate pgvector migration must preserve hybrid retrieval quality before switching internal serving. |
| Consumer distribution | LanceDB remains the supported embedded/offline export. After pgvector migration, build reproducible LanceDB packages from canonical records; no independently edited dual corpora. |

BE-34 does not prevent this extraction: n8n remains a platform integration tool, while this application's durable work is owned by its backend/JetStream.

## Job and output behavior to preserve

API proposals: submit a job, query status, list/download artifacts, explicitly retry an eligible stage, and request a versioned rerun. API routes, error schema, authorization roles, and event schemas are application decisions to specify in CBM-01.

Persist meeting identity, source revision/hashes, job/stage attempts, prompt/model versions, model usage, artifact hashes/paths, corpus versions, and publication receipts in PostgreSQL. Keep immutable input/output files on managed backed-up application storage. Stage complete files atomically before recording ready state; clean up orphan staging files safely after crashes.

Use a transactional outbox so committing a job and publishing work cannot lose an accepted job. JetStream redelivery is not exactly-once business execution: workers must acquire a valid claim and detect completed stages. Acknowledge only after durable outcome recording. Handle long model calls with bounded timeouts/lease renewal and preserve unknown outcomes without blindly repeating publication or model spend. Database/file/queue recovery must reconcile from authoritative job state.

Expose independent states: waiting for input, running stage, artifacts ready, indexing partial/complete, Git publication failed/complete, distribution validated/released. A partial ingest must not be reported as complete. Publishing failures leave the prior valid release intact. Retrying must preserve successful artifacts and avoid silently overwriting the originals.

Preserve filenames and document semantics: `transcript.txt`, `prepared-transcript.md`, `extracted-signal.md` (six canonical sections), `community-post.md`, `community-post-compressed.md`, and the next-Tuesday dated weekly invite. Preserve transcript-only backfill state and failure continuation. Match calls using validated meeting identity/timezone/date, not filenames alone.

Current retrieval uses vector + BM25/RRF, metadata boosts, candidate injection, trust-separated source/derived metadata, and provenance. Preserve source IDs/schema, embeddings/model/dimensions, prompts, speaker/entity registries and consumer index compatibility. Do not re-embed the corpus merely to move hosts. Registry locks are process-local; coordinate lint/ingestion and any future multiple writers. Force re-extraction is a destructive per-session rewrite and requires specific scope.

## Live baseline established 2026-09-09

| Item | Evidence |
| --- | --- |
| Source checkout | `pchouinard@n8n-automation.patchoutech.lab:/home/pchouinard/n8n` |
| Source Git | Clean `feat/chunked-llm-pipeline` at `b6f1aa46996d4ab7ccbbaed567864cc2d71f433a`, matching the remote branch when inspected. Main is older; do not rebase onto old main by discarding this work. |
| VM | 101 on PVE2, 4 vCPU, 10 GiB max / 6 GiB balloon minimum, 512 GiB disk. |
| Containers | n8n 2.36.8, PostgreSQL 17, Community Brain 0.5.0, Open WebUI, dockerproxy. |
| Corpus | Runtime schema 1.1, LanceDB 0.34.0, embedding model nomic-embed-text; 87 sessions observed. |
| Sizes | LanceDB approximately 94 MiB; output 13 MiB; historical 11 MiB; watch 4.1 MiB; WebUI volume 1.1 GiB. Measurements are baseline, not quotas. |
| Code parity | Retrieval container Python source bytes match the VM checkout. |
| Inference | Existing Ollama dependency on Mac `10.1.50.219`; retain during first migration. |
| Inputs | Mac `~/Documents/Zoom/`; manual input flow. No working restricted collector has been installed. |
| Latest call | 2026-09-08 artifacts exist; ingest logged 29 chunks written, 1 failed, while the outer workflow reported success. Do not silently reprocess it during preparation. |
| Trigger state | Workflows 1–6 inactive/manual as applicable; only `openrouterCall` active, with no autonomous trigger. Poller documentation describing an active schedule is stale. |
| Access drift | Live retrieval is LAN-published, and no retrieval API key is configured in its inspected environment; older loopback-only docs are stale. New deployment must explicitly configure access policy. |
| Maintenance | VM daily snapshot 06:00 UTC; weekly artifact auto-commit/push Wednesday 06:30 UTC; daily corpus lint 04:00 UTC. Mac pull/freshness scripts and backup directory exist. |

Seven workflow IDs: 1 legacy Zoom-only summarizer; 2 Fathom poller; 3 list recordings; 4 fetch transcript; 5 weekly merged summarizer; 6 transcript-only backfill; `openrouterCall` shared LLM component.

## Reconciliation disposition

Preservation contains complete live workflow rows and workflow history privately. The Forge diff is field-selective, not a wholesale export:

- Workflow 2: align HTTP defaults/options, boolean partner-file condition, Execute Workflow resource locator/input mapping, and `binaryMode` setting.
- Workflow 5: align aliases HTTP method default, 30-minute ingest timeout/options (remove repo-only retry option), strict boolean prep/signal retry conditions, and `binaryMode` setting.
- Workflow 6: nodes, connections and settings already matched; left intact.
- Workflows 3/4 and shared OpenRouter component: observed differences are credential references; keep repository references intact and resolve future credentials through Infisical. Do not import live binding IDs as portable secrets/configuration.
- Workflow 1 is retired: its model/message/schema differences are preserved in the archive but deliberately not promoted into the new processing baseline.
- Node IDs, UI positions, version counters, pin data, credential references and other runtime metadata are not normalized into source. Production was not re-imported or activated.

## Preservation evidence and boundaries

Private logical archive on source VM:
`/home/pchouinard/migration-preservation/2026-09-09-community-brain/`

Verified second copy on Mac:
`/Users/pchouinard/RecapFlow-backups/migration/2026-09-09-community-brain/`

These directories are mode 0700 and files mode 0600. They contain recovery secrets and private data; they are **not source artifacts** and were not copied into the Forge checkout. Retain under controlled backup access. Recovery copies are not a replacement operational secret authority. Infisical onboarding and removal of obsolete operational copies are pending the later authorized secret-migration phase.

Contents include full `n8n/` workspace including `.git`, ignored files and venv; separate distribution and Patchou-plan workspaces; non-hidden loose home-directory files; a logical PostgreSQL custom dump; all workflow rows/history; Docker configuration/image identifiers; cron definitions; package inventory; LanceDB/config/artifact hashes; and a restorable Open WebUI volume with transactionally backed-up SQLite databases. Personal agent login stores, SSH private keys, and unrelated hidden home directories are not copied by this logical archive; the whole-VM PBS recovery archive covers the full disk. Mac Zoom originals remain on the Mac; previously copied/tracked inputs are in the workspace archive.

No new decrypted n8n credential export was produced. The logical archive necessarily preserves existing private environment/configuration files for recovery. Both SQLite databases (`webui.db`, `vector_db/chroma.sqlite3`) returned `integrity_check=ok`. PostgreSQL `pg_restore --list` could read the logical dump. All 2,693 durable source-file hashes matched before/after workspace archival; GNU tar exited 0. Both logical archive copies passed all 14 SHA256 checks.

Protected PBS archive: `pbs:backup/vm/101/2026-09-09T16:08:13Z`, completed in 74 seconds. Guest-agent enablement was pending, so guest filesystem freeze was skipped; treat this as crash-consistent. The logical DB backups supplement that limitation. No VM restart or configuration application was performed. The protection flag prevents normal pruning of this baseline.

No full restore rehearsal, model-backed run, new corpus publication, or end-to-end consumer installation has been performed. The current archive is a baseline, not the final cutover sync; production may change after capture. Recheck drift and recapture at cutover.

## Forge development setup

Checkout: `/home/t3code/projects/RecapFlow-automation`, owned by `t3code`.
Node 24.21.0 was already available. Installed uv 0.12.11 and managed Python 3.11.15 in the runtime user's home, using the official uv installer. `.venv` belongs to this checkout; never copy or reuse the VM's editable venv.

The old `uv.lock` incorrectly described package 0.1.0 / LanceDB 0.30.2 despite pyproject requiring 0.5.0 / LanceDB >=0.34,<0.35. Reconciled the lock to package 0.5.0 and LanceDB 0.34.0 while retaining the remaining resolution where possible. This is a development baseline correction, not a production upgrade. `uv sync --locked` now validates the project.

Setup after a fresh clone:

```sh
uv sync --project community-brain --locked --python 3.11.15 --extra dev
```

Canonical current baseline:

```sh
./scripts/verify-forge.sh
```

Verification on 2026-09-09: **150 Node tests and 771 Python tests passed**. Python emitted 70 LanceDB FTS deprecation warnings; the deprecated API cleanup is outside this preparation. `git diff --check` passed.

This runs the existing Node workflow behavior tests and Python retrieval/ingestion tests against fixtures/temporary state. Fixed fixture path resolution to honor REPO_ROOT outside the old `/repo` Docker mount. It is not certification of future PostgreSQL/JetStream/UI behavior. The verification script refuses a checkout containing the root or retrieval private `.env` files. No production credentials or live LanceDB copy were placed in this checkout. Tracked historical fixtures/artifacts already distributed through the existing repository are present from Git.

Disposable PostgreSQL/JetStream/Compose infrastructure and frontend tooling are for subsequent development tickets. Do not point tests at the shared production services. The development environment is not the future production VM.

GitHub clone access worked without transferring a token. Authenticated push/release access was not provisioned or tested. This branch is local on Forge until Patrick requests publication; no migration PR has been opened. Provider sign-ins for T3's Codex/Claude were verified earlier in this session, but no agent/model execution was requested for preparation.

## Dependency-ordered implementation backlog

Each ticket is development-only until its separate deployment gate is authorized.

| Ticket | Work | Completion criteria |
| --- | --- | --- |
| CBM-00 | Preservation/reconciliation/Forge handoff | This preparation record, verified archives, reconciled branch, repeatable baseline checks. |
| CBM-01 | Job and artifact contracts; isolated test harness | Define durable states, idempotency/claim/lease semantics, artifact publication ordering, retry/error contracts and recovery. Add real disposable PostgreSQL/JetStream dependencies, canonical verification, and tests for duplicate delivery and crash boundaries; no shared-platform mutations. |
| CBM-02 | Python pipeline extraction | Preserve current chunking, prompts/config, strict structure checks, budget/retry caps and backfill behavior against the JS oracle and representative fixtures. No live model spend by default. |
| CBM-03 | Job API, persistence/outbox and worker | SQLAlchemy/Alembic/Psycopg models, durable acceptance, outbox publication, consumer idempotency, partial-indexing states; restart/timeout/redelivery acceptance. |
| CBM-04 | Fathom acquisition and Mac collector | Mocked Fathom adapter; scoped list/read/upload collector, path/symlink/identity validation, hashes, waiting-for-input behavior, manual upload fallback. Live identity/secret installation is separately gated. |
| CBM-05 | Personal UI and identity integration | React/Vite/Base UI stack; job list/status, artifact previews/downloads, explicit reruns; OIDC and permission tests; no board auto-posting. |
| CBM-06 | Retrieval and both publication paths | Preserve API/consumer semantics, single-writer boundaries, versioned corpus export, checksums, Git receipts and independent statuses; test consumer package install and safe release retries. |
| CBM-07 | Reviewed deployment packet | VM/Compose configuration, shared DB/JetStream resources, Infisical secret inventory/identity bootstrap, OIDC, ingress, observability and DB+files+queue restore procedures; concrete cutover and rollback packet ready for authorization. |
| CBM-08 | Authorized deployment, rehearsal and cutover | Restore on new VM, compare representative calls/queries, drain old work, final sync, one intake owner, Open WebUI endpoint update, both output paths verified; retain old VM through two successful weekly cycles and restore rehearsal. |
| CBM-09 | Separate pgvector transition | Measured hybrid retrieval equivalence, canonical record/provenance mapping, compatible LanceDB export, reversible read-path switch. |
| CBM-10 | Final output-quality review — always last | Address [the explicit quality backlog](cbm-final-quality-backlog.md) after all migration work, including CBM-08 stabilization and CBM-09. Preserve v1 during migration; close each finding with validated evidence or Patrick’s explicit acceptance before declaring the whole migration complete. |

## Boundaries that must survive the handoff

- Production VM and platform services stay unchanged until the appropriate phase is authorized. Preservation did not authorize implementation/deployment implicitly.
- Preserve Git publication and consumer releases, but tests and preparation never push artifacts or releases.
- Infisical becomes the sole operational secret authority; explicitly solve machine bootstrap and historical backup retention. Avoid copying Mac provider tokens or SSH private keys to Forge.
- Production recovery spans PostgreSQL records, files, LanceDB/export versions and queue state. A VM snapshot alone does not recover the future external database. On restore, reconstruct eligible jobs from durable records; do not blindly replay publication messages.
- Keep the old VM's n8n DB/key/data and WebUI state until their retirement scope is explicit. The latest failed ingestion is known baseline debt, not permission to rewrite a session.
- Stack version selection, generated API client, UI routing/state library, Mac collector transport, subject names, hostname/IP, VM ID, machine bootstrap and retention policies remain project decisions, not new global defaults.

## Primary references

Development follow-on (2026-09-09): Patrick separately authorized beginning
CBM-01 with isolated dependencies. See
[CBM-01 contracts and test harness](cbm-01-job-artifact-contracts.md) for the
development decisions, verification setup and limits of the test-only probes.
The preparation evidence above and production gates remain unchanged.

- [n8n Server CLI](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line)
- [n8n encryption key](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key)
- [Fathom meeting listing](https://developers.fathom.ai/api-reference/meetings/list-meetings)
- [Fathom transcript retrieval](https://developers.fathom.ai/api-reference/recordings/get-transcript)
- [JetStream consumer semantics](https://github.com/nats-io/nats.docs/blob/master/nats-concepts/jetstream/consumers.md)
- [Infisical Universal Auth](https://infisical.com/docs/documentation/platform/identities/universal-auth)
- [uv installation](https://docs.astral.sh/uv/getting-started/installation/)
- [uv managed Python](https://docs.astral.sh/uv/guides/install-python/)

## Continued development (2026-09-09)

Patrick subsequently authorized CBM-02 and later development tickets until
intervention is needed. See [development progress](cbm-development-progress.md)
and the [CBM-07 deployment packet](cbm-07-deployment-packet.md). This authorization
does not permit production deployment, cutover, secret migration or publication.
The image build/boot awaits an isolated Docker-capable environment.
