# Request035 consumed: development controller, production path still open

September 24. Forge verified all nine named response artifact hashes, all 15
archive members, and independent byte-for-byte parity for the 14 source members
on VM108. The unchanged packet is at
`deploy/community-brain/stage2-controller-035/`; the response and Forge
verification are at
`docs/migrations/receipts/cbm-stage2-controller-20260924/`.
Agent-ops source commit `aadf565486ab1112816c7f239927158c0c602642` was
pushed on branch `codex/request035-controller`; the parent gitlink was not
changed. Packet manifest SHA-256:
`35aa5cf9fe5eff8095345221c1b6f6df150679e72211fd0c7eb7b6301fd942dd`.
Request035 was acknowledged as consumed in the shared handoff.

On VM108 the exact synthetic packet passed normal same-incumbent finalization,
Mac-client kill, lost SSH acknowledgment without replay, worker kill with
independent finalizer, and competing/adverse readback refusals. An expired
guardian restored only after its stopped timer was resumed, exceeding the
60-second target. Deliberate finalizer failure left admission closed and partial
state retained; the synthetic incumbent and database ACL were then manually
restored without rewriting that failed result. Source, hold, volume, incumbent
and authority negatives were read-only altered-expectation checks, not actual
mount/protected-file mutations. Unit syntax and ordering passed static checks;
the shared VM108 was not rebooted. The four standing dev containers remain
running. The Request035 guardian timer is stopped after the terminal-failure
probe, with units, fixture and journals retained.

**Stage 2 remains incomplete.** `plan.py` implements only
`synthetic-development`; its `PRODUCTION_VALIDATORS` map is empty, so none of
the 21 production receipt slots can pass semantic verification. The worker's
phase is a synthetic no-op, and installer/finalizer unit names, paths and SQL
are VM108 fixture-specific. This is a useful, tested control-plane prototype,
not a production-capable controller or VM109 enrollment packet. Both Request029
production refusals remain, all 21 production evidence slots are null, and
production identities expired September 22 with renewal still unresolved.

Request036 targets a production-capable, fail-closed source implementation and
semantic validators using only isolated VM108 fixtures. Actual protected
preservation receipts, current production authority, persistent VM109
installation, real-session acceptance, serving cutover and processing resume
remain separately authorized phases. VM101 remains recovery-only.
