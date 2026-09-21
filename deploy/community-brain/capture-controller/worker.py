"""Managed synthetic capture child; the detached supervisor owns host recovery."""
import io,json,os,sys,time
from pathlib import Path
import common as c
import database as db
import operation,transport,receipt
r=c.r

def execute(s):
    op=Path(s['operation']);fixture=Path(s['fixture']);source=s['database']['source']['id'];target=s['database']['restore']['id']
    component=op/'database-component';component.mkdir(mode=0o700)
    with db.fence(s) as fence:
        before_time=time.time();before=db.observe(source,fixture/'state');src=db.identity(source)
        r.write_new(component/'before.json',r.encode(before))
        if s['exercise']!='normal':
            r.write_new(op/'interrupt-ready.json',r.encode({'at':time.time(),'fence_pid':fence['pid']}))
            while time.time()<s['deadlines']['capture_by']+5:
                if not db.fence_alive(s,fence):raise ValueError('database fence lost')
                time.sleep(.1)
        if time.time()>=s['deadlines']['capture_by']:raise ValueError('capture deadline expired')
        dump=c.command(['docker','exec',source,'pg_dump','-U','fixture','-d','fixture','-Fc','--no-owner','--no-acl','--snapshot',fence['snapshot']],timeout=8)
        if db.observe(source,fixture/'state')!=before or db.identity(source)!=src:raise ValueError('source observations changed under fence')
        r.write_new(component/'database.dump',dump)
        digest=r.capture({'state':fixture/'state','controls':fixture/'controls','database':component},op/'bundle',s['capture_id'],{'operation_id':s['operation_id'],'owner_id':s['owner_id'],'packet_sha256':s['packet_sha256'],'holds':s['hold_bindings'],'database_snapshot':fence['snapshot']})
        if not db.fence_alive(s,fence):raise ValueError('database fence lost before completion')
        if time.time()>=s['deadlines']['capture_by']:raise ValueError('capture completion expired')
        r.write_new(op/'fence-release-intent.json',r.encode({'at':time.time()}))
    r.write_new(op/'fence-released.json',r.encode({'at':time.time()}))
    r.write_new(op/'capture-ready.json',r.encode({'manifest_sha256':digest,'at':time.time()}))
    while not (op/'serving-restored.json').exists():
        if time.time()>s['deadlines']['serving_by']:raise ValueError('serving deadline')
        time.sleep(.1)
    stream=io.BytesIO();transport.pack(op/'bundle',digest,stream);stream.seek(0)
    transport.receive(stream,op/'received',digest,8*1024*1024)
    r.restore(op/'received',digest,op/'restored');receipt.verify(op/'received',digest,op/'restored')
    destination=s['database']['destination_database']
    c.command(['docker','exec',target,'createdb','-U','fixture',destination])
    c.command(['docker','exec','-i',target,'pg_restore','-U','fixture','-d',destination,'--exit-on-error','--no-owner','--no-acl'],r.stable_bytes(op/'restored/database/database.dump'),timeout=10)
    after=db.observe(target,op/'restored/state',destination);dst=db.identity(target,destination)
    evidence=op/'evidence';evidence.mkdir(mode=0o700)
    r.write_new(evidence/'before.json',r.encode(before));r.write_new(evidence/'after.json',r.encode(after))
    result={'schema':'cbm.database-evidence/1','scope':s['scope'],'owner_id':s['owner_id'],'operation_id':s['operation_id'],'capture_id':s['capture_id'],'packet_sha256':s['packet_sha256'],'manifest_sha256':digest,'bundle':str(op/'received'),'restored':str(op/'restored'),'dump':{'component':'database','path':'database.dump','sha256':r.sha(dump),'bytes':len(dump)},'before_sha256':r.sha(r.encode(before)),'after_sha256':r.sha(r.encode(after)),'source_identity':src,'destination_identity':dst,'observed_before':before_time,'observed_after':time.time(),'deadline_epoch':s['deadlines']['validate_by']}
    r.write_new(evidence/'database-receipt.json',r.encode(result))
    verified=db.verify_evidence(evidence,s,digest)
    r.write_new(op/'worker-result.json',r.encode(dict(verified,manifest_sha256=digest)))
    return verified

if __name__=='__main__':
    path,sha=sys.argv[1:];s=c.load_spec(path,sha,check_time=False)
    core={'scope':'synthetic-development','deadline_epoch':s['deadlines']['validate_by'],'max_seconds':max(.1,s['deadlines']['validate_by']-time.time()),'locks':[],'holds':s['holds']}
    operation.run(Path(s['operation'])/'core-operation',core,lambda:execute(s))
