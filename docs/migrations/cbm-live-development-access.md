# Community Brain live development access

Provisioned 2026-09-09 by the Mac management environment for VM 108,
`community-brain-dev.patchoutech.lab` (`10.1.30.20`). Production and remote
corpus publication remain out of scope. No paid inference calls have run.

## Public OIDC settings

| Setting | Value |
| --- | --- |
| Issuer | `https://auth.patchoutech.lab/application/o/community-brain-dev/` |
| Client ID / expected audience | `community-brain-dev` |
| JWKS | `https://auth.patchoutech.lab/application/o/community-brain-dev/jwks/` |
| Discovery | `https://auth.patchoutech.lab/application/o/community-brain-dev/.well-known/openid-configuration` |
| Browser origin | `http://localhost:8090` |
| Exact callback | `http://localhost:8090/callback` |
| Exact post-logout redirect | `http://localhost:8090` |
| Requested scopes | `openid profile` |
| Client / flow | Public client, authorization code; SPA must use PKCE S256 |
| Signing / token lifetime | RS256; access token 15 minutes |
| Development group | `community-brain-dev-operators`, initial member `pchouinard` |

A provider-specific profile mapping grants `cb_scope=community-brain-dev` and
`jobs:read`, `jobs:submit`, `jobs:retry`, `jobs:rerun`, `jobs:reconcile`,
`sources:upload`, `artifacts:read`, `retrieval:read` only to that group.
`corpus:publish` is absent. Include claims in ID/access tokens is enabled.
Provider ID 7, application UUID `ffba89e6-6641-452e-aa9c-d804be63f179`.

Authentik 2026.5.3 has no provider-level allowed-origins field in its installed
API schema. Token/UserInfo OPTIONS requests accept the localhost origin, but
also reflect an unrelated origin under the existing shared CORS behavior.
This is not an origin allowlist. Shared CORS was not changed; redirects are
strict. Verify the actual browser code/PKCE exchange and signed access-token
claims before any model call. Management previews are not a completed login.

## Infisical authority and runtime delivery

- Project: `homelab`, ID `a508e594-7686-43a1-9b0f-cafa8b348ad4`.
- Environment: `development`, ID `75941b56-eb02-4200-bbb6-85ca9a59bdd9`.
- Path: `/applications/community-brain`.
- Runtime: `/etc/community-brain-development/runtime.env` on VM 108.
- Scoped test process only: `/etc/community-brain-development/test-client.env`.
- Public settings copy: `/etc/community-brain-development/public.env`.

The directory is root-owned mode 0700; all three files are root-owned 0600.
Forge can use its existing `ssh community-brain-dev` and `sudo -n` access.
Infisical is authoritative; these files are private rendered delivery copies.
No Authentik admin credential, broad Infisical bootstrap identity, Fathom key,
or GitHub publication credential was transferred to Forge or the guest.

`runtime.env` includes `CB_OPENROUTER_API_KEY`, hashed `CB_SERVICE_IDENTITIES`,
public `CB_OIDC_*`/`CB_CORPUS_SCOPE`, and separate development-only
`CB_DEV_POSTGRES_PASSWORD` / `CB_DEV_NATS_PASSWORD`. Construct the isolated
Compose database/NATS URLs from these passwords; no shared database or NATS
service has been configured. Model calls and network publication both start
false (`CB_ENABLE_MODEL_CALLS`, `CB_ENABLE_NETWORK_PUBLICATION`). Enable model
calls only for the approved bounded exercise after authentication checks;
keep network publication disabled.

`test-client.env` holds independent `CB_DEV_OPERATOR_TOKEN`,
`CB_DEV_READER_TOKEN`, and deliberately expired `CB_DEV_EXPIRED_TOKEN`.
The operator has the eight permissions above; the reader has only jobs,
artifacts and retrieval read permissions. All have the development scope.
Valid test identities expire **2026-09-10 19:43:21 UTC** (Unix 1789069401).
The API runtime contains only their hashes/subjects/scope/permissions/expiry.
Load raw test tokens only into the scoped test process, never the app/worker
container, logs, chat, repository, or browser client. Ask management to renew
through Infisical if expired; do not replace them with timeless fixture keys.

Pass the private runtime file to Compose with `sudo docker compose --env-file`
and explicit service environment mappings in the new development Compose file.
Use `config --quiet` for validation; plain `config` can print resolved secrets.
Do not source all test-client values into a general-purpose interactive session.

## OpenRouter allowance

New inference key name: `community-brain-dev`; authority secret:
`CB_OPENROUTER_API_KEY` at the development path above. Provider verification:
US$5 total limit, reset `null` (none), US$5 remaining, usage US$0,
`is_management_key=false`, `include_byok_in_limit=true`.
SHA-256 fingerprint (not a provider key ID):
`eca3a55660240c5b82efe816788bb480d7bf6b06e4c2526db0eb4bbb98abc8b5`.

Recheck authenticated `/api/v1/key` allowance before the first paid request.
Halt for unknown/exhausted allowance or uncertain effects; never substitute
production credentials. No Fathom acquisition or Mac collector is included.

## Container trust and browser access

The guest's `/etc/ssl/certs/ca-certificates.crt` contains public roots and the
lab CA. Bind it read-only at `/run/certs/ca-bundle.pem`, and set
`SSL_CERT_FILE=/run/certs/ca-bundle.pem` and
`REQUESTS_CA_BUNDLE=/run/certs/ca-bundle.pem` for relevant Python clients.
A disposable Python container successfully verified Authentik discovery/JWKS
and OpenRouter public HTTPS with this combined bundle. Preserve public roots.

On Patrick's Mac, using the existing management SSH identity:

```sh
ssh -N -L 127.0.0.1:8090:127.0.0.1:8090 pchouinard@10.1.30.20
```

Then open **http://localhost:8090**, matching the registered callback exactly.
The new API/web service must bind only guest loopback. No public route was added.
Do not copy Forge's source-restricted guest SSH key to the Mac or containers.

## Validation and next action

Passed: authorized-group preview with expected issuer/audience and eight claims;
nonmember denied with no custom claims; Forge sudo access to private files;
service-token hash/expiry checks; container public and lab TLS; capped inference
key verification. No live application Compose project was launched by management.

Continue from `cbm-live-development-identity-handoff.md`: build the separate
live-development Compose project and private state, perform real browser login,
verify signed claims and negative authorization cases, then the tiny synthetic
weekly job within the approved allowance. Verify Ollama endpoint/model separately
before claiming semantic retrieval quality. Keep remote publication disabled.
