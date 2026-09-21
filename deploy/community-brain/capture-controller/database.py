"""Synthetic database capture observations and strict component evidence validator."""
import json,time,re,os,select,subprocess
from pathlib import Path,PurePosixPath
from contextlib import contextmanager
import common as c
r=c.r
import receipt as tree_receipt

def sql(container,query,database='fixture',timeout=8):
    return c.command(['docker','exec','-i',container,'psql','-X','-qAt','-U','fixture','-d',database,'-v','ON_ERROR_STOP=1'],query.encode(),timeout=timeout).decode().strip()

def identity(container,database='fixture'):
    row=c.inspect(container)
    v=json.loads(sql(container,"SELECT json_build_object('system_identifier',system_identifier::text,'version',current_setting('server_version'),'database',current_database(),'database_oid',(SELECT oid FROM pg_database WHERE datname=current_database())) FROM pg_control_system();",database))
    return dict(v,container_id=row['Id'],image=row['Image'])

def observe(container,files,database='fixture'):
    columns=json.loads(sql(container,"SELECT coalesce(json_agg(t ORDER BY table_name,ordinal_position),'[]') FROM (SELECT table_name,ordinal_position,column_name,data_type,is_nullable,column_default FROM information_schema.columns WHERE table_schema='public') t;",database))
    constraints=json.loads(sql(container,"SELECT coalesce(json_agg(t ORDER BY table_name,name),'[]') FROM (SELECT cl.relname AS table_name,con.conname AS name,pg_get_constraintdef(con.oid) AS definition FROM pg_constraint con JOIN pg_class cl ON cl.oid=con.conrelid JOIN pg_namespace n ON n.oid=cl.relnamespace WHERE n.nspname='public') t;",database))
    indexes=json.loads(sql(container,"SELECT coalesce(json_agg(t ORDER BY tablename,indexname),'[]') FROM (SELECT tablename,indexname,indexdef FROM pg_indexes WHERE schemaname='public') t;",database))
    sequence_definitions=json.loads(sql(container,"SELECT coalesce(json_agg(t ORDER BY sequencename),'[]') FROM (SELECT sequencename,data_type,start_value,min_value,max_value,increment_by,cycle,cache_size FROM pg_sequences WHERE schemaname='public') t;",database))
    tables=sql(container,"SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename;",database).splitlines()
    rows={}
    for table in tables:
        if not re.fullmatch('[a-z_]+',table):raise ValueError('unreviewed table identifier')
        raw=sql(container,'SELECT row_to_json(t)::text FROM public.'+table+' t ORDER BY row_to_json(t)::text;',database)
        values=[json.loads(line) for line in raw.splitlines()]
        rows[table]={'rows':len(values),'sha256':r.sha(r.encode(values))}
    sequences={}
    for name in sql(container,"SELECT sequencename FROM pg_sequences WHERE schemaname='public' ORDER BY sequencename;",database).splitlines():
        if not re.fullmatch('[a-z_]+',name):raise ValueError('unreviewed sequence')
        sequences[name]=json.loads(sql(container,'SELECT row_to_json(t) FROM (SELECT last_value,is_called FROM public.'+name+') t;',database))
    relationships=json.loads(sql(container,"SELECT json_build_object('orphan_artifacts',(SELECT count(*) FROM artifacts a LEFT JOIN sources s ON a.source_id=s.id WHERE s.id IS NULL),'orphan_stages',(SELECT count(*) FROM stages s LEFT JOIN jobs j ON j.id=s.job_id WHERE j.id IS NULL),'orphan_attempts',(SELECT count(*) FROM attempts a LEFT JOIN stages s ON s.id=a.stage_id WHERE s.id IS NULL),'unknown_attempts',(SELECT count(*) FROM attempts WHERE outcome='outcome_unknown'),'fts_matches',(SELECT count(*) FROM vectors WHERE body @@ plainto_tsquery('simple','provenance')));",database))
    refs=[]
    for line in sql(container,'SELECT json_build_object(\'path\',a.path,\'database_sha256\',s.sha256) FROM artifacts a JOIN sources s ON s.id=a.source_id ORDER BY a.id;',database).splitlines():
        ref=json.loads(line);relative=PurePosixPath(ref['path'])
        if relative.is_absolute() or '..' in relative.parts:raise ValueError('escaping file reference')
        p=r.no_links(Path(files)/relative)
        if not p.is_relative_to(Path(files)):raise ValueError('foreign reference')
        ref.update(sha256=r.sha(r.stable_bytes(p)),bytes=p.stat().st_size)
        if ref['sha256']!=ref['database_sha256']:raise ValueError('database/file content mismatch')
        refs.append(ref)
    return {'schema':{'columns':columns,'constraints':constraints,'indexes':indexes,'sequence_definitions':sequence_definitions},'tables':rows,'sequences':sequences,'relationships':relationships,'file_references':refs}

