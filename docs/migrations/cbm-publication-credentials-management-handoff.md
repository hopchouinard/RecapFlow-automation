# Request022 — approved scoped publication credential preparation

Target: home.servers. Patrick explicitly approved provisioning scoped GitHub write
credentials for the automation and distribution repositories while keeping
publication disabled, and instructed Forge to create this request in HANDOFF.
Request021 is verified and acknowledged. No further approval is pending for the
credential preparation described here.

## Authorized work

Provision Infisical-managed publication credentials limited to these repositories:
- hopchouinard/RecapFlow-automation
- hopchouinard/community-brain-distribution

Use the existing management credential mechanism where it can meet the scope.
Required repository permissions: metadata read and contents write (Git commits
and release assets). No organization-wide access, unrelated repository access,
administration, workflow write, branch-protection bypass or provider/model access.
Do not broaden an existing shared credential or disturb existing credentials.
Record the actual mechanism, repository restrictions, expiry/renewal arrangement
and private Infisical storage paths. If the supported mechanism needs Patrick's
interactive action, return the precise action; never ask him to paste a secret
into the handoff or Forge conversation.

Prepare private runtime delivery solely for the future separately gated
publication oneshot. A new publisher-only bundle may be rendered privately on
VM109 under /etc/community-brain-production/ with root ownership and mode0600;
report its actual path and intended consumption. Do not modify existing API,
processing, acquisition, probe or other worker env files. Do not add credentials
to any running container, browser, source checkout, handoff or log. No service
restart, application deployment or publication worker activation is requested.

Perform read-only identity/repository/permission checks. Inspect branch protection
and report whether the proposed delivery flow needs a separately reviewed PR or
additional permission. Do not request extra grants or mutate a remote repository
as a capability test. Clearly distinguish verified permission metadata from an
untested Git push/release operation.

## Boundary that remains in force

CB_ENABLE_NETWORK_PUBLICATION stays false. No Git push, remote branch/tag/draft/
release/asset creation, PR, publication-stage enqueue, candidate upload, model
call, processing, reindex, historical replacement or retirement. Request016 Mac
permission work stays stopped. Keep the existing weekly runtime and credentials
unchanged; this request grants no permission to expand the weekly selector.

The private v1.2.0 candidate and September15 six-file scope are documented in the
companion readiness report for context only. Neither the candidate nor its
proposed repository branches/version has publication activation approval. That
later review will bind exact content hashes, target branches/commit, live worker
controls and recovery receipts. Do not publish the dirty Forge migration checkout.

## Return receipt

Write responses/CBM-PUBLICATION-CREDENTIALS-20260917-022/status.json and receipt.md,
plus hashed safe evidence. Include:
- credential type and nonsecret identity, exact repositories and permissions;
- Infisical paths and any private publisher-only rendered path/modes;
- expiry/renewal behavior and relevant branch-protection findings;
- what read-only checks passed and which write operations remain untested;
- evidence existing credentials/runtime/publication-disabled controls are unchanged;
- any concrete remaining management blocker.

Never include token values, private keys, bootstrap credentials or environment
contents. Report completion of credential preparation separately from publication,
which remains prohibited by this request.
