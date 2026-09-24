"""Real schema, isolated PG18.6 servers, application-scoped writer closure and restore."""
import hashlib,json,os,select,subprocess,sys,time,uuid
from pathlib import Path
from database import Database,HERE,command,digest,encode
ROOT=Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033')
IMAGE='sha256:4ef4dbc939d61acea57712655ddb4b4ab27419c913f94cca0cd57cb3ea3c2280'
def save(p,v):
 with p.open('xb') as f:f.write(encode(v))
 p.chmod(0o600)
def setup(label):
 name='cbm-r033-pg-'+label;data=ROOT/label;data.mkdir(mode=0o700);os.chown(data,999,999)
 ident=command(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','256m','--cpus','0.5','-e','POSTGRES_HOST_AUTH_METHOD=trust','--mount','type=bind,source='+str(data)+',target=/var/lib/postgresql',IMAGE]).decode().strip()
 save(ROOT/(label+'-created.json'),{'id':ident,'name':name,'data':str(data),'image':IMAGE})
 for _ in range(80):
  p=subprocess.run(['docker','exec',name,'pg_isready','-h','127.0.0.1','-U','postgres'],capture_output=True)
  if p.returncode==0:break
  time.sleep(.2)
 else:raise ValueError('database readiness')
 command(['docker','exec','-i',name,'psql','-U','postgres','-v','ON_ERROR_STOP=1'],b'CREATE ROLE cbm_prod_migration LOGIN;CREATE ROLE cbm_prod_runtime LOGIN;CREATE ROLE unrelated_service LOGIN;CREATE DATABASE unrelated_db OWNER unrelated_service;CREATE DATABASE community_brain_prod OWNER cbm_prod_migration;')
 return Database(name,'community_brain_prod')
def fixtures(db,files):
 db.sql("REVOKE ALL ON DATABASE community_brain_prod FROM PUBLIC;GRANT CONNECT ON DATABASE community_brain_prod TO cbm_prod_runtime;ALTER SCHEMA public OWNER TO cbm_prod_migration;REVOKE ALL ON SCHEMA public FROM PUBLIC;GRANT USAGE ON SCHEMA public TO cbm_prod_runtime;SET ROLE cbm_prod_migration;ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT,INSERT,UPDATE,DELETE ON TABLES TO cbm_prod_runtime;ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT,USAGE ON SEQUENCES TO cbm_prod_runtime;CREATE TABLE alembic_version(version_num varchar(32) NOT NULL,CONSTRAINT alembic_version_pkc PRIMARY KEY(version_num));INSERT INTO alembic_version VALUES ('0001_jobs');"+(HERE/'actual-schema-source/0001_jobs.sql').read_text())
 files.mkdir(mode=0o700);body=b'Request033 synthetic source artifact response';(files/'artifact.txt').write_bytes(body);sha=hashlib.sha256(body).hexdigest();ids=[str(uuid.UUID(int=i)) for i in range(1,10)];source,job,stage,attempt,artifact,model,operation,outbox=ids[:8]
 sql=f"""INSERT INTO cb_sources(id,scope,meeting_id,kind,sha256,path,size) VALUES ('{source}','community-brain','synthetic','chat','{sha}','artifact.txt',{len(body)});
 INSERT INTO cb_jobs(id,scope,principal,key,request_hash,identity,sources,mode,config,version,processing,artifacts,indexing,git,distribution) VALUES ('{job}','community-brain','synthetic','key','{sha}','{{}}','["{source}"]','held','{{}}','synthetic','held','held','held','held','held');
 INSERT INTO cb_stages(id,job_id,name,state,generation,fence,attempts) VALUES ('{stage}','{job}','synthetic','held',1,1,1);
 INSERT INTO cb_attempts(id,stage_id,fence,owner,state) VALUES ('{attempt}','{stage}',1,'synthetic','outcome_unknown');
 INSERT INTO cb_artifacts VALUES ('{artifact}','{job}','{stage}',1,'synthetic','artifact.txt','{sha}',{len(body)});
 INSERT INTO cb_model_calls VALUES ('{model}','{job}','synthetic',1,'outcome_unknown','{{}}','artifact.txt','{sha}','{{}}');
 INSERT INTO cb_operations VALUES ('{operation}','community-brain','synthetic','submit','key','{sha}','{job}');
 INSERT INTO cb_outbox(id,stage_id,generation) VALUES ('{outbox}','{stage}',1);
 INSERT INTO cb_rejected_events(sha256,reason) VALUES ('{sha}','synthetic rejection retained');"""
 db.sql(sql)
def client(db,role,query,database=None):
 p=subprocess.Popen(['docker','exec','-i','-e','PGAPPNAME=synthetic-writer',db.container,'psql','-X','-qAt','-U',role,'-d',database or db.database,'-v','ON_ERROR_STOP=1'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
 p.stdin.write(query+";SELECT 'READY';\n");p.stdin.flush()
 assert select.select([p.stdout],[],[],10)[0] and p.stdout.readline().strip()=='READY';return p
def run(label):
 ROOT.mkdir(mode=0o700,parents=True,exist_ok=True);src=setup(label+'source');dst=setup(label+'restore');files=ROOT/(label+'files');fixtures(src,files)
 before=src.snapshot(files);assert before['unknown_outcomes']=={'cb_attempts':1,'cb_model_calls':1}
 other=client(src,'unrelated_service','BEGIN',database='unrelated_db')
 clients=[client(src,'cbm_prod_runtime',"BEGIN;UPDATE cb_jobs SET reason='uncommitted'"),client(src,'cbm_prod_migration','BEGIN;CREATE TABLE should_rollback(id int)')]
 original=src.close_writers()
 for p in clients:
  p.stdin.write('COMMIT;\n');p.stdin.flush();p.wait(timeout=10);assert p.returncode!=0
 assert other.poll() is None
 # TCP attempts exercise actual CONNECT ACLs; local trust still enforces database ACL.
 denies=[]
 for role in ('cbm_prod_runtime','cbm_prod_migration'):
  p=subprocess.run(['docker','exec',src.container,'psql','-U',role,'-d',src.database,'-c','SELECT 1'],capture_output=True);assert p.returncode!=0;denies.append(role)
 src.assert_closed();dump=command(['docker','exec',src.container,'pg_dump','-U','postgres','-Fc','-d',src.database]);src.assert_closed();path=ROOT/(label+'.dump');path.write_bytes(dump);path.chmod(0o600)
 src.restore_connect();assert src.snapshot(files)==before
 command(['docker','exec','-i',dst.container,'pg_restore','-U','postgres','--exit-on-error','-d',dst.database],dump);dst.restore_connect();after=dst.snapshot(files);assert before==after
 ids=[d.rows('SELECT system_identifier::text AS id FROM pg_control_system()')[0]['id'] for d in (src,dst)];assert ids[0]!=ids[1]
 # Real mutations on restored server; restore every mutation before proceeding.
 cases=[('index_keys','DROP INDEX ix_cb_artifacts_job_id;SET ROLE cbm_prod_migration;CREATE INDEX ix_cb_artifacts_job_id ON cb_artifacts(stage_id);RESET ROLE','DROP INDEX ix_cb_artifacts_job_id;SET ROLE cbm_prod_migration;CREATE INDEX ix_cb_artifacts_job_id ON cb_artifacts(job_id);RESET ROLE'),('sequence','CREATE SEQUENCE forbidden','DROP SEQUENCE forbidden'),('acl','REVOKE SELECT ON cb_jobs FROM cbm_prod_runtime','GRANT SELECT ON cb_jobs TO cbm_prod_runtime'),('extra_acl','GRANT TRUNCATE ON cb_jobs TO cbm_prod_runtime','REVOKE TRUNCATE ON cb_jobs FROM cbm_prod_runtime'),('default_acl','ALTER DEFAULT PRIVILEGES FOR ROLE cbm_prod_migration IN SCHEMA public REVOKE INSERT ON TABLES FROM cbm_prod_runtime','ALTER DEFAULT PRIVILEGES FOR ROLE cbm_prod_migration IN SCHEMA public GRANT INSERT ON TABLES TO cbm_prod_runtime'),('role_membership','GRANT cbm_prod_migration TO cbm_prod_runtime','REVOKE cbm_prod_migration FROM cbm_prod_runtime'),('view','CREATE VIEW forbidden AS SELECT 1 AS x','DROP VIEW forbidden'),('function',"CREATE FUNCTION public.forbidden() RETURNS int LANGUAGE sql AS 'SELECT 1'",'DROP FUNCTION public.forbidden()'),('model_unknown',"UPDATE cb_model_calls SET state='completed'","UPDATE cb_model_calls SET state='outcome_unknown'"),('attempt_unknown',"UPDATE cb_attempts SET state='completed'","UPDATE cb_attempts SET state='outcome_unknown'"),('alembic',"UPDATE alembic_version SET version_num='wrong'","UPDATE alembic_version SET version_num='0001_jobs'"),('operation',"UPDATE cb_operations SET request_hash='changed'","UPDATE cb_operations SET request_hash='"+hashlib.sha256((files/'artifact.txt').read_bytes()).hexdigest()+"'"),('rejected_event',"UPDATE cb_rejected_events SET reason='changed'","UPDATE cb_rejected_events SET reason='synthetic rejection retained'"),('model_file',"UPDATE cb_model_calls SET response_hash='changed'","UPDATE cb_model_calls SET response_hash='"+hashlib.sha256((files/'artifact.txt').read_bytes()).hexdigest()+"'")]
 results=[]
 for name,mutate,undo in cases:
  dst.sql(mutate)
  try:
   try:assert dst.snapshot(files)==before
   except (ValueError,AssertionError):results.append({'case':name,'actual_postgresql_mutation':True,'rejected':True})
   else:raise AssertionError('accepted '+name)
  finally:dst.sql(undo)
  assert dst.snapshot(files)==before
 # Unknown administrator is not terminated; capture is refused and ACL restored.
 admin=client(src,'postgres','BEGIN')
 try:
  try:src.close_writers()
  except ValueError:pass
  else:raise AssertionError('unreviewed administrator accepted')
  assert admin.poll() is None
 finally:
  src.restore_connect();admin.stdin.write('ROLLBACK;\n\\q\n');admin.stdin.flush();admin.wait(timeout=10)
 other.stdin.write('SELECT 1;\nROLLBACK;\n\\q\n');other.stdin.flush();other.wait(timeout=10);assert other.returncode==0
 receipt={'scope':'synthetic-actual-schema','application_schema_matches_admin_profile':True,'tables':10,'indexes':19,'sequences':0,'dump_sha256':hashlib.sha256(dump).hexdigest(),'source_system_id':ids[0],'restored_system_id':ids[1],'independent_servers':True,'before_sha256':digest(before),'after_sha256':digest(after),'unknown_outcomes':before['unknown_outcomes'],'actual_clients_terminated':2,'new_application_connect_denied':denies,'unrelated_database_client_unchanged':True,'global_role_login_changed':False,'unknown_admin_refused_not_terminated':True,'negative_cases':results,'all_mutations_reverted':True,'production_rows_used':False,'production_qualified':False}
 save(ROOT/(label+'-database-receipt.json'),receipt);print(json.dumps(receipt))
if __name__=='__main__':run(sys.argv[1])
