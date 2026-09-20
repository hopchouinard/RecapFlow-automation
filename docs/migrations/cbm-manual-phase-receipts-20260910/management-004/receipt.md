# CBM-COLLECTOR-SCOPE-20260910-004 — pending scope corrected

The pending production collector now has exactly **`sources:upload:chat`**, scoped `community-brain`, subject `community-brain-prod-mac-collector`.

Updated Infisical `CB_MANUAL_PREP_SERVICE_IDENTITIES` and VM109 private files:

- `/etc/community-brain-production/manual-preparation/server-identities.json`
- `/etc/community-brain-production/manual-preparation/api.env.pending`

Token, expiry, manual operator, retrieval, probe and human grants are preserved. Existing live `CB_SERVICE_IDENTITIES`/API runtime and disabled Mac collector config are unchanged. The broad preparation record was never activated.

No API restart, upload or activation occurred. The writer hold and September 11 01:25 UTC rollback / 01:30 UTC hard deadline remain unchanged. Verified staging and live authorization checks still precede activation. This additive receipt supersedes only the pending collector permission described in request003; it does not alter the earlier historical receipts.
