# CBM-07 deployment review packet

Current readiness and the approved provisioning/staging boundary are recorded in
[the September 10 production phase gate](cbm-production-phase-gate.md). Live
development/provider/collector and preserved-data rehearsals now have evidence;
Patrick approved provisioning and staged deployment on September 10. The newer
gate supersedes the historical preparation restrictions below for that scope;
cutover, remote publication and retirement remain gated.

Date: 2026-09-09. Scope: development preparation only. **Do not execute the
production steps below until Patrick authorizes CBM-08 and supplies/approves the
preflight decisions.** This packet does not authorize secrets onboarding, VM
provisioning, production database/JetStream mutations, corpus publication, or intake cutover.

Source: Forge branch `migration/community-brain-forge-handoff`; application
repository remains `hopchouinard/RecapFlow-automation`. Consumer distribution
remains `hopchouinard/community-brain-distribution`. The root n8n Compose and
workflows remain the preserved production installation. Candidate files are
isolated under `deploy/community-brain/`.

## Deployment inputs requiring preflight

| Input | Candidate / required decision |
| --- | --- |
| VM | Small Ubuntu VM on PVE1; 2 vCPU, 4 GiB RAM, 32 GiB OS + 64 GiB state proposed. Confirm capacity, VM ID, OS release, storage placement, backup policy; no reservation exists. |
| Network | Confirm IP, DNS, ingress owner/network path and step-ca issuance. API defaults to loopback; change `CB_API_BIND` only with an explicit reverse-proxy/firewall plan. |
| Database | Shared platform-db, PostgreSQL 18. Create separate `community_brain_prod` and `community_brain_dev` databases/roles. No shared tables, no superuser runtime, no access to other apps. Confirm TLS CA, backup/PITR and connection limits. |
| Events | Shared platform-events JetStream. Validate account ACLs, file storage, server version, replicas supported, quota and max-message policy before applying the example stream/consumer JSON. One replica is a proposal, not an HA claim. |
| Identity | Authentik issuer, audience, JWKS URL, public SPA client ID, exact HTTPS origin and `/callback` redirect. Configure `cb_scope=community-brain` and explicit `cb_permissions`; no wildcard claims. |
| Inference | Confirm retained Ollama endpoint/model availability. OpenRouter model slugs, ceilings and prompt versions preserve the extracted baseline; verify availability before enabling any paid rehearsal. |
| Publishing | Confirm artifact Git repository/branch identity, constrained push identity and a pinned 40-character distribution source commit. Confirm GitHub release naming compatibility with the actual consumer checkout. |
| Collector | Install on the Mac only after scoped identity delivery is authorized. Root is fixed to `~/Documents/Zoom`; set fixed HTTPS backend. Hermes gets the restricted entrypoint, not general shell or Fathom credentials. |

The deployment image is specified by a dedicated Dockerfile and Compose file.
The image was built and booted on the authorized development VM 108; see
[standalone rehearsal evidence](cbm-development-rehearsal.md). The disposable
API/database/JetStream checks passed. The [simulated worker/retrieval/restore rehearsal](cbm-development-scenario-results.md)
also passed on disposable development state. Live identities/providers and a
production-representative restore remain required before production cutover.

## Secret inventory and bootstrap

Infisical is the sole migrated operational authority. Create separate prod/dev
paths, for example `/applications/community-brain`, and independently scoped
machine identities. Deliver these runtime values without committing an `.env`:

