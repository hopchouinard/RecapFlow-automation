# Production API staging — ready for Mac monitoring preflight

September 10, 2026. Applied the updated management handoff and companion
`cbm-production-integrations-readiness.json`. The older guest-only JSON remains
historical. **The staging API is healthy; workers are stopped.** Cutover,
publication and retirement remain gated.

## Completed application checks

- Ran explicit Alembic `upgrade head` with only the migration identity from
  `/etc/community-brain-production/migration.env`. Revision `0001_jobs` created
  nine application tables plus `alembic_version` in `community_brain_prod`.
- Verified the runtime role over verified TLS: all tables belong to the separate
  migration owner; DML privileges present; transactional insert/update/delete
  succeeded and rolled back; schema/database CREATE and real-table ALTER denied.
  Repeated after API checks: jobs and other application records remain empty.
- Installed the approved candidate (1,901 successful rows, 87 sessions, schema
  1.1, 768 dimensions, nomic-embed-text provenance) into `/srv/community-brain/corpus`.
  Validated pinned archive, manifest, exclusion provenance and every file hash.
  All 13 preserved configuration files matched their normalized source manifest.
  Full-text coverage is **1,901 indexed / 0 unindexed rows**.
- Started only the standalone staging API, bound to `10.1.30.21:8090` behind the
  management-configured Traefik source restriction. Uses immutable image
  `community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449`.
  The API receives only its scoped runtime bundle; all state bind mounts are
  read-only. Provider, queue and publishing credentials are absent. Model and
  remote publication flags are false. Existing Alloy remains running.
- Authenticated retrieval matched the development full-index control: four
  questions, all 20 top-five positions identical, with vector/BM25 contributions,
  date filters and provenance. Empty-date result, missing-auth denial, hidden
  ingestion routes and legacy X-API-Key read transport passed. Only existing
  Ollama query embeddings were used; no generation, extraction or re-embedding.
- API read identity, empty jobs list, SPA/callback and public OIDC settings passed.
  Job submission and metrics access with the read token were denied; independent
  metrics access succeeded and that identity was denied jobs access.
- From Forge, lab-trusted HTTPS `/health` returned 200 and unauthenticated jobs
  returned 401 through Traefik. Forge's default system trust lacked the lab CA;
  used the public CA bundle delivered on VM109, fetched through verified SSH.
  TLS verification was never disabled. Authenticated checks ran on the guest;
  Mac activation must perform its own end-to-end HTTPS authenticated probes.
- After queries, every installed corpus/config hash still matched and immutable
  files storage remained empty. No legacy job history was fabricated.

The first offline corpus check used root with all capabilities dropped and could
not read UID10001's private files. Reran as the image's normal UID10001, supplying
the public manifest in memory; all checks passed. Application permissions were
not widened. Deployment tests: 11 passed. New operational helpers passed Ruff and
`git diff --check`. The previously verified application image was not modified.

## Mac management continuation

The API is ready for the prepared monitoring activation preflight. From the
existing Mac management environment, run **`CB_ACTIVATE_MONITORING=1` with
`integrations/run.sh provision-kuma.py`**, as documented in the management
receipt. Its successful health, authenticated metrics and retrieval checks must
precede resuming Kuma monitors 30/31 and enabling the Prometheus API target.
Return those results and subsequent UP status. No new authorization is needed
for this documented integration step.

Repeat the scoped database backup and disposable restore now that all application
tables and the Alembic revision exist. Verify all ten table definitions, ownership,
revision and empty job counts; preserve the target DB. Copy the new dump through
the existing verified off-host procedure. Current restore evidence covers only
the pre-migration empty schema, not these application objects. Recovery remains
daily logical restore points, not PITR.

Patrick confirmed the **real production browser login passed** on September 10:
Authentik completed without an authorization error and the recap workspace loaded
with an empty jobs list, as expected. This is user-confirmed acceptance; Forge
did not obtain browser credentials or session tokens. Monitoring activation and
post-migration restore still await management receipts.

Probe identities expire **September 11 at 02:05:38 UTC**. Existing management
instructions require explicit Infisical rotation/rerender and coordinated API
reload before expiry if staging continues; hourly certificate renewal does not
renew these identities.

## Evidence and operation paths

- Helpers and standalone Compose on VM109:
  `/srv/community-brain/workspaces/staging/`.
- Root-private operation logs: `production-staging/{migrate,dbcheck,up,check}.log`
  under that workspace. Never publish raw runtime files or resolved Compose config.
- Private original candidate/config inputs, installation receipt, corpus check
  and API receipt: `/srv/community-brain/artifacts/cbm-staging-inputs/`.
- Repository companion: `cbm-production-api-readiness.json`.
- Source helpers: `deploy/community-brain/production-staging/`; frozen image/source
  evidence remains in `cbm-production-image-readiness.md`.

No current intake, Mac production sync, n8n workflow, Open WebUI endpoint or old
production corpus was changed. The worker's TLS-first/scoped-inbox integration
remains necessary before any later worker activation. CBM-10 and its explicit
Q-01 through Q-05 findings remain the final step of the whole migration.

## Subsequent acceptance — management continuation complete

The [post-API management receipt](cbm-production-post-api-management-readiness.md)
closes monitoring activation and migrated-schema restore checks. Kuma 30/31 and
both API/node Prometheus targets were UP. The actual ten-table schema, grants,
owners, revision and row counts matched a disposable restore. Forge independently
verified the off-host dump SHA-256 on VM109. The API remains healthy and only API
and Alloy are running. Earlier pending wording above describes the prior handoff.

The tested API staging acceptance is complete, including Patrick's real login.
Nonempty production job recovery and full PBS guest restore are not claimed.
The [bounded worker phase proposal](cbm-production-worker-phase-proposal.md) is
prepared for Patrick's decision; no worker or provider activation is authorized
by these receipts. Probe expiry remains September 11 at 02:05:38 UTC.
