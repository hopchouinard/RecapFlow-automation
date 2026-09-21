"""Create only new Request031 synthetic fixtures; never adopt an old container."""
import json,os,socket,sys,time
from pathlib import Path
import common as c
import database as db
r=c.r

def setup():
    if socket.gethostname()!='community-brain-dev':raise ValueError('VM108 only')
    for name in ('operations','specs','fixtures'):(c.ROOT/name).mkdir(mode=0o700)
    r.write_new(c.ROOT/'controller.lock',b'')
    out={}
    for kind in ('source','restore'):
        name='cbm-r031-pg-'+kind;data=c.ROOT/(name+'-data');data.mkdir(mode=0o700);os.chown(data,999,999)
        image=json.loads(c.command(['docker','image','inspect','postgres:18.6']))[0]['Id']
        c.command(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','256m','--cpus','0.5','--security-opt','no-new-privileges:true','-e','POSTGRES_HOST_AUTH_METHOD=trust','-e','POSTGRES_USER=fixture','-e','POSTGRES_DB=fixture','--mount','type=bind,source='+str(data)+',target=/var/lib/postgresql',image])
        for _ in range(100):
            try:
                if db.sql(name,'SELECT 1;')=='1':break
            except RuntimeError:pass
            time.sleep(.3)
        else:raise ValueError('new postgres not ready')
        row=c.inspect(name);out[kind]={'name':name,'id':row['Id'],'image':row['Image'],'identity':db.identity(name)}
    content=b'Request031 synthetic upload provenance\n';digest=r.sha(content)
    db.sql(out['source']['id'],"""CREATE TABLE jobs(id serial primary key,state text);CREATE TABLE stages(id serial primary key,job_id int references jobs(id),state text);CREATE TABLE attempts(id serial primary key,stage_id int references stages(id),outcome text);CREATE TABLE sources(id serial primary key,sha256 text);CREATE TABLE artifacts(id serial primary key,source_id int references sources(id),path text);CREATE TABLE outbox(id serial primary key,state text);CREATE TABLE vectors(id serial primary key,embedding real[],body tsvector);INSERT INTO jobs(state) VALUES('held');INSERT INTO stages(job_id,state) VALUES(1,'outcome_unknown');INSERT INTO attempts(stage_id,outcome) VALUES(1,'outcome_unknown');INSERT INTO sources(sha256) VALUES('"""+digest+"""');INSERT INTO artifacts(source_id,path) VALUES(1,'files/upload.txt');INSERT INTO outbox(state) VALUES('sent'),('pending');INSERT INTO vectors(embedding,body) VALUES(ARRAY[0.1,0.2,0.3],to_tsvector('simple','synthetic retrieval provenance'));CREATE INDEX vectors_fts ON vectors USING gin(body);""")
    r.write_new(c.ROOT/'database-bindings.json',r.encode(out));print(json.dumps(out))

def prepare(label,packet,packet_sha,exercise='normal'):
    if socket.gethostname()!='community-brain-dev' or not label.isalnum():raise ValueError('fresh safe fixture label required')
    c.packet(packet,packet_sha)
    fixture=c.ROOT/'fixtures'/label;fixture.mkdir(mode=0o700)
    controls=fixture/'controls';controls.mkdir(mode=0o700)
    for n in ('runner.lock','manual.lock','submission.lock'):r.write_new(controls/n,b'')
    for n in ('paused','attention.json','boot-state.json','checkpoint-needed.json'):r.write_new(controls/n,('synthetic held '+n).encode())
    state=fixture/'state';state.mkdir(mode=0o700);(state/'files').mkdir(mode=0o700);(state/'empty').mkdir()
    r.write_new(state/'files/upload.txt',b'Request031 synthetic upload provenance\n')
    (state/'files/link').symlink_to('upload.txt')
    name='cbm-r031-inc-'+label
    image=json.loads(c.command(['docker','image','inspect','python:3.11-slim']))[0]['Id']
    c.command(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','64m','--cpus','0.25','--read-only','--cap-drop','ALL','--user','10001:10001','--security-opt','no-new-privileges:true',image,'python','-B','-m','http.server','8080','--directory','/tmp'])
    row=c.inspect(name)
    for _ in range(30):
        try:
            c.command(['docker','exec',row['Id'],'python','-B','-c',"import urllib.request; assert urllib.request.urlopen('http://127.0.0.1:8080',timeout=1).status==200"],timeout=3);break
        except (RuntimeError, __import__('subprocess').TimeoutExpired):time.sleep(.2)
    else:raise ValueError('fresh incumbent not ready')
    now=time.time();opid='r031-'+label+'-'+str(int(now))
    spec={'schema':1,'scope':'synthetic-development','owner_id':'home-servers-request031','operation_id':opid,'capture_id':'capture-'+opid,'packet':str(packet),'packet_sha256':packet_sha,'operation':str(c.ROOT/'operations'/opid),'fixture':str(fixture),'locks':[str(controls/n) for n in ('runner.lock','manual.lock','submission.lock')],'holds':[str(controls/n) for n in ('paused','attention.json','boot-state.json','checkpoint-needed.json')],'incumbent':{'name':name,'id':row['Id'],'fingerprint':c.fingerprint(row),'started_at':row['State']['StartedAt']},'database':json.loads(r.stable_bytes(c.ROOT/'database-bindings.json')),'exercise':exercise}
    spec['hold_bindings']=r.hold_state(spec['holds']);spec['database']['destination_database']='restore_'+label
    spec['deadlines']={'prepare_by':now+12,'capture_by':now+(18 if exercise!='normal' else 65),'serving_by':now+(55 if exercise!='normal' else 100),'validate_by':now+(75 if exercise!='normal' else 125)}
    path=c.ROOT/'specs'/(opid+'.json');r.write_new(path,r.encode(spec));print(json.dumps({'spec':spec,'spec_sha256':r.sha(r.encode(spec)),'path':str(path)}))

if __name__=='__main__':
    if sys.argv[1]=='setup':setup()
    else:prepare(*sys.argv[2:])
