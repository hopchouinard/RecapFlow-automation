"""Real file/lock boundary probes on an already completed synthetic fixture."""
import copy,fcntl,json,os,sys,time
from pathlib import Path
import common as c
r=c.r

def check(path,sha):
    original=c.load_spec(path,sha,check_time=False);root=Path(original['operation'])/'boundary-checks';root.mkdir(mode=0o700)
    before=c.inspect(original['incumbent']['id']);holds=r.hold_state(original['holds']);results=[]
    edits={'unknown_field':lambda s:s.update(accepted=True),'production':lambda s:s.update(scope='production'),
        'mixed_operation_path':lambda s:s.update(operation_id='r031-other-operation'),
        'foreign_fixture':lambda s:s.update(fixture='/srv/community-brain'),
        'wrong_lock_order':lambda s:s['locks'].reverse(),
        'missing_hold':lambda s:s['holds'].pop(),
        'nan_deadline':lambda s:s['deadlines'].update(capture_by=float('nan')),
        'stale_deadline':lambda s:s['deadlines'].update(prepare_by=0),
        'source_manifest_mismatch':lambda s:s.update(packet_sha256='0'*64),
        'forged_database_name':lambda s:s['database']['source'].update(name='cbm-r031-pg-wrong'),
        'foreign_database_name':lambda s:s['database']['source'].update(name='production')}
    other=c.ROOT/'packet-v1'
    edits['wrong_executing_packet']=lambda s:s.update(packet=str(other),packet_sha256=r.sha(r.stable_bytes(other/'packet-manifest.json')))
    for name,edit in edits.items():
        s=copy.deepcopy(original);now=time.time();s['deadlines']={'prepare_by':now+20,'capture_by':now+40,'serving_by':now+80,'validate_by':now+100};edit(s)
        p=root/(name+'.json');r.write_new(p,r.encode(s))
        try:c.load_spec(p,r.sha(r.stable_bytes(p)))
        except ValueError as exc:results.append({'case':name,'rejected':True,'reason':str(exc)})
        else:raise AssertionError(name)
    try:c.load_spec(path,'0'*64,check_time=False)
    except ValueError:results.append({'case':'spec_hash_mismatch','rejected':True})
    else:raise AssertionError('spec hash')
    for path in original['locks']:
        fd=os.open(path,os.O_RDWR|os.O_NOFOLLOW);fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        try:
            try:
                with r.quiet(original['locks'],original['holds']):raise AssertionError('busy lock acquired')
            except BlockingIOError:results.append({'case':'busy_'+Path(path).name,'rejected':True})
        finally:os.close(fd)
    after=c.inspect(original['incumbent']['id'])
    assert before['State']['StartedAt']==after['State']['StartedAt'] and c.fingerprint(before)==c.fingerprint(after)
    assert holds==r.hold_state(original['holds'])
    value={'cases':results,'negative_count':len(results),'incumbent_unchanged':True,'holds_unchanged':True,'production_effects':False}
    r.write_new(root/'result.json',r.encode(value));print(json.dumps(value))

if __name__=='__main__':check(*sys.argv[1:])
