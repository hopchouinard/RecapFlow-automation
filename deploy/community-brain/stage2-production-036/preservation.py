"""Request030 capture/restore adapter; no remote transfer or production CLI.

The caller must already have stopped every non-cooperative writer and fenced the
database. This interface checks a bounded local file phase, not those missing
external guarantees. It preserves incomplete directories on every failure.
"""
from pathlib import Path
import time


def local_preservation(recovery, *, components, locks, holds, bundle, restored,
                       capture_id, deadline_epoch, scope='synthetic-development'):
    if scope != 'synthetic-development':
        raise ValueError('production preservation requires a reviewed operation wrapper')
    if deadline_epoch <= time.time():
        raise ValueError('preservation deadline expired')
    bundle, restored = Path(bundle), Path(restored)
    if bundle.exists() or restored.exists():
        raise ValueError('new capture and restore destinations required')
    with recovery.quiet(locks, holds) as before:
        digest = recovery.capture(components, bundle, capture_id,
                                  {'holds': before, 'writer_exclusion': 'caller-certified stopped and fenced'},
                                  scope=scope)
        if time.time() >= deadline_epoch:
            raise TimeoutError('capture exceeded deadline; partial retained')
        manifest = recovery.validate_bundle(bundle, digest, expected_scope=scope)
        result = recovery.restore(bundle, digest, restored, expected_scope=scope)
        if time.time() >= deadline_epoch:
            raise TimeoutError('restore exceeded deadline; partial retained')
        for name, source in components.items():
            if recovery.tree(source) != recovery.tree(restored / name):
                raise ValueError('independent restore differs: ' + name)
    return {'schema': 'cbm.local-preservation/1', 'scope': scope,
            'capture_id': capture_id, 'manifest_sha256': digest,
            'components': sorted(manifest['components']),
            'restore_receipt': result, 'holds_unchanged': True,
            'production_qualified': False}
