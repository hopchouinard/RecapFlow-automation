# Requested automatic processing of new meetings

Patrick questioned the upload-only behavior and requested that saving a new
meeting trigger processing. The current API already creates a queued processing
stage and transactional outbox entry for complete inputs, but production has no
ordinary worker: migration execution has used explicitly selected oneshot stages.
The upload-only message accurately describes that temporary deployment state.

## Intended change

A successful new manual submission should enqueue and automatically execute its
processing stage once the required transcript/chat sources are present. The browser
must return promptly with durable queued/running/progress states and eventual
Markdown previews/downloads. Provider credentials remain worker-only; Authentik
human upload/submit scopes do not expand. No browser-held worker/model credentials.

Use the existing PostgreSQL/JetStream/Compose architecture. A persisted eligibility
marker must be assigned only to newly accepted submissions after activation, in
the acceptance transaction. Never infer eligibility from merely queued state:
production retains three older unsent indexing events, including excluded
synthetics and September8's existing-session collision. Existing jobs, reruns and
preserved history must not be silently opted in or replayed by a general sweep.
Honor idempotency, single-worker selection/claim locks and unknown-outcome stops.
The generic serve() recovery/outbox sweep must not be enabled unchanged.

Keep the existing non-resetting US$2 provider cap and per-request allowance checks;
no top-up or new spend policy is inferred. Last settled remaining balance was
US$1.607892834; recheck before live activation/calls. Exhaustion or uncertain calls
must produce a visible stopped/attention state rather than repeated spend.
No existing-session replacement, remote Git/distribution publication, board posting,
recurring Fathom discovery, old service retirement or final-quality changes.

## Approved scope

Patrick answered **“Do the full loop”**: new submissions automatically acquire
only the selected Fathom transcript when needed, generate recap Markdown, and
index the new meeting for Open WebUI. Remote publication remains disabled.
Existing history and reruns never inherit automatic eligibility.

Implementation uses the existing selected-stage worker, invoked by a nonoverlapping
cron launcher. Generation/attempt guards, provider budget checks, durable execution
markers and lease fencing stop uncertain work without automatic retry. A completed
job blocks the next job until management records its paired recovery checkpoint.
The API exposes automatic behavior only when the matching runtime is enabled.
The date tree includes generated new-meeting artifacts alongside preserved files.

Verification uses private PostgreSQL/JetStream and fake providers. Production
activation requires the tested packet and management checkpoint hook; no actual
meeting or provider call is introduced merely to demonstrate this feature.
