# Request022 — credential preparation verified

2026-09-17. Forge verified all eight SHA256-listed receipt files and independently
checked publication.env ownership/root0600 and its disabled-publication flag.
The API has no publisher bundle mount or CB_PUBLISHER_* variables and still has
CB_ENABLE_NETWORK_PUBLICATION=false. No token or signing material was printed.

Dedicated App: Community Brain Publication, ID4978270, installation162488086.
Exactly two repositories: hopchouinard/RecapFlow-automation and
hopchouinard/community-brain-distribution. Management verified contents:write and
metadata:read only, including installation-token metadata and repository reads.
No write operation has been exercised. Both main branches were unprotected at
inspection; their heads match the candidate preparation's recorded bases.

Infisical authority: prod /applications/community-brain-publication.
Publisher-only delivery: /etc/community-brain-production/publication.env.
Prepared installation token expiry: 2026-09-17T14:33:43Z. This is not durable
readiness: management must mint and verify a fresh token under the approved
selected-run contract before execution. Do not renew it by exposing the signing
key to Forge or to a workload. No unattended renewal was activated.

Management confirms all19 preexisting runtime files, application secret values
and API identity/environment/mount fingerprints are unchanged. The signing key
is held in Infisical; neither it nor bootstrap credentials are in the publisher
bundle. Credential preparation is complete; publication remains unauthorized.

Evidence: receipts/cbm-publication-credentials-022/.
The first-publication phase proposal documents the exact candidate and remaining
live publisher wiring/rehearsal requirements. Request022 alone does not authorize
publication, production worker deployment or stage transitions.
