# Development image boot rehearsal

The next implementation step is building and booting the packaged application on
the separate development VM described in `cbm-development-vm-proposal.md`.
The user's instruction to proceed covers continued development; production
deployment/cutover remain excluded. Forge's broker provides GET-only inspection,
not provisioning or guest execution. No attempt was made to widen its access.

## Development host

[VM handoff](cbm-development-vm-handoff.md) supersedes the earlier provisioning
prerequisites. VM 108 on PVE1 is ready; `ssh community-brain-dev` connects as
`cbmdev`. Development deployments are authorized. Production remains excluded.
Canonical source stays on Forge. The rehearsal used an allowlisted 85-file build
context under `/srv/dev-data/workspaces/cbm-rehearsal-20260909`, excluding private
runtime state, environment files, SSH keys, credentials, caches and real corpus.

## Run on the development VM

Transfer the reviewed application source to a separate guest checkout, excluding
private runtime data, `.env`, build caches and credentials. Current changes are
local on Forge, so cloning the remote branch alone does not deliver them.
The dedicated Dockerfile ignore file restricts the image build context.

From that checkout, run each command separately:

```sh
docker compose --env-file /dev/null -f deploy/community-brain/compose.rehearsal.yml config --quiet
docker compose --env-file /dev/null -f deploy/community-brain/compose.rehearsal.yml build api
docker compose --env-file /dev/null -f deploy/community-brain/compose.rehearsal.yml up -d --wait --wait-timeout 180 api nats
docker compose --env-file /dev/null -f deploy/community-brain/compose.rehearsal.yml run --rm smoke
docker image inspect community-brain:rehearsal --format '{{.Id}}'
docker compose --env-file /dev/null -f deploy/community-brain/compose.rehearsal.yml ps -a
```

Image pulls/builds require outbound access on the development host. Running
services use an internal Compose network, disposable project volumes, no host
ports, and fixed fixture-only credentials. The API serves the actual built SPA;
the fixture OIDC issuer intentionally cannot authenticate a browser user.
The smoke service uses a scoped read-only fixture identity against the actual
authentication implementation. No auth bypass is added to production code.

The migration is an explicit one-shot service; API startup waits for it. Checks
cover schema health, unauthenticated denial, scoped identity, an empty job list,
SPA/callback assets, and a JetStream publish/read round trip. This is the first
image boot check, not a full worker, retrieval, OIDC or restore rehearsal.

Record image ID, checks, service logs on failure and peak host resource use. Do
not treat the mutable local `rehearsal` tag as a production image identity.
After recording results, remove only this disposable project and its test data:

```sh
docker compose --env-file /dev/null -f deploy/community-brain/compose.rehearsal.yml down --volumes
```

## Completed rehearsal — 2026-09-09

**PASS on the actual development VM:** image build, explicit Alembic migration,
API/database health, unauthenticated HTTP 401, scoped authenticated identity/job
reads, built SPA and callback assets, and JetStream publish/read round trip.
A second migration invocation also exited zero. No model or publication calls.

Tested image ID:
`sha256:79e97792d7bdf98587f4ac34bcea5e1c3b6e154931141ba0aacc59aea2b725f8`.
Docker reports image size 250,755,652 bytes; runtime Python is 3.11.16.
PostgreSQL 18.6 and NATS 2.10.27 were the disposable dependencies.

Actual execution found and fixed three packaging defects:

1. The proposed Node patch-version image tag did not exist. Node 24 and Python
   3.11 base images now use registry-verified immutable manifest digests.
2. Root-owned mode-0600 migration files were unreadable by runtime UID 10001.
   The Dockerfile now copies application sources/migrations with runtime ownership.
3. Tokenizer initialization attempted an external download during API startup.
   The build now populates a readable `cl100k_base` cache in the image, permitting
   startup on the internal network with a read-only container filesystem.

Four local deployment configuration/isolation tests passed. The actual image boot
and smoke checks validate the fixes beyond configuration-only tests.

Post-test Docker memory snapshot: API 158.3 MiB, PostgreSQL 34.52 MiB, NATS
3.742 MiB. These are steady-state observations, not peak sizing measurements.
Five-second vmstat samples during builds/rehearsal observed up to 95% CPU busy
and zero swap use; filesystem caches make free RAM alone an unreliable peak
application-memory measure. No running service reported OOMKilled.
Keep one build/rehearsal at a time on the 2-vCPU/4-GiB VM.

All services had empty host port bindings. After recording logs, the disposable
project containers, network and database/JetStream volumes were removed. A final
project-filtered Docker listing returned no containers. The image, build cache,
allowlisted source and evidence remain on the development disk for reuse/review.

Evidence directory on the VM:
`/srv/dev-data/artifacts/cbm-rehearsal-20260909/`, including final build/boot/smoke
logs, service logs, resource samples and `final-context.tar.gz`. The initial
`context.tar.gz` predates the packaging fixes; the final archive captures them.

This completes the requested standalone boot rehearsal. Full processing-worker,
retrieval, live OIDC and coordinated restore rehearsals remain separate work;
this result does not authorize or establish readiness for production cutover.

References: [Compose startup ordering](https://docs.docker.com/compose/how-tos/startup-order/),
[internal networks](https://docs.docker.com/reference/compose-file/networks/),
[PostgreSQL image storage layout](https://hub.docker.com/_/postgres).
