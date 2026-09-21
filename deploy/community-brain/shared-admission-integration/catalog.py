"""Closed, explicit PostgreSQL 18.6 synthetic catalog and writer-admission profile."""
import json,re,time
from pathlib import Path
import common as c
r=c.r
DATABASE='cbm_app'
ROLES={'fixture','cbm_owner','cbm_runtime','cbm_ddl'}
SCHEMAS={'public','app','audit'}
EXTENSIONS={'plpgsql','pgcrypto'}

def sql(container,query,database=DATABASE,role='fixture',timeout=10):
    return c.command(['docker','exec','-i','-e','PGAPPNAME=cbm-r032-observe',container,'psql','-X','-qAt','-U',role,'-d',database,'-v','ON_ERROR_STOP=1'],query.encode(),timeout=timeout).decode().strip()

def j(container,query,database=DATABASE):return json.loads(sql(container,query,database))
def ident(value):
    if not re.fullmatch('[a-z_][a-z_0-9]*',value):raise ValueError('unsupported SQL identifier')
    return '"'+value+'"'

def rows(container,query,database=DATABASE):
    return j(container,"SELECT coalesce(json_agg(t ORDER BY row_to_json(t)::text),'[]') FROM ("+query+") t;",database)

def acl_query(object_kind):
    if object_kind=='database':return "SELECT CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END AS grantee,pg_get_userbyid(a.grantor) AS grantor,a.privilege_type,a.is_grantable FROM pg_database d CROSS JOIN LATERAL aclexplode(coalesce(d.datacl,acldefault('d',d.datdba))) a WHERE d.datname=current_database()"
    if object_kind=='schema':return "SELECT n.nspname AS object,CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END AS grantee,pg_get_userbyid(a.grantor) AS grantor,a.privilege_type,a.is_grantable FROM pg_namespace n CROSS JOIN LATERAL aclexplode(coalesce(n.nspacl,acldefault('n',n.nspowner))) a WHERE n.nspname IN ('public','app','audit')"
    return "SELECT n.nspname||'.'||cl.relname AS object,CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END AS grantee,pg_get_userbyid(a.grantor) AS grantor,a.privilege_type,a.is_grantable FROM pg_class cl JOIN pg_namespace n ON n.oid=cl.relnamespace CROSS JOIN LATERAL aclexplode(coalesce(cl.relacl,acldefault(CASE WHEN cl.relkind='S' THEN 's'::\"char\" ELSE 'r'::\"char\" END,cl.relowner))) a WHERE n.nspname IN ('public','app','audit') AND cl.relkind IN ('r','S')"

def controls(container,database=DATABASE):
    return {'roles':rows(container,"SELECT rolname,rolcanlogin FROM pg_roles WHERE rolname !~ '^pg_'",database),
            'database_acl':rows(container,acl_query('database'),database)}

def apply_database_acl(container,database,acls):
    if {x['grantee'] for x in acls}-ROLES-{'PUBLIC'}:raise ValueError('unsupported DB grantee')
    query='REVOKE ALL ON DATABASE '+ident(database)+' FROM PUBLIC,'+','.join(ident(x) for x in sorted(ROLES))+';'
    for a in acls:
        if set(a)!={'grantee','grantor','privilege_type','is_grantable'} or a['grantor'] not in ROLES or a['privilege_type'] not in ('CREATE','CONNECT','TEMPORARY'):raise ValueError('unsupported DB ACL')
        grantee='PUBLIC' if a['grantee']=='PUBLIC' else ident(a['grantee'])
        query+='GRANT '+a['privilege_type']+' ON DATABASE '+ident(database)+' TO '+grantee+(' WITH GRANT OPTION' if a['is_grantable'] else '')+';'
    sql(container,query,database)

def close_writers(s):
    container=s['database']['source']['id'];op=Path(s['operation']);original=controls(container)
    if {x['rolname'] for x in original['roles']}!=ROLES:raise ValueError('unreviewed login role census')
    r.write_new(op/'writer-admission-intent.json',r.encode(original))
    sql(container,'ALTER ROLE cbm_runtime NOLOGIN;ALTER ROLE cbm_ddl NOLOGIN;REVOKE CONNECT ON DATABASE cbm_app FROM PUBLIC,cbm_runtime,cbm_ddl;')
    sql(container,"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname=current_database() AND usename IN ('cbm_runtime','cbm_ddl');")
    assert_closed(s)
    r.write_new(op/'writer-admission-closed.json',r.encode({'at':time.time(),'controls':controls(container),'original_sha256':r.sha(r.stable_bytes(op/'writer-admission-intent.json'))}))

