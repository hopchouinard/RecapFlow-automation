# Request032 candidate admission and database evidence

Development-only integration. `LINEAGE.json` identifies exact imported Forge,
Request031 recovery core and installed Mac scheduler bytes. Imports remain
unchanged. Scheduler/manual/capture use `shared.py`, the existing Mac mutex and
one durable journal; target evidence is obtained through authenticated SSH with
a fresh challenge. Intent survives caller and transport death. Recovery resolves
an existing intent and never replays an effect.

The scheduler is derived from the actual installed source. Its timing, hourly
attempt persistence and heartbeat flow are retained; production helpers are
explicitly mapped to synthetic health/maintenance helpers. It is not installed.
The retained Request029 pending pointer is not cleared or migrated: its explicit
retirement disposition is pinned to local hashes and fresh target observations.
Any additional pending marker or changed retirement observation refuses dispatch.

## Recovery contract

The target supervisor owns bounded runtime and an independent ExecStopPost
finalizer. Boot reconciliation closes admission before examining the retained
owner, source, holds, incumbent, database controls and current boot. Startup and
dependent admission are ordered by systemd Requires/After. Failed finalization
keeps admission closed until authoritative state reconciliation succeeds. Boot
recovery restores serving state only; it never captures, restores a database or
replays scheduler effects. Unknown orphan operations require explicit review.

Tests use isolated transient systemd units on the existing kernel boot. They do
not prove a real VM reboot. Persistent unit files are inert templates, not an
installation. Recovery requires accessible control storage, Docker and PostgreSQL;
unconditional availability is not claimed.

## Database scope

The closed PostgreSQL18.6 profile includes public/app/audit schemas, plpgsql and
pgcrypto, explicit roles and membership, database/schema/relation/column/default
ACLs, extension function ACLs, table/column/index/constraint definitions,
sequence definitions and values, row digests, unknown outcomes, FTS and file
references. It compares an independent restored PostgreSQL server with exact
source observations and dump identity. Vector arrays are synthetic relational
fixtures, not a claim about production LanceDB.

Writer admission revokes application CONNECT and LOGIN, terminates pre-existing
application writers, rejects unmanaged backends, and verifies controls around
capture. SHARE locks and exported snapshots are additional checks. The fixture
controller is a trusted superuser; protection against a hostile superuser is not
claimed. Unsupported catalog classes are enumerated and rejected. Fixture
coverage does not establish that the production catalog fits this profile.

Component membership, synthetic signing digest, actual volume identity, engine
version, source/restored server identity and recovery deadlines are bound into
receipts. No production data or signing bytes are used. Native Mac fixture tests
adapt five Linux metadata fixtures explicitly and separately test native xattr
rejection. Production metadata checks remain unchanged.

See OPERATOR-PROPOSAL.md for the remaining gate and execution plan.
