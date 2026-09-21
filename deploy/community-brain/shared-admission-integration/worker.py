"""Managed synthetic effects; detached supervisor owns serving and writer recovery."""
import io,json,re,sys,time
from pathlib import Path
import common as c
import database as db
import catalog,operation,transport,receipt
r=c.r

def execute(s):
    op=Path(s['operation']);fixture=Path(s['fixture']);source=s['database']['source']['id'];target=s['database']['restore']['id']
    if s['kind']!='capture':
        r.write_new(op/'capture-ready.json',r.encode({'kind':s['kind'],'at':time.time()}))
        while not (op/'serving-restored.json').exists():
            if time.time()>=s['deadlines']['serving_by']:raise ValueError('serving deadline')
            time.sleep(.1)
        if not c.healthy(s):raise ValueError('real synthetic service unhealthy')
        result={'kind':s['kind'],'actual_service_health':True,'state_sha256':r.sha(r.stable_bytes(fixture/'state/files/upload.txt')),'production_qualified':False}
        r.write_new(op/'worker-result.json',r.encode(result));return result
    component=op/'database-component';component.mkdir(mode=0o700)
    catalog.close_writers(s)
    with db.fence(s) as fence:
        before_time=time.time();before=db.observe(source,fixture/'state');src=db.identity(source)
        r.write_new(component/'before.json',r.encode(before))
        denied=[]
        for role,query,label in [('cbm_runtime',"INSERT INTO app.outbox(state) VALUES('forbidden');",'dml_connection_denied'),('cbm_ddl','CREATE TABLE app.forbidden(id int);','ddl_connection_denied'),('cbm_runtime',"SELECT nextval('app.jobs_id_seq');",'sequence_connection_denied')]:
            try:catalog.sql(source,query,role=role)
            except RuntimeError:denied.append(label)
            else:raise ValueError('writer admitted during capture')
        if s['exercise']!='normal':
            r.write_new(op/'interrupt-ready.json',r.encode({'at':time.time(),'fence_pid':fence['pid']}))
            while time.time()<s['deadlines']['capture_by']:
                if not db.fence_alive(s,fence):raise ValueError('database fence lost')
                catalog.assert_closed(s);time.sleep(.1)
            raise ValueError('capture deadline expired')
        catalog.assert_closed(s)
        dump=c.command(['docker','exec','-e','PGAPPNAME=cbm-r032-dump',source,'pg_dump','-U','fixture','-d','cbm_app','-Fc','--snapshot',fence['snapshot']],timeout=15)
        globals_sql=c.command(['docker','exec',source,'pg_dumpall','-U','fixture','--roles-only','--no-role-passwords'],timeout=15)
        if db.observe(source,fixture/'state')!=before or db.identity(source)!=src:raise ValueError('source changed under admission')
        proof={'method':'nologin-revoke-connect-terminate-existing-sessions','closed_observation':catalog.assert_closed(s),'before_controls_sha256':r.sha(r.stable_bytes(op/'writer-admission-intent.json')),'after_dump_observation':catalog.assert_closed(s),'negative_clients':denied}
        for n,b in [('database.dump',dump),('globals.sql',globals_sql),('writer-proof.json',r.encode(proof)),('writer-original.json',r.stable_bytes(op/'writer-admission-intent.json'))]:r.write_new(component/n,b)
        digest=r.capture({'state':fixture/'state','controls':fixture/'controls','database':component,'private':fixture/'private'},op/'bundle',s['capture_id'],{'operation_id':s['operation_id'],'owner_id':s['owner_id'],'packet_sha256':s['packet_sha256'],'holds':s['hold_bindings'],'database_snapshot':fence['snapshot'],'signing_sha256':s['signing_sha256'],'volume':s['volume']})
        if time.time()>=s['deadlines']['capture_by'] or not db.fence_alive(s,fence):raise ValueError('capture completion expired/unfenced')
        r.write_new(op/'fence-release-intent.json',r.encode({'at':time.time()}))
    catalog.restore_writers(s)
    r.write_new(op/'capture-ready.json',r.encode({'manifest_sha256':digest,'at':time.time()}))
    while not (op/'serving-restored.json').exists():
        if time.time()>s['deadlines']['serving_by']:raise ValueError('serving deadline')
        time.sleep(.1)
    stream=io.BytesIO();transport.pack(op/'bundle',digest,stream);stream.seek(0);transport.receive(stream,op/'received',digest,16*1024*1024)
    r.restore(op/'received',digest,op/'restored');receipt.verify(op/'received',digest,op/'restored')
    existing=catalog.sql(target,"SELECT rolname FROM pg_roles WHERE rolname !~ '^pg_';",'fixture').splitlines()
    role_script=globals_sql.decode()
    for role in existing:role_script=role_script.replace('CREATE ROLE '+catalog.ident(role)+';','').replace('CREATE ROLE '+role+';','')
    catalog.sql(target,role_script,'fixture')
    destination=s['database']['destination_database']
    c.command(['docker','exec',target,'createdb','-U','fixture','-O','cbm_owner',destination])
    c.command(['docker','exec','-i',target,'pg_restore','-U','fixture','-d',destination,'--exit-on-error'],r.stable_bytes(op/'restored/database/database.dump'),timeout=25)
    catalog.apply_database_acl(target,destination,before['database_acl'])
    after=db.observe(target,op/'restored/state',destination);dst=db.identity(target,destination)
    evidence=op/'evidence';evidence.mkdir(mode=0o700)
    r.write_new(evidence/'before.json',r.encode(before));r.write_new(evidence/'after.json',r.encode(after))
    v={'schema':'cbm.database-evidence/2','scope':s['scope'],'owner_id':s['owner_id'],'operation_id':s['operation_id'],'capture_id':s['capture_id'],'packet_sha256':s['packet_sha256'],'manifest_sha256':digest,'bundle':str(op/'received'),'restored':str(op/'restored'),'dump':{'sha256':r.sha(dump),'bytes':len(dump)},'globals_sha256':r.sha(globals_sql),'before_sha256':r.sha(r.encode(before)),'after_sha256':r.sha(r.encode(after)),'source_identity':src,'destination_identity':dst,'observed_before':before_time,'observed_after':time.time(),'deadline_epoch':s['deadlines']['validate_by'],'components':['controls','database','private','state'],'signing_sha256':s['signing_sha256'],'volume':s['volume'],'writer_proof_sha256':r.sha(r.encode(proof))}
    r.write_new(evidence/'database-receipt.json',r.encode(v));verified=db.verify_evidence(evidence,s,digest)
    r.write_new(op/'worker-result.json',r.encode(verified));return verified

if __name__=='__main__':
    path,sha=sys.argv[1:];s=c.load_spec(path,sha,check_time=False)
    core={'scope':'synthetic-development','deadline_epoch':s['deadlines']['validate_by'],'max_seconds':max(.1,s['deadlines']['validate_by']-time.time()),'locks':[],'holds':s['holds']}
    operation.run(Path(s['operation'])/'core-operation',core,lambda:execute(s))
