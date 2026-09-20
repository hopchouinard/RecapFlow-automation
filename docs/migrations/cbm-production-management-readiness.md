Current status: monitoring activation and post-migration restore passed. See [the continuation receipt](cbm-production-post-api-management-readiness.md). The commissioning record below predates API startup.

# Production management readiness: Forge can continue API staging

Management configuration is complete for **PVE1 VM109**, `community-brain-prod`,
`10.1.30.21`. The application API and workers are stopped. Only the Alloy log
shipper is running in Docker. Cutover, publication and retirement remain gated.

## Secret delivery and identity

Patrick approved the existing Mac renderer, replacing Enterprise-only Infisical
custom roles and source-IP controls. Infisical remains authoritative in
`homelab/prod /applications/community-brain`. No Infisical login or management
credential was transferred to VM109 or Forge.

On VM109, `/etc/community-brain-production` is root:root 0700. Its 0600 files are:

| File | Contents / intended use |
|---|---|
| `api.env` | Runtime DB URL, public OIDC settings, hashed service identities only |
| `migration.env` | Migration-owner URL under `CB_DATABASE_URL`; explicit Alembic only |
| `worker.env` | Future scoped NATS credentials, processing/publication disabled |
| `probes.env` | Independent raw read/metrics probe tokens and expiry; never API env |

Infisical round-trip, delivered bytes, ownership and permissions passed. The frozen
image accepted exact read/metrics permissions and denied expired identities without
starting the API. **Probe expiry: September 11, 2026, 02:05:38 UTC.** Probe renewal is
explicit: rotate both tokens and `CB_PROBE_EXPIRES_AT` in Infisical, rerender,
refresh the private monitoring credentials and coordinate the API reload. The
hourly maintenance job does not extend probe lifetimes or restart the application.

Public OIDC settings:

- Issuer: `https://auth.patchoutech.lab/application/o/community-brain/`
- Client ID/audience: `community-brain`
- JWKS: `https://auth.patchoutech.lab/application/o/community-brain/jwks/`
- Callback: `https://community-brain.patchoutech.lab/callback`
- Origin/logout: `https://community-brain.patchoutech.lab`
- Public code-flow client; SPA must use PKCE S256.
- Group: `community-brain-operators`, Patrick only initially.
- Scope `community-brain`; `jobs:read`, `artifacts:read`, `retrieval:read` only.

Membership/claim preview and nonmember denial passed. Real browser login remains
an application acceptance check after startup.

## Database and recovery

`community_brain_prod` on `platform-db.patchoutech.lab:5432` uses owner/login
`cbm_prod_migration` and restricted runtime login `cbm_prod_runtime`. TLS
`verify-full`, DML/sequence defaults and denied DDL/cross-application/plaintext
checks passed. Access is restricted to VM109. No migration has been run.

Native `community-brain-db-backup.timer` runs daily at **00:30 UTC**, retaining
14 private custom-format dumps under `/var/backups/community-brain` on platform-db.
A disposable restore of the current dump passed, then its test database was removed.
This database has no application tables yet; repeat restore acceptance after migration.

The Mac copies the latest dump hourly, verifies SHA-256 and retains 14 copies in
VM109 `/srv/community-brain/db-backups`. Clean handoff PBS snapshot:
`pbs:backup/vm/109/2026-09-10T02:29:04Z`. It includes the verified dump copy.
Existing nightly VM109 PBS scheduling remains 21:00 America/Toronto, with seven
last, four weekly and three monthly snapshots retained.

Recovery uses daily logical restore points, **not PITR** (`archive_mode=off`).
Mac outages delay off-host copies. A full PBS guest restore was not performed in
this phase; the scoped PostgreSQL dump restore was performed.

## Network and certificates

`community-brain.patchoutech.lab` resolves to Traefik `10.1.10.100`.
The private HTTPS route targets VM109 port8090. Docker forwarding and UFW allow
that port only from Traefik. The observed backend source was `10.1.10.100`.

A disposable backend returned HTTPS200 with verified lab trust; direct Mac and
Forge connections timed out. An unapproved source (`10.1.10.52`) received HTTPS403.
The probe was removed. HTTP502 is expected while the application is stopped.
The router permits only Mac `.50.219`, Forge `.10.60`, Kuma `.10.56` and monitoring
`.10.30`; request access logs are disabled. No public Internet ingress was added.

