# Request020 completed — workspace recovery production rollout

Request: CBM-RECOVERY-20260917-020
Actor: home.servers
Completed: 2026-09-17 UTC

## Installed behavior and scope

Deployed the approved workspace recovery partial overlay on the verified r019
base. The UI and API now provide same-job transcript fallback and bounded safe
resume, retaining operator gates for uncertain/charged/partially materialized
outcomes. The workspace separates backup acknowledgement from indexing and
publication. No Authentik permission expansion was needed.

Seven backend files changed: jobs/api.py, runtime.py, store.py, automatic.py,
worker.py, automatic_host.py and scan.py. All other effective backend files match
r019, including acquisition.py and its real worker mount, SelectedFathom, archive,
selection helpers, weekly $5 budget guards and extraction settings.

The approved host helper received one deployment mount adjustment: worker.py was
added to its scan-module loop so the changed Worker is loaded by runtime imports.
The API also mounts the changed worker.py. Selected workers retain the existing
read-only store/automatic/worker/acquisition mounts. Actual launcher-generated
scan and worker mounts were captured without executing a production selection,
then used in disposable containers on the unchanged pinned image.

The new frontend retains all 14 previous hashed assets. The reused CSS had the
same hash; no differing-name collision was allowed. Trusted HTTPS serves all 16
files, including the new root and recovery JavaScript.

## Read-only backup status and trust

CB_AUTOMATION_ROOT=/state/automation-public is configured in the rendered Compose
runtime. The API mounts only /srv/community-brain/automation-public read-only.
The new helper published status before API startup and is also invoked by the
current renderer and normal runner ticks.

The public directory is root-owned 0755; its sole checkpoints.json is root-owned
0644. Its validated schema contains only job UUIDs, verified/requires_review
statuses, and the management_attention boolean. It contains no paths, receipt
hashes, credentials, transcripts or model output. Private automation remains
0700/0600 and is not mounted into the API. UID10001 can read the projection and
cannot write it.

The existing September15 job 744d0f3f-8da7-4c12-bc15-5ec0a046518d returns backup
verified through authenticated HTTPS detail. This status comes from its existing
management acknowledgement, which was not changed.

The API alone was recreated with fresh Infisical authority. Existing read-only
CA-bundle mounting and SSL_CERT_FILE/REQUESTS_CA_BUNDLE survived recreation.
The API successfully fetched OIDC JWKS with TLS verification, so no extra CA
mutation or certificate reissuance was required. Trusted ingress and retrieval
checks passed; retrieval returned three hits. No provider/queue credentials were
introduced into the API or frontend. Models and network publication stay disabled
in the API.

## Verification and preservation

- All four handoff document hashes, packet file hashes and expected r019 base
  hashes verified before rollout.
- Credential-free UID10001 containers with network disabled verified the actual
  scan/worker module hashes and API modules, including archive.py and the new
  resume route. No production fixture submission or recovery action was made.
- Deployment verification covers installed bytes, mounts, live read paths and
  controls. Forge's packet evidence supplies the broader 963 application,
  60 disposable PostgreSQL/JetStream, overlapping 25 focused, 6 frontend-unit
  and 5 browser checks plus TypeScript/build results. Those suites were not
  represented as rerun against production.
- Native policy/claim tests still pass for akadmin and pchouinard in both apps,
  including inactive, nonmember, mismatched identity and unrelated-user denials.
  Before/after Authentik control captures are identical.
- Every database table/schema/sequence fingerprint is unchanged: 4 jobs,
  9 sources, 21 artifacts, 42 model-call rows and 7 attempt rows.
- Files, configuration, corpus and archive fingerprints match exactly:
  88 sessions, 1,924 rows, 1,924 FTS-indexed rows, zero unindexed rows.
- Extraction configuration remains SHA256
  008a6b15d4dd617c2bdf170714e086574ed996ed61534cdd2bb3e8c54de09de1,
  retaining z-ai/glm-5.3-flash. Token-renewal definitions, image digest and
  independent management/recovery fixes are preserved.
- Source/live current renderer, launcher and recovery inventory are updated
  together; six files match their recorded hashes and compile. git diff --check
  passed. Only these three management-library definitions changed.

No production acquisition, processing, generative model call, reindex, publication,
retirement, historical replacement, migration or request016 Mac-permission work
was performed. The read-only retrieval probe used the existing retrieval path.
No active or eligible work, attention marker or pending checkpoint was found.

The scheduled new runner returned idle at 2026-09-17T02:44:05.697416+00:00. Mac management
confirmed enabled, unpaused, idle, with no attention or pending checkpoint at
2026-09-17T02:44:18.774686+00:00. The scheduled public projection still reports verified.

## Effective pins

```json
{
  "changed_packet_files": [
    "automatic_host.py",
    "jobs/api.py",
    "jobs/automatic.py",
    "jobs/runtime.py",
    "jobs/store.py",
    "jobs/worker.py",
    "scan.py"
  ],
  "extraction_config_sha256": "008a6b15d4dd617c2bdf170714e086574ed996ed61534cdd2bb3e8c54de09de1",
  "frontend": "/srv/community-brain/workspaces/cbm-workspace-recovery-20260917-frontend",
  "frontend_files": 16,
  "frontend_sha256": "564a565276db86eda41352ce7f490f1d8fcc548ecc26a468795b6d03243b15ee",
  "image": "community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449",
  "packet": "/srv/community-brain/workspaces/cbm-workspace-recovery-20260917-effective-r020",
  "packet_sha256": "e3ba6ed250d64881f2d6d1c3bcf70b0515e90ab1f23fe0ca1133cf9d4400fabd",
  "preserved_assets": 14,
  "runtime_sha256": "cf22ff3ce1c026e8edc24cb8ef34bef1e38f69d19edbbb6ae31bd41c4ce29d11",
  "compose_sha256": "fd4f21aa5e818ec867586cd3b239b2cb01e5e03cc362319833b09d3a3b564d87",
  "boot_guard_sha256": "70d93cdde9d2360294b5e960dfd4586ec20184bc2bdae69be1dbb148d347f7ac",
  "recovery_inventory_sha256": "8a4546272cafaccb5e4f291161424527e3d93ac580aaea6d7755f083e6bc6168"
}
```

## Recovery copies and rollback

Private Mac evidence:
/Users/pchouinard/.local/state/community-brain-management/request020/
VM109 before/after:
/srv/community-brain/artifacts/cbm-recovery-20260917-020/{before,after}/
Verified off-host copies:
/var/backups/community-brain/recovery-020-{before,after}/

before-receipt.json and after-receipt.json record file sizes and SHA256 values.
The after capture intentionally includes the deployment pause; deployment.json
records its later removal after successful checks. Recovery inventory includes
the new effective packet, frontend and public projection. Mac control captures
exclude Infisical bootstrap credentials. Historical checkpoint evidence remains
unchanged. rollback.md requires checking any new recovery generations before
returning to r019, whose scheduler cannot execute safe-resume generations.

Source controls and journal remain uncommitted in forge-inspection-access.
Unrelated dirty work is preserved. No pushes or parent gitlink updates.
