"""Fixed-request, lock-serialized terminal ownership control. No legacy resurrection."""
import datetime,fcntl,json,os,pathlib,stat,tempfile
REQUEST='CBM-MANUAL-OWNERSHIP-20260910-007'
ORIGINAL='CBM-RETRIEVAL-20260910-001'
RECEIPT='3172c4c082c7cce4f5bba5952ec4549bb91a40f806e861c3b8f6d125ede2bd67'
LATEST_START=datetime.datetime.fromisoformat('2026-09-11T01:15:00+00:00')
CHECKS={'maintenance_tests','live_copy_rehearsal','calendar_installed','health_metrics_live','post_job_procedure','expiry_metadata_verified','controller_tests','mac_hook_installed','database_unchanged','corpus_unchanged','paired_checkpoint_verified','webui_verified'}
def read_private(p):
    s=p.lstat();assert stat.S_ISREG(s.st_mode) and s.st_uid==os.geteuid() and stat.S_IMODE(s.st_mode)==0o600
    return json.loads(p.read_text())
def atomic_json(p,value):
    fd,name=tempfile.mkstemp(prefix='.'+p.name+'.',dir=p.parent)
    try:
        with os.fdopen(fd,'w') as stream:
            os.fchmod(stream.fileno(),0o600);json.dump(value,stream,indent=2);stream.write('\n');stream.flush();os.fsync(stream.fileno())
        os.replace(name,p)
        fd=os.open(p.parent,os.O_RDONLY)
        try:os.fsync(fd)
        finally:os.close(fd)
    finally:
        if os.path.exists(name):os.unlink(name)
def terminal(state):
    if state['phase']!='superseded':
        assert 'ownership' not in state,'Inconsistent terminal record'
        return False
    record=state['ownership']
    assert record['request_id']==REQUEST and record['accepted_recovery_receipt_sha256']==RECEIPT
    assert state['request_id']==ORIGINAL and state['mac_resume_allowed'] is False and state['guard_active'] is True
    assert record['legacy_writers_disabled'] is True
    return True
def public(state):
    result={k:state.get(k) for k in ['request_id','phase','deadline_utc','hold_started_at','guard_active','rollback_verified','mac_resume_allowed']}
    if terminal(state):result['ownership']=state['ownership']
    return result
class Controller:
    def __init__(self,root,legacy,verify_live,now=None):
        self.root=pathlib.Path(root);self.legacy=legacy;self.verify_live=verify_live;self.now=now or (lambda:datetime.datetime.now(datetime.timezone.utc))
    def execute(self,command,force=False):
        assert command in ['status','rollback','supersede']
        fd=os.open(self.root/'control.lock',os.O_CREAT|os.O_RDWR|os.O_NOFOLLOW,0o600)
        try:
            # Timer rollback waits for a transient status lock rather than losing its
            # sole deadline invocation. systemd retains its existing300s timeout.
            # New supersession/status calls fail fast if another operation owns it.
            fcntl.flock(fd,fcntl.LOCK_EX if command=='rollback' else fcntl.LOCK_EX|fcntl.LOCK_NB)
            state=read_private(self.root/'state.json');assert state['request_id']==ORIGINAL
            assert state['phase'] in ['prepared','holding','held','switched','rollback_failed','restored','superseded']
            if terminal(state) or command=='status':return public(state)
            if command=='rollback':
                self.legacy.rollback(force=force)
                return public(read_private(self.root/'state.json'))
            assert state['phase']=='switched' and state['guard_active'] is True
            now=self.now();assert now<LATEST_START,'Insufficient deadline margin; leave original rollback effective'
            ready=read_private(self.root/'ownership-readiness007.json')
            assert ready['request_id']==REQUEST and ready['accepted_recovery_receipt_sha256']==RECEIPT
            assert set(ready['checks'])==CHECKS and all(v is True for v in ready['checks'].values())
            assert 0<=(now-datetime.datetime.fromisoformat(ready['checked_at'])).total_seconds()<600
            self.verify_live()
            # One atomic state replacement IS the durable terminal record. No pending marker
            # can suppress pre-existing rollback before this commit point.
            state.update(phase='superseded',mac_resume_allowed=False,updated_at=now.isoformat(),ownership={'request_id':REQUEST,'accepted_recovery_receipt_sha256':RECEIPT,'committed_at':now.isoformat(),'legacy_writers_disabled':True,'readiness':ready})
            atomic_json(self.root/'state.json',state)
            return public(read_private(self.root/'state.json'))
        finally:os.close(fd)
