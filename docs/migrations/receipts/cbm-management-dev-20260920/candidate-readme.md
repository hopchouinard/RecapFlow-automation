# Request027: development management integration

Candidate only; not installed on production. The implementation uses the unchanged
Request024 five-identity renewal policy with actual Infisical, SSH leases,
Community Brain API, Open WebUI, Kuma and Prometheus on dedicated VM108 targets.
See [ROLLOUT.md](ROLLOUT.md) for production prerequisites and rollback inputs.

## Authorized scope

Patrick superseded the request's separate-project restriction. The existing
`homelab` project may be used for development material under
`/development/community-brain-dev`; production keys remain forbidden.
`authority.py` accepts only project
`a508e594-7686-43a1-9b0f-cafa8b348ad4`, environment `prod`, and child folder
`/development/community-brain-dev/request027`. It preserves unrelated values,
checks the lease around operations, and verifies save results by reading the
actual store. There is no file-authority fallback. The renewal journal exists
only in Infisical; local receipts contain safe metadata.

Patrick also approved creating `chat.patchoutech.lab` DNS, Traefik routing and a
Step CA certificate. Those actions await a ready replacement target. This approval
does not authorize production source installation, data transfer, rotation,
cutover, processing resume or retirement. The development network has no published
ports and needs no DNS or Traefik route.

## Source and immutable packet

- `incumbent/` contains byte-exact deployed policy, transport, lease, quiet-window,
  journal and terminal intake policy, with source provenance. The terminal
  superseded guard is tested to avoid any old-host fetch or resume call.
- `manager.py` runs on the Mac under an isolated scheduler mutex and checked
  VM108 quiet lease. Generated development values travel through private SSH
  stdin, never command arguments. The management login stays on the Mac.
- `host.py` targets only the dedicated VM108 root and explicit replacement
  containers. It uses real API authentication and the actual WebUI filter cache.
  API recreation checks all20 recorded module/frontend files, the image ID,
  absence of old overlays and unchanged hold hashes.
- `consumers.py` and `kuma.js` deliver to dedicated service bundles, an isolated
  real Kuma monitor and Prometheus. Verification consumes delivered files and
  requires fresh successful monitor observations. The Mac collector configuration
  is a separate development file; installed desktop intake is untouched.
- `successor.py`, `runtime_contract.py`, `run.py`, `indexing.py` and the boot/held
  launcher share the descriptor's image, source, signing and recovery inventory.
  `workers/` reconciles the r020 helper sources to the same image and isolated
  state/network; old application module overlays are removed. The indexing budget
  helper remains byte-identical. No paid worker execution is claimed.
- `build_packet.py` reproducibly seals the exact helper/descriptor file set. A
  separate expected manifest hash is required at invocation. No r020 assertion is
  bypassed and no sealed revision is modified in place. Run Python with `-B`.

The final tested packet is `packet-v7` under
`/srv/dev-data/workspaces/cbm-management-integration-20260920-027`, manifest:

```
19c85b5cbece351f9c9c09606ab3ccaa35065fd4bcee35f65e8ab2cb502d08a9
```

The generic repository builder reproduced those bytes exactly. Prior immutable
revisions remain for diagnosis. Source-control provenance and actual verification
receipts accompany the shared handoff response.

## Actual validation and its limits

- Real Infisical initialization/read/save/read equality passed with five generated
  development identities; parent development values were unchanged.
- Actual scheduler mutex exclusion, ordered SSH lease locks, lost SSH response,
  readback without replay and lease-loss refusal passed.
- The API's actual write middleware returned503 while the submission lock was
  held; retrieval remained available. Manual launch refused held processing and
  the actual automatic helper was excluded by the runner lock.
- An intentional lost delivery acknowledgment retained ten old/new accepted
  identities. A subsequent real Kuma freshness failure also preserved overlap.
  The same Infisical generation resumed successfully, delivered all consumers,
  verified fresh acceptance and rejected all five old credentials.
- Final renewal-driven API recreations retained the stabilization image, all20
  module/frontend hashes and identical pause, attention and unreconciled-boot
  markers. Real API/WebUI/LanceDB retrieval used synthetic data.
- Six boundary tests passed on the Mac and VM108. Negative scope, old image/host,
  altered signing path, hold clearance, changed packet content and extra bytecode
  are rejected; terminal intake never fetches the old host.

The embedding/model-list provider is an isolated deterministic fixture. Desktop
collector intake/upload, paid model calls, production data restoration, human
browser login after migration and worker execution are not certified here.
Development service bundles were consumed by actual authenticated API probes.
No production monitor, collector, application, credential or hold was changed.

## Reconciled development failures

Strict umask removed Prometheus's group directory access; the candidate now
explicitly applies0750 to its private configuration directory and0640 to files.
Fresh Kuma2.4 requires database initialization before user setup. An early SQLite
inspection created an empty database; it was verified empty, preserved under a
separate filename and replaced by Kuma's own fresh schema initialization. The
adapter now opens SQLite read-only.

The initial Kuma setup called resume after add, although add already starts the
monitor. Repeated `stat_hourly` uniqueness errors prevented fresh acceptance.
The duplicate start was removed and only the dedicated development Kuma instance
was restarted, retaining its database. The stale-heartbeat failure correctly
stopped revocation. These failures and recovery limits are recorded, not counted
as clean first-attempt passes.

## Production observations

All25 captured installed management files still matched Request024. The deployed
library is `~/.local/lib/community-brain-management`, not a Git checkout.
Production identity metadata still showed completed renewal and expiry at
September22,20:53:07 UTC.

r020's recorded files match manifest
`e3ba6ed250d64881f2d6d1c3bcf70b0515e90ab1f23fe0ca1133cf9d4400fabd`,
but an extra `__pycache__/run.cpython-314.pyc` would fail its exact-file-set gate.
Nothing was removed or repaired there. The proposed chat hostname was NXDOMAIN
and absent from active Traefik dynamic configuration during read-only inspection.
