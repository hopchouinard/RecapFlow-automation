# CBM-STABILIZATION-DIAGNOSIS-20260920-024

Target: home.servers. Read-only source/diagnosis request supporting Patrick's
accepted S-01/S-02/S-03 implementation. All subsequent changes must be tested on
community-brain-dev VM108 before production promotion. This request changes no
runtime, secrets, paused state, or Mac permissions.

Forge is implementing runner diagnostics and safe UI readiness locally and will
validate them on VM108. Please supply the current management source (code only,
no runtime values) and safe read-only diagnosis needed for the renewal repair:

- Exact deployed service_renewal_live.py, service_renewal_policy.py, secret_store.py,
  renew-service-tokens.py, associated tests and boot/reconciliation helpers,
  hashes, and their canonical repository/commit/local-change status.
- Current renewal error's failing remote operation/host and safe exception class,
  return code and cause, without tokens or raw private output. The September15
  preserved source maps service_renewal_live.py:112 to the OpenWebUI read-only
  inspection on n8n-automation. Verify against current source before concluding.
- Read-only old-VM/OpenWebUI container/path/SSH status and current scheduler/renewal
  journal phase (only phase, no secret journal content). Do not run the renewal,
  clear holds, change TCC permissions, or retry uncertain effects.
- Current supported boot/runner reconciliation procedure and any recorded cause
  of VM109's September18 19:46 RuntimeError. Boot pause on September19 is separate.

Live VM109 still has pause + attention, boot reconciled=false. Five identities
expire September22 20:53:07 UTC. Its three consumer bundles match active API token
hashes and remain0600. No production job has been started by this work.

Deliver safe source files and metadata through the existing response directory.
No deployment or rotation is requested here: fixes and a concrete rollout packet
follow only after the exact candidate passes on VM108. Request023 is acknowledged.