def assert_closed(s):
    container=s['database']['source']['id']
    value=j(container,"SELECT json_build_object('login_roles',(SELECT json_agg(rolname ORDER BY rolname) FROM pg_roles WHERE rolcanlogin AND rolname !~ '^pg_'),'unexpected_backends',(SELECT count(*) FROM pg_stat_activity WHERE datname=current_database() AND pid<>pg_backend_pid() AND (usename<>'fixture' OR application_name NOT LIKE 'cbm-r032-%')));")
    if value!={'login_roles':['fixture'],'unexpected_backends':0}:
        p=Path(s['operation'])/'writer-admission-refused.json'
        if not p.exists():r.write_new(p,r.encode({'at':time.time(),'observation':value,'reason':'unreviewed login role or backend; no quiescence claim'}))
        raise ValueError('writer admission lost')
    current=controls(container)
    if any(x['privilege_type']=='CONNECT' and x['grantee'] in ('PUBLIC','cbm_runtime','cbm_ddl') for x in current['database_acl']):raise ValueError('CONNECT admission remains open')
    return value

def restore_writers(s):
    op=Path(s['operation']);path=op/'writer-admission-intent.json'
    if not path.exists():return
    original=json.loads(r.stable_bytes(path));container=s['database']['source']['id']
    if {x['rolname'] for x in original['roles']}!=ROLES:raise ValueError('unknown admission recovery roles')
    if controls(container)==original:return
    apply_database_acl(container,DATABASE,original['database_acl'])
    for row in original['roles']:
        if row['rolname'] in ('cbm_runtime','cbm_ddl'):
            sql(container,'ALTER ROLE '+ident(row['rolname'])+(' LOGIN;' if row['rolcanlogin'] else ' NOLOGIN;'))
    if controls(container)!=original:raise ValueError('writer controls not restored exactly')
    c.atom(op/'writer-admission-restored.json',{'at':time.time(),'original_sha256':r.sha(r.stable_bytes(path)),'equal':True})

