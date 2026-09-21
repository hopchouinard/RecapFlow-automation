"""Retained malformed evidence and real restored-catalog mutation checks."""
import copy,json,shutil,sys,time,os
from pathlib import Path
import common as c,database as db,catalog,candidate
r=c.r

def check(path,sha,template_path):
    s=c.load_spec(path,sha,check_time=False);op=Path(s['operation']);evidence=op/'evidence';receipt=json.loads(r.stable_bytes(evidence/'database-receipt.json'));manifest=receipt['manifest_sha256']
    positive=db.verify_evidence(evidence,s,manifest);template=json.loads(r.stable_bytes(Path(template_path)));prep=candidate.prepare(template,evidence,s,manifest)
    root=op/'negative-evidence';root.mkdir(mode=0o700);results=[]
    def reject(name,edit=None,change=None,digest=None):
        d=root/name;shutil.copytree(evidence,d);v=copy.deepcopy(receipt);spec=copy.deepcopy(s)
        if edit:edit(d,v)
        if change:change(spec)
        c.atom(d/'database-receipt.json',v)
        try:db.verify_evidence(d,spec,digest or manifest)
        except (ValueError,KeyError,FileNotFoundError,TypeError):results.append({'case':name,'rejected':True});return
        raise AssertionError('accepted '+name)
    reject('missing_before',lambda d,v:(d/'before.json').unlink())
    reject('extra_member',lambda d,v:(d/'extra').touch())
    reject('unknown_acceptance',lambda d,v:v.update(accepted=True))
    reject('production_receipt',lambda d,v:v.update(scope='production'))
    reject('development_as_production',change=lambda s:s.update(scope='production'))
    for key in ('owner_id','operation_id','capture_id','packet_sha256','manifest_sha256','globals_sha256','writer_proof_sha256','signing_sha256','before_sha256','after_sha256'):
        reject('mixed_'+key,lambda d,v,k=key:v.update({k:'0'*64}))
    reject('foreign_external_manifest',digest='0'*64)
    reject('volume_identity',lambda d,v:v['volume'].update(inode=0))
    reject('extra_component',lambda d,v:v['components'].append('unknown'))
    reject('missing_component',lambda d,v:v['components'].pop())
    reject('dump_changed',lambda d,v:v['dump'].update(sha256='0'*64))
    reject('unknown_dump_flag',lambda d,v:v['dump'].update(accepted=True))
    reject('expired',lambda d,v:v.update(deadline_epoch=1),lambda s:s['deadlines'].update(validate_by=1))
    reject('stale_observation',lambda d,v:v.update(observed_before=s['deadlines']['prepare_by']-601))
    reject('future_observation',lambda d,v:v.update(observed_after=s['deadlines']['validate_by']+1))
    reject('same_server',lambda d,v:v.update(destination_identity=copy.deepcopy(v['source_identity'])))
    reject('changed_version',lambda d,v:v['destination_identity'].update(version='18.5'))
    reject('forged_server',lambda d,v:v['destination_identity'].update(system_identifier='unrelated'))
    baseline=json.loads(r.stable_bytes(evidence/'after.json'));target=s['database']['restore']['id'];destination=s['database']['destination_database']
    def actual(name,mutation,rollback,unsupported=False):
        catalog.sql(target,mutation,destination)
        outcome={'case':name,'actual_postgresql_mutation':True,'rejected':False,'unsupported':unsupported}
        try:
            try:after=db.observe(target,op/'restored/state',destination)
            except ValueError as e:
                if not unsupported:raise
                outcome.update(rejected=True,reason=str(e));r.write_new(root/(name+'-catalog-refusal.json'),r.encode(outcome))
            else:
                if unsupported:raise AssertionError('unsupported object accepted')
                assert after!=baseline
                def edit(d,v):c.atom(d/'after.json',after);v['after_sha256']=r.sha(r.stable_bytes(d/'after.json'))
                reject(name,edit);outcome['rejected']=True
        finally:catalog.sql(target,rollback,destination)
        restored=db.observe(target,op/'restored/state',destination)
        if restored!=baseline:
            r.write_new(root/(name+'-rollback-difference.json'),r.encode(restored));raise ValueError('test catalog rollback differs: '+name)
        outcome['catalog_rollback_equal']=True;results.append(outcome)
    actual('missing_select_acl','REVOKE SELECT ON app.jobs FROM cbm_runtime;','GRANT SELECT ON app.jobs TO cbm_runtime;')
    actual('extra_truncate_acl','GRANT TRUNCATE ON app.jobs TO cbm_runtime;','REVOKE TRUNCATE ON app.jobs FROM cbm_runtime;')
    actual('missing_default_acl','ALTER DEFAULT PRIVILEGES FOR ROLE cbm_owner IN SCHEMA app REVOKE SELECT ON TABLES FROM cbm_runtime;','ALTER DEFAULT PRIVILEGES FOR ROLE cbm_owner IN SCHEMA app GRANT SELECT ON TABLES TO cbm_runtime;')
    actual('missing_role_membership','REVOKE cbm_owner FROM cbm_ddl;','GRANT cbm_owner TO cbm_ddl;')
    actual('changed_role_power','ALTER ROLE cbm_runtime CREATEROLE;','ALTER ROLE cbm_runtime NOCREATEROLE;')
    actual('extension_function_acl','REVOKE EXECUTE ON FUNCTION public.digest(bytea,text) FROM PUBLIC;','GRANT EXECUTE ON FUNCTION public.digest(bytea,text) TO PUBLIC;')
    actual('column_acl','GRANT SELECT(state) ON app.jobs TO cbm_runtime;','REVOKE SELECT(state) ON app.jobs FROM cbm_runtime;')
    seq=baseline['sequence_values']['app.jobs_id_seq']
    actual('changed_sequence',"SELECT setval('app.jobs_id_seq',77,true);","SELECT setval('app.jobs_id_seq',"+str(seq['last_value'])+','+str(seq['is_called']).lower()+');')
    actual('unknown_outcome_cleared',"UPDATE app.attempts SET outcome='succeeded' WHERE id=1;","UPDATE app.attempts SET outcome='outcome_unknown' WHERE id=1;")
    actual('extra_table','CREATE TABLE app.unreviewed(id int);','DROP TABLE app.unreviewed;')
    actual('unsupported_view','CREATE VIEW app.unreviewed AS SELECT id FROM app.jobs;','DROP VIEW app.unreviewed;',True)
    actual('unsupported_routine',"CREATE FUNCTION app.unreviewed() RETURNS int LANGUAGE sql AS 'SELECT 1';",'DROP FUNCTION app.unreviewed();',True)
    actual('unsupported_enum',"CREATE TYPE app.unreviewed AS ENUM('synthetic');",'DROP TYPE app.unreviewed;',True)
    actual('unsupported_rls','ALTER TABLE app.jobs ENABLE ROW LEVEL SECURITY;','ALTER TABLE app.jobs DISABLE ROW LEVEL SECURITY;',True)
    actual('unsupported_database_setting','ALTER DATABASE '+catalog.ident(destination)+" SET work_mem='6MB';",'ALTER DATABASE '+catalog.ident(destination)+' RESET work_mem;',True)
    for name,relative in [('actual_signing_drift','private/signing.key'),('actual_artifact_drift','state/files/upload.txt')]:
        f=op/'restored'/relative;raw=r.stable_bytes(f);st=f.stat()
        f.write_bytes(b'FORGED-SYNTHETIC-CONTENT')
        try:
            try:db.verify_evidence(evidence,s,manifest)
            except ValueError:results.append({'case':name,'actual_file_mutation':True,'rejected':True})
            else:raise AssertionError(name)
        finally:f.write_bytes(raw);os.utime(f,ns=(st.st_atime_ns,st.st_mtime_ns))
        db.verify_evidence(evidence,s,manifest)
    for name,mutate in [('filled_production_slot',lambda t:t['required_evidence'].update({next(iter(t['required_evidence'])):positive})),('enabled_production',lambda t:t.update(deployable=True))]:
        t=copy.deepcopy(template);mutate(t)
        try:candidate.prepare(t,evidence,s,manifest)
        except ValueError:results.append({'case':name,'rejected':True})
        else:raise AssertionError(name)
    # Count unique cases: native comparison cases also have their retained rejection copy.
    value={'positive':positive,'candidate':prep,'negative_cases':results,'negative_unique_count':len({x['case'] for x in results}),'actual_catalog_mutations':sum(bool(x.get('actual_postgresql_mutation')) for x in results),'retained_path':str(root),'at':time.time()}
    r.write_new(op/'database-checks.json',r.encode(value));print(json.dumps(value))

if __name__=='__main__':check(*sys.argv[1:])