| Consumer | Secret/material |
| --- | --- |
| API | PostgreSQL runtime URL; service identity hash/permission map; TLS trust material if private CA is not in the image trust store |
| Worker | PostgreSQL URL; JetStream URL/identity; OpenRouter and Fathom keys; publishing identity when enabled |
| Git publisher | Restricted Git SSH key or installation credential via an Infisical-delivered credential helper; never put a token in remote URLs or process arguments |
| GitHub release publisher | Short-lived scoped token for distribution repo contents; no workflow administration permission |
| Mac collector | Separate opaque `sources:upload:chat` token, fixed backend URL; no Fathom/model/DB credentials |
| Hermes | Separate `jobs:submit`, `jobs:read` token; grant artifact reads only if needed |
| Open WebUI | Separate `retrieval:read` token and new retrieval base URL at cutover |
| Monitoring | Separate `metrics:read` service token scoped to this application |
| Recovery | Existing n8n encryption material and any backup encryption keys under restricted recovery access; never rotate n8n encryption keys during migration |

Machine bootstrap requires an operator-established root of trust. Use Infisical
Universal Auth with an application-scoped identity, short TTL, source-IP limits
and only the required path/environment permissions. Keep the bootstrap secret in
a root-owned mode-0600 host credential location (or the approved host credential
facility), not Git or the Compose project. Deliver process environment through
the approved Infisical runtime integration. Do not echo, log or persist the
returned secret bundle. The Compose candidate requires explicit values and has
no private `env_file` fallback. `CB_SERVICE_IDENTITIES` contains token SHA-256,
subject, scope, permissions and required future `expires_at` (Unix seconds); plaintext consumer tokens live only in Infisical
and their scoped consuming process. Plan rotation by overlapping old/new hashes
temporarily, then revoke old identities after verification.

The API validates the configured application scope for all users, including
retrieval: a single corpus serves one access scope. It is not a multi-tenant
corpus. The API mounts the preserved retrieval implementation in its existing
read-only distribution mode; ingestion/reindex routes are not exposed there.
The worker alone writes the corpus and registries. Lint/maintenance must acquire
the same `writer.lock` in the managed corpus root. Do not transfer the old VM's
cron entries unchanged or run two writer owners during migration.

## Reviewed operation order for the later authorized phase

1. Record source branch/commit and rerun the canonical credential-free verification.
   Build the dedicated image, record its immutable image digest, inspect the build
   context and confirm no private input/state/secrets are included. Boot it with
   disposable PostgreSQL/JetStream and fixture data before provisioning production.
2. Provision the approved VM and managed state disk. Create `/srv/community-brain`
   subdirectories `files`, `corpus`, `config` owned by container UID/GID 10001,
   mode 0700 where private. Set quotas/alerts before copying data.
3. Have the platform operator create the approved application databases and scoped
   JetStream account/stream/consumer using the reviewed example files. Runtime DB
   role gets DML/sequence use, not DDL; a separate migration role owns the schema.
   Consumer permissions include only its subject, the scoped JetStream API calls,
   ACK subjects and reply inboxes required by the Python client. Verify denied
   cross-application DB/subject access with the final identities.
4. Bootstrap Infisical identities and Authentik mappings. Configure public client
   code flow with PKCE, HTTPS exact redirects, no client secret in the browser,
   and no wildcard redirect URI. Confirm invalid issuer/audience/expired tokens
   and cross-scope service tokens are denied in the deployed image.
5. With the migration role and reviewed target URL, explicitly run
   `alembic -c /app/community-brain/alembic.ini upgrade head` in the new image.
   Application startup never applies migrations. Validate schema and DML role
   privileges, then remove migration privileges from runtime.
6. Restore preserved config/registries/LanceDB and artifacts to a rehearsal copy.
   Preserve LanceDB 0.34.0, schema 1.1, nomic-embed-text/768 dimensions and source
   IDs. Do not re-embed. Keep original n8n DB/key/data and WebUI untouched.
   Old artifacts are preservation inputs; importing legacy job/provenance records
   requires a reviewed mapping, not synthesized successful attempts.
7. Start API only, model/publication flags false. Verify `/health`, authenticated
   `/retrieval/query`, session counts, representative ranking/provenance and UI
   login/download/copy behavior. Configure Traefik/step-ca, firewall, Kuma,
   Prometheus/Grafana/Alertmanager and Loki without logging request bodies/tokens.
