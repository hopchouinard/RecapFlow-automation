# Actual production mapping ledger

`helper-mappings.json` is the closed nine-helper contract; `verify_mapping.py` verifies the deployed source and embedded receipt bytes independently of Forge's shape checker. Each helper has its installed deadline below. The complete scheduler cycle retains the same mutex and journal as manual and capture. The Mac guard also rechecks retained legacy pending state and the retired Request032 journal. Unknown cycles block every kind; no replay or automatic acknowledgement.

## pre-pbs-copy

- Installed deadline: 210 seconds.
- Effects: DB10.1.10.50 native dump inventory and pg_restore list; native exit status and freshness <=7200 seconds; Mac private temporary stream and VM109 /srv/community-brain/db-backups checksum-paired object; next PBS window 21:00 local.
- Recovery: Read native status, source size/hash before and after, final destination hash. Retain partials and uncertain journal; never infer success from SSH exit. A protected capture uses exclusive capture IDs, not the old rolling-copy prune policy.

## legacy-intake-ownership

- Installed deadline: 45 seconds.
- Effects: Read retained terminal superseded ownership receipt and legacy LaunchAgent ownership; Keep AppleScript intake disabled; do not fetch, renew, restart or depend on VM101.
- Recovery: Terminal superseded state is authoritative; retain old recovery receipt. Any ownership regression blocks admission. Never restart the old writer as recovery.

## renew-service-tokens

- Installed deadline: 180 seconds.
- Effects: Infisical /production/community-brain service authority; five subject identities, seven-day life and three-day lead; Successor VM109 API generation, collector, successor WebUI filter, Kuma monitor and Prometheus bearer file; Old/new overlap verified at every consumer before old authority revocation; journal stays in Infisical.
- Recovery: Read the same generation journal and every consumer identity. Resume that generation only after explicit reconciliation, never mint on an unknown outcome. Independent finalizer restores exact incumbent if recreation is interrupted. Dormant VM101 references are replaced by successor VM109 binding; real successor acceptance remains a separate gate.

## provision-nats-tls

- Installed deadline: 180 seconds.
- Effects: Step CA 24-hour certificate; renew below 12-hour remaining lifetime; Infisical certificate/key fields; PVE1 CT304 at 10.1.10.54, Nginx TLS sidecar port4223 permits VM109; backend4222 and unrelated services unchanged.
- Recovery: Read authority certificate fingerprint/expiry and exact sidecar files, running container and TLS handshake. Preserve previous files and container ID; unknown issuance is reconciled by fingerprint before any reissue. Protocol tests cover the current-certificate deployment branch; actual CA issuance acceptance is not claimed.

## renew-app-tls

- Installed deadline: 180 seconds.
- Effects: Step CA application leaf certificate and Infisical certificate/key fields; Traefik /mnt/HDD_2TB_Main/traefik/certs and dynamic TLS configuration, hot reload.
- Recovery: Read exact source/deployed certificate fingerprint and private-CA route handshake. Restore retained previous files on failed acceptance, without restarting shared Traefik. Unknown issuance or deployment blocks replay. No live issuance was invoked.

## copy-backup

- Installed deadline: 180 seconds.
- Effects: Stream latest native dump from DB10.1.10.50 through private Mac tempfile to VM109 /srv/community-brain/db-backups; Actual deployed writer stages .partial then replaces final name; ordinary policy retains14 backups.
- Recovery: Read source and final size/hash, plus partial identity. Preserve every Request033/protected-capture attempt. Do not reuse the deployed overwrite/prune behavior for protected capture. An unverified final object is not a successful copy.

## management-health

- Installed deadline: 180 seconds.
- Effects: Read expiry, TLS, renewal and recovery-copy state; Publish VM109 management JSON and node-exporter textfile health status.
- Recovery: Read both actual output files and freshness timestamp; report critical/stale truthfully. Retain prior output and pending journal on unknown write, do not translate health publication into application acceptance.

## checkpoint-consumer

- Installed deadline: 1200 seconds.
- Effects: Read actual processing pause before checkpoint effects; Nonpaused source can capture DB/files/PBS, restore and acknowledge under a quiet-window lease; those effects remain forbidden in this mapping phase.
- Recovery: Candidate exercises the actual paused branch and preserves attention/checkpoint bytes. Unpaused state requires its separate checkpoint owner and authorization; capture must never silently acknowledge or replay retained work.

## monitor-publish

- Installed deadline: 30 seconds.
- Effects: Publish actual heartbeat/status metrics; Failure publication can create management-attention only when absent; existing attention/checkpoint are preserved.
- Recovery: Compare durable status and hold hashes, mark stale/blocked explicitly. Never clear attention or use a heartbeat to bypass the common journal.

## Database

The independently privileged metadata census reconciles Forge's runtime census. PostgreSQL18.6 has public/plpgsql,10 tables,19 indexes and zero sequences. `database.py` rejects profile/catalog drift, unmanaged writers and unsupported classes. CONNECT revocation is database-scoped for only the two application roles, never global NOLOGIN; unrelated roles/databases survive the real concurrent test. The actual migration and model source supply schema definitions; all rehearsal rows are synthetic. Independent server restore compares canonical rows, Alembic, relationships, unknown outcomes and referenced file hashes. Fourteen actual reverted mutations exercise failures.

## Services

Actual mount UUID, machine, incumbent, Docker restart policy, boot guard, cron and ownership are pinned in `production-contract.json` and evidence. The new Docker ordering drop-in puts the existing processing-pause guard before Docker restores unless-stopped containers. Serving may then start before management admission, with processing still paused. Recovery after Docker verifies the exact incumbent before admission; the unchanged cron tick keeps reporting paused state. It does not wait for the new target or clear boot reconciliation. Actual dev systemd ordering and failed-finalizer tests use isolated transient units. Persistent templates are concrete review artifacts, uninstalled, and their production executor deliberately refuses. An enabled production controller requires separately authorized qualification; this packet cannot be installed as an operational production controller.

## Private preservation

`private_contract.py`, `production-contract.json` and OPERATOR-PROPOSAL.md bind exact component membership, signing bytes, metadata/link policy, private off-host and independent restore destinations. VM108 receives no private bytes. Ordinary rolling-copy retention is not protected-capture retention. Offline equality does not prove a real browser session, capacity, or production consumer acceptance.

## Evidence limits

Nine actual installed algorithms and embedded remote file writers execute against explicit transport fixtures. The live renewal adapter executes against local HTTP/authentication and scoped consumer fixtures; this is not an actual Infisical/CA/Kuma/WebUI acceptance test. Real PostgreSQL, Docker replacement and systemd failure/recovery are separately exercised. Tests of existing-certificate TLS deployment do not prove certificate issuance. VM101 is a metadata-only preservation source, never a functional successor dependency. No claim of end-to-end production acceptance is made.
