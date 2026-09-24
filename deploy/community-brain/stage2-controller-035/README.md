# Request035 development controller

This is a **synthetic VM108 implementation packet**, not a VM109 enrollment or a
production approval. `plan.py` refuses production while any of the 21 required
receipts is absent or its semantic validator is unimplemented. The Request033
`production-contract.json` is an exact historical mapping anchor, not current
authority. The Request034 `accepted:true` envelopes do not qualify as receipts.

All VM108 effects are confined to
`/srv/dev-data/workspaces/cbm-stage2-controller-20260924-035`, two `cbm-r035-*`
containers, a `cbm-r035-pg` Docker volume, and four `cbm-r035-*` systemd units.
The synthetic source contains no private content or provider credentials. The
incumbent and PostgreSQL use exact pinned container IDs and images. The
controller never clears the paused, attention, boot or checkpoint files; it
does not open processing admission. The three writer locks are acquired in
runner, manual, submission order. The Mac entry point also takes Request029's
existing `~/.local/state/community-brain-management/scheduler.lock`.

The Mac externally pins the immutable plan SHA and packet manifest SHA before
admission. Scheduler, manual and capture calls use the same `admit` path. Each
accepted attempt first writes and fsyncs an exclusive intent and a closed
admission state, then starts a systemd worker. A lost SSH reply leaves a local
pending record and requires exact-attempt readback; it is never a retry signal.
The worker stops only the pinned incumbent and revokes only the two synthetic
PostgreSQL roles. `ExecStopPost` invokes an independent finalizer; a separate
systemd guardian timer expires frozen or killed workers and invokes that same
finalizer. The finalizer restores the database ACL and starts the same
container ID, checks its HTTP endpoint, retains the entire intent and phase
journal, and keeps processing admission closed. Failed restoration remains a
closed, retained partial that requires explicit reconciliation.

The `installer.py dry-run|install|uninstall <manifest-sha>` interface verifies
the complete immutable packet and exact VM108 mount before touching units.
Install/uninstall are idempotent. Uninstall refuses an unresolved intent and
retains source, fixture, and journals. Units require Docker and the data mount,
and require the synthetic paused file. The guardian timer is started, not
enabled for a shared-VM reboot. `systemd-analyze verify` covers unit syntax and
ordering; no real VM108 reboot is claimed.

Conditional guarantee: the guardian can recover a lost caller or worker only
while VM108, systemd, its timer, the data mount, Docker, PostgreSQL and exact
container metadata remain available. A frozen/stopped guardian or failed
finalizer leaves admission closed and may leave serving down. The 60-second
restore deadline is an intent target; systemd/Docker/storage unavailability
can exceed it. Production needs independently validated preservation receipts,
current authority, a reviewed mapping-specific DB fence, and separately
authorized enrollment before any production effect.
