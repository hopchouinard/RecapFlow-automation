# Request018 completed — Community Brain human access

Request: CBM-AKADMIN-20260917-018
Actor: home.servers
Completed: 2026-09-17 UTC

## Outcome

Existing active akadmin (pk4, UUID dfae6a7f-e5a5-4575-9796-8187cbdd45b1)
now has the same human application access and claims as pchouinard (pk6,
UUID 36812476-ed34-4073-a1a5-ae3ad53b1781), independently in both applications.

Production/provider8: jobs:read, artifacts:read, retrieval:read, jobs:submit,
sources:upload. Development/provider7: jobs:read, jobs:submit, jobs:retry,
jobs:rerun, jobs:reconcile, sources:upload, artifacts:read, retrieval:read.
No development-only permissions were added to production.

## Before and exact changes

Actual before-policy evaluations denied BOTH users in BOTH apps: policy mode
all required the app operator group AND platform-admins AND platform-operators
AND platform-users. pchouinard's mapping preview nevertheless carried the listed
permissions; akadmin's preview was empty. This was a real app-local access
misconfiguration, not a reason to add either user to shared platform roles.

Added only akadmin to community-brain-operators and
community-brain-dev-operators. pchouinard's identity and memberships are unchanged.
For each app, retained its operator-group binding, disabled its three app-local
platform-group bindings, and added one dedicated identity expression policy and
binding. Existing shared groups/policies and unrelated apps were not modified.

Both custom scope mappings and both new access policies require an active user,
the exact authorized pk/UUID pair, and the intended app-specific group. Being an
Authentik administrator alone grants nothing. Mapping associations remain exclusive
to their intended provider. Exact object IDs and new expression hashes follow:

```json
[
  {
    "application": "community-brain",
    "added_group_member": 4,
    "group_id": "69a3fcd8-fc2d-4ad2-b565-41f15c40701a",
    "disabled_app_binding_ids": [
      "429c32af-d1cd-4cb3-9d4f-718dacca6c25",
      "cf61fe38-9099-4f7c-beee-aef80dfc20fb",
      "5afbf6b7-7013-4e07-8fe1-26ad03e0f548"
    ],
    "created_policy_id": "5f11c03f-6301-4fcc-9a47-c2d8049dd33a",
    "created_binding_id": "bc75bc43-f164-412b-962b-11bcbc00369a",
    "mapping_id": "962deddf-1792-4e27-9e01-b0c9249dae2b",
    "policy_expression_hash": "ac948805d69c689bf46adc112534003f2b66082e51aea309dee2cdb95bf899c6",
    "mapping_expression_hash": "3f952d847e69b13d106ccf0924c2693a9413ce621b9c56bec600b1250aae37d2"
  },
  {
    "application": "community-brain-dev",
    "added_group_member": 4,
    "group_id": "291e026d-b5d5-4871-beb2-af01750233b3",
    "disabled_app_binding_ids": [
      "6d8de529-0bdd-4319-8115-e305b54dedca",
      "93d5968f-3657-4765-bfc0-f76b58f630e9",
      "759f9f6e-d0d6-4d01-a983-b02720e19bb4"
    ],
    "created_policy_id": "bf02dd69-cc4f-468b-853e-35535c75ad08",
    "created_binding_id": "82ff61aa-4ea2-4e01-97b3-04bb9aa793b5",
    "mapping_id": "a3b5a36d-daa8-41d2-852a-83a6dfc6534f",
    "policy_expression_hash": "dfb100dae08bcfae40efb7d99a67935667cd9dd3d306722a4932a41f75138b86",
    "mapping_expression_hash": "83ca8631ad1429fd03bbee11629c34722551ced326ef19a0293b0bb627fdf279"
  }
]
```

## Verification

Ran the installed Authentik PolicyEngine with cache disabled and native
ScopeMapping.evaluate previews, before the transaction, inside it, and again
from a separate post-commit process. Both users are allowed, and permissions are
equal within each app. Eighteen positive/negative cases passed: real identities,
in-memory inactive identity previews, nonmember previews, mismatched pk/UUID
previews, and an unrelated real active user. An additional sweep denied all
three other active accounts on both apps (six actual evaluations), with empty
custom claims. No test accounts, password changes, or login impersonation.

Provider definition hash, unrelated application/binding/mapping hashes, group
definition hash, and all non-target group memberships are unchanged. This covers
OIDC provider fields including issuers, clients, redirects, lifetimes, flows,
keys and provider credentials without disclosing their values.

## Current controls and recovery

Updated both current provision-auth.py definitions, current public-settings.json
renderer inputs, and source/live management_controls.py. Added human_access.py
as the shared exact identity/per-app permissions definition. Current recovery
capture now verifies both apps, exact claims and policies, active bindings,
memberships, active identities, and mapping/provider exclusivity. General
historical checkpoint evidence was not rewritten.

Private before state: /Users/pchouinard/.local/state/community-brain-management/request018/before.json
Private original controls: same directory, before-controls/
Private current capture: same directory, current-recovery/
VM109 current copy: /srv/community-brain/artifacts/cbm-akadmin-20260917-018/current-controls/
Off-host copy: /var/backups/community-brain/akadmin-018/current-controls/
Both copies were hash-verified. Supplemental source-renderer bundle and final
control hashes are stored under each request018 source-controls/ directory.
See current-controls-receipt.json and changed-controls.json for individual hashes.
The earlier current-controls/changed-controls.json captures the first control
update; source-controls/changed-controls.json adds the two renderer metadata files.

Extraction configuration remains at SHA256
008a6b15d4dd617c2bdf170714e086574ed996ed61534cdd2bb3e8c54de09de1,
including the authorized z-ai/glm-5.3-flash change. It was included in the new
current-control copy. No jobs, model calls, re-extraction, publication, service
identity, renewal or budget changes were performed. No services were started on
VM108 (the VM itself was observed running). Request016 permission work remains
stopped. Existing automatic management remains idle with pending/attention false.

Source edits remain uncommitted in the existing forge-inspection-access worktree;
its unrelated dirty work was preserved. No pushes or parent gitlink updates.

## Rollback and browser acceptance

rollback.md describes removal of only akadmin's grant while retaining working
pchouinard access and the app-local policy correction. Blindly restoring the old
four-group AND would restore the original denial and is not the scoped rollback.

Patrick confirmed in the conversation after implementation: "I confirm browser login worked correctly". Human browser acceptance is complete. The agent did not impersonate akadmin or obtain browser credentials; no credential or token values appear in this receipt.
