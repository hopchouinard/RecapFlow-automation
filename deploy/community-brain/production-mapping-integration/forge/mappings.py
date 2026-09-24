"""Closed mapping review checks. No executor, production flags remain false."""
import hashlib,json
from pathlib import Path

HELPERS={
 'pre-pbs-copy':'platform-services/community-brain-prod/integrations/pre-pbs-copy.py',
 'legacy-intake-ownership':'mac-intake.py',
 **{n:'platform-services/community-brain-prod/integrations/'+n+'.py' for n in
 ('renew-service-tokens','provision-nats-tls','renew-app-tls','copy-backup','management-health')},
 'checkpoint-consumer':'platform-services/community-brain-prod/automatic-recovery/consumer.py',
 'monitor-publish':'platform-services/community-brain-prod/automatic-recovery/monitor_status.py',
}


def digest(v):return hashlib.sha256((json.dumps(v,sort_keys=True,indent=2)+'\n').encode()).hexdigest()


def compare_catalog(census,profile):
    """Detect drift in observed metadata only; not full restore qualification."""
    if census.get('schema')!='cbm.metadata-census/1' or census.get('application_rows_read') is not False:raise ValueError('metadata census required')
    o=census['observations']
    if len(o['identity'])!=1 or o['identity'][0]['read_only']!='on':raise ValueError('read-only observation required')
    keys=set(profile['observations'])
    if set(o)!=keys|{'identity'}:raise ValueError('census coverage mismatch')
    differences=[k for k in sorted(keys) if o[k]!=profile['observations'][k]]
    return dict(compatible_observed_metadata=not differences,differences=differences,
                administrative_coverage_verified=False,restore_qualified=False,
                production_execution_enabled=False)


def validate_helper_mappings(value):
    if set(value)!=set(HELPERS):raise ValueError('missing or extra helper mapping')
    fields={'source_path','source_sha256','effects','admission','unknown_outcome','recovery','dev_receipt_sha256','legacy_dependency'}
    for name,row in value.items():
        if set(row)!=fields or row['source_path']!=HELPERS[name]:raise ValueError('helper source contract mismatch')
        for k in ('source_sha256','dev_receipt_sha256'):
            h=row[k]
            if not isinstance(h,str) or len(h)!=64 or any(c not in '0123456789abcdef' for c in h):raise ValueError('source and development proof required')
        if row['admission']!='shared-journal-before-effect' or row['unknown_outcome']!='retain-and-readback-no-replay':raise ValueError('unreviewed helper admission/replay policy')
        if row['legacy_dependency'] is not False:raise ValueError('legacy production dependency forbidden')
        if not row['effects'] or not isinstance(row['effects'],list) or any(not isinstance(x,str) or not x.strip() for x in row['effects']):raise ValueError('effect inventory required')
        if not isinstance(row['recovery'],str) or not row['recovery'].strip():raise ValueError('helper recovery contract required')
    return {'mapping_shape_valid':True,'source_and_receipt_bytes_require_independent_verification':True,'production_execution_enabled':False}
