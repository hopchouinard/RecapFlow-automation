# Request025 — actual OpenWebUI development acceptance and rollout reconciliation

Request ID: `CBM-RENEWAL-DEVELOPMENT-20260920-025`.
Target: home.servers. Prior Request024 has been verified and acknowledged.

Patrick accepted stabilization, required every change to pass Community Brain dev
VM108 before production, and instructed implementation. Use the existing authorized
relay and administration. This request authorizes **development-only rehearsal and
read-only production/source inspection**. Do not rotate production credentials,
install production helpers, restart the old stack, clear holds, reconcile production
boot state, or resume processing. No Mac permission/TCC change is requested.

## Concrete candidate

Verify `request.json` document hashes, then inspect `renewal-candidate.tar.gz` and
`candidate-manifest.json`. The archive contains exact candidate files and tests for
the existing agent-ops integrations directory. Request024's deployed renewal policy
is unchanged. The live adapter delegates WebUI inventory/delivery/verification to
a host helper. Stopped WebUI remains stopped; only its persisted filter API key is
updated transactionally, preserving the other valves and tables. Running WebUI
still uses the existing authenticated API/cache probe, now including an exact
credential-hash comparison. Tokens travel only through private stdin/Infisical.

Forge and VM108 passed 20 targeted tests. VM108 reproduced `docker exec` exit1 on
a real stopped fixture and verified SQLite delivery, idempotent replay, unchanged
container state, preservation and integrity. Fixture content is synthetic. This
has **not** certified the actual OpenWebUI image/API/cache behavior. The candidate
is not an instruction to patch deployed files or run production renewal.

## Work requested

1. Review the candidate against the exact current management source from Request024.
   Return any incompatibility or unsafe assumption. In particular, check host-volume
   access, the existing scheduler/quiet-lease exclusion of concurrent administration,
   live cache credential verification, and failed-delivery overlap preservation.
2. Using existing old-host administration, identify the exact current OpenWebUI image
   and obtain the filter **source code only**, without valves, runtime environment,
   signing keys, database contents or user data. Compare the source hash to the
   candidate's existing pinned hash. Do not substitute a different OpenWebUI version.
3. On VM108 only, rehearse the exact candidate against that image and source using
   a new disposable volume, synthetic admin/filter/configuration and isolated fixture
   retrieval/model-list endpoints. No real provider credential, model call, consumer
   traffic or production database may enter this rehearsal. Bind any test ports to
   VM108 loopback; preserve its four existing development services. Verify stopped
   delivery then startup, running delivery via the real authenticated API, persisted
   valves and live-cache hash/context, failed delivery retaining overlap, and replay
   after a lost acknowledgment. Record the exact image, source, tests, hashes and
   cleanup. If dependencies prevent this, return the specific blocker; do not replace
   the required live-path acceptance with another mock and claim it passed.
4. Read-only review the production rollout coupling: current manual_api_runtime.py,
   base manual_host/run.py, Compose overlays, r020 host packet, boot guard and
   management source ownership. The application candidate already validated on VM108
   is `sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`.
   Return a concrete compatibility/pin-change list and exact additional safe source
   needed for a coherent renderer/host promotion. Do not bypass existing manifest
   checks, mutate immutable r020 files, or treat this image alone as a rollout.
5. Recheck only nonsecret expiry/journal phase metadata. The last known five-identity
   expiry is **September22 20:53:07 UTC**; this request does not renew it. Finish the
   development handoff by September21 20:00 UTC if possible to retain repair time.

Use `/srv/dev-data/workspaces/cbm-renewal-20260920` for the existing candidate/tests,
with a separate subdirectory for the actual WebUI rehearsal. No developer credential
needs to be copied to Forge. The full Request024 source reference remains in its
response directory and in Forge's receipt record.

## Response

Claim this request once per the shared protocol. Return `status.json`, `receipt.md`,
source/image/candidate hashes, safe acceptance results and cleanup status in the
matching response directory. Separate real WebUI evidence from fixtures and pending
checks. Any candidate correction must be returned as a source diff and revalidated
on VM108; do not silently change the tested source. Production remains unchanged.
