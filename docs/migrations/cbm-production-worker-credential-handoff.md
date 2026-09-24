# Bounded worker credential delivery — authorized US$2 total

Patrick approved the bounded production-worker phase on September 10 and explicitly
set its total OpenRouter cap to **US$2**. This supersedes the proposal's earlier
US$1 figure. Do not reuse the US$5 development key. This delivery needs no further
routine authorization and does not activate processing by itself.

## Management delivery

Use the existing Mac management renderer and Infisical authority
`homelab/prod /applications/community-brain`. Deliver root:root 0600 files under
the existing 0700 `/etc/community-brain-production` on VM109:

- `bounded-model.env`: only `CB_OPENROUTER_API_KEY`, from a new dedicated production
  rehearsal key. Provider-side limit **2 USD**, `limit_reset=null` (non-resetting),
  `include_byok_in_limit=true`, not a management key. Verify current key usage and
  remaining allowance and report those numeric fields only. Do not make a model
  request or change the existing development key.
- `rehearsal-api.env`: same scoped production runtime DB URL and public OIDC
  settings as `api.env`, but a separate service identity hash map containing only
  the temporary rehearsal operator. Scope `community-brain`, permissions exactly
  `sources:upload`, `jobs:submit`, `jobs:read`, `artifacts:read`. Set a concrete
  expiration no later than September 11, 2026, 02:05:38 UTC. If that window is no
  longer usable, coordinate explicit renewal instead of silently extending it.
- `rehearsal-client.env`: raw `CB_REHEARSAL_OPERATOR_TOKEN` and Unix-seconds
  `CB_REHEARSAL_EXPIRES_AT` for the above identity. Only the short-lived submission
  client receives this file's contents; never the API or worker.

Keep existing public `api.env`, Patrick's read-only claims and monitoring
identities unchanged. The separate rehearsal API bundle is intended for a
short-lived internal-only API container with writable immutable-file storage and
no host port, used solely to submit the two approved jobs, then removed. The
public staging API continues to mount those files read-only, allowing Patrick to
inspect resulting artifacts without gaining submit permission. Do not start the
private API or worker from management; Forge owns the bounded exercise.

Existing `worker.env` queue credentials remain separate and disabled by default.
The bounded worker will receive only DB, queue and the new model credential,
read-only preserved config, and writable files; no Fathom/Git/publishing secret.
All other processing, recurring intake, indexing and publication stay disabled.
No application database management credentials are required.

Return a readiness receipt with file paths, permissions, exact granted scopes,
expiry and numeric provider allowance verification, without any secret values.
Existing monitoring probes expire September 11 at 02:05:38 UTC; renew through the
already documented coordinated process if staging continues past that deadline.

## Forge readiness evidence and remaining application work

Implemented `production-staging/bounded_worker.py` and copied the exact existing
synthetic fixture bytes into `synthetic-fixture.json`. The runner accepts exactly
one weekly and one transcript-backfill job ID, checks their meeting identity and
source bytes (including frozen aliases), and refuses previous attempts/model
intents or previously dispatched events. It dispatches only those two processing
stages, with no indexing, publishing or acquisition handlers. Twelve requests per
job, twenty-four maximum for the exercise; provider-side US$2 allowance checked
before each actual model request. Uncertain outcomes stop the exercise.

All 28 disposable PostgreSQL/JetStream tests passed, including synthetic execution,
no indexing attempts, no replay, modified-source rejection, quota/request guards
and uncertain-outcome stop before job two. Live connection-only check using the
installed immutable image passed TLS-first, scoped inbox and binding the existing
consumer. It fetched/published zero messages. The general production worker was
not started. TLS checking created only a short-lived check container, now removed.

After delivery: verify allowance and fixture model availability without paid calls;
prepare the internal submission container/client and capture exactly two job IDs;
freeze/check helper hashes; run each processing stage once; verify all resulting
artifact hashes through the public read API. Check original corpus/config hashes
remain unchanged. Preserve intents on failure; do not silently retry. Then request
coordinated DB/files backup and isolated restore acceptance with the two real
synthetic job records. Production job creation and model processing have not yet
occurred. No claim of a finished production worker rehearsal is made here.
