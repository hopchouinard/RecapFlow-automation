# Request029: serving activation and management transport

Development integration for `CBM-ACTIVATION-INTEGRATION-20260921-029`. This directory
reconciles Forge's controller with the accepted Request028 successor. Production
serving execution and the successor production worker loader both refuse execution.
The production plan template is deliberately incomplete and non-deployable.

This README and `ROLLOUT.md` govern this integration. The imported
`activation/README.md` and `activation/rehearse.py` preserve Forge's original
host-local implementation and context; they are not the Request029 entry points.
The original schema-1 rehearsal plan is not accepted by this schema-2 controller.

## Entry points and ownership

`activation/plan.py` compiles an immutable development plan from actual existing
recovery evidence. It binds every file and exact manifest in the current and
referenced prior sealed packets, Compose/environment/CA hashes, external signing
environment, exact incumbent ID/configuration, current hold hashes/modes/inodes/
devices, external WebUI volume identity, and real paired-restore observations.
It refuses stale, incomplete or changed bindings. It does not create restoration
success flags. The original recovery packet stays bound when a later controller
revision consumes that receipt.

`activation/management.py` owns the deployed Mac `scheduler.lock`. It writes a
private fsynced intent and a pending pointer before one SSH dispatch. A pending
transport outcome blocks a fresh operation ID. `manager.py` also refuses renewal
or other management effects while an activation remains uncertain or active.
The deployed production management library is not modified by this candidate.

`activation/remote.py` creates a unique operation directory and starts one detached
controller process. That process owns the existing VM runner, manual-worker and
submission locks, in that order; the caller must not wrap it in a quiet lease
that already owns those locks. The worker revalidates the plan under the locks,
retains them through readiness, and writes a durable result. SSH loss neither
releases these locks nor dispatches a replacement worker. Mac readback remains
under its mutex for a bounded 950 seconds. An unresolved result stays pending;
the next action is readback and reconciliation, never a new dispatch.

`activation/activate.py` journals intent before effects, compares exact runtime
image, environment hash, mounts, volume, ports, resource/security configuration
and container identity, and preserves all processing holds. Generic Docker
inspection was corrected to `--type container`: a retained volume with the same
name must not be mistaken for an existing candidate container.

`activation/rehearsal.py` operates only the fresh Request029 workspace. It restores
the real synthetic WebUI backup into new external volumes, accepting only relative
cache symlinks that remain within the volume. Prior failed restores, plans,
operations, containers and volumes remain retained. No original fixture is reused
for a completed or uncertain external effect.

## Development authority and validation

Only `/development/community-brain-dev/request029` in the existing `homelab`
project is used for new authority. Management bootstrap credentials stay on the
Mac. Five real development service identities, real TLS-first NATS, real API and
OpenWebUI, real Kuma/Prometheus and synthetic provider/corpus data are used.

The unchanged renewal policy is exercised against the final management recreation
configuration, including lost delivery acknowledgment, same-generation resume,
overlap, delivered bundles/cache, fresh monitors and old-token rejection. Any
later controller-only revisions and bound prior packet dependencies are explicitly
identified in the version/equivalence receipt; they are not mislabeled as a fresh
renewal execution.

Docker on VM108 records published-port metadata for its internal network without
opening a host listener. `development_loopback.py` is an explicit loopback-only
test relay for `/health` and anonymous `/api/v1/me`; it refuses absent or ambiguous
running port owners and reports the exact selected container ID. It is not
production ingress. Authenticated API/filter and monitor checks also exercise the
actual internal-network services. The relay source hash is bound in the plans and
its process is stopped during cleanup.

Run the local boundary suites with Python `-B`. The packet builder excludes
bytecode and preserves exact file sets. `test_activation_integration.py` tests the
compiler, stale holds, unresolved intent, production refusal and safe restoration
link boundary; `activation/test_activate.py` tests controller uncertainty and
rollback. Live receipts, rather than unit tests, substantiate Mac/SSH, service,
restore, monitor and retained-write behavior.

## Limits

Serving activation does not enable workers or reconcile boot. Private environment
values, database dumps, signing material and user content are excluded from the
relay. Safe plans contain paths, hashes and metadata only. Production metadata is
read-only; VM101 remains recovery-only and is not contacted.

Synthetic restore and API-driven development login/filter/chat tests do not certify
protected production restoration, human browser/signup/session continuity,
production capacity, real paid providers or budget enforcement. Those gates and
the production execution phase remain separate. See the returned receipt for
exact source/plan hashes, results, retained failures and cleanup disposition.
