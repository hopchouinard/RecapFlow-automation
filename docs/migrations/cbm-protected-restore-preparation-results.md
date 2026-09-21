# Request030 accepted — September 21, 2026

Forge verified and acknowledged the completed preparation. This closes source/
destination discovery and fresh synthetic recovery mechanics; it does not close
the production orchestration, protected-transfer or production-acceptance gates.

## Independent verification

All 52 artifacts listed in the response manifest match their sizes/hashes (53
including that manifest). All 15 source-v6 files independently match VM108 and
the delivered archive. All 39 boundary tests pass locally. The receipt records
39 passing Mac tests, 39 VM108 tests and 293 parent tests. Only the four baseline
dev services are currently running.

Source commit `4c16f84ef8e5d77dcb01953ee5635ceb27c646d9`, branch
codex/request030-protected-restore, is imported unchanged at
[`protected-restore`](../../deploy/community-brain/protected-restore/README.md).
It was not pushed. Original safe receipts/source/diff are retained in the
[evidence directory](receipts/cbm-protected-restore-20260921/receipt.md).

## Accepted mechanics and limits

- Actual PostgreSQL18.6 dump and independent-server restore preserve seven
  representative synthetic tables, relationships, outbox and an unknown-outcome
  attempt. The exported-snapshot SHARE fence rejects an actual concurrent INSERT.
- Final source-v6 captures, streams, verifies and independently restores a fresh
  component bundle, including empty directories, modes, ownership, timestamps and
  contained links. Corruption, traversal, foreign scope, unsupported metadata,
  existing targets, lock replacement and hold drift are rejected. New writes in
  an existing destination are preserved by refusing overwrite.
- Real pinned WebUI synthetic API checks passed old-session continuity, fresh
  login, retained chat, anonymous rejection, disabled signup and wrong-key rejection.
  No rendered browser, real user/upload/session or protected restoration is claimed.
- Six synthetic budget tests exercise the unchanged helper's allowance, ceiling,
  endpoint and uncertain-response boundaries. No external or paid calls occurred.
- Production compiler refusal remains effective; all 21 evidence slots remain null.
  The new component-based recovery schema is incompatible with Request029's flat
  receipt layout. No adapter is installed, and a true flag cannot substitute for
  missing observations.

The eleven Request030 containers are stopped and retained. Earlier containers and
production runtime identities/configuration/start/restart state were preserved.
Six durable trees and the three protected holds match. Whole automation-tree
equality is **not certified**: its digest changed, with status.json heartbeat
mtime consistent with the paused tick; complete per-file starting hashes were
not captured. Preserve this evidence limit rather than claiming total equality.

## Resolved bindings and corrected inventory

Current database: community_brain_prod on 10.1.10.50:5432, PostgreSQL18.6;
runtime role cbm_prod_runtime, owner cbm_prod_migration. Read-only observations
found 4 jobs,20 stages,9 attempts,9 sources,21 artifacts,12 outbox rows and42
model-call rows. Only canonical digests/counts were returned, not rows.

Dormant WebUI's SQLite, signing and Chroma observations remain unchanged. Its
strict tree inventory counts 637 regular files,166 directories,46 contained links
and 1,178,802,835 regular-file bytes. The historical approximately2.34GB estimate
followed cache links and double-counted referenced bytes; it is not evidence of
data deletion. The container is stopped; the VM still has other services.

The proposed private off-host receiver is
10.1.60.10:/var/lib/proxmox-backup/cbm-protected-recovery/<capture-id>, outside
the managed PBS datastore. About414GiB was available; no directory/data was created.
This is not a claim of new encryption or automatic PBS coverage. The Mac internal
disk has about3.9GiB free and is unsuitable for staging.

The proposed independent restore is a new root-private VM108 enclave at
/srv/dev-data/protected-restores/<capture-id>, network none, no ports or real-data
application startup. Protected data/signing can enter it only under an explicit
phase naming that destination. Ordinary dev fixtures remain synthetic. Retention
of at least30days and through acceptance is proposed, not yet executed.

## Next implementation and decisions

1. **Finish the orchestration before transfer authorization:** implement and validate
   the exact capture wrapper, persistent pending-operation guard, maintenance
   deadline, interruption/readback and strict receiver bindings on VM108. The
   delivered library/session/DB tests do not certify that missing wrapper.
2. **Reconcile receipt validation:** implement a separately reviewed validator for
   immutable component manifests, independent DB/vector/relationship observations,
   scope/authorization/expiry, current holds and volume identities. Keep production
   compilation disabled until actual required evidence passes.
3. **Present the bounded protected phase:** one current CB database/state pair,
   stopped WebUI/signing pair, private off-host copy and independent offline restore.
   The [operator proposal](../../deploy/community-brain/protected-restore/OPERATOR-PROPOSAL.md)
   defines destinations, command forms, retention and rollback. It excludes real-data
   app startup, ordinary dev clones, installation, rotation, ingress and processing.
   Finalize the wrapper and interruption evidence before asking to execute it.
4. **Separate capacity/provider decisions:** the proposed concurrent limits total
   approximately4.96GiB before restore/OS headroom, so current4GiB VM108 does not
   certify that profile. An8GiB development capacity phase is proposed, not approved
   or applied. A real-provider proposal caps the exercise at3 requests/US$0.10,
   subject to scoped dev identities and verified model-cost bounds before approval.
   No paid call or resizing occurred. Actual LanceDB/Chroma/relationships, rendered
   browser and real staged-session acceptance also remain open.

The production expiry was refreshed at12:41 UTC: **September22,20:53:07 UTC**, with
completed journal. A proposed two-hour phase would need to start by18:53:07 that
day, subject to any shorter fresh deadline. This is a scheduling constraint, not
permission to skip gates or restart VM101. No protected transfer or production
deployment occurred. Previously approved ingress still awaits a ready replacement.
