# Request020 — production rollout verified

2026-09-17. Patrick approved the rollout; home.servers completed it. Forge
verified the receipt and supplemental fingerprint hashes, all three new frontend
files over trusted HTTPS, all seven backend files (including the documented scan
worker mount adjustment), and actual API mounts. The local host source now
includes that exact deployment adjustment; all seven host tests pass.

Authenticated API detail for the existing September15 job reports processing
succeeded, indexing complete, backup verified. The API has only the read-only
public backup projection, not the private automation directory. Runner idle at
02:49:05 UTC; no pause, attention or pending checkpoint.

Forge's direct VM-origin HTTPS probe received an ingress 403; the authenticated
API check instead used the existing guest-bound API address. Forge verified
public HTTPS frontend bytes separately. home.servers' completed receipt records
successful authenticated HTTPS, TLS/JWKS, retrieval and both human policy checks.
No ingress/auth configuration was changed to accommodate the inspection.

Management's before/after database, corpus and managed-file fingerprints match:
4 jobs, 9 sources, 21 artifacts, 42 model-call rows; 88 sessions and 1,924 indexed
rows with none unindexed. No acquisition, retry, processing or reindex was run.
Read the preserved safe evidence in receipts/cbm-recovery-020/.

Effective backend: /srv/community-brain/workspaces/cbm-workspace-recovery-20260917-effective-r020
Effective frontend: /srv/community-brain/workspaces/cbm-workspace-recovery-20260917-frontend

Patrick confirmed browser acceptance with “yes”: the new progress indicators are
visible on the September15 run. Request020 implementation, deployment, independent
verification and browser acceptance are complete. No failed job was manufactured
or successful meeting rerun for acceptance.

CBM-08 still retains its two successful weekly-cycle and both-output-path gates;
this UI acceptance does not close the whole migration. Remote publication,
retirement, CBM-09 and final CBM-10 quality review retain their separate gates.
