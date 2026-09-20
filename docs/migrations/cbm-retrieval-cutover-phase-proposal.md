# Controlled retrieval cutover — approved phase

Status: **approved by Patrick on September 10, 2026**. The bounded production worker and paired nonempty
recovery phase is complete for its approved scope. The next recommended phase is
retrieval-only cutover, keeping processing activation separate because production
indexing, ongoing intake ownership and ordinary operational model budgets have
not been approved or exercised on the new target.

## Concrete intended change

Move the existing Open WebUI retrieval integration to
`https://community-brain.patchoutech.lab/retrieval/query`, using a new dedicated
`retrieval:read` service identity for scope `community-brain`. Retain Open WebUI
and the old retrieval service on VM101 for rollback. Preserve the integration's
existing query/response contract and X-API-Key transport; no UI/model change,
consumer distribution push or service retirement is included.

Execution begins with [the management preflight handoff](cbm-retrieval-cutover-management-preflight.md). No endpoint switch has occurred. The existing filter stores a full query URL, not a base URL.

## Mandatory preflight before switching

1. Management records the current Open WebUI filter/base URL and credential
   configuration privately, with its exact restoration procedure. Confirm the
   actual requesting container/source IP and lab trust. The current Traefik
   allowlist does not include VM101: add only its verified requesting source if
   required, preserving all existing restrictions. Test authenticated requests
   from the actual Open WebUI process before changing its active endpoint.
2. Create the independently scoped production retrieval identity through Infisical
   and deliver it directly to Open WebUI. Define its expiration, rotation owner and
   reload procedure. Do not reuse short-lived monitoring/development/rehearsal keys.
   Rotate the existing probes explicitly before September 11 at 02:05:38 UTC if
   staging continues beyond that deadline.
3. Obtain a fresh read-only source inventory of corpus/config/registries and
   writer schedules from VM101; compare to the September 9 preservation manifest.
   The approved candidate is a point-in-time copy, not evidence of current parity.
   Capture a verified final data-only checkpoint under a controlled writer pause.
   Preserve provenance and the exact approved 13-divider exclusion policy; do not
   silently exclude new failures, re-extract or re-embed changed content. Unexpected
   data differences requiring a new policy return to Patrick before execution.
4. Establish corpus ownership and freshness **before** routing live retrieval.
   A one-time copy followed by continued old-host writes would become stale.
   Record either a bounded no-write cutover window or a tested, explicitly scoped
   refresh process from the sole authoritative writer. If this cannot be established,
   keep retrieval staged. Do not activate the new worker or transfer processing
   ownership as an incidental consequence of the retrieval switch.
5. Build/install the verified current candidate in a separate target directory,
   compare representative queries and current-row FTS coverage, preserve the prior
   target for rollback, and retain a paired backup. Recheck health, actual Patrick
   login, monitoring and final source drift immediately before the endpoint change.

After preflight, this approved phase permits the exact Open WebUI endpoint /
scoped credential switch and verification through an actual user query. Record
before/after identities, data manifests, results and time. If any acceptance fails,
restore the saved endpoint/credential configuration and verify the old path.
No model-generation budget is inferred for unrelated Open WebUI chat activity;
query embedding checks remain the retained retrieval dependency.

## Explicit exclusions and later work

No new processing schedule, Mac intake destination change, Fathom acquisition,
synthetic pending-index replay, historical processing, Git/corpus publication,
old-service retirement or broader firewall access. Worker production readiness
still needs its own indexing/ingestion and ownership work. The two synthetic jobs'
unsent indexing events remain inert. Unused US$2 allowance grants no new jobs.

A successful retrieval-only switch is partial CBM-08 progress, not completion of
migration or its two successful weekly-cycle stabilization requirement. CBM-09
remains separate. CBM-10/Q-01 through Q-05 stay the final step of the whole migration.
