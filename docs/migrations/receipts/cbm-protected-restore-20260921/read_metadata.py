import subprocess,json,pathlib,hashlib,os,shutil,datetime,tarfile,io,sqlite3
sha=lambda b:hashlib.sha256(b).hexdigest()
which=__import__('sys').argv[1]
out={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'hostname':__import__('socket').gethostname()}
if which=='production':
 code="""import os,json,hashlib
from sqlalchemy import create_engine,text
engine=create_engine(os.environ['CB_DATABASE_URL'])
u=engine.url
out={'configured_env':'CB_DATABASE_URL','host':u.host,'port':u.port,'database':u.database,'role':u.username,'driver':u.drivername}
with engine.connect() as c:
 c.exec_driver_sql('BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ READ ONLY')
 out['server']=dict(c.execute(text("select current_database() as database,current_user as role,inet_server_addr()::text as address,inet_server_port() as port,current_setting('server_version') as version,pg_database_size(current_database()) as bytes")).mappings().one())
 out['tables']={}
 for schema,table in c.execute(text("select schemaname,tablename from pg_tables where schemaname not in ('pg_catalog','information_schema') order by 1,2")):
  q=engine.dialect.identifier_preparer.quote
  count=c.exec_driver_sql('select count(*) from '+q(schema)+'.'+q(table)).scalar()
  out['tables'][schema+'.'+table]={'rows':count}
 out['other_sessions']= [dict(r) for r in c.execute(text("select usename,application_name,state,backend_type,count(*) as count from pg_stat_activity where datname=current_database() and pid<>pg_backend_pid() group by 1,2,3,4")).mappings()]
 c.rollback()
print(json.dumps(out))
"""
 r=subprocess.run(['docker','exec','-i','community-brain-production-staging-api-1','python','-B','-'],input=code.encode(),capture_output=True)
 if r.returncode: raise RuntimeError('read-only database metadata failed: '+r.stderr.decode()[-500:])
 out['database']=json.loads(r.stdout)
 root=pathlib.Path('/srv/community-brain');out['trees']={}
 for n in ['files','config','corpus','meeting-archive-20260910','automation','automation-public','manual-approvals']:
  d=root/n;rows=[];size=0;files=0;links=0
  for f in sorted(d.rglob('*')):
   s=f.lstat();row=[str(f.relative_to(d)),s.st_mode,s.st_uid,s.st_gid]
   if f.is_symlink():row+=['link',os.readlink(f)];links+=1
   elif f.is_file():row+=['file',sha(f.read_bytes()),s.st_size];size+=s.st_size;files+=1
   elif f.is_dir():row+=['directory']
   else:row+=['special']
   rows.append(row)
  out['trees'][n]={'path':str(d),'files':files,'links':links,'bytes':size,'private_manifest_digest':sha(json.dumps(rows,sort_keys=True).encode()),'root_uid':d.stat().st_uid,'root_gid':d.stat().st_gid,'root_mode':oct(d.stat().st_mode&511)}
 out['disk']=shutil.disk_usage(root)._asdict()
 out['locks']={}
 for f in (root/'automation').glob('*lock*'):
  s=f.stat();out['locks'][str(f)]={'inode':s.st_ino,'device':s.st_dev,'mode':oct(s.st_mode&511)}
 out['private_paths']=[str(f) for f in root.iterdir() if f.is_file()]
elif which=='legacy':
 r=json.loads(subprocess.check_output(['docker','inspect','--type','container','open-webui']))[0];assert not r['State']['Running']
 out['container_id']=r['Id'];out['signing']={}
 for n in ['/app/backend/.webui_secret_key','/app/package.json']:
  b=subprocess.check_output(['docker','cp','open-webui:'+n,'-'])
  with tarfile.open(fileobj=io.BytesIO(b)) as t:
   m=next(x for x in t if x.isfile());v=t.extractfile(m).read()
  out['signing'][n]={'bytes':len(v),'sha256':sha(v),'mode':oct(m.mode),'uid':m.uid,'gid':m.gid}
 root=pathlib.Path('/var/lib/docker/volumes/open-webui-data/_data');out['links']=[]
 for f in root.rglob('*'):
  if f.is_symlink():out['links'].append({'path_sha256':sha(str(f.relative_to(root)).encode()),'contained':f.resolve().is_relative_to(root),'exists':f.exists()})
 db=root/'vector_db/chroma.sqlite3'
 c=sqlite3.connect('file:'+str(db)+'?mode=ro&immutable=1',uri=True)
 out['chroma']={'sha256':sha(db.read_bytes()),'integrity':c.execute('pragma integrity_check').fetchone()[0],'counts':{n:c.execute('select count(*) from '+n).fetchone()[0] for n in ['collections','embeddings']}}
 out['disk']=shutil.disk_usage(root)._asdict()
elif which=='development':
 out['disk']=shutil.disk_usage('/srv/dev-data')._asdict();out['memory']=pathlib.Path('/proc/meminfo').read_text().splitlines()[:3]
 out['images']=json.loads(subprocess.check_output(['docker','image','ls','--format','json']).decode().replace('}\n{','},{').join(['[',']']))
print(json.dumps(out))
