# Request036 reviewable partial source

This package is **not** a production Stage 2 controller. It cannot install on
VM109, stop an incumbent, transfer private content, authorize a phase, or open
processing. `review_plan.py` compiles an exact, source-pinned review record from
Request033 and a five-minute VM109 readback. It leaves all 21 production evidence
slots, all three phase authorities, current authority generation, and deadline
null. `require_executable` refuses this record. `observe_vm.py` only reports
hashes/metadata, never control contents or credentials.

`preservation.py` calls Request030's actual content-addressed capture, bundle
validation and exact tree restore routines. It is dev-only. The caller must
already have stopped noncooperative writers and fenced PostgreSQL; Request030's
cooperative locks cannot accomplish either. A local deadline is checked before
and after the file phase. The operation does not yet enforce a hard wall-time
limit inside capture/restore, terminate a lost remote process, maintain a DB
fence, transfer to PBS, or run the independent production finalizer. On error,
the exclusive capture/restore directories remain for readback; there is no
retry or deletion path. The VM108 rehearsal uses a fresh synthetic component.

The missing implementation is concrete: each of the 21 evidence slots needs a
member-level schema and a semantic verifier tied to independently produced
observations, source/capture/attempt/scope/authority and expiry. The existing
Request034 `accepted:true` format has none of these proofs. Request035 has no
production validators. Current production service identity expiry was
September 22. The historical Request033 private destinations do not exist, and
no fresh protected-preservation, serving, or processing-resume authority has
been presented. A production installer/controller/finalizer that safely binds
Request033's real PostgreSQL, Docker, systemd, Mac mutex, transport and
independent recovery contracts still requires implementation and VM108 fault
acceptance. The existing Request035 dev-only implementation is deliberately
unchanged.

Run `python3 -B -m unittest -v test_review_plan.py` here. The VM108 rehearsal
requires an exact copy and SHA-256 pin of Request030 `recovery.py`; invoke
`rehearse_preservation_vm108.py <library-path> <library-sha256>` on VM108 as root.
It exclusively creates `/srv/dev-data/workspaces/cbm-stage2-production-20260924-036`.
