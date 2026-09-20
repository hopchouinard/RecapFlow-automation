# Live development identity handoff

Patrick selected separate development Authentik and Infisical identities and
approved a **US$5 total, non-resetting OpenRouter key limit** on 2026-09-09.
No paid calls have run. Development deployments on VM 108 are authorized;
production deployment, cutover and remote corpus publication remain prohibited.

The simulated worker, recovery, restore, retrieval and local publication checks
are complete: see `cbm-development-scenario-results.md`.

## Work for the existing management environment

Forge can administer VM 108 but has only the installed GET-only infrastructure
broker. It has no Authentik administration or Infisical provisioning identity.
Use the existing approved management environment to create this development-only
bundle; do not broaden the inspection broker or transfer production credentials.

### Authentik

- Application/provider name and proposed slug: `community-brain-dev`.
- Public OAuth2/OIDC client; authorization code + PKCE, RS256 signing, no SPA
  client secret. Restrict access to a separate development operator group.
- Initial browser origin: `http://localhost:8090`, reached through an approved
  SSH tunnel to guest loopback `127.0.0.1:8090`. No public/Traefik route is needed.
- Exact redirect: `http://localhost:8090/callback`; post-logout redirect:
  `http://localhost:8090`. Configure the provider's allowed browser origin for
  token/userinfo access as required. No wildcard redirects.
- Current SPA requests `openid profile`. Attach a **development-provider-only**
  profile scope mapping that supplies the following claims; do not change a
  globally shared profile mapping. Ensure these appear in the **access token**,
  not only UserInfo. Authentik's Include claims in id_token provider setting
  controls inclusion in both ID/access tokens according to its documentation.

```json
{
  "cb_scope": "community-brain-dev",
  "cb_permissions": [
    "jobs:read", "jobs:submit", "jobs:retry", "jobs:rerun",
    "jobs:reconcile", "sources:upload", "artifacts:read", "retrieval:read"
  ]
}
```

Apply these claims only to the authorized development group. Do not grant
`corpus:publish` for the live fixture phase. Preserve issuer/audience validation;
return the actual issuer, client ID/audience and JWKS URL from the created
provider/discovery document. Do not infer them from the proposed slug.

### Infisical and development provider key

- Use the existing application's approved Infisical project with a distinct
  **development environment** and proposed path `/applications/community-brain`.
  Confirm actual project/environment identifiers in the return handoff.
- Create a separate OpenRouter inference key named `community-brain-dev` with
  **US$5 limit**, no periodic reset. Do not use a management API key for inference.
  Store it as `CB_OPENROUTER_API_KEY`. Verify the provider reports the intended
  limit before any request. Halt on exhausted/unknown allowance or uncertain calls;
  never substitute a production key. Provider limits are the spending control;
  token estimates alone are not a hard dollar cap.
- The first live exercise uses uploaded synthetic transcript/chat, not Fathom.
  Do not transfer Fathom production credentials or install the Mac collector.
  The worker now configures Fathom only when a key is supplied; manual-input
  jobs need no Fathom key. Acquisition jobs without an adapter fail explicitly.
- Use a separate, short-lived development runtime identity if VM-side Infisical
  retrieval is the established deployment mechanism. Scope it to this environment
  and path. Otherwise use the existing operator renderer to deliver a private
  runtime file on VM 108; no broad Infisical bootstrap identity belongs on Forge.
- For service/API test tokens, create independent opaque tokens with expiry,
  scope `community-brain-dev`, and only the needed permissions. API configuration
  holds SHA-256 hashes plus subject/scope/permissions/Unix `expires_at`; raw tokens
  remain in Infisical and the scoped test process. Human login uses Authentik.

### Return handoff (no secret values in chat)

Provide a small `cbm-live-development-access.md` handoff containing:

1. Actual public OIDC issuer, client ID, expected audience and JWKS URL, plus the
   approved development group and redirect/origin settings.
2. Infisical project/environment/path and the approved VM-side runtime delivery
   command or private runtime-file location. Do not include token/key values.
3. Confirmation that the development OpenRouter key has a US$5 non-resetting
   limit; its non-secret identifier may be recorded for auditing.
4. The trusted public lab CA bundle location for container HTTPS/JWKS access.
   Preserve public roots as well as the lab CA so OpenRouter HTTPS still validates.
5. An approved browser SSH-tunnel path from Patrick's workstation. The dedicated
   Forge key is source-restricted; do not copy it to the Mac or containers.

## Next application steps after that handoff

Create a separate live-development Compose project and private state, with API
bound only to guest loopback. Keep disposable database/JetStream isolated; grant
only the API's required identity egress and worker's required provider egress.
Do not reuse fixture service tokens or the internal-only simulated Compose file
as the live deployment configuration.

Verify discovery/TLS/claims and real browser code/PKCE login first. Validate denied
access for missing/wrong claims and expired service tokens. Then exercise a tiny
synthetic weekly job using the bounded development key, inspect returned usage,
artifacts and statuses, and stop if any effect is uncertain. Live Ollama retrieval
needs a separately verified endpoint/model; synthetic embeddings are not evidence
of semantic relevance. Keep network publication disabled throughout.

References: [Authentik OAuth2/OIDC](https://docs.goauthentik.io/add-secure-apps/providers/oauth2/),
[scope mappings](https://docs.goauthentik.io/add-secure-apps/providers/property-mappings/),
[OpenRouter key limits](https://openrouter.ai/docs/api/api-reference/api-keys/create-keys).
