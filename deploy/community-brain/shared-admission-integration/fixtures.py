"""Create only new Request032 synthetic fixtures; never adopt an old container."""
import json,os,socket,sys,time
from pathlib import Path
import common as c
import database as db
r=c.r

def setup():
    if socket.gethostname()!='community-brain-dev':raise ValueError('VM108 only')
    for name in ('operations','specs','fixtures'):(c.ROOT/name).mkdir(mode=0o700)
    r.write_new(c.ROOT/'controller.lock',b'')
    r.write_new(c.ROOT/'boot.lock',b'')
    out={}
    for kind in ('source','restore'):
        name='cbm-r032-pg-'+kind;data=c.ROOT/(name+'-data');data.mkdir(mode=0o700);os.chown(data,999,999)
        image=json.loads(c.command(['docker','image','inspect','postgres:18.6']))[0]['Id']
        c.command(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','256m','--cpus','0.5','--security-opt','no-new-privileges:true','-e','POSTGRES_HOST_AUTH_METHOD=trust','-e','POSTGRES_USER=fixture','-e','POSTGRES_DB=fixture','--mount','type=bind,source='+str(data)+',target=/var/lib/postgresql',image])
        for _ in range(100):
            try:
                if c.command(['docker','exec',name,'psql','-h','127.0.0.1','-X','-qAt','-U','fixture','-d','fixture','-c','SELECT 1;']).strip()==b'1':break
            except RuntimeError:pass
            time.sleep(.3)
        else:raise ValueError('new postgres not ready')
        row=c.inspect(name);out[kind]={'name':name,'id':row['Id'],'image':row['Image'],'identity':db.identity(name,'fixture')}
    content=b'Request032 synthetic upload provenance\n';digest=r.sha(content)
    source=out['source']['id']
    db.sql(source,"CREATE ROLE cbm_owner NOLOGIN;CREATE ROLE cbm_runtime LOGIN;CREATE ROLE cbm_ddl LOGIN;GRANT cbm_owner TO cbm_ddl;CREATE DATABASE cbm_app OWNER cbm_owner;",'fixture')
    db.sql(source,"CREATE EXTENSION pgcrypto;ALTER SCHEMA public OWNER TO cbm_owner;CREATE SCHEMA app AUTHORIZATION cbm_owner;CREATE SCHEMA audit AUTHORIZATION cbm_owner;SET ROLE cbm_owner;CREATE TABLE app.jobs(id serial primary key,state text NOT NULL);CREATE TABLE app.stages(id serial primary key,job_id int references app.jobs(id),state text);CREATE TABLE app.attempts(id serial primary key,stage_id int references app.stages(id),outcome text);CREATE TABLE app.sources(id serial primary key,sha256 text);CREATE TABLE app.artifacts(id serial primary key,source_id int references app.sources(id),path text);CREATE TABLE app.outbox(id serial primary key,state text);CREATE TABLE app.vectors(id serial primary key,embedding real[],body tsvector);CREATE TABLE audit.events(id serial primary key,job_id int references app.jobs(id),kind text);INSERT INTO app.jobs(state) VALUES('held');INSERT INTO app.stages(job_id,state) VALUES(1,'outcome_unknown');INSERT INTO app.attempts(stage_id,outcome) VALUES(1,'outcome_unknown');INSERT INTO app.sources(sha256) VALUES('"+digest+"');INSERT INTO app.artifacts(source_id,path) VALUES(1,'files/upload.txt');INSERT INTO app.outbox(state) VALUES('sent'),('pending');INSERT INTO app.vectors(embedding,body) VALUES(ARRAY[0.1,0.2,0.3],to_tsvector('simple','synthetic retrieval provenance'));CREATE INDEX vectors_fts ON app.vectors USING gin(body);INSERT INTO audit.events(job_id,kind) VALUES(1,'held');GRANT USAGE ON SCHEMA app,audit TO cbm_runtime;GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA app,audit TO cbm_runtime;GRANT USAGE,SELECT ON ALL SEQUENCES IN SCHEMA app,audit TO cbm_runtime;ALTER DEFAULT PRIVILEGES FOR ROLE cbm_owner IN SCHEMA app GRANT SELECT ON TABLES TO cbm_runtime;GRANT CONNECT ON DATABASE cbm_app TO cbm_runtime,cbm_ddl;")
    out['source']['identity']=db.identity(source)
    r.write_new(c.ROOT/'database-bindings.json',r.encode(out));print(json.dumps(out))

def prepare(label,packet,packet_sha,exercise='normal',kind='capture'):
    if socket.gethostname()!='community-brain-dev' or not label.isalnum():raise ValueError('fresh safe fixture label required')
    c.packet(packet,packet_sha)
    fixture=c.ROOT/'fixtures'/label;fixture.mkdir(mode=0o700)
    controls=fixture/'controls';controls.mkdir(mode=0o700)
    for n in ('runner.lock','manual.lock','submission.lock'):r.write_new(controls/n,b'')
    for n in ('paused','attention.json','boot-state.json','checkpoint-needed.json'):r.write_new(controls/n,('synthetic held '+n).encode())
    state=fixture/'state';state.mkdir(mode=0o700);(state/'files').mkdir(mode=0o700);(state/'empty').mkdir()
    r.write_new(state/'files/upload.txt',b'Request032 synthetic upload provenance\n')
    (state/'files/link').symlink_to('upload.txt')
    state.chmod(0o755);(state/'files').chmod(0o755);(state/'files/upload.txt').chmod(0o644)
    private=fixture/'private';private.mkdir(mode=0o700)
    r.write_new(private/'signing.key',b'SYNTHETIC-REQUEST032-NOT-PRODUCTION-SIGNING')
    name='cbm-r032-inc-'+label
    image=json.loads(c.command(['docker','image','inspect','python:3.11-slim']))[0]['Id']
    c.command(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','64m','--cpus','0.25','--read-only','--cap-drop','ALL','--user','10001:10001','--security-opt','no-new-privileges:true','--mount','type=bind,source='+str(state)+',target=/srv/state,readonly',image,'python','-B','-m','http.server','8080','--directory','/srv/state'])
    row=c.inspect(name)
    r.write_new(fixture/'incumbent-created.json',r.encode({'name':name,'id':row['Id'],'fingerprint':c.fingerprint(row),'at':time.time()}))
    for _ in range(30):
        try:
            c.command(['docker','exec',row['Id'],'python','-B','-c',"import urllib.request; assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=1).status==200"],timeout=3);break
        except (RuntimeError, __import__('subprocess').TimeoutExpired):time.sleep(.2)
    else:raise ValueError('fresh incumbent not ready')
    now=time.time();opid='r032-'+label+'-'+str(int(now))
    spec={'schema':1,'scope':'synthetic-development','owner_id':'home-servers-request032','operation_id':opid,'capture_id':'capture-'+opid,'packet':str(packet),'packet_sha256':packet_sha,'operation':str(c.ROOT/'operations'/opid),'fixture':str(fixture),'locks':[str(controls/n) for n in ('runner.lock','manual.lock','submission.lock')],'holds':[str(controls/n) for n in ('paused','attention.json','boot-state.json','checkpoint-needed.json')],'incumbent':{'name':name,'id':row['Id'],'fingerprint':c.fingerprint(row),'started_at':row['State']['StartedAt']},'database':json.loads(r.stable_bytes(c.ROOT/'database-bindings.json')),'exercise':exercise,'kind':kind,'machine_id':c.machine_id(),'host_boot_id':c.boot_id(),'volume':{'path':str(state),'device':state.stat().st_dev,'inode':state.stat().st_ino,'mountpoint':'/srv/state'},'signing_sha256':r.sha(r.stable_bytes(private/'signing.key'))}
    spec['hold_bindings']=r.hold_state(spec['holds']);spec['database']['destination_database']='restore_'+label
    spec['deadlines']={'prepare_by':now+35,'capture_by':now+(45 if exercise!='normal' else 140),'serving_by':now+(90 if exercise!='normal' else 190),'validate_by':now+(130 if exercise!='normal' else 300)}
    path=c.ROOT/'specs'/(opid+'.json');r.write_new(path,r.encode(spec));print(json.dumps({'spec':spec,'spec_sha256':r.sha(r.encode(spec)),'path':str(path)}))

if __name__=='__main__':
    if sys.argv[1]=='setup':setup()
    else:prepare(*sys.argv[2:])
