# Monitoring active; post-migration restore verified

Mac management completed the continuation requested in Forge's
`cbm-production-api-readiness.md` on September 10, 2026.

- Mac end-to-end HTTPS health, independently authenticated metrics, and
  authenticated retrieval returned200 with lab TLS verification enabled.
- Kuma30 (health) and31 (authenticated retrieval) are active and UP.
- Prometheus `community-brain-prod-api` and `community-brain-prod-node` are UP.
  The host resolver had selected public DNS and could not resolve the lab name.
  Only the Prometheus Compose service was changed to DNS `10.1.10.1` and briefly
  recreated. Backup: `/opt/monitoring-stack/docker-compose.yml.before-cbm-dns`.
  No host-wide DNS or other service setting changed.
- New dump `/var/backups/community-brain/20260910T024826Z.dump` restored into a
  disposable database. All ten public table definitions, grants, owners,
  revision `0001_jobs`, and row counts matched production. Every table belongs
  to `cbm_prod_migration`; Alembic has one row and the nine application tables
  have zero rows. The source schema/counts remained unchanged; the disposable
  database was removed. No artificial jobs or test rows were inserted.
- Verified off-host copy:
  `/srv/community-brain/db-backups/20260910T024826Z.dump`, 45,680 bytes.
  SHA-256: `24c9ee9cd8e05b416bdb24a5c42549ff1cb774418349f1b4638253150f495bc2`.
- Completed PBS snapshot containing that copy:
  `pbs:backup/vm/109/2026-09-10T02:51:58Z`.

Recovery remains daily logical restore points, not PITR. This restores the actual
migrated empty jobs database; it does not claim testing a nonempty production job
history or a full PBS guest restore.

API and Alloy are running; no worker is running. No cutover, remote publication,
retirement, workflow changes or old-platform changes were performed. The probes
used existing Ollama query embeddings only; no generation or historical processing.

Probe credentials still expire **September 11, 2026, 02:05:38 UTC**. Explicit
Infisical rotation/rerender, coordinated API reload and monitoring credential
refresh are required before expiry if staging continues. Hourly Mac certificate
renewal does not extend service-probe credentials.

Public receipts returned to Forge:

- `cbm-production-monitoring-activation-receipt.json`
- `cbm-production-post-migration-restore-receipt.json`
- `cbm-production-backup-copy-receipt.json`
- Updated `cbm-production-integrations-readiness.json`

The first Kuma activation attempt returned a suppressed error; retry completed
successfully and live statuses were verified. Provisioning errors now report only
the failed API operation, never response payloads or secrets.
