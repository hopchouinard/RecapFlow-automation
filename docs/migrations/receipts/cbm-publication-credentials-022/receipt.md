# Request022 completed: scoped publication credential preparation

Request: `CBM-PUBLICATION-CREDENTIALS-20260917-022`  
Actor: `home.servers`  
**Credential preparation completed. Publication remains disabled and unauthorized.**

## Provisioned identity and scope

Dedicated private GitHub App **Community Brain Publication**, slug `community-brain-publication`, App ID **4978270**, client ID `Iv23liMPbFrVbgsr580T`, installation ID **162488086**, owner `hopchouinard`. Registration is restricted to this account. Webhooks, user OAuth installation authorization, and device flow are disabled. No client secret was created.

Installation selection is **Only select repositories**, exactly:
- `hopchouinard/RecapFlow-automation`, repository ID **1176379254**.
- `hopchouinard/community-brain-distribution`, repository ID **1249770482**.

The App, installation, and minted token permission metadata each verified exactly **contents:write** and **metadata:read**. No organization, administration, workflow-write, PR, bypass or provider/model permissions were requested. No shared GitHub credential/App was broadened. GitHub's ordinary public-repository read availability is not an additional private-repository grant; write authorization and installation membership are confined to the two selected repositories.

The original GitHub CLI management OAuth credential has broader `gist`, `read:org`, `repo`, `workflow` scopes. It was not delivered, repurposed or altered.

## Infisical authority and delivery

Infisical environment **prod**, new private path **`/applications/community-brain-publication`**:
- `CB_PUBLISHER_GITHUB_APP_ID`
- `CB_PUBLISHER_GITHUB_INSTALLATION_ID`
- `CB_PUBLISHER_GITHUB_PRIVATE_KEY_BASE64`
- `CB_PUBLISHER_GITHUB_REPOSITORY_IDS`

The private key is base64-encoded for storage, not encrypted by base64; confidentiality is provided by Infisical. Readback matched the written values. Existing `/applications/community-brain` secret values were compared in memory before/after and were unchanged. No old credential or secret folder was replaced.

The browser initially blocked a generated key download. Patrick completed the replacement download; the final GitHub UI shows one key, fingerprint **`SHA256:8vviABYPgwVoYmEN+ijoAHTaa0SpTUWT5JaypQ2Eyno=`**. The inaccessible first key is absent. Download and temporary local key files are removed after successful Infisical readback. No private key contents entered chat, handoff, source or logs.

VM109 publisher-only bundle: **`/etc/community-brain-production/publication.env`**, **root:root0600**, atomic creation with ownership, mode and value readback verified. It contains the scoped token, expiry, nonsecret App/installation/repository IDs, and `CB_ENABLE_NETWORK_PUBLICATION=false`. It contains neither the signing key nor Infisical bootstrap credentials.

This bundle is for a future separately reviewed publisher oneshot only. It is not consumed by a service, and checks found no publisher environment variables or bundle/directory mounts in either running container. Do not source it into the API, processing, acquisition, probe, or existing worker environments.

## Expiry and renewal

The prepared token expires **2026-09-17T14:33:43Z** (**10:33:43 EDT**). It is a short-lived GitHub App installation token, not a permanent PAT. No automatic renewal or publication worker was activated.

At a future approved publication run, management must retrieve the signing material from the above Infisical path, sign an App JWT, recheck installation identity and permissions, mint a fresh installation token with explicit repository IDs `[1176379254,1249770482]` and only `contents:write,metadata:read`, validate metadata and read-only access, then atomically refresh only the publisher bundle. The preparation helper refuses to overwrite an existing bundle; refreshing it must be an explicit management action under the later reviewed oneshot contract. The current token must not be treated as durable readiness after expiry. The App signing key itself has no one-hour expiry and requires explicit managed rotation/revocation; no rotation schedule was installed.

Private management helper retained at `/Users/pchouinard/.local/state/community-brain-management/request022/publisher_credentials.py`. Its preparation and first-render paths ran successfully. Future renewal and publication integration were not executed or certified. The helper does not publish anything.

References: [GitHub App registration](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app), [installation-token scope and expiry](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app).

## Read-only checks and publication limits

Passed: App identity, installation identity/owner/selection/permissions, exact minted permission/repository metadata, GET `/installation/repositories` returning exactly two repositories, both repository GETs and both main-branch GETs using the new token, Infisical write/readback, runtime bundle readback and private permissions.

Both repository default branches are `main`, unprotected. Management checks report Branch not protected (404), empty rulesets and empty effective main-branch rules. Observed main SHAs:
- RecapFlow-automation: `dd29e82aa21f3e52d0ea7a96561f8dec9af28055`.
- community-brain-distribution: `a192f7832e70d60a10de838aa4136b5f3432f15b`.

No current branch protection requires a PR or additional permission. Recheck protection and content/workflow constraints during the later activation review; do not silently add grants. No push, branch/tag/ref creation, release/draft/asset, PR or candidate upload was used as a write test. **Git push and release operations remain untested.** GitHub permission metadata is not a completed publication.

## Existing runtime preserved

All **19 existing files** under `/etc/community-brain-production/` retained identical hashes, ownership and modes. The only added file is `publication.env`. The API container ID, image, start time, complete environment fingerprint and canonical mount fingerprint match the pre-provision baseline. Existing application secrets remained equal. API `CB_ENABLE_NETWORK_PUBLICATION=false` and `CB_ENABLE_MODEL_CALLS=false` remain unchanged.

No service restart/deployment, running-container credential injection, weekly-selector expansion, publication-stage enqueue, processing, model call, reindex, historical mutation or retirement was performed. Request016 permission work stays stopped. The v1.2.0 candidate and six-file scope remain context only; Request022 does not activate publication.

Safe evidence is listed and SHA256-hashed in `receipt-manifest.json`. No secret values, private keys, bootstrap credentials, or environment contents are included. There is no remaining credential-preparation blocker.