@contextmanager
def fence(s):
    container=s['database']['source']['id'];op=Path(s['operation']);app='cbm-r031-'+s['operation_id']
    tables=sql(container,"SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename;").splitlines()
    if not tables or any(not re.fullmatch('[a-z_]+',n) for n in tables):raise ValueError('table set unavailable')
    p=subprocess.Popen(['docker','exec','-i',container,'psql','-X','-qAt','-U','fixture','-d','fixture','-v','ON_ERROR_STOP=1'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1)
    try:
        p.stdin.write("SET application_name='"+app+"'; BEGIN ISOLATION LEVEL REPEATABLE READ; SET LOCAL lock_timeout='2s'; LOCK TABLE "+','.join('public.'+n for n in tables)+" IN SHARE MODE; SELECT json_build_object('snapshot',pg_export_snapshot(),'pid',pg_backend_pid());\n");p.stdin.flush()
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
    if app!='cbm-r031-'+s['operation_id']:raise ValueError('fence owner mismatch')
    return sql(s['database']['source']['id'],f"SELECT count(*) FROM pg_stat_activity WHERE pid={pid} AND application_name='{app}' AND state='idle in transaction';")== '1'

def release_fence(s):
    p=Path(s['operation'])/'fence.json'
    if p.exists():
        v=json.loads(r.stable_bytes(p));app='cbm-r031-'+s['operation_id']
        if v['application_name']!=app or v['container_id']!=s['database']['source']['id']:raise ValueError('foreign fence refused')
        sql(v['container_id'],f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid={int(v['pid'])} AND application_name='{app}';")

def verify_evidence(directory,s,manifest_sha):
    """Validate exact files/identities/observations; never accepts production scope."""
    d=r.no_links(directory)
    if {p.name for p in d.iterdir()}!={'database-receipt.json','before.json','after.json'}:raise ValueError('database evidence member set mismatch')
    v=json.loads(r.stable_bytes(d/'database-receipt.json'))
    keys={'schema','scope','owner_id','operation_id','capture_id','packet_sha256','manifest_sha256','bundle','restored','dump','before_sha256','after_sha256','source_identity','destination_identity','observed_before','observed_after','deadline_epoch'}
    if set(v)!=keys or v['schema']!='cbm.database-evidence/1' or v['scope']!='synthetic-development' or s['scope']!='synthetic-development':raise ValueError('unknown or production acceptance refused')
    for k in ('owner_id','operation_id','capture_id','packet_sha256'):
        if v[k]!=s[k]:raise ValueError('mixed attempt or source identity')
    if v['manifest_sha256']!=manifest_sha or v['deadline_epoch']!=s['deadlines']['validate_by']:raise ValueError('evidence binding mismatch')
    op=Path(s['operation'])
    if v['bundle']!=str(op/'received') or v['restored']!=str(op/'restored'):raise ValueError('foreign evidence paths')
    if not (v['observed_before']<=v['observed_after']<=v['deadline_epoch']) or v['observed_before']<s['deadlines']['prepare_by']-600 or time.time()>v['deadline_epoch']:raise ValueError('stale or invalid evidence interval')
    tree_receipt.verify(v['bundle'],manifest_sha,v['restored'])
    manifest=r.validate_bundle(v['bundle'],manifest_sha)
    if manifest['capture_id']!=s['capture_id']:raise ValueError('mixed capture')
    dump=op/'restored/database/database.dump';expected={'component':'database','path':'database.dump','sha256':r.sha(r.stable_bytes(dump)),'bytes':dump.stat().st_size}
    if v['dump']!=expected:raise ValueError('dump identity mismatch')
    before_raw=r.stable_bytes(d/'before.json');after_raw=r.stable_bytes(d/'after.json')
    if r.sha(before_raw)!=v['before_sha256'] or r.sha(after_raw)!=v['after_sha256']:raise ValueError('observation digest mismatch')
    if r.stable_bytes(op/'restored/database/before.json')!=before_raw:raise ValueError('unpaired before observation')
    before=json.loads(before_raw);after=json.loads(after_raw)
    fields={'schema','tables','sequences','relationships','file_references'}
    if set(before)!=fields or set(after)!=fields or before!=after:raise ValueError('canonical database observations differ')
    validate_observation(before)
    validate_observation(after)
    if not before['schema']['columns'] or not before['tables'] or not before['sequences']:raise ValueError('incomplete database observation')
    if set(before['relationships'])!={'orphan_artifacts','orphan_stages','orphan_attempts','unknown_attempts','fts_matches'} or any(before['relationships'][k]!=0 for k in ('orphan_artifacts','orphan_stages','orphan_attempts')):raise ValueError('invalid relationships')
    if len(before['file_references'])!=before['tables']['artifacts']['rows']:raise ValueError('incomplete file references')
    for ref in before['file_references']:
        if set(ref)!={'path','database_sha256','sha256','bytes'}:raise ValueError('unknown file reference')
        path=PurePosixPath(ref['path'])
        if path.is_absolute() or '..' in path.parts:raise ValueError('foreign file reference')
        f=r.no_links(op/'restored/state'/path)
        if r.sha(r.stable_bytes(f))!=ref['sha256'] or ref['sha256']!=ref['database_sha256'] or f.stat().st_size!=ref['bytes']:raise ValueError('file reference mismatch')
    src,dst=v['source_identity'],v['destination_identity']
    identity_keys={'system_identifier','version','database','database_oid','container_id','image'}
    if set(src)!=identity_keys or set(dst)!=identity_keys:raise ValueError('incomplete server identity')
    if src['container_id']!=s['database']['source']['id'] or dst['container_id']!=s['database']['restore']['id'] or src['image']!=s['database']['source']['image'] or dst['image']!=s['database']['restore']['image']:raise ValueError('foreign database server')
    expected_dst=dict(s['database']['restore']['identity'],database=s['database']['destination_database'],database_oid=dst['database_oid'])
    if src!=s['database']['source']['identity'] or dst!=expected_dst:raise ValueError('server identity not pinned by specification')
    if src['container_id']==dst['container_id'] or src['system_identifier']==dst['system_identifier'] or dst['database']!=s['database']['destination_database'] or src['database']!='fixture':raise ValueError('restore is not independently bound')
    return {'schema':'cbm.database-verification/1','capture_id':s['capture_id'],'operation_id':s['operation_id'],'manifest_sha256':manifest_sha,'database_receipt_sha256':r.sha(r.stable_bytes(d/'database-receipt.json')),'canonical_observations_equal':True,'independent_servers':True,'production_qualified':False}


def validate_observation(v):
    """Exact public-schema observation shape; new acceptance fields fail closed."""
    if set(v)!={'schema','tables','sequences','relationships','file_references'}:raise ValueError('unknown observation fields')
    schema=v['schema']
    shapes={'columns':{'table_name','ordinal_position','column_name','data_type','is_nullable','column_default'},'constraints':{'table_name','name','definition'},'indexes':{'tablename','indexname','indexdef'},'sequence_definitions':{'sequencename','data_type','start_value','min_value','max_value','increment_by','cycle','cache_size'}}
    if set(schema)!=set(shapes):raise ValueError('unknown schema fields')
    for key,fields in shapes.items():
        if not isinstance(schema[key],list) or not schema[key]:raise ValueError('empty schema observations')
        for row in schema[key]:
            if set(row)!=fields:raise ValueError('unknown canonical schema field')
    if {row['table_name'] for row in schema['columns']}!=set(v['tables']):raise ValueError('table observation set mismatch')
    if {row['sequencename'] for row in schema['sequence_definitions']}!=set(v['sequences']):raise ValueError('sequence observation set mismatch')
    for row in v['tables'].values():
        if set(row)!={'rows','sha256'} or type(row['rows']) is not int or row['rows']<0 or not re.fullmatch('[0-9a-f]{64}',row['sha256']):raise ValueError('invalid table observation')
    for row in v['sequences'].values():
        if set(row)!={'last_value','is_called'} or type(row['last_value']) is not int or type(row['is_called']) is not bool:raise ValueError('invalid sequence observation')
    if set(v['relationships'])!={'orphan_artifacts','orphan_stages','orphan_attempts','unknown_attempts','fts_matches'} or any(type(x) is not int or x<0 for x in v['relationships'].values()):raise ValueError('invalid relationship observations')
