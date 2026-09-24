# CBM-NAVIGATION-20260910-010: completed

The requested date tree and New meeting frontend are deployed. Patrick's existing
human account has exactly two additional Community Brain permissions:
jobs:submit and sources:upload. No production meeting, upload, provider call,
worker, publication, corpus replacement or retirement was executed for acceptance.
Patrick must sign out/in for refreshed signed claims and visually accept the form.

## Precisely scoped human grant

Established account ID6 was verified live as active pchouinard, then bound by BOTH
that database ID and its existing UUID. The UUID fingerprint is recorded in
 auth-checks.json. Mapping962deddf-1792-4e27-9e01-b0c9249dae2b is exclusive to
Community Brain provider8. The original application/group policy, provider,
issuer/audience, mapping scope and existing read grants remain unchanged.

Before: jobs:read, artifacts:read, retrieval:read.
After, for the matching active Patrick account within the existing operator group:
the same three permissions plus jobs:submit and sources:upload.
No aliases, retry/rerun/reconcile, metrics, publication or management grants were
added. Other operator-group members keep read-only claims; nonmembers get none.
All service identities and restricted collector permissions remain unchanged.

Six Authentik expression cases passed: actual Patrick member, actual nonmember,
in-memory non-Patrick member, Patrick nonmember, wrong UUID and inactive Patrick.
Only the first receives the two added permissions. Actual provider claim previews
and application-access checks passed for Patrick and the existing nonmember
account5. No login/token was minted and no real membership was altered by tests.
The initial negative-case harness incorrectly passed Patrick as the evaluator user;
that failed before saving. Correcting the evaluator user yielded the six passing
cases. The single expression change committed transactionally and its exact hash
and exclusive provider binding were subsequently reread outside the transaction.

Before expression SHA256:
1549b87cbcfc43a7427b0557155bf677f3477a76480e1b7be902284f5d967fc2
After expression SHA256:
f1ad8f91c3a4219b49b00858597df176b934783e9f036616d31662527bff0a71

## Frontend and invariant checks

All three supplied assets matched Forge's manifest. Six previous hashed assets
were retained without collisions, giving nine pinned static files. Only the
API static bind changed; the backend image, entire API environment, archive
modules/dataset, hidden synthetic IDs and worker packets remain unchanged.
The existing Mac renderer retains all prior archive/module/static checks and
adds the new static manifest pin before fresh-authority API-only recreation.

Runtime manifest before:
943daa14a4821e50d215b43780770720ea0ff9c4fbc071824ef5e7b5421db610
Runtime manifest after:
54353de6e2489db57bb8835844a6e5ff72b8d7c1abdb4a8feafad7eca5d7a488
New static manifest:
7b2f6cebf4f15aa7e33aaae3c77bf99e9d57682edc60535aa64fbd76537e0bb5
Current Mac helper:
3f2585765bb8f442d69592f6f6a0295412d1bed3a419c24f28eea70a2e80fef9

Eleven HTTPS static/root/callback checks and all15 service auth/scope checks
passed. The87-date catalog and all481 preserved download hashes/headers passed.
Only the real job appears; both synthetic jobs and all nine synthetic artifact
URLs remain hidden. All six real-job artifacts pass hash/size checks. These are
service-token checks, not evidence of Patrick's actual browser login.

API is healthy with13 cue rules; only API and Alloy are running. Original mount
modes remain intact, with writable managed files and read-only corpus/config,
archive/modules/static. Provider/queue credentials remain absent from API.
Prometheus and Kuma checks passed. Actual cached Open WebUI returns ten sources
and context using the unchanged function and accepted retrieval URL.
All ten DB fingerprints/counts/schema and every managed-file/corpus/config/archive
hash remain unchanged. Three jobs and29 model calls remain. Terminal ownership,
masked/inactive deadline units, held legacy writers/cron/intake and all2,867
immutable inodes are intact. No production test records were created.

Forge's fake-API browser tests cover keyboard navigation, search, form/timezone
validation and upload behavior. Management verified exact deployed bytes and
live read/auth/data behavior; actual human sign-in and selected real submission
remain later acceptance, not fabricated production tests.

## Private recovery and rollback

New static path: /srv/community-brain/workspaces/cbm-navigation-20260910/.
Preserved VM109 before-state:
/srv/community-brain/artifacts/cbm-navigation-20260910/.
Preserved Mac/helper/Auth snapshots:
~/.local/state/community-brain-management/navigation-010-before/.
Two root0600 verified off-host archives under platform-db
/var/backups/community-brain/navigation-010/ preserve static/recreation controls
and original/new Authentik mapping/policy snapshots. Exact paths, sizes and hashes
are in recovery-copies.json. Off-host member checks verified all nine static files,
current helper/recovery inventory and that original/new mapping differs only in
its expression. No snapshot contents or secret values are exposed in the relay.

POST-MANUAL-JOB.md now includes the active navigation frontend/pin and explicit
human grant policy along with the unchanged request009 archive/source inventory.
Prior application checkpoints and archive backups remain immutable and retained.

Controlled rollback if verification fails or specifically requested: preserve
current evidence; restore the saved manual overlay/runtime manifest and prior
pinned Mac helper to both operator checkout and installed management location.
Restore ONLY this mapping's prior expression after verifying the current
expression hash/exclusive app binding; retain provider, application policy,
service identities and other settings. Render current Infisical authority and
recreate API only. Never restore api.env.before. Verify prior archive UI/assets,
read-only human claim evaluation, service scopes, health and data invariants.
An expression rollback affects newly issued claims; any previously issued signed
access token remains subject to its existing15-minute lifetime. Do not claim
instant revocation solely from changing the mapping. Keep all checkpoints and
legacy guards intact. Rollback was not required or executed.

No blocker. Next human acceptance is sign out/in, check the date tree and New
meeting form, and submit only an explicitly selected real meeting when intended.
No later migration phase is authorized by this receipt. Companion hashes are in
receipt-manifest.json.
