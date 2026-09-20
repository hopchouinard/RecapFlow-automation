# Request018 — equal human access for akadmin

Patrick explicitly requested that the existing Authentik user akadmin receive
same access as pchouinard to Community-brain and Community-brain-dev. Preserve
pchouinard access. This authorizes the necessary targeted membership/application
policy and provider-claim changes; no additional approval needed.

Inspect actual active accounts by exact username and stable IDs/UUIDs, both
application/provider relationships, group policy bindings and claim expressions.
Existing documentation: production provider8/community-brain uses operator group
and profile mapping962deddf-1792-4e27-9e01-b0c9249dae2b, with upload/submit additionally
restricted to pchouinard's pk6 AND UUID. Group membership alone is insufficient.
Development provider7/community-brain-dev uses community-brain-dev-operators and
its own mapping. Treat live state as authoritative; fail on ambiguous identities.

Add only existing active akadmin to the app-specific groups/policies needed for
access and extend any identity-specific human permission predicate to include its
verified ID/UUID pair. Match pchouinard's CURRENT effective claims independently
per app; never union dev privileges into production. Document expected before/after.
Last recorded production privileges: jobs:read,artifacts:read,retrieval:read,
jobs:submit,sources:upload. Last recorded dev privileges additionally include
jobs:retry,jobs:rerun,jobs:reconcile. Inspect before relying on those snapshots.
Preserve denial of unrelated/nonmember/inactive accounts. Do not grant access to
all Authentik administrators or change shared policies used by unrelated apps.

Use existing authorized management access. No password/token values in receipts.
Keep OIDC issuers,audiences,redirects,session lifetimes,service identities,renewal,
provider key/budget and publication settings unchanged. Do not start services on
VM108 simply to validate Authentik policy. No jobs/model calls/reprocessing or
remote publication. Request016 stopped Mac permission work remains untouched.

Preserve before-policy/membership/mapping snapshots privately and update current
management desired state/renderers/recovery Authentik-control inventory where
these policies are pinned, so future maintenance preserves the intentional grant.
Do not overwrite historical recovery evidence. Record changed control hashes and
rollback that removes only this grant, keeping pchouinard functional.

Verify actual access evaluation and provider claim previews for pchouinard AND
akadmin on each application; verify permissions equal for those two users within
each app, while unrelated user,nonmember,inactive and mismatched identity cases
remain denied/no new grants. Verify mapping remains exclusive to intended provider.
Return safe hashed completion receipt with exact group/policy changes, per-app
permissions, validation evidence, private recovery-control paths and any limits.
Actual akadmin browser-login acceptance is Patrick's final check; don't ask him
for credentials or impersonate a login. Request017 is complete and acknowledged.

FYI separate authorized config change on September17: production extraction-config.yaml
now has z-ai/glm-5.3-flash for both session_themes and chunk_extraction, SHA256
008a6b15d4dd617c2bdf170714e086574ed996ed61534cdd2bb3e8c54de09de1.
Preserve it during any current-control snapshot/update; this is not an unexpected
drift to roll back. No corpus re-extraction accompanied that change.