8. In an isolated rehearsal environment, authorize a bounded model budget and
   enable the worker with test identities. Run one weekly and one historical
   meeting, test waiting inputs, restart during model work, duplicate delivery,
   partial indexing and failed publication. Unknown effects require explicit
   reconciliation, not automatic retries. Compare results with preserved artifacts.
9. Test both outputs: Git candidate receipt and compatible LanceDB package on a
   fresh consumer installation, plus authenticated UI preview/copy/download of each
   file. Network publishing remains false until its destination/scope is authorized.
10. Stop new intake, drain known work, capture a final source drift/hash inventory
    and consistent backup, and approve any differences from the 2026-09-09 archive.
    Choose exactly one intake owner. Change the Mac collector/Hermes target and
    Open WebUI retrieval URL/credential only after this explicit cutover checkpoint.
11. Monitor two successful weekly cycles and complete restore rehearsal before
    proposing retirement of any old VM service, secret or backup. Retirement and
    CBM-09 pgvector transition remain separate decisions.

## Restore, recovery and rollback

Recovery spans external PostgreSQL, managed immutable files, corpus/registry
versions, export candidates and queue delivery state. Back up the DB with the
platform's approved consistent dump/PITR procedure and snapshot/copy application
files under the corpus writer lock. Record one recovery manifest with DB backup
identity/time, source/artifact hashes, corpus/export versions and published
receipts. Never assume the application VM snapshot includes the shared DB.

Restore into isolated prod-equivalent dependencies first. Apply the reviewed
schema version, restore files and verify every referenced hash, then restore the
matching corpus/config snapshot. Verify the consumer package independently.
Restore with model/publication flags false. Reconcile external receipts and
unresolved model intents; the recovery sweep marks expired unresolved effects
`outcome_unknown`, and reconstructs eligible delivery from PostgreSQL. After
queue loss, sent but still eligible stages are redispatched after a five-minute
grace period. Broker MaxDeliver is not the application's retry counter. Restore
never blindly replays publication events or treats missing artifacts as ready.

Keep backups and orphan private files until the retention policy is approved.
The application deliberately has no destructive orphan purge command yet:
unreferenced staging/response files may contain unknown-effect evidence. A later
cleanup operation must enumerate closed/unreferenced candidates, apply the
24-hour grace, quarantine under the job lock and preserve unresolved evidence.
Do not substitute a broad filesystem cleanup for this protocol.

If rehearsal/cutover acceptance fails: disable new intake, stop the new worker,
preserve DB/files/receipts for diagnosis, and restore the old Open WebUI endpoint
and previous intake owner. Keep the last valid consumer release. Do not roll back
a database schema under a running worker or push a force rewrite to repair Git.
If new jobs ran after cutover, reconcile them individually before resuming the
old pipeline to avoid duplicate model spend and posts. No encryption-key changes.

## Observability acceptance

Kuma probes `/health`; it checks database/schema reachability. A separate
authenticated retrieval probe validates corpus availability. Prometheus scrapes
`/metrics` with its scoped identity: stage/state gauges show stuck/unknown/failed
work. Alert on unknown outcomes, failed/partial indexing, queue backlog,
lease/recovery churn, disk capacity, publication failure, backup age and restore
test age. Configure NATS advisories for MaxDeliver. Log identifiers and sanitized
error codes only; model requests/responses remain private hashed files. Configure
central log retention explicitly before enabling Loki shipping.

This packet still requires the production preflight values, broader rehearsal evidence,
approved model rehearsal budget, backup retention/bootstrap policy and final
cutover authorization. No such production operations have been performed.

## Final migration quality review

Keep [CBM-10's explicit quality backlog](cbm-final-quality-backlog.md) as the last
step after all migration work and stabilization. Patrick deferred semantic prompt
improvements until that step; the migration preserves v1 parity. Deployment or
cutover success alone does not close the whole migration or its quality findings.
