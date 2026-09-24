"""Actual cb_* profile. Only application database CONNECT/clients are fenced."""
import hashlib,json,subprocess,time,os
from pathlib import Path
HERE=Path(__file__).resolve().parent
QUERIES=json.loads((HERE/'catalog-queries.json').read_bytes())
APP_ROLES=('cbm_prod_runtime','cbm_prod_migration')
TABLES=('alembic_version','cb_artifacts','cb_attempts','cb_jobs','cb_model_calls','cb_operations','cb_outbox','cb_rejected_events','cb_sources','cb_stages')
def encode(v):return (json.dumps(v,sort_keys=True,indent=2)+'\n').encode()
def digest(v):return hashlib.sha256(encode(v)).hexdigest()
def command(args,data=None):
 p=subprocess.run(args,input=data,capture_output=True,timeout=30)
 if p.returncode:raise ValueError('database command refused; private output suppressed')
 return p.stdout
class Database:
 def __init__(self,container,database):
  if not container.startswith('cbm-r033-pg-') or database!='community_brain_prod':raise ValueError('development database binding required')
  self.container=container;self.database=database
 def sql(self,query):return command(['docker','exec','-i','-e','PGAPPNAME=cbm-r033-controller',self.container,'psql','-X','-qAt','-U','postgres','-d',self.database,'-v','ON_ERROR_STOP=1'],query.encode()).decode().strip()
 def rows(self,query):return json.loads(self.sql("SELECT coalesce(jsonb_agg(x),'[]'::jsonb) FROM ("+query+") x;"))
 def census(self):
  parts=["BEGIN ISOLATION LEVEL REPEATABLE READ READ ONLY; SET LOCAL statement_timeout='10s';"]
  for key,query in QUERIES.items():parts.append("SELECT jsonb_build_object('name','"+key+"','rows',coalesce(jsonb_agg(x),'[]'::jsonb)) FROM ("+query+") x;")
  parts.append('ROLLBACK;');rows=[json.loads(x) for x in self.sql('\n'.join(parts)).splitlines() if x.startswith('{')];v={x['name']:x['rows'] for x in rows}
  self.supported(v);return v
 def supported(self,v):
  p=json.loads((HERE/'admin-profile.json').read_bytes())['observations']
  for key in p:
   if key not in ('identity','writers','shared_scope') and v[key]!=p[key]:raise ValueError('actual production profile differs: '+key)
  if v['shared_scope'][0]['application_shared_labels']!=0:raise ValueError('unsupported application shared labels')
  if not v['identity'][0]['version'].startswith('18.6') or v['identity'][0]['read_only']!='on':raise ValueError('engine/read-only mismatch')
  if any(x['expressions'] or x['predicate'] for x in v['index_attributes']):raise ValueError('unsupported index expression/predicate')
  if sum(x['kind']=='S' for x in v['relations'])!=0:raise ValueError('sequence creation outside zero-sequence profile')
  if len(v['index_attributes'])!=19:raise ValueError('index census mismatch')
 def snapshot(self,files):
  v=self.census();catalog={k:v[k] for k in v if k not in ('identity','writers','shared_scope')}
  rows={name:self.rows('SELECT * FROM public."'+name+'" ORDER BY '+('version_num' if name=='alembic_version' else 'sha256' if name=='cb_rejected_events' else 'id')) for name in TABLES}
  if rows['alembic_version']!=[{'version_num':'0001_jobs'}]:raise ValueError('Alembic revision changed')
  refs=[]
  for table,pathkey,hashkey,sizekey in [('cb_sources','path','sha256','size'),('cb_artifacts','path','sha256','size'),('cb_model_calls','response_path','response_hash',None)]:
   for row in rows[table]:
    if row[pathkey] is None:continue
    rel=Path(row[pathkey]);p=Path(files)/rel
    if rel.is_absolute() or '..' in rel.parts or p.is_symlink() or not p.resolve().is_relative_to(Path(files).resolve()):raise ValueError('unsafe application file reference')
    raw=p.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    if sha!=row[hashkey] or sizekey and len(raw)!=row[sizekey]:raise ValueError('application file binding changed')
    refs.append({'table':table,'id':row['id'],'path':str(rel),'sha256':sha,'bytes':len(raw)})
  jobs={r['id']:r for r in rows['cb_jobs']};stages={r['id']:r for r in rows['cb_stages']};sources={r['id']:r for r in rows['cb_sources']}
  for row in rows['cb_jobs']:
   if row['parent_id'] and row['parent_id'] not in jobs:raise ValueError('orphan parent job')
   if any(x not in sources for x in row['sources']):raise ValueError('orphan job source')
  for table in ('cb_stages','cb_operations','cb_model_calls','cb_artifacts'):
   if any(r['job_id'] not in jobs for r in rows[table]):raise ValueError('orphan job relation')
  for table in ('cb_attempts','cb_outbox','cb_artifacts'):
   if any(r['stage_id'] not in stages for r in rows[table]):raise ValueError('orphan stage relation')
  if any(stages[r['stage_id']]['job_id']!=r['job_id'] for r in rows['cb_artifacts']):raise ValueError('cross-job artifact stage')
  return {'catalog':catalog,'tables':{n:{'rows':len(r),'sha256':digest(r)} for n,r in rows.items()},'file_references':refs,'unknown_outcomes':{n:sum(r['state']=='outcome_unknown' for r in rows[n]) for n in ('cb_attempts','cb_model_calls')},'alembic_revision':'0001_jobs','sequences':[]}
 def close_writers(self):
  before=self.rows("SELECT datacl::text AS acl FROM pg_database WHERE datname=current_database()")
  self.sql('REVOKE CONNECT ON DATABASE community_brain_prod FROM PUBLIC,cbm_prod_runtime,cbm_prod_migration;')
  self.sql("SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname=current_database() AND usename IN ('cbm_prod_runtime','cbm_prod_migration') AND pid<>pg_backend_pid();")
  self.assert_closed();return before
 def assert_closed(self):
  value=self.rows("SELECT (SELECT count(*) FROM pg_stat_activity WHERE datname=current_database() AND pid<>pg_backend_pid() AND NOT (usename='postgres' AND application_name='cbm-r033-controller')) AS unknown_clients,(SELECT count(*) FROM pg_database d CROSS JOIN LATERAL aclexplode(d.datacl) a WHERE d.datname=current_database() AND a.privilege_type='CONNECT' AND (a.grantee=0 OR pg_get_userbyid(a.grantee) IN ('cbm_prod_runtime','cbm_prod_migration'))) AS allowed_application_connect")
  if value!=[{'unknown_clients':0,'allowed_application_connect':0}]:raise ValueError('unreviewed writer or open application CONNECT')
 def restore_connect(self):
  self.sql('REVOKE ALL ON DATABASE community_brain_prod FROM PUBLIC;GRANT CONNECT ON DATABASE community_brain_prod TO cbm_prod_runtime,cbm_prod_migration;')
  expected=json.loads((HERE/'admin-profile.json').read_bytes())['observations']['database_acl']
  if self.rows(QUERIES['database_acl'])!=expected:raise ValueError('database ACL recovery mismatch')
