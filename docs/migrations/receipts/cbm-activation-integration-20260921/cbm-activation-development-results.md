# Serving activation and rollback — VM108, September 21

Implemented a target-host serving activation controller at
[`activation/activate.py`](../../deploy/community-brain/activation/activate.py).
The complete development rehearsal passed with the pinned Community Brain and
OpenWebUI images. Production was not changed. This is a serving controller, not
permission to enable workers, rotate credentials or restore real user data.

## What the implementation does

An externally pinned plan binds source, Compose, private configuration and a
paired-recovery receipt. Production plans additionally require protected WebUI,
signing-material and off-host recovery assertions backed by real evidence. The
controller verifies the target hostname, acquires existing runner/manual/submission
locks in order, and preserves required pause, attention and boot marker hashes,
modes and inodes.

It journals intent before stopping the incumbent or creating each replacement.
After a lost acknowledgment, an already-running matching container is verified
instead of recreated. An absent uncertain target, changed container or changed hold
fails closed. Images, mounts, ports, resource limits, command, user and network
are compared to the reviewed plan before readiness is accepted.

Rollback stops and retains replacement containers/volumes and restarts the exact
preserved incumbent API container. It never copies dormant data over new writes,
recreates the incumbent, clears holds or contacts VM101. A completed rollback is
terminal for that journal. See [operator boundaries](../../deploy/community-brain/activation/README.md).

## Actual VM108 acceptance

The final plan hash is
`eb0dd4381e7a757cc3b6c91b05075ac3b566ef82cdd7759db401252f56475815`.
The [result](receipts/cbm-activation-dev-20260921/result.json) records:

- Real API port ownership transferred from the incumbent to the candidate.
  The API used six state/trust mounts and a 2 GiB/2 CPU limit; WebUI used its own
  volume and a 1.5 GiB/1.5 CPU limit on an isolated internal network.
- A held runner lock refused activation before any journal or container effect.
- An injected lost acknowledgment after Docker created the API was reconciled
  without a second creation. Repeating completed activation retained both IDs.
- The actual API accepted its scoped development identity and rejected anonymous
  access. Both API and OpenWebUI passed health checks.
- A synthetic write to the replacement WebUI volume survived rollback. The same
  original API container returned healthy, the prior artifact was unchanged and
  all processing holds were preserved.
- A synthetic PostgreSQL dump restored into a separate database before activation;
  source and backup artifact bytes matched. No production data or identity was used.
- Ten boundary tests passed on Forge and VM108, covering uncertain effects, drift,
  foreign journals, rollback and Docker inspection behavior.

Private configuration, database dump, stopped containers, WebUI volume and failed
attempts remain under the dedicated
`/srv/dev-data/workspaces/cbm-activation-validation-20260921` workspace. The safe
receipts contain hashes and metadata only. All six fixture containers are stopped;
the four pre-existing dev services remain running.

## Failures reconciled before acceptance

The initial schema command used make_store, which also attempted to create storage
as UID10001 without a state mount. The database still had zero public tables. The
fixture now creates schema directly and resumed only at that verified empty-schema
boundary; it did not replay setup.

Preflight then found an actual fingerprint defect: repeated Docker inspections
returned mounts in differing orders (five raw hashes over eight reads). Sorting
mounts produced one stable hash. The controller was fixed and regression-tested
before any activation effect. Docker also returned lowercase absent-container
errors; the adapter now handles both cases while rejecting daemon failures.

The next attempt correctly refused WebUI's runtime because the fixture assumed an
empty default user, while this exact image declares `0:0`. The actual image and
all other runtime fields were checked before explicitly stopping only the two
disposable candidates and restoring the same incumbent. The failed journal was
preserved. The corrected plan used fresh candidate names and a separate journal;
no runtime assertion was weakened or failed journal rewritten.

## Remaining integration and promotion gates

Request029 carries this tested controller to home.servers for the existing Mac
scheduler/management integration. The caller must retain its scheduler mutex and
coordinate SSH uncertainty with the controller-owned VM locks; it must not nest
the controller inside a lease already holding the same locks. Validate that actual
transport with the complete successor, authentication/filter and fresh monitoring
checks, rather than treating this host-local failure injection as SSH evidence.

Before production use, bind the complete immutable successor/activation source,
current authority configuration, current hold hashes, exact incumbent before-state,
real protected restoration receipt and restored external WebUI volume into the
production plan. Validate any resulting code/configuration changes on VM108.
Request028's development-only worker loader remains unchanged and processing held.

Real user-data/signing restoration, browser/session/signup acceptance, intended
capacity and real-provider/budget validation remain outstanding. Production
installation, rotation and cutover require their authorized phase after those gates.
Previously approved DNS/Traefik/Step CA awaits a ready replacement. The recorded
production credential expiry remains September22 at20:53:07 UTC; it does not
authorize restarting VM101 or skipping development validation.
