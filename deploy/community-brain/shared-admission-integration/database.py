"""Synthetic database capture observations and strict component evidence validator."""
import json,time,re,os,select,subprocess
from pathlib import Path,PurePosixPath
from contextlib import contextmanager
import common as c
r=c.r
import receipt as tree_receipt

import catalog
sql=catalog.sql
observe=catalog.observe

def identity(container,database='cbm_app'):
    row=c.inspect(container)
    v=json.loads(sql(container,"SELECT json_build_object('system_identifier',system_identifier::text,'version',current_setting('server_version'),'database',current_database(),'database_oid',(SELECT oid FROM pg_database WHERE datname=current_database())) FROM pg_control_system();",database))
    if not v['version'].startswith('18.6 '):raise ValueError('PostgreSQL 18.6 required')
    return dict(v,container_id=row['Id'],image=row['Image'])

@contextmanager
def fence(s):
    container=s['database']['source']['id'];op=Path(s['operation']);app='cbm-r032-'+s['operation_id']
    tables=sql(container,"SELECT schemaname||'.'||tablename FROM pg_tables WHERE schemaname IN ('public','app','audit') ORDER BY schemaname,tablename;").splitlines()
    if not tables or any(not re.fullmatch('[a-z_.]+',n) for n in tables):raise ValueError('table set unavailable')
    p=subprocess.Popen(['docker','exec','-i','-e','PGAPPNAME=cbm-r032-fence',container,'psql','-X','-qAt','-U','fixture','-d','cbm_app','-v','ON_ERROR_STOP=1'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1)
    try:
        p.stdin.write("SET application_name='"+app+"'; BEGIN ISOLATION LEVEL REPEATABLE READ; SET LOCAL lock_timeout='2s'; LOCK TABLE "+','.join(n for n in tables)+" IN SHARE MODE; SELECT json_build_object('snapshot',pg_export_snapshot(),'pid',pg_backend_pid());\n");p.stdin.flush()
        if not select.select([p.stdout],[],[],5)[0]:raise ValueError('fence acquisition timeout')
        v=json.loads(p.stdout.readline());v.update(application_name=app,container_id=container)
        r.write_new(op/'fence.json',r.encode(v))
        yield v
        if not fence_alive(s,v):raise ValueError('database fence lost')
        p.stdin.write('ROLLBACK;\n');p.stdin.flush();p.stdin.close();p.wait(timeout=3)
        if p.returncode:raise ValueError('database fence failed')
    finally:
        if p.poll() is None:
            try:p.stdin.close();p.wait(timeout=2)
            except (BrokenPipeError,subprocess.TimeoutExpired):p.kill();p.wait()
        release_fence(s)

def fence_alive(s,v):
    pid=int(v['pid']);app=v['application_name']
    if app!='cbm-r032-'+s['operation_id']:raise ValueError('fence owner mismatch')
    return sql(s['database']['source']['id'],f"SELECT count(*) FROM pg_stat_activity WHERE pid={pid} AND application_name='{app}' AND state='idle in transaction';")== '1'

def release_fence(s):
    p=Path(s['operation'])/'fence.json'
    if p.exists():
        v=json.loads(r.stable_bytes(p));app='cbm-r032-'+s['operation_id']
        if v['application_name']!=app or v['container_id']!=s['database']['source']['id']:raise ValueError('foreign fence refused')
        sql(v['container_id'],f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid={int(v['pid'])} AND application_name='{app}';")


def verify_evidence(directory,s,manifest_sha):
    d=r.no_links(directory);op=Path(s['operation'])
    if {p.name for p in d.iterdir()}!={'database-receipt.json','before.json','after.json'}:raise ValueError('evidence member set')
    v=json.loads(r.stable_bytes(d/'database-receipt.json'))
    keys={'schema','scope','owner_id','operation_id','capture_id','packet_sha256','manifest_sha256','bundle','restored','dump','globals_sha256','before_sha256','after_sha256','source_identity','destination_identity','observed_before','observed_after','deadline_epoch','components','signing_sha256','volume','writer_proof_sha256'}
    if set(v)!=keys or v['schema']!='cbm.database-evidence/2' or v['scope']!='synthetic-development' or s['scope']!='synthetic-development':raise ValueError('unknown acceptance or production scope')
    for key in ('owner_id','operation_id','capture_id','packet_sha256','signing_sha256','volume'):
        if v[key]!=s[key]:raise ValueError('mixed attempt identity: '+key)
    if v['manifest_sha256']!=manifest_sha or v['deadline_epoch']!=s['deadlines']['validate_by']:raise ValueError('unbound evidence')
    if v['bundle']!=str(op/'received') or v['restored']!=str(op/'restored'):raise ValueError('foreign evidence path')
    if not (s['deadlines']['prepare_by']-600<=v['observed_before']<=v['observed_after']<=v['deadline_epoch']) or time.time()>v['deadline_epoch']:raise ValueError('stale evidence')
    tree_receipt.verify(v['bundle'],manifest_sha,v['restored']);manifest=r.validate_bundle(v['bundle'],manifest_sha)
    if manifest['capture_id']!=s['capture_id'] or v['components']!=['controls','database','private','state'] or sorted(manifest['components'])!=v['components']:raise ValueError('component/capture mismatch')
    restored=op/'restored';dump=restored/'database/database.dump'
    if v['dump']!={'sha256':r.sha(r.stable_bytes(dump)),'bytes':dump.stat().st_size}:raise ValueError('dump mismatch')
    for field,name in [('globals_sha256','globals.sql'),('writer_proof_sha256','writer-proof.json')]:
        if v[field]!=r.sha(r.stable_bytes(restored/'database'/name)):raise ValueError('unbound database component')
    if r.sha(r.stable_bytes(restored/'private/signing.key'))!=v['signing_sha256']:raise ValueError('signing identity mismatch')
    before_raw=r.stable_bytes(d/'before.json');after_raw=r.stable_bytes(d/'after.json')
    if r.sha(before_raw)!=v['before_sha256'] or r.sha(after_raw)!=v['after_sha256'] or before_raw!=r.stable_bytes(restored/'database/before.json'):raise ValueError('observation digest/source mismatch')
    before=json.loads(before_raw);after=json.loads(after_raw)
    fields={'profile','schemas','extensions','extension_functions','column_acls','roles','memberships','columns','tables','constraints','indexes','sequence_definitions','sequence_values','table_values','database_acl','schema_acl','relation_acl','default_acls','relationships','file_references','unsupported_objects'}
    if set(before)!=fields or set(after)!=fields or before!=after or before['profile']!='cbm.pg18-synthetic/1':raise ValueError('canonical catalog/state differs')
    if {x['nspname'] for x in before['schemas']}!=catalog.SCHEMAS or {x['extname'] for x in before['extensions']}!=catalog.EXTENSIONS or {x['rolname'] for x in before['roles']}!=catalog.ROLES:raise ValueError('unsupported catalog census')
    if any(before['unsupported_objects'].values()) or set(before['unsupported_objects'])!={'relations','routines','types','triggers','event_triggers','publications','subscriptions','foreign_servers','large_objects','user_collations','policies','rules','statistics','operators','operator_classes','operator_families','user_casts','text_search','settings','security_labels','tablespaces'}:raise ValueError('unsupported object classes')
    if [x['rolname'] for x in before['roles'] if x['rolcanlogin']]!=['fixture']:raise ValueError('restore writer roles not closed')
    if any(before['relationships'][x] for x in ('orphan_stages','orphan_attempts','orphan_artifacts')) or before['relationships']['unknown_attempts']!=1:raise ValueError('unknown outcomes or relationships changed')
    refs=before['file_references']
    if len(refs)!=before['table_values']['app.artifacts']['rows']:raise ValueError('incomplete artifact membership')
    for ref in refs:
        if set(ref)!={'path','database_sha256','sha256','bytes'}:raise ValueError('unknown artifact acceptance field')
        p=Path(ref['path'])
        if p.is_absolute() or '..' in p.parts:raise ValueError('foreign artifact')
        raw=r.stable_bytes(r.no_links(restored/'state'/p))
        if len(raw)!=ref['bytes'] or r.sha(raw)!=ref['sha256'] or ref['sha256']!=ref['database_sha256']:raise ValueError('artifact identity mismatch')
    proof=json.loads(r.stable_bytes(restored/'database/writer-proof.json'))
    if set(proof)!={'method','closed_observation','before_controls_sha256','after_dump_observation','negative_clients'} or proof['method']!='nologin-revoke-connect-terminate-existing-sessions' or proof['closed_observation']!={'login_roles':['fixture'],'unexpected_backends':0} or proof['after_dump_observation']!=proof['closed_observation']:raise ValueError('incomplete writer admission evidence')
    if proof['negative_clients']!=['dml_connection_denied','ddl_connection_denied','sequence_connection_denied']:raise ValueError('writer exclusion not exercised')
    if proof['before_controls_sha256']!=r.sha(r.stable_bytes(restored/'database/writer-original.json')):raise ValueError('writer recovery controls unbound')
    for key,slot,database in [('source_identity','source','cbm_app'),('destination_identity','restore',s['database']['destination_database'])]:
        identity=v[key];pin=s['database'][slot]['identity']
        if set(identity)!={'system_identifier','version','database','database_oid','container_id','image'}:raise ValueError('unknown server identity field')
        if any(identity[x]!=pin[x] for x in ('system_identifier','version','container_id','image')) or identity['database']!=database:raise ValueError('server/version not pinned')
    if v['source_identity']['system_identifier']==v['destination_identity']['system_identifier'] or v['source_identity']['container_id']==v['destination_identity']['container_id']:raise ValueError('independent restore required')
    return {'schema':'cbm.database-verification/2','operation_id':s['operation_id'],'capture_id':s['capture_id'],'manifest_sha256':manifest_sha,'database_receipt_sha256':r.sha(r.stable_bytes(d/'database-receipt.json')),'canonical_observations_equal':True,'independent_servers':True,'writer_admission_exercised':True,'production_qualified':False}
