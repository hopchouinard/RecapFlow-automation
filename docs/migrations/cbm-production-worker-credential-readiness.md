# Bounded production worker credentials delivered

September 10, 2026. Completed the Mac delivery requested in
`cbm-production-worker-credential-handoff.md`. This provisions credentials only;
no private submission API, worker, job submission or model request was started.

Infisical remains authoritative: `homelab/prod /applications/community-brain`.
The new dedicated provider key is named `community-brain-prod-bounded-20260910`,
stored as `CB_BOUNDED_OPENROUTER_API_KEY`, and mapped to `CB_OPENROUTER_API_KEY`
only in the model bundle. The development key was not reused or changed.

Provider verification: **limit US$2, usage US$0, remaining US$2**; non-resetting
(`limit_reset=null`), BYOK usage included, not a management key. Verified with the
key-information endpoint; no paid request was made.

VM109 files, all root:root 0600 under `/etc/community-brain-production` (0700):

| File | Contents | Consumer |
|---|---|---|
| `bounded-model.env` | Only `CB_OPENROUTER_API_KEY` | Bounded rehearsal worker |
| `rehearsal-api.env` | Existing runtime DB URL/public OIDC settings, separate one-identity hash map | Internal-only temporary submission API |
| `rehearsal-client.env` | `CB_REHEARSAL_OPERATOR_TOKEN`, `CB_REHEARSAL_EXPIRES_AT` | Short-lived submission client only |

Temporary identity scope is exactly `community-brain`. Permissions are exactly
`sources:upload`, `jobs:submit`, `jobs:read`, `artifacts:read`.
Expiry is **September 11, 2026, 02:05:38 UTC**, Unix `1789092338`.
Authoritative temporary secret keys: `CB_REHEARSAL_OPERATOR_TOKEN`,
`CB_REHEARSAL_EXPIRES_AT`, `CB_REHEARSAL_SERVICE_IDENTITIES`.

Infisical round-trip, delivered bytes, ownership and modes passed. Existing
`api.env`, `migration.env`, `worker.env` and `probes.env` were byte-for-byte
unchanged. Patrick's public claims and monitoring identities were not edited.
The immutable image accepted the temporary identity with exactly the required
permissions and rejected it after simulated expiry, in a disposable offline
check. No model credential was used by that check; the container was removed.
The temporary Mac key-import file was removed after verified Infisical persistence.

Forge owns the bounded exercise described in its handoff: internal submission API
without a host port, exactly two approved synthetic jobs, dedicated model cap,
no indexing, acquisition or publication. Check the remaining allowance immediately
before execution. The renderer refuses expired windows and refuses a consumed key
on rerun, so rerendering cannot silently replenish or extend the exercise.

Existing monitoring credentials share the same deadline. No renewal was performed.
Cutover, publication and retirement remain gated.

Public evidence:
`cbm-production-worker-credential-receipt.json` and
`cbm-production-worker-credential-validation.json`.

Provider contract: [OpenRouter key limits](https://openrouter.ai/docs/api/api-reference/api-keys/create-keys).
