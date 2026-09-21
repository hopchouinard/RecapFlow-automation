# Controlled serving activation

This controller implements a reviewed API/OpenWebUI serving handoff. It never
clears processing holds, rotates credentials, restores databases, deletes volumes,
recreates the incumbent, changes ingress, or contacts VM101. Its production path
is code for a separately authorized phase; it has not been run on VM109.

The target-host invocation requires root and an externally reviewed SHA256 of the
exact JSON plan:

```
python3 -B activate.py activate PLAN.json EXPECTED_PLAN_SHA256 PRIVATE_JOURNAL.json
python3 -B activate.py rollback PLAN.json EXPECTED_PLAN_SHA256 PRIVATE_JOURNAL.json
```

The production state root is fixed to /srv/community-brain. The development root
must be below /srv/dev-data/workspaces. The plan binds source, Compose JSON,
private environment files and a verified paired-recovery receipt. The receipt for
production additionally requires verified WebUI restoration, signing material and
off-host backup. These flags are assertions to review against actual receipts,
not a replacement for evidence or user authorization. Never manufacture them.

The controller acquires existing runner, manual-worker and submission lock inodes
in order. The Mac caller must retain its scheduler mutex for the whole operation;
do not nest this call inside a quiet lease that already owns those VM locks.
Integrating that caller and lost-SSH-response handling is a separate required
management test before promotion. Host-local failure injection does not certify
an actual Mac/SSH interruption.

A private, fsynced journal records intent before each effect. A missing candidate
after recorded creation intent is uncertain and cannot be silently recreated.
A matching running candidate after a lost acknowledgment can be verified and
accepted without another create. Configuration drift, changed holds or an unknown
container stop the operation. API/WebUI health and exact image/mount/resource
checks are activation prerequisites; they do not replace authenticated retrieval,
browser/session, monitor, provider or capacity acceptance.

Rollback stops and retains candidate containers and their volumes, starts the
same preserved incumbent container, checks its health and preserves the hold
hashes/modes/inodes. It does not copy old data over replacement writes. Rollback
is terminal for that journal; another activation needs another reviewed plan and
fresh candidate names. Absent/changed containers and uncertain effects require
explicit reconciliation. Preserve an interrupted .tmp journal for inspection.

The supplied VM108 rehearsal uses an isolated internal network, disposable
PostgreSQL, generated development identities and a separate OpenWebUI volume.
It exercises the actual pinned images with the six API mounts and production
resource limits, but no real corpus, restored user data, provider or production
identity. Setup is single-use; resume-setup is allowed only at the verified empty
schema boundary. Do not replay exercise against a retained journal.

For an operational production plan, review and bind every relevant runtime input:
all sealed successor files and its manifest, exact source/Compose/environment/CA
hashes, the protected recovery receipt, current hold hashes, current incumbent
identity/configuration and the external restored WebUI volume. Define and verify
post-activation authenticated API/filter checks and fresh monitor observations.
Review startup/migration write effects and capacity against the protected before-
state. Expiry is not permission to bypass any of these checks.
