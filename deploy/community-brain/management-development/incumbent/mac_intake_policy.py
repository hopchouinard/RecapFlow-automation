"""Testable Mac peer policy. A terminal local observation never trusts stale status."""
REQUEST='CBM-MANUAL-OWNERSHIP-20260910-007'
ORIGINAL='CBM-RETRIEVAL-20260910-001'
RECEIPT='3172c4c082c7cce4f5bba5952ec4549bb91a40f806e861c3b8f6d125ede2bd67'
def terminal_record(record):
    assert record['request_id']==REQUEST and record['accepted_recovery_receipt_sha256']==RECEIPT and record['legacy_writers_disabled'] is True
def decide(local,fetch,save,ensure_disabled,resume):
    assert local['request_id']==ORIGINAL
    if local['phase']=='superseded':
        terminal_record(local['ownership']);ensure_disabled();return 'superseded'
    assert local['phase'] in ['pending','held','restored'] and 'ownership' not in local
    remote=fetch();assert remote['request_id']==ORIGINAL
    if remote['phase']=='superseded':
        terminal_record(remote['ownership']);assert remote['mac_resume_allowed'] is False
        local.update(phase='superseded',ownership=remote['ownership'],server_rollback_verified=False)
        save(local) # Persist the refusal before any external action; later stale peers cannot resume.
        ensure_disabled();return 'superseded'
    assert 'ownership' not in remote
    if remote['phase']=='restored' and remote['rollback_verified'] is True and remote['mac_resume_allowed'] is True:
        resume(local['previous_enabled']);local.update(phase='restored',server_rollback_verified=True);save(local);return 'restored'
    ensure_disabled();return 'held'