After migration/corpus readiness, Forge must set **`CB_API_BIND=10.1.30.21`** in
its standalone production staging invocation; the default loopback bind cannot
receive Traefik traffic. Supply the reviewed immutable `CB_IMAGE` separately.

Application leaf/key are authoritative in Infisical and delivered privately under
Traefik `/mnt/HDD_2TB_Main/traefik/dynamic/community-brain-private`. Dynamic TLS and
route files are separate `community-brain-tls.yml` and `community-brain-production.yml`.
Leaves last24h and are renewed when less than12h remain, without a Traefik restart.

## Queue and Mac maintenance

Dedicated NATS account/stream `COMMUNITY_BRAIN_PROD`, durable
`community-brain-worker`, subject `cbm.prod.jobs.stage.ready.v1`; one stream and
consumer, 64MiB file quota. Scoped TLS publish/pull/ACK and unrelated-subject denial
passed again. Test messages were removed. No application worker connected.

The separate TLS endpoint `tls://platform-events.patchoutech.lab:4223` is active
and source-restricted to VM109. Existing clients/listener were unchanged. Future
worker clients need **`tls_handshake_first=True`** and inbox prefix
**`_INBOX.cbm_prod_worker`**. The staging API does not use the queue.

Mac LaunchAgent `lab.patchoutech.community-brain-management` runs hourly from
`/Users/pchouinard/.local/lib/community-brain-management`. It renews/delivers the
NATS and application leaves and copies the latest database dump. All three tasks
passed under launchd. Public status:
`/Users/pchouinard/.local/state/community-brain-management/maintenance-status.json`.
It uses the existing operator bootstrap file in its existing location, not a copy.
The Mac user session, source volume and management network must be available.

## Monitoring and remaining application checks

VM109 node exporter is restricted to monitoring-stack `10.1.10.30`. Prometheus
reports it UP; disk-below15% (10m) and host-down (5m) alert rules are healthy.
API metrics credentials are separate and private on monitoring-stack; its
file-discovery target list is empty until activation.

Kuma monitors30 (health) and31 (authenticated retrieval query) are configured with
TLS verification and paused. After Forge starts and verifies the API, the Mac can
run `CB_ACTIVATE_MONITORING=1` with `integrations/run.sh provision-kuma.py`.
It first requires successful health, authenticated metrics and retrieval checks,
then resumes those monitors and enables the prepared Prometheus API target.
No additional infrastructure permissions need to be given to Forge.

Alloy ships only fixed lifecycle messages from this Compose project to existing
Loki. This intentionally narrower logging configuration prevents arbitrary request
bodies, tokens and application content from being shipped. Live test: 58 lifecycle
lines observed, zero synthetic private-sentinel lines. The test container was removed.
Access logs are disabled in Traefik and the supplied uvicorn command.

Forge's next steps remain explicit Alembic, real-object privilege verification,
verified approved corpus/config installation, standalone API startup, browser
login and retrieval comparison. Then activate the prepared monitors from the Mac
and repeat DB restore acceptance with application data. Those application-dependent
checks are not claimed as passed by this management receipt.

## Rollback boundaries

Stop only the Community Brain staging API/Alloy if needed. Remove only the two
Community Brain Traefik dynamic YAML files to withdraw its route/certificate;
remove its new DNS policy by exact name. The pre-proxy guest firewall script is
`/usr/local/sbin/cbm-docker-ingress.before-proxy` (restore and remove the exact
8090 allow rule if withdrawing ingress). Existing SSH rules remain required.
Prometheus pre-change config is `prometheus.yml.before-community-brain`; preserve
later unrelated changes when removing the two new jobs and its dedicated rule file.
Pause Kuma30/31. Disable the scoped DB backup timer and Mac LaunchAgent only if
retiring these additions. Do not delete the database, Infisical authority or PBS
backups as part of routine rollback. Existing shared NATS backup/config is documented
in the prior account receipt; withdraw only this account/sidecar if necessary.

Companion: `cbm-production-integrations-readiness.json`.
