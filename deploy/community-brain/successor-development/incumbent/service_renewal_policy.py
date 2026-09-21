"""Resumable seven-day service credential renewal, with no plaintext local journal."""
import hashlib
import json
import secrets
import uuid

LIFETIME = 7 * 86400
LEAD = 3 * 86400
PENDING = 'CB_SERVICE_RENEWAL_JOURNAL'
IDENTITIES = 'CB_SERVICE_IDENTITIES'
SPECS = (
    ('CB_OPENWEBUI_RETRIEVAL_TOKEN', 'CB_OPENWEBUI_RETRIEVAL_EXPIRES_AT', 'community-brain-openwebui', ['retrieval:read']),
    ('CB_PROD_MAC_COLLECTOR_TOKEN', 'CB_PROD_MAC_COLLECTOR_EXPIRES_AT', 'community-brain-prod-mac-collector', ['sources:upload:chat']),
    ('CB_PROD_MANUAL_OPERATOR_TOKEN', 'CB_PROD_MANUAL_OPERATOR_EXPIRES_AT', 'community-brain-prod-manual-operator', ['sources:upload', 'jobs:submit', 'jobs:read', 'artifacts:read']),
    ('CB_READ_PROBE_TOKEN', 'CB_PROBE_EXPIRES_AT', 'community-brain-prod-read-probe', ['jobs:read', 'artifacts:read', 'retrieval:read']),
    ('CB_METRICS_PROBE_TOKEN', 'CB_PROBE_EXPIRES_AT', 'community-brain-prod-metrics-probe', ['metrics:read']),
)


def validate(values):
    records = json.loads(values[IDENTITIES])
    assert len(records) == len(SPECS)
    for key, expiry, subject, permissions in SPECS:
        matches = [r for r in records if r['subject'] == subject]
        assert len(matches) == 1
        r = matches[0]
        assert r['scope'] == 'community-brain' and r['permissions'] == permissions
        assert r['sha256'] == hashlib.sha256(values[key].encode()).hexdigest()
        assert r['expires_at'] == int(values[expiry])
    return records


def due(values, now):
    pending = json.loads(values.get(PENDING, '{}'))
    if pending and pending['phase'] != 'completed':
        return True
    return now >= min(r['expires_at'] for r in validate(values)) - LEAD


def run(adapter, now, *, force=False):
    """Effects are read/compare/set and re-verifiable after lost acknowledgments.

    The adapter must hold the Mac scheduler mutex and the production quiet lease.
    The only secret-bearing journal is an Infisical secret. Never print it.
    """
    values = adapter.read()
    journal = json.loads(values.get(PENDING, '{}'))
    if not journal or journal['phase'] == 'completed':
        if not force and not due(values, now):
            return {'state': 'not_due', 'next_due': min(r['expires_at'] for r in validate(values)) - LEAD}
        old = validate(values)
        assert min(r['expires_at'] for r in old) > now, 'Expired identity requires explicit reconciliation'
        adapter.inventory(values)
        expiry = int(now) + LIFETIME
        updates = {}
        new = []
        for key, expkey, subject, _ in SPECS:
            token = secrets.token_urlsafe(48)
            updates[key] = token
            updates[expkey] = str(expiry)
            previous = next(r for r in old if r['subject'] == subject)
            new.append({**previous, 'sha256': hashlib.sha256(token.encode()).hexdigest(), 'expires_at': expiry})
        journal = {'cycle': str(uuid.uuid4()), 'phase': 'prepared', 'created_at': int(now),
                   'old': {k: values[k] for k in updates}, 'updates': updates,
                   'before': old, 'after': new, 'expires_at': expiry}
        adapter.save({PENDING: json.dumps(journal, separators=(',', ':'))})

    def mark(phase):
        journal['phase'] = phase
        adapter.save({PENDING: json.dumps(journal, separators=(',', ':'))})

    # Always re-establish and verify overlap on resume, even if a prior phase
    # acknowledgment was lost. Never extend the prepared token's lifetime.
    assert journal['expires_at'] > now + 3600, 'Prepared renewal too old; reconcile without revocation'
    if journal['phase'] not in ('final_authority', 'final_api'):
        adapter.save({**journal['updates'], IDENTITIES: json.dumps(journal['before'] + journal['after'], separators=(',', ':'))})
        adapter.accept(adapter.read())
        adapter.verify_overlap(journal)
        mark('overlap_verified')
        adapter.deliver(journal)
        adapter.verify_consumers(journal)
        mark('consumers_verified')
        # Recheck every consumer immediately before removing old acceptance.
        adapter.verify_consumers(journal)
        adapter.save({IDENTITIES: json.dumps(journal['after'], separators=(',', ':'))})
        mark('final_authority')
    adapter.accept(adapter.read())
    mark('final_api')
    adapter.verify_consumers(journal)
    adapter.verify_revoked(journal)
    result = {'state': 'completed', 'cycle': journal['cycle'], 'expires_at': journal['expires_at'],
              'next_due': journal['expires_at'] - LEAD, 'subjects': [s[2] for s in SPECS]}
    # The authority retains only safe completion metadata after revocation.
    adapter.save({PENDING: json.dumps({**result, 'phase': 'completed'}, separators=(',', ':'))})
    return result
