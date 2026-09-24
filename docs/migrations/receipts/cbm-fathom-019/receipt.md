# Request019 completed — Fathom production rollout

Request: CBM-FATHOM-20260917-019
Actor: home.servers
Completed: 2026-09-17 UTC

## Result

Deployed Forge's approved six-file partial packet as a new effective overlay on
current r016. Only jobs/acquisition.py, selected_fathom.py, and the one-line
manual_host.py module-mount loop changed in the worker packet. All other files
match r016, preserving its attention handling and weekly $5 guards. The original
r016 directory and historical checkpoint evidence remain unchanged.

The new acquisition module is mounted read-only in the real worker launch path:
`/srv/community-brain/workspaces/cbm-fathom-20260917-effective-r019/jobs/acquisition.py`
→ `/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs/acquisition.py`.
The scheduled boot guard points to the new automatic_host.py; that launcher uses
the new manual_host.py, which invokes manual_worker.py and SelectedFathom.
Actual launcher arguments were captured using fixture environment/state, then
its actual helper/jobs mounts were used in a disposable, network-disabled
container on the unchanged pinned image. The imported module path and hash were
verified inside that container. No production worker/job was executed for testing.

The UI uses the approved root and new hashed assets, retaining all 13 previous
hashed assets without collisions. Fifteen files are served from the new frontend
bundle. Current Compose, runtime manifest, source/live renderer, boot launcher,
and recovery file inventory now select the new packet/frontend. Source and live
Mac controls have matching bytes. The API alone was recreated with freshly read
Infisical authority; provider credentials remain outside the API and frontend.

## Verification

- Packet and handoff document hashes matched Forge's manifest.
- Disposable HTTP fixture checks passed for full URL and numeric call ID,
  native recording ID, trusted url/share_url resolution, ±600 seconds accepted,
  ±601 seconds rejected, exact identity/time checks, five metadata pages maximum,
  disabled metadata extras, one selected transcript, and rejection of unrelated
  requests. Supplied timezone/date metadata stayed unchanged.
- Trusted HTTPS verified all 15 static files, root and callback hashes, health,
  authorized reads, denied unauthenticated/invalid/collector job reads, and
  automatic_processing=true.
- API Docker health is healthy. Its five jobs mounts and frontend mount point
  at the new effective directories. The image digest is unchanged.
- Authentik native access/claim checks passed for akadmin and pchouinard in both
  apps, including inactive/nonmember/mismatched/unrelated denial cases. Current
  Authentik control capture is identical before and after this rollout.
- Database schema, sequences and every table fingerprint match before/after:
  4 jobs, 21 artifacts, 9 sources, 42 model-call rows. No model-call increase.
- Files, config, corpus and meeting archive fingerprints match exactly:
  88 sessions, 1,924 rows, 1,924 FTS-indexed rows, zero unindexed rows.
- Extraction configuration remains SHA256
  008a6b15d4dd617c2bdf170714e086574ed996ed61534cdd2bb3e8c54de09de1,
  preserving the authorized z-ai/glm-5.3-flash configuration.
- Before/after private control copies were verified on the off-host backup server.
  No Infisical bootstrap credentials were included in the Mac-control archives.

No production meeting submission, transcript fetch, model call, reindex,
September15 replay, token renewal, budget change, or broader migration occurred.
Scheduled renewal definitions are unchanged. Request016 Mac-permission work
remains stopped. Publication/replacement/retirement gates remain unchanged.
Manual-transcript fallback and friendlier acquisition errors are outside this
patch and are not claimed fixed. Browser scenarios were Forge's pre-rollout
packet evidence; this deployment verified served bytes and backend fixtures.

The scheduled runner returned idle at 2026-09-17T02:10:04.965219+00:00. Mac management
confirmed idle, enabled, unpaused, with no attention or pending checkpoint at
2026-09-17T02:09:29.610065+00:00.

## Effective pins

```json
{
  "changed_packet_files": [
    "jobs/acquisition.py",
    "manual_host.py",
    "selected_fathom.py"
  ],
  "extraction_config_sha256": "008a6b15d4dd617c2bdf170714e086574ed996ed61534cdd2bb3e8c54de09de1",
  "frontend": "/srv/community-brain/workspaces/cbm-fathom-20260917-frontend",
  "frontend_files": 15,
  "frontend_sha256": "0a08992b6c77668fce774bf609d4b92897ee9d4eb59a6adda4b5f165939e1599",
  "image": "community-brain@sha256:be0e7d818334bcd08b494d71b3582cd51a12e2e246c03c2414e01d9cb9b10449",
  "packet": "/srv/community-brain/workspaces/cbm-fathom-20260917-effective-r019",
  "packet_sha256": "f5e7afe55d4034a1723b6df27584a35db7e3bba9b9ae9b8e7fced8ae047710eb",
  "preserved_assets": 13,
  "runtime_sha256": "a77105d642729ecb70843f71be35ec8288eac7dcce829381eb6a6bd44813ca43",
  "compose_sha256": "43ba00cfac282a75543c4fd24265c7c123438da2fdce08890ea13506f6841067",
  "boot_guard_sha256": "81fe3cb7c6921060a31d74e5ba3e40970451f299ff8525dce16a5379fe9d3b35",
  "recovery_inventory_sha256": "a89c6188bb798bdbbcd2606935569100c60a0ff047a75df35445bd648ec74e48"
}
```

## Current control copies and recovery

Private Mac evidence:
/Users/pchouinard/.local/state/community-brain-management/request019/
VM109 before/after:
/srv/community-brain/artifacts/cbm-fathom-20260917-019/{before,after}/
Off-host before/after:
/var/backups/community-brain/fathom-019-{before,after}/

before-receipt.json and after-receipt.json contain verified individual file hashes.
The after archive intentionally captured the deployment pause; deployment.json
records its subsequent removal after health, access, and preservation checks.
Normal restore requires reconciliation and starts paused. Never blindly restore
all historical files. rollback.md describes the scoped runtime-only rollback.

A generated r016 __pycache__/run.cpython-314.pyc was preserved in the before
archive and original directory but excluded from the new immutable packet.
No historical checkpoint receipts were edited. The initial API health check
ran before Docker's health state became healthy; validation then passed without
another API recreation. Preparation retries made no application/data changes.

Source edits and the journal remain uncommitted in forge-inspection-access;
unrelated dirty work is preserved. No push or parent gitlink update.
