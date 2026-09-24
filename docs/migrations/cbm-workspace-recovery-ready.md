# Workspace recovery — implementation ready, production rollout pending

2026-09-17. Patrick approved implementing the next CBM-08 stabilization feature
with “Yes proceed.” This packet has not been deployed to production or dispatched
as a production execution request. Request019 remains the last completed rollout.

## Behavior

- Acquisition failures expose fixed, actionable error codes rather than provider
  response bodies. The workspace offers transcript upload into the original job.
  Binding a fallback resolves a failed/queued acquisition, retains the failed
  attempt, and queues processing once. Repeating the exact binding is a no-op;
  changing a frozen source remains rejected. Running, unknown or partial
  acquisition cannot be overridden by the browser.
- Existing `jobs:submit` permission allows the new scoped
  `POST /api/v1/jobs/{job}/stages/{stage}/resume` endpoint. The reason and expected
  generation are required; requests are idempotent. No Authentik grant expansion.
  Only automatic root jobs, failed acquisition or processing with no ModelCall
  or Artifact records, and generations below 3 qualify. Three generations total
  are allowed. Exhausting acquisition retries still permits fallback upload.
- Each safe resume records `safe_resume_authorized` for its new generation.
  Only this explicit marker admits generation >1 into the automatic selector.
  General retry/reconciliation does not implicitly authorize automatic replay.
  Unknown model outcomes, charged/partially materialized processing, and indexing
  failures remain operator work. No corpus replacement or publication is enabled.
- Recoverable failures return host state `needs_input` without latching a new
  root-only attention marker. Other failures keep their existing stop behavior.
  Existing attention markers are never automatically cleared by this feature.
  The deployed first-failure timestamp/error-class preservation is retained.
- The workspace shows acquisition, processing, Markdown files, indexing and backup.
  Publication/distribution remain visible separately. Backup is verified only
  from the management acknowledgement; it is independent of indexing completion.

## Tested packet

VM108: `/srv/dev-data/workspaces/cbm-workspace-recovery-20260917/`.
The companion `cbm-workspace-recovery-manifest.json` describes ten files:
five jobs modules, `automatic_host.py`, `scan.py`, and three frontend files.
Manifest SHA-256:
`e15aeb753d309a9af73064dd271b6c7dbd83c2f2feacc7837802eb764f022ddf`.
This is a partial overlay, not a complete runtime directory.

Validation: existing application suite 963 passed; final disposable PostgreSQL /
JetStream suite 60 passed; recovery/host focused checks 25 passed (overlap with
those suites); frontend 6 unit and 5 browser scenarios passed; TypeScript and
Vite build passed. Browser scenarios cover same-job fallback and safe resume.
The existing suite reports LanceDB deprecation warnings.
VM108 tested the pinned production candidate image as UID10001, read-only,
network disabled, without credentials. Patched modules and resume route load
correctly alongside the existing archive module. The disposable container was
removed. No real transcript, model call, corpus write or production job mutation.

## Concrete production rollout for the next authorized management request

1. Verify packet hashes and the expected r019 base hashes in the manifest.
   Inspect the latest actual effective directory before composing an overlay.
   Preserve management changes, acquisition.py from request019, archive.py,
   selection helpers, budget guards, extraction model and all existing mounts.
   Current inspected base is
   `/srv/community-brain/workspaces/cbm-fathom-20260917-effective-r019`.
2. Under the existing Mac scheduler and runner/manual/submission quiet locks,
   verify no selected worker, eligible work or pending checkpoint. Build a new
   effective backend/frontend packet; never replace the old directory in place.
   Retain all previous hashed frontend assets and fail on differing collisions.
3. Overlay jobs/api.py, runtime.py, store.py, automatic.py, worker.py and both host
   helpers. API must use the changed api/runtime/store modules; selected workers
   and the scan container must use the changed store/automatic/worker modules.
   Existing helper and module mount paths already provide the worker mechanism;
   verify actual generated arguments. Do not substitute an old baked-in module.
4. Configure `CB_AUTOMATION_ROOT=/state/automation-public` in the management
   renderer, mounting `/srv/community-brain/automation-public` there read-only
   for API only. Invoke the new `publish_checkpoint_status()` helper once before
   API startup; subsequent runner ticks refresh it. The directory is root-owned
   0755 and its sole `checkpoints.json` is root-owned 0644. It contains only job
   UUIDs, backup status, and a management-attention boolean. It contains no paths,
   hashes, credentials, receipts, transcripts or model output. Private original
   `/srv/community-brain/automation` modes remain 0700/0600; never mount that
   directory into API or grant API write access to host state.
5. Preserve renderer/runtime/frontend/recovery pins together, then recreate API
   with fresh Infisical rendering and reapply CA trust as required. Preserve both
   human identities, $5 weekly cap, token renewal, GLM extraction configuration,
   public ingress and retrieval integration. Checkpoint/control copies remain
   management-owned. Keep request016 permission work stopped.
6. Verify trusted HTTPS assets, authenticated real-job detail, API-readable backup
   projection, and an idle runner. September15's existing verified receipt should
   display backup verified. Confirm unchanged jobs/sources/artifacts/model calls,
   corpus counts and retrieval. Do not manufacture a production failure, retry,
   model call or reindex. No pending attention marker was observed during this
   implementation; if one appears, inspect it instead of clearing it.
7. Return hashed safe receipts and effective pins. Real recovery remains available
   for the next actual failed acquisition; it is not necessary to rerun a meeting
   for acceptance. Rollback restores the prior effective frontend/API/host pins
   under quiet locks. If recovery has since been used, review DB generations first:
   the old scheduler cannot execute the new safe-resume generation automatically.

Remote publication, historical replacement, retirement and subsequent major
migration phases remain gated. CBM-10 final quality review remains last.
