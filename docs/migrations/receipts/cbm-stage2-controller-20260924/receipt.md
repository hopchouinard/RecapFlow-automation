# Request035 verification receipt

Request: `CBM-STAGE2-CONTROLLER-20260924-035`  
Actor: `home.servers`  
Recorded: `2026-09-24T01:46:50Z`  
Disposition: **development implementation delivered; stage 2 production acceptance remains false.**

The isolated `agent-ops` branch `codex/request035-controller` is clean at commit
`aadf565486ab1112816c7f239927158c0c602642`. It was pushed to
`Patchoulab/agent-ops`; remote parity was verified at `2026-09-24T02:38:06Z`
in `publication.json`. The `home-servers` parent gitlink was not changed.
The exact 14-member source packet
is `packet-v6`, manifest SHA-256
`35aa5cf9fe5eff8095345221c1b6f6df150679e72211fd0c7eb7b6301fd942dd`,
archive SHA-256
`bd342d4c407895c9cc96a2a949a5d694e8b9e7c185517d3dd0d9cb615f6af458`.
Mac path:
`/Users/pchouinard/.local/state/community-brain-management/request035/packet-v6.tar.gz`.
VM108 immutable path:
`/srv/dev-data/workspaces/cbm-stage2-controller-20260924-035/packet-v6`.
The committed members, local archive manifest, and independent VM108 member
readback agree; see `source-verification.json` and `packet-manifest.json`.

On actual VM108 Docker, PostgreSQL 18, systemd and Mac/SSH, the final packet
passed normal admission/finalization, actual Mac-client SIGKILL with exact
readback, lost SSH acknowledgement with no replay, worker-main SIGKILL with
independent finalizer, and competition/refusal checks. The guardian was stopped
through a restore deadline: no recovery occurred while it was unavailable;
resuming it restored the same incumbent and DB ACL. A deliberate finalizer
failure left admission closed, the failed result and partials retained, and
installer uninstall refused. I manually restored the **synthetic** DB ACL and
the same container ID afterward and verified its HTTP 200. The failed result
was not rewritten. The guardian timer is stopped; the installed dev units,
fixture, packet generations and journals are retained for review. The four
standing VM108 dev containers remain running. No shared VM108 reboot was done;
systemd unit syntax and Docker/mount ordering were checked statically.

Read-only negative tests refused altered expected source, hold, volume identity,
incumbent and expired authority against live VM108 state. They did not mutate
the actual mount or protected files. All 21 production evidence slots are null;
fake `accepted:true` envelopes fail because semantic production validators are
unimplemented. This is the **specific remaining implementation/acceptance
blocker**, along with independently validated preservation receipts and current
production authority. There was no VM109 enrollment or production effect,
renewal, private transfer, VM101 change, resize or paid provider call. Recovery
bounds are conditional on VM108, systemd/timer, mount, Docker and PostgreSQL
remaining available. The frozen-guardian case exceeded its target while the
timer was stopped. See `acceptance-ledger.json` for the single disposition.

Safe relay artifacts (SHA-256):

| File | SHA-256 |
| --- | --- |
| `packet-v6.tar.gz` | `bd342d4c407895c9cc96a2a949a5d694e8b9e7c185517d3dd0d9cb615f6af458` |
| `packet-manifest.json` | `35aa5cf9fe5eff8095345221c1b6f6df150679e72211fd0c7eb7b6301fd942dd` |
| `source-verification.json` | `307469b2a41d144bad49e2eaed645dffac124b95686268b18fa3ef923a469b10` |
| `vm108-final-parity.json` | `bc4d8837f23df6b7f2d6ed8ec0b2aad1a22cc48ec5e91a13b9b7de98192862de` |
| `negative-matrix.json` | `ca4a704c97a4a53f8059614ef0c91faee0dc3d5e3f9082ff7e012b3ad4620b46` |
| `attempts.json` | `cf892860f6d28e699caa5ab34c40759dbdd0555df7dd5989863ea596b4238e78` |
| `acceptance-ledger.json` | `1558ed15916438caa5abd0785bde2570c207255b092685b039c653aed0fe2a75` |
| `systemd-units.json` | `32460b984c5fbc65fcd87066d6e9b82ecbbd6acefc4194228bcbba8cadec88fc` |
| `publication.json` | `b7f54cbeca9fee42b88f5b01b4d85ad311511517b4e08fd3b5f8e75491e6796b` |

No production approval is inferred. A separately authorized protected
preservation phase must supply independently validated production receipts;
serving and processing-resume authority remain separate.
