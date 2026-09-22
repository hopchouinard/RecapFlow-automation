"""Metadata-only diagnosis using existing local runtime DB identity. No row data."""
import datetime,json,os
from sqlalchemy import create_engine,text

QUERIES={
'identity':"SELECT current_database() AS database,current_user AS observer,current_setting('server_version') AS version,current_setting('transaction_read_only') AS read_only",
'application_roles':"SELECT rolname AS name,rolsuper AS superuser,rolcanlogin AS login,rolcreaterole AS create_role,rolcreatedb AS create_db,rolreplication AS replication,rolbypassrls AS bypass_rls FROM pg_roles WHERE rolname IN ('cbm_prod_runtime','cbm_prod_migration') ORDER BY 1",
'schemas':"SELECT nspname AS name,pg_get_userbyid(nspowner) AS owner FROM pg_namespace WHERE nspname NOT LIKE 'pg_%' AND nspname<>'information_schema' ORDER BY 1",
'extensions':"SELECT extname AS name,extversion AS version,n.nspname AS schema FROM pg_extension e JOIN pg_namespace n ON n.oid=e.extnamespace ORDER BY 1",
'relations':"SELECT n.nspname AS schema,c.relname AS name,c.relkind AS kind,pg_get_userbyid(c.relowner) AS owner,c.relispartition AS partition,c.relrowsecurity AS row_security,c.relforcerowsecurity AS force_row_security FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname NOT LIKE 'pg_%' AND n.nspname<>'information_schema' ORDER BY 1,2",
'custom_routines':"SELECT n.nspname AS schema,p.proname AS name,p.prokind AS kind FROM pg_proc p JOIN pg_namespace n ON n.oid=p.pronamespace WHERE n.nspname NOT LIKE 'pg_%' AND n.nspname<>'information_schema' AND NOT EXISTS(SELECT 1 FROM pg_depend d WHERE d.classid='pg_proc'::regclass AND d.objid=p.oid AND d.deptype='e') ORDER BY 1,2",
'custom_types':"SELECT n.nspname AS schema,t.typname AS name,t.typtype AS kind FROM pg_type t JOIN pg_namespace n ON n.oid=t.typnamespace WHERE n.nspname NOT LIKE 'pg_%' AND n.nspname<>'information_schema' AND (t.typtype IN ('d','e','r','m') OR (t.typtype='b' AND t.typcategory<>'A')) ORDER BY 1,2",
'column_types':"SELECT DISTINCT n.nspname AS schema,format_type(a.atttypid,a.atttypmod) AS type FROM pg_attribute a JOIN pg_class c ON c.oid=a.attrelid JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname NOT LIKE 'pg_%' AND n.nspname<>'information_schema' AND c.relkind IN ('r','p') AND a.attnum>0 AND NOT a.attisdropped ORDER BY 1,2",
'database_acl':"SELECT pg_get_userbyid(datdba) AS owner,datacl::text AS acl FROM pg_database WHERE datname=current_database()",
'default_acls':"SELECT pg_get_userbyid(defaclrole) AS owner,coalesce(n.nspname,'*') AS schema,defaclobjtype AS kind,defaclacl::text AS acl FROM pg_default_acl d LEFT JOIN pg_namespace n ON n.oid=d.defaclnamespace ORDER BY 1,2,3",
'object_counts':"SELECT (SELECT count(*) FROM pg_event_trigger) AS event_triggers,(SELECT count(*) FROM pg_publication) AS publications,(SELECT count(*) FROM pg_policy) AS policies,(SELECT count(*) FROM pg_foreign_server) AS foreign_servers,(SELECT count(*) FROM pg_largeobject_metadata) AS large_objects,(SELECT count(*) FROM pg_statistic_ext) AS statistics",
}

def census():
    result={}
    engine=create_engine(os.environ['CB_DATABASE_URL'])
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(text('SET TRANSACTION ISOLATION LEVEL REPEATABLE READ, READ ONLY'))
            conn.execute(text("SET LOCAL statement_timeout='10s'"))
            for name,query in QUERIES.items():
                result[name]=[dict(row) for row in conn.execute(text(query)).mappings()]
    engine.dispose()
    return dict(schema='cbm.metadata-census/1',observed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),application_rows_read=False,coverage='initial runtime-role metadata census; administrator coverage remains required',observations=result)

if __name__=='__main__':
    try:print(json.dumps(census(),indent=2,sort_keys=True))
    except Exception as exc:
        # Driver exceptions can contain connection details; never print them.
        print(json.dumps({'error_type':type(exc).__name__,'census_complete':False}));raise SystemExit(1)
