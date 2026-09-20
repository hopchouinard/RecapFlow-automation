# Manual production operations after request006

Request: CBM-MANUAL-RECOVERY-20260910-006. This is the current operating recipe;
the commissioning notes in integrations/README.md describe earlier states.

## API recreation and credential ownership

Use the existing Mac Infisical renderer with `manual_api_runtime.py`. Its deployed
copy is under `/Users/pchouinard/.local/lib/community-brain-management/platform-services/community-brain-prod/integrations/`.
Invoke its existing `run.sh manual_api_runtime.py` with the already configured
`INFISICAL_ENV_FILE`; no new bootstrap login is copied anywhere. The helper reads
fresh authority, renders only the API DB URL, public OIDC settings and identity
hash map, verifies all14 public assets, and invokes:

`sudo python3 /srv/community-brain/workspaces/manual-20260910/production-staging/manual_host.py api-up`

This combines compose.production-staging.yml and compose.production-manual.yml.
The old staging `run.py up` rejects the collector/operator write scopes and is no
longer the recreation recipe. Never copy the historical `api.env.pending` over
live configuration. Preserve both manual-20260910 API and manual-20260910-v2
selected-worker packets. No scheduled API recreation was added.

Required outcome: image be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449,
five final service identities,13 cue rules, files writable, corpus/config
read-only, no queue/provider/Fathom credentials in API, model/publication flags
false. Verify health, CA/TLS, allowed/denied scopes, monitoring and the actual
cached Open WebUI filter after a recreation. Two controlled recreations passed
during the overlap-protected probe rotation in this request.

Infisical remains authoritative. Probe tokens now expire **2026-09-17 06:22:56 UTC**.
Mac management owns explicit rotation and consumer delivery, not Forge or VM109.
Renew with old/new hashed grant overlap, verify both keys, atomically replace the
Prometheus token file and update only Kuma31's Authorization header through its
live API, then remove old hashes and verify old-token401 and cross-scope403.
The request006 scripts/journal are one-time records, not blindly rerunnable jobs.
No automatic token extension was added. WebUI and collector/operator tokens keep
their independent September17 expiries and require their own coordinated renewal.

Kuma30/31 remain active. Prometheus reads its existing private metrics-token file.
The hourly Mac job still handles application/NATS certificate renewal, dump copy,
and the existing conservative Mac rollback-resume hook. Latest health must be
checked from its maintenance-status.json, not inferred from installation.

## Recovery ownership and coverage

platform-db owns the native daily00:30UTC logical dump,14-copy retention. Mac
management owns off-host copying and paired DB/files/runtime verification. PVE1
owns the existing nightly21:00 America/Toronto VM109 PBS job (7last/4weekly/3monthly).
The current explicit paired set is recorded in paired-recovery-manifest.json and
off-host-copy.json, with PBS checkpoint vm/109/2026-09-10T06:28:34Z.

Restore into a disposable database with PUBLIC CONNECT revoked and connection
limit0; use management access only. No worker, provider key, queue or publication
handler enters the restore. Restore archives into a new private directory, reject
unsafe members, compare all tables/schema/owners/grants and every reference/hash.
The canonical index check runs in a network-disabled read-only container. Remove
only the disposable resources after evidence capture. Never restore on top of
production or broadly replay the three inert indexing outbox events.

This was a quiescent, before/after verified logical pairing, not a simultaneous
cross-host snapshot, PITR or full PBS guest restore. The42-file runtime archive
captures the pre-renewal runtime/approval state. Later API recreations change
their own logs/cache; the archived executable packets remain preserved. Secret
configuration is rendered from current Infisical authority on recovery. Preserve
manual `.started` markers and reconcile durable outcomes before any execution.

## Remaining maintenance gaps

- The hourly Mac copy's observed :25 phase can precede the00:30UTC DB dump and
  miss the01:00UTC (21:00EDT) PBS run. A later approved maintenance change should
  establish a verified dump→copy→PBS dependency or a bounded pre-PBS copy with
  freshness failure reporting. Mac availability remains a dependency. Today's
  checkpoint used an explicit verified copy before PBS and has no such gap.
- Routine dumps plus guest backups do not automatically create a quiescent paired
  DB/files/corpus/config/runtime checkpoint after each manual job. Mac management
  should perform the tested pairing after accepted manual changes until a reviewed
  orchestration recipe is installed. No corpus-mutating schedule is enabled here.
- Probe/WebUI/collector/operator renewal is explicit, with no expiry extension
  hidden in certificate maintenance. Schedule management attention before the
  earliest relevant expiry. No model-key top-up/reset is implied.
- The Mac Folder Action lookup can fail while System Events is cold. Read-only
  enumeration reliably exposes the exact saved path. The current hook fails
  closed; any future superseding hook should enumerate then match the exact path,
  never enable associations globally or guess from a display name.
- Manual recap integrity passed; semantic quality acceptance, live indexing of an
  eligible session, two weekly cycles and final migration quality work remain
  separate. The September8 canonical session is protected from replacement.
