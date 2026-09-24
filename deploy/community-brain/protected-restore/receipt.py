"""Verify component restore evidence from disk. Does not qualify production."""
import json
from pathlib import Path
import recovery as r


def verify(bundle, expected, destination):
    value = r.validate_bundle(bundle, expected, 'synthetic-development')
    destination = r.no_links(destination)
    receipt = json.loads(r.stable_bytes(destination/'restore-receipt.json'))
    intent = json.loads(r.stable_bytes(destination/'restore-intent.json'))
    identity = dict(capture_id=value['capture_id'], manifest_sha256=expected)
    if intent != identity:
        raise ValueError('restore intent mismatch')
    expected_receipt = dict(schema='cbm.restore-receipt/1', scope=value['scope'],
        **identity, destination=str(destination), tree_comparison='exact',
        components={k:r.sha(r.encode(v)) for k,v in value['components'].items()},
        database_acceptance=None, application_acceptance=None, production_qualified=False)
    if receipt != expected_receipt:
        raise ValueError('receipt identity or acceptance mismatch')
    capture_intent = json.loads(r.stable_bytes(Path(bundle)/'intent.json'))
    if capture_intent != dict(capture_id=value['capture_id'], state='capture_started',
                              evidence=value['writer_exclusion']):
        raise ValueError('capture intent mismatch')
    if {p.name for p in destination.iterdir()} != {*value['components'], 'restore-intent.json', 'restore-receipt.json'}:
        raise ValueError('restore member set mismatch')
    for name, rows in value['components'].items():
        if r.tree(destination/name) != rows:
            raise ValueError('restored component mismatch')
    return {'schema':'cbm.component-verification/1', **identity,
            'components_verified': sorted(value['components']),
            'production_qualified':False, 'database_acceptance':None,
            'application_acceptance':None, 'legacy_adapter_installed':False}
