# Request036: production-capable Stage 2 source and semantic evidence

ID: `CBM-STAGE2-PRODUCTION-PATH-20260924-036`. Target: `home.servers`.
Deadline: `2026-09-27T18:00:00Z`. Request035 is consumed and acknowledged.

Patrick authorized full Stage 2 development on September 23. The exact
Request035 VM108 packet (`35aa5cf9fe5eff8095345221c1b6f6df150679e72211fd0c7eb7b6301fd942dd`)
passed synthetic controller/guardian fault rehearsals, but its `plan.py` has
zero production semantic validators, and its controller, installer and finalizer
hardcode VM108 synthetic state and a no-op work phase. Its acceptance ledger
correctly says `stage2_complete=false`. This request implements that specific
missing source path. Preserve Request033 production mapping, Request034 actual
dev acceptance, and all Request035 fixtures, source and journals. Forge's
verified imports are under `deploy/community-brain/` in the canonical checkout.

Authorization is development-only. Use isolated VM108 state and scoped dev
identities for every new change, including receipt schemas and external test
data. Read-only VM109 diagnosis is allowed. Do not renew production secrets,
install on VM109, stop production, capture or transfer private production data,
perform a provider call, cut over, resume processing, resize, or touch VM101.
Production identities expired September 22; no bypass is permitted.

Deliver a source-coherent production path, not another synthetic-only packet:

1. Implement all 21 named production evidence-slot semantic validators against
   explicit immutable receipt schemas. Verify actual named member bytes and
   hashes, source/capture/attempt/scope binding, independent observations and
   expiry as appropriate to each slot. Distinguish dev fixture acceptance from
   real production evidence. `accepted:true` or a signed envelope alone must
   never satisfy a slot. Keep the 21 real production values null. Return a
   validator matrix with one positive development fixture and at least one
   corrupted/foreign/expired negative per slot.
2. Compile a production-capable *review* plan from the exact Request033 mapping
   and current read-only VM109 observations. Bind exact source archive/commit,
   config, host, state mount, incumbent ID/image/fingerprint, controls and lock
   inode/device, current authority generation, private destinations, operation,
   deadline and rollback owner. A production plan with null receipts or expired
   authority must refuse execution. Separate protected preservation, serving
   and processing-resume authorities. No hardcoded fixture path or DB role in
   the production path.
3. Provide a staged VM109 installer/controller/finalizer source package for
   later review, but **do not install it on VM109**. Adapt the Request035 durable
   intent, external pin, Mac mutex, common scheduler/manual/capture admission,
   same-incumbent stop/recovery, DB fence, finalizer, per-phase deadlines and
   no-replay readback to the actual Request033 service and private contracts.
   Integrate a real bounded protected-preservation operation interface with
   the Request030 capture/restore primitives, without calling it on production.
   Keep the old management source and boot processing pause; failure must keep
   admission closed, original/partial generations and checkpoints retained.
4. Validate the exact final source on VM108 against a fresh synthetic
   production-shaped fixture with actual Docker, PostgreSQL, systemd and
   Mac/SSH transport. Exercise a successful bounded preservation and verified
   restore, installer dry-run/install/uninstall and startup ordering, plus
   caller/worker/guardian loss, guardian freeze, failed finalizer, stale or
   foreign readback, competing callers, drift and authority expiry. Report
   deadline misses and conditional bounds explicitly. No shared-VM reboot
   claim. Every final changed byte must have VM108 parity/readback evidence.

Return exact source commit/archive/member manifest, receipts and a single
acceptance ledger. State separately: source implementation complete, VM108
acceptance, production admission, and remaining protected production gates.
If a production-capable implementation cannot be completed within scope,
identify the precise missing contract or access and provide reviewable partial
source; do not mark Stage 2 complete. Do not fill any production slot with a dev
fixture or infer a production phase from this request.
