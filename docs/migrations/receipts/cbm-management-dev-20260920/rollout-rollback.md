# Request027 rollout and recovery review packet

Status: review inputs only. No production source installation, data transfer,
credential rotation, processing resume or cutover is authorized by Request027.
Patrick separately approved the proposed `chat.patchoutech.lab` DNS record,
Traefik route and Step CA certificate. These ingress actions should be applied
when the replacement is ready; they do not authorize the other phases below.

## Source and runtime contract

The current installed management library is
`~/.local/lib/community-brain-management`, a deployed copy rather than a Git
checkout. Request027 compared its25 captured source files with Request024;
all matched. Candidate ownership is the operator repository, branch
`codex/request027-management`, rooted at commit
`f7356151a563d4d07f390872efd9265b6b9302bf`. Final source and packet hashes accompany
the handoff receipt. Nothing is installed from this branch automatically.

The development packet has one descriptor for the API image, worker image,
WebUI image, module/frontend provenance, external signing environment, held boot
launcher and recovery image/file inventory. The API and worker image are pinned
at `sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b`.
Twenty actual image module/frontend files are hash checked after recreation.
No r020 `jobs/` or old frontend mounts are accepted. All packet members and the
exact file set are checked against an externally supplied manifest hash.

The WebUI development manifest is
`sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b`,
imported from the Request026 verified0.8.12 image. Its original registry digest
is `ghcr.io/open-webui/open-webui@sha256:b8095f79a6a8ffad8f830bdacc9b5b0aef805689b31bca0b065cc2424d3cfaeb`.
Docker stores can assign different manifest IDs on import; require matching
configuration and RootFS layers, not a guessed equivalence from a tag.

This is a development management packet, **not a drop-in production worker
packet**. `run.py` exposes API management, controls and held ticks. The copied
r020 manual/automatic worker helpers use the same image, development state and
isolated network, with old module mounts removed. The indexing budget helper is
preserved byte-for-byte. Per-helper provenance records the original and candidate
hashes. Manual launch is denied while held; the actual automatic entry is excluded
by the runner lease. The boot checker does not reconcile boot state. No worker
execution or paid-provider call is claimed. Forge must review the complete
production descriptor and certify worker execution before a processing release;
do not install the development held-tick entry over production worker machinery.

## Protected before-state, before any later production phase

1. Capture fresh actual container IDs/images/mounts, management/helper hashes,
   scheduler and boot launcher, ordered lock inodes, boot ID, hold bytes/modes,
   identity expiry and journal phase, and relevant routes/monitors. Do not export
   secret values or production databases through the handoff.
2. Verify no unfinished credential journal, uncertain worker effect, unresolved
   restore or pending checkpoint is being hidden by a healthy API. Preserve
   attention, paused and unreconciled-boot markers.
3. Preserve immutable r020. Its recorded members match, but the observed extra
   `__pycache__/run.cpython-314.pyc` causes the existing exact-file-set gate to
   reject it. Investigate and record provenance; do not delete evidence or bypass
   assertions to make an old manifest pass.
4. Capture compatible paired database, files/corpus/config, archive and WebUI
   data recovery points, with off-host verification and the current authoritative
   identities available through the approved secret-management path.

## Protected data and signing transfer, separately authorized later

- VM101 remains recovery-only. Never start its stopped WebUI to fetch or deliver
  credentials. Read and copy the preserved source volume through a controlled
  recovery operation only after the data-transfer phase is approved.
- Transfer copies into replacement-owned volumes; preserve the source byte tree
  and checksums. Verify SQLite, Chroma, uploads, chats, model/prompt records and
  their relationships before admitting user writes. Request026's synthetic
  restoration evidence is not evidence that production data was transferred.
- Preserve the original external signing material separately. The signing key
  used by the old WebUI is outside its data volume; a volume-only copy is
  insufficient. Deliver it privately through Infisical or a controlled0600
  secret file. Never place it in the packet, Git, command arguments or receipts.
- Use a new immutable host directory and exact manifest. Render from the current
  authority; never restore expired tokens from a copied environment or backup.

## Ordered activation and verification

1. Acquire the Mac scheduler mutex, then the VM109 runner, manual-worker and
   submission quiet locks through the checked lease. A dead SSH process is not
   proof that a remote effect stopped. Persist intent, reconcile actual state,
   and resume the same generation after uncertainty.
2. Install only the reviewed complete successor. Render a fresh API environment
   and external WebUI signing material. Verify image, all module/frontend/helper
   hashes, no old overlays, health, scope denials and exact hold preservation.
3. Run WebUI locally against the replacement API, maintaining local user
   authentication. Disable signup explicitly in persisted settings and startup
   configuration after creating/restoring the intended accounts. Verify login,
   cookies, session continuity and a cache probe against the real retrieval
   backend. Set the canonical WebUI URL and allowed origin to the new hostname.
4. For authorized ingress, recheck that `chat.patchoutech.lab` is unclaimed,
   create its UniFi DNS record pointing to10.1.10.100, issue the private Step CA
   certificate, and route Traefik to the replacement's dedicated VM109 port3000.
   Restrict the backend to the proxy and use reviewed source restrictions and
   security headers. Verify DNS, CA trust, SNI, HTTP upgrade/streaming, local
   login, unauthenticated denial and direct-backend restrictions. The API keeps
   its own route. Do not point the new route at a development fixture or VM101.
5. Under a separately approved production credential phase, use the unchanged
   overlap/journal policy. Deliver to explicit replacement targets and existing
   approved clients; require fresh Kuma/Prometheus observations and actual WebUI
   cache acceptance before removing old identities. Keep the old overlap when
   any consumer fails. Never extend a prepared generation on retry.
6. Verify scheduler, renewal, delivery and serving have no VM101 SSH dependency.
   Preserve the terminal superseded Mac-intake guard. Intentionally retained
   recovery-host monitoring is a different dependency and should be documented.
7. Only a separate processing decision may clear holds, reconcile boot state or
   activate worker execution. API health and ingress success do not clear them.

## Rollback and expiry

Before replacement user writes, stop the replacement and retain its private
staged data; restore only the captured configuration elements actually changed.
After new writes, preserve those writes and reconcile a compatible data/runtime
recovery. Do not overwrite them with the dormant copy, restore an old identity
map, restart VM101, or remove holds as a rollback shortcut.

If a renewal is interrupted, read the Infisical journal and actual consumers.
Resume its generation and expiry; do not generate a competing one. If expired
or too old for policy recovery, stop and reconcile explicitly.

The metadata-only production check on September20 confirms completed journal
phase and September22 at20:53:07 UTC expiry. The Request027 receipt deadline is
September21 at20:00 UTC. Neither deadline authorizes a validation bypass.

## Remaining decisions and gates

- Production descriptor/helper review and worker execution validation, including
  the paid-provider budget/audit boundary without production keys. Management
  validation and held-launcher checks do not certify worker execution.
- Replacement resource sizing and verified full production data/signing restore.
- Browser login/session acceptance after protected restoration, explicit signup
  policy, proxy-only backend access and real provider/production load checks.
- Separate approval for source installation, data transfer, production rotation,
  cutover, backup-credential updates, boot reconciliation and processing resume.
  DNS/Traefik/certificate creation has already been approved and needs no repeat
  approval when its prerequisite target is ready.