def observe(container,files,database=DATABASE):
    schemas=rows(container,"SELECT nspname,pg_get_userbyid(nspowner) AS owner FROM pg_namespace WHERE nspname NOT LIKE 'pg_%' AND nspname<>'information_schema'",database)
    extensions=rows(container,"SELECT extname,extversion,pg_get_userbyid(extowner) AS owner,n.nspname AS schema FROM pg_extension e JOIN pg_namespace n ON n.oid=e.extnamespace",database)
    roles=rows(container,"SELECT rolname,rolsuper,rolinherit,rolcreaterole,rolcreatedb,rolcanlogin,rolreplication,rolbypassrls,rolconnlimit,rolvaliduntil::text,rolconfig FROM pg_roles WHERE rolname !~ '^pg_'",database)
    if {x['nspname'] for x in schemas}!=SCHEMAS or {x['extname'] for x in extensions}!=EXTENSIONS or {x['rolname'] for x in roles}!=ROLES:raise ValueError('unsupported schema/extension/role census')
    coverage=j(container,"""SELECT json_build_object(
      'relations',(SELECT count(*) FROM pg_class cl JOIN pg_namespace n ON n.oid=cl.relnamespace WHERE n.nspname IN ('public','app','audit') AND (cl.relkind NOT IN ('r','S','i') OR cl.relispartition OR cl.relrowsecurity OR cl.relforcerowsecurity)),
      'routines',(SELECT count(*) FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace WHERE n.nspname IN ('public','app','audit') AND NOT EXISTS(SELECT 1 FROM pg_depend d WHERE d.classid='pg_proc'::regclass AND d.objid=p.oid AND d.deptype='e')),
      'types',(SELECT count(*) FROM pg_type t JOIN pg_namespace n ON n.oid=t.typnamespace WHERE n.nspname IN ('public','app','audit') AND (t.typtype IN ('d','e','r','m') OR (t.typtype='b' AND t.typcategory<>'A'))),
      'triggers',(SELECT count(*) FROM pg_trigger t JOIN pg_class cl ON cl.oid=t.tgrelid JOIN pg_namespace n ON n.oid=cl.relnamespace WHERE n.nspname IN ('public','app','audit') AND NOT t.tgisinternal),
      'event_triggers',(SELECT count(*) FROM pg_event_trigger),
      'publications',(SELECT count(*) FROM pg_publication),
      'subscriptions',(SELECT count(*) FROM pg_subscription),
      'foreign_servers',(SELECT count(*) FROM pg_foreign_server),
      'large_objects',(SELECT count(*) FROM pg_largeobject_metadata),
      'policies',(SELECT count(*) FROM pg_policy),
      'rules',(SELECT count(*) FROM pg_rewrite rw JOIN pg_class cl ON cl.oid=rw.ev_class JOIN pg_namespace n ON n.oid=cl.relnamespace WHERE n.nspname IN ('public','app','audit')),
      'statistics',(SELECT count(*) FROM pg_statistic_ext),
      'operators',(SELECT count(*) FROM pg_operator o JOIN pg_namespace n ON n.oid=o.oprnamespace WHERE n.nspname IN ('public','app','audit')),
      'operator_classes',(SELECT count(*) FROM pg_opclass o JOIN pg_namespace n ON n.oid=o.opcnamespace WHERE n.nspname IN ('public','app','audit')),
      'operator_families',(SELECT count(*) FROM pg_opfamily o JOIN pg_namespace n ON n.oid=o.opfnamespace WHERE n.nspname IN ('public','app','audit')),
      'user_casts',(SELECT count(*) FROM pg_cast WHERE oid>=16384),
      'text_search',(SELECT count(*) FROM (SELECT cfgnamespace AS ns FROM pg_ts_config UNION ALL SELECT dictnamespace FROM pg_ts_dict UNION ALL SELECT prsnamespace FROM pg_ts_parser UNION ALL SELECT tmplnamespace FROM pg_ts_template) ts JOIN pg_namespace n ON n.oid=ts.ns WHERE n.nspname IN ('public','app','audit')),
      'settings',(SELECT count(*) FROM pg_db_role_setting),
      'security_labels',(SELECT count(*) FROM pg_seclabel),
      'tablespaces',(SELECT count(*) FROM pg_tablespace WHERE spcname NOT LIKE 'pg_%'),
      'user_collations',(SELECT count(*) FROM pg_collation co JOIN pg_namespace n ON n.oid=co.collnamespace WHERE n.nspname IN ('public','app','audit')));""",database)
    if any(coverage.values()):raise ValueError('unsupported object class: '+','.join(k for k,v in coverage.items() if v))
    extension_functions=rows(container,"SELECT n.nspname AS schema,p.proname AS name,pg_get_function_identity_arguments(p.oid) AS arguments,pg_get_userbyid(p.proowner) AS owner,pg_get_functiondef(p.oid) AS definition,(SELECT json_agg(z ORDER BY row_to_json(z)::text) FROM (SELECT CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END AS grantee,pg_get_userbyid(a.grantor) AS grantor,a.privilege_type,a.is_grantable FROM aclexplode(coalesce(p.proacl,acldefault('f',p.proowner))) a) z) AS acl FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace WHERE n.nspname IN ('public','app','audit') AND EXISTS(SELECT 1 FROM pg_depend d WHERE d.classid='pg_proc'::regclass AND d.objid=p.oid AND d.deptype='e')",database)
    column_acls=rows(container,"SELECT n.nspname AS schema,cl.relname AS table,a.attname AS column,a.attacl::text AS acl FROM pg_attribute a JOIN pg_class cl ON cl.oid=a.attrelid JOIN pg_namespace n ON n.oid=cl.relnamespace WHERE n.nspname IN ('public','app','audit') AND cardinality(a.attacl)>0",database)
    memberships=rows(container,"SELECT pg_get_userbyid(roleid) AS role,pg_get_userbyid(member) AS member,pg_get_userbyid(grantor) AS grantor,admin_option,inherit_option,set_option FROM pg_auth_members WHERE pg_get_userbyid(member) !~ '^pg_'",database)
    columns=rows(container,"SELECT n.nspname AS schema,cl.relname AS table,a.attnum AS position,a.attname AS name,format_type(a.atttypid,a.atttypmod) AS type,a.attnotnull AS not_null,a.attidentity AS identity,a.attgenerated AS generated,pg_get_expr(d.adbin,d.adrelid) AS default FROM pg_attribute a JOIN pg_class cl ON cl.oid=a.attrelid JOIN pg_namespace n ON n.oid=cl.relnamespace LEFT JOIN pg_attrdef d ON d.adrelid=cl.oid AND d.adnum=a.attnum WHERE n.nspname IN ('public','app','audit') AND cl.relkind='r' AND a.attnum>0 AND NOT a.attisdropped",database)
    tables=rows(container,"SELECT n.nspname AS schema,cl.relname AS name,pg_get_userbyid(cl.relowner) AS owner,cl.relkind,cl.relpersistence,cl.reloptions,am.amname AS access_method FROM pg_class cl JOIN pg_namespace n ON n.oid=cl.relnamespace LEFT JOIN pg_am am ON am.oid=cl.relam WHERE n.nspname IN ('public','app','audit') AND cl.relkind='r'",database)
    constraints=rows(container,"SELECT n.nspname AS schema,cl.relname AS table,con.conname AS name,pg_get_constraintdef(con.oid) AS definition FROM pg_constraint con JOIN pg_class cl ON cl.oid=con.conrelid JOIN pg_namespace n ON n.oid=cl.relnamespace WHERE n.nspname IN ('public','app','audit')",database)
    indexes=rows(container,"SELECT schemaname,tablename,indexname,indexdef FROM pg_indexes WHERE schemaname IN ('public','app','audit')",database)
    sequences=rows(container,"SELECT schemaname,sequencename,sequenceowner,data_type,start_value,min_value,max_value,increment_by,cycle,cache_size FROM pg_sequences WHERE schemaname IN ('public','app','audit')",database)
    values={}
    for row in sequences:
        name=row['schemaname']+'.'+row['sequencename'];values[name]=j(container,'SELECT row_to_json(t) FROM (SELECT last_value,is_called FROM '+'.'.join(map(ident,name.split('.')))+') t;',database)
    table_values={}
    for row in tables:
        name=row['schema']+'.'+row['name'];data=rows(container,'SELECT * FROM '+'.'.join(map(ident,name.split('.'))),database)
        table_values[name]={'rows':len(data),'sha256':r.sha(r.encode(data))}
    default_acls=rows(container,"SELECT pg_get_userbyid(d.defaclrole) AS role,coalesce(n.nspname,'') AS schema,d.defaclobjtype,CASE WHEN a.grantee=0 THEN 'PUBLIC' ELSE pg_get_userbyid(a.grantee) END AS grantee,pg_get_userbyid(a.grantor) AS grantor,a.privilege_type,a.is_grantable FROM pg_default_acl d LEFT JOIN pg_namespace n ON n.oid=d.defaclnamespace CROSS JOIN LATERAL aclexplode(d.defaclacl) a",database)
    relationships=j(container,"SELECT json_build_object('orphan_stages',(SELECT count(*) FROM app.stages s LEFT JOIN app.jobs j ON j.id=s.job_id WHERE j.id IS NULL),'orphan_attempts',(SELECT count(*) FROM app.attempts a LEFT JOIN app.stages s ON s.id=a.stage_id WHERE s.id IS NULL),'unknown_attempts',(SELECT count(*) FROM app.attempts WHERE outcome='outcome_unknown'),'orphan_artifacts',(SELECT count(*) FROM app.artifacts a LEFT JOIN app.sources s ON s.id=a.source_id WHERE s.id IS NULL),'fts_matches',(SELECT count(*) FROM app.vectors WHERE body @@ plainto_tsquery('simple','provenance')));",database)
    refs=rows(container,"SELECT a.path,s.sha256 AS database_sha256 FROM app.artifacts a JOIN app.sources s ON a.source_id=s.id",database)
    for ref in refs:
        path=Path(ref['path'])
        if path.is_absolute() or '..' in path.parts:raise ValueError('escaping artifact')
        p=r.no_links(Path(files)/path);ref.update(sha256=r.sha(r.stable_bytes(p)),bytes=p.stat().st_size)
        if ref['sha256']!=ref['database_sha256']:raise ValueError('artifact digest mismatch')
    return {'profile':'cbm.pg18-synthetic/1','schemas':schemas,'extensions':extensions,'roles':roles,'memberships':memberships,
        'extension_functions':extension_functions,'column_acls':column_acls,'columns':columns,'tables':tables,'constraints':constraints,'indexes':indexes,'sequence_definitions':sequences,'sequence_values':values,
        'table_values':table_values,'database_acl':rows(container,acl_query('database'),database),'schema_acl':rows(container,acl_query('schema'),database),
        'relation_acl':rows(container,acl_query('relation'),database),'default_acls':default_acls,'relationships':relationships,'file_references':refs,'unsupported_objects':coverage}
