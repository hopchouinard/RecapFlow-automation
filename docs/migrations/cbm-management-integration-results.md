# Request027: management integration acceptance

Forge consumed and acknowledged Request027 on September 20, 2026. Actual
development management integration passed; the successor is **not ready for
production promotion**. Production services and the legacy recovery VM were not
changed by Forge.

## Evidence and source reconciliation

Verified all 27 returned artifacts and independently read all 34 packet members
from VM108. The exact packet manifest is
`19c85b5cbece351f9c9c09606ab3ccaa35065fd4bcee35f65e8ab2cb502d08a9`.
The unchanged candidate from agent-ops commit
`3022cda148f9fd3b1732a687a40ba2220bcc90ef` is imported under
[`management-development`](../../deploy/community-brain/management-development/README.md).
Its evidence is retained separately in the
[receipt directory](receipts/cbm-management-dev-20260920/receipt.md), including the
original source archive. The upstream candidate was committed but not pushed or
installed in production. Six boundary tests also passed locally on Forge.

An independent Forge build produced semantically identical descriptor content,
but a different packet identity:
`6c7be365ca7659a1dcf17f8a83d34e7b21297ab6348a5c311fce3c308d7f8b9e`.
Only descriptor.json differs in bytes: build_packet.py constructs helper_files
from unsorted Path.rglob results, so JSON member ordering depends on the filesystem.
The received VM108 packet remains verified; cross-filesystem byte reproducibility
is not established. Preserve that packet and validate deterministic serialization
on VM108 before sealing a successor. See
[Forge rebuild evidence](receipts/cbm-management-dev-20260920/forge-rebuild-verification.json).

## What the development run established

- Real Infisical save/read equality and the five-identity journal workflow passed
  in the isolated development child. No production secret material was used.
- The actual Mac mutex and ordered SSH quiet lease passed lost-response readback,
  lease-loss refusal and API write exclusion while retrieval remained available.
- Actual WebUI retrieval and dedicated Kuma/Prometheus monitoring accepted the
  development identities. Probe, operator and collector bundles passed API probes.
- Lost delivery acknowledgment and a stale Kuma heartbeat both retained overlap.
  Resuming the same generation completed the journal and rejected all five old
  identities only after fresh consumer/monitor acceptance.
- API recreation preserved the pinned stabilization image and 20 module/frontend
  checks. Pause, attention and boot markers remained unchanged. Held manual and
  automatic entry points refused execution; this is not worker execution evidence.
- Six request containers were stopped without OOM; the four pre-existing dev
  services retained their start times. Private development state remains retained.

## Remaining gates and order

1. Fix and validate deterministic packet rendering; bind the actual production
   descriptor, worker entry points, paths, images and recovery inventory. Exercise
   worker execution and the complete resulting configuration on isolated VM108
   state. Do not install the development held-tick entry point over production.
2. Reconcile the reported r020 extra `__pycache__/run.cpython-314.pyc`. Manifest
   members match, but the exact file set fails. Its provenance is unresolved;
   preserve it and the recovery workspace rather than deleting it or relaxing checks.
3. Complete protected real WebUI data/signing-key transfer preparation, destination
   resource acceptance, browser acceptance, ingress and coordinated rollback.
   Synthetic restore and the earlier pipeline load test remain valid evidence for
   their tested versions, not acceptance of a new production-bound configuration.
4. Execute only the separately authorized production phase after those development
   gates, then verify renewal, serving and removal of legacy dependencies. Processing
   resume, weekly-cycle evidence and retirement remain distinct outstanding gates.

The handoff reports Patrick authorized development material in
`/development/community-brain-dev`; this run used child `request027` in the homelab
project's environment named `prod`. That environment name does not make its test
material production authority. Parent development values were unchanged.

It also reports authorization for `chat.patchoutech.lab` DNS on UniFi, the Traefik
route and Step CA certificate when the replacement is ready. Do not request those
same approvals again. They do not authorize production source installation,
private-data/signing-key transfer, rotation or cutover. No ingress change is claimed.
The recorded production identity expiry remains September 22 at 20:53:07 UTC;
it is a deadline to manage, not grounds to bypass development validation.
