"""Fresh VM108 synthetic PostgreSQL and file preservation rehearsal, no providers."""
import json
import os
from pathlib import Path
import resource
import shutil
import socket
import sqlite3
import subprocess
import time
import recovery as r
from pg_fence import fence

ROOT = r.DEV_ROOT/'attempt04'
PG_IMAGE = 'postgres:18.6'
NAMES = ['cbm-r030-pg-source-a04','cbm-r030-pg-restore-a04']


def command(args, data=None):
    result = subprocess.run(args, input=data, capture_output=True, timeout=120)
    if result.returncode:
        r.write_new(ROOT/('failure-'+str(time.time_ns())+'.log'), result.stderr)
        raise RuntimeError('command failed; private diagnostic retained')
    return result.stdout


def sql(name, query):
    return command(['docker','exec','-i',name,'psql','-X','-U','fixture','-d','fixture','-v','ON_ERROR_STOP=1','-At'],query.encode())


def db_observation(name):
    out={}
    for table in ['jobs','stages','attempts','sources','artifacts','outbox','vectors']:
        raw=sql(name,'COPY (SELECT row_to_json(t)::text FROM '+table+' t ORDER BY id) TO STDOUT;')
        out[table]={'rows':len(raw.splitlines()),'sha256':r.sha(raw)}
    out['foreign_key_violations']=int(sql(name,"select count(*) from artifacts a left join sources s on a.source_id=s.id where s.id is null;").strip())
    out['unknown_attempts']=int(sql(name,"select count(*) from attempts where outcome='outcome_unknown';").strip())
    return out


def start_pg(name):
    data=ROOT/name;data.mkdir(mode=0o700);os.chown(data,999,999)
    image=json.loads(command(['docker','image','inspect',PG_IMAGE]))[0]['Id']
    command(['docker','run','-d','--name',name,'--network','none','--restart','no','--memory','256m','--cpus','0.5',
             '--security-opt','no-new-privileges:true','-e','POSTGRES_HOST_AUTH_METHOD=trust','-e','POSTGRES_USER=fixture',
             '-e','POSTGRES_DB=fixture','--mount','type=bind,source='+str(data)+',target=/var/lib/postgresql',image])
    for _ in range(60):
        x=subprocess.run(['docker','exec',name,'pg_isready','-U','fixture'],capture_output=True)
        if x.returncode==0:return
        time.sleep(0.5)
    raise RuntimeError('fresh postgres readiness timeout')


def main():
    assert socket.gethostname()=='community-brain-dev'
    ROOT.mkdir(mode=0o700)
    intent=ROOT/'rehearsal-intent.json'
    r.write_new(intent,r.encode({'scope':'synthetic-development','started_at':time.time(),'names':NAMES}))
    start=time.monotonic();before_disk=shutil.disk_usage(ROOT).free
    source=ROOT/'synthetic-source';source.mkdir(mode=0o700)
    for name in ['files','config','corpus','meeting_archive','controls','webui','private_runtime','database']:
        (source/name).mkdir(mode=0o700)
    for name in ['paused','attention.json','boot-state.json','checkpoint-needed.json']:
        (source/'controls'/name).write_text('synthetic held '+name)
    locks=[source/'controls'/n for n in ['runner.lock','manual.lock','submission.lock']]
    for p in locks:p.touch(mode=0o600)
    holds=[source/'controls'/n for n in ['paused','attention.json','boot-state.json','checkpoint-needed.json']]
    (source/'corpus'/'empty-required-tree').mkdir()
    (source/'files'/'upload.bin').write_bytes(b'synthetic upload\0'*4096)
    (source/'corpus'/'vectors.bin').write_bytes(bytes(range(256))*4096)
    (source/'webui'/'cache').mkdir();(source/'webui'/'cache'/'link').symlink_to('../../files/upload.bin')
    # Cross-component links are intentionally refused; valid cache links remain within webui.
    (source/'webui'/'cache'/'link').unlink();(source/'webui'/'upload.bin').write_bytes(b'synthetic webui upload')
    (source/'webui'/'cache'/'link').symlink_to('../upload.bin')
    c=sqlite3.connect(source/'webui'/'webui.db')
    c.executescript("create table users(id text primary key);create table chats(id text primary key,user_id text references users(id),body text);insert into users values('synthetic');insert into chats values('chat','synthetic','synthetic retained chat');")
    c.close()
    (source/'private_runtime'/'synthetic-signing').write_bytes(os.urandom(32));(source/'private_runtime'/'synthetic-signing').chmod(0o600)
    (source/'config'/'runtime.json').write_text(json.dumps({'automatic_processing':False,'network_publication':False,'model_calls':False,'endpoint':'http://synthetic.invalid','credential':'synthetic-only'}))
    before=r.hold_state(holds);attempts=[]
    try:
        start_pg(NAMES[0]);start_pg(NAMES[1])
        sql(NAMES[0],"""CREATE TABLE jobs(id int primary key,state text);
CREATE TABLE stages(id int primary key,job_id int references jobs(id),state text);
CREATE TABLE attempts(id int primary key,stage_id int references stages(id),outcome text);
CREATE TABLE sources(id int primary key,sha256 text);
CREATE TABLE artifacts(id int primary key,source_id int references sources(id),path text);
CREATE TABLE outbox(id int primary key,state text);
CREATE TABLE vectors(id int primary key,embedding real[],body tsvector);
INSERT INTO jobs VALUES(1,'held');INSERT INTO stages VALUES(1,1,'outcome_unknown');INSERT INTO attempts VALUES(1,1,'outcome_unknown');
INSERT INTO sources VALUES(1,'synthetic');INSERT INTO artifacts VALUES(1,1,'upload.bin');INSERT INTO outbox VALUES(1,'sent'),(2,'pending');
INSERT INTO vectors VALUES(1,ARRAY[0.1,0.2,0.3],to_tsvector('simple','synthetic retrieval provenance'));
CREATE INDEX vectors_fts ON vectors USING gin(body);
""")
        original=db_observation(NAMES[0])
        with r.quiet(locks,holds), fence(NAMES[0], ['jobs','stages','attempts','sources','artifacts','outbox','vectors']) as snapshot:
            blocked=subprocess.run(['docker','exec','-i',NAMES[0],'psql','-X','-U','fixture','-d','fixture','-v','ON_ERROR_STOP=1'],input=b"SET lock_timeout='100ms'; INSERT INTO jobs VALUES(2,'should-not-write');",capture_output=True)
            assert blocked.returncode!=0 and b'lock timeout' in blocked.stderr
            dump=command(['docker','exec',NAMES[0],'pg_dump','-U','fixture','-d','fixture','-Fc','--no-owner','--no-acl','--snapshot',snapshot])
            r.write_new(source/'database'/'database.dump',dump)
            r.write_new(source/'database'/'observation.json',r.encode(original))
            components={p.name:p for p in source.iterdir()}
            digest=r.capture(components,ROOT/'capture','cbm-r030-synthetic-pair-a04',{'holds':before,'writer_inventory':'only rehearsal process; no network or workers'})
            receipt=r.restore(ROOT/'capture',digest,ROOT/'independent-restore')
            assert r.hold_state(holds)==before
        with (ROOT/'independent-restore/database/database.dump').open('rb') as f:
            command(['docker','exec','-i',NAMES[1],'pg_restore','-U','fixture','-d','fixture','--exit-on-error','--no-owner','--no-acl'],f.read())
        restored=db_observation(NAMES[1]);assert restored==original
        assert sql(NAMES[1],"select count(*) from vectors where body @@ plainto_tsquery('simple','provenance');").strip()==b'1'
        db=ROOT/'independent-restore/webui/webui.db';c=sqlite3.connect('file:'+str(db)+'?mode=ro&immutable=1',uri=True)
        assert c.execute('pragma integrity_check').fetchone()[0]=='ok';assert c.execute('select count(*) from chats c join users u on c.user_id=u.id').fetchone()[0]==1;c.close()
        # Retained new writes must not be overwritten by retrying restore.
        (ROOT/'independent-restore/webui/new-write').write_text('synthetic post-restore write')
        try:r.restore(ROOT/'capture',digest,ROOT/'independent-restore')
        except FileExistsError:pass
        else:raise AssertionError('overwrite accepted')
        assert (ROOT/'independent-restore/webui/new-write').read_text()=='synthetic post-restore write'
        output=dict(scope='synthetic-development',manifest_sha256=digest,tree_receipt=receipt,database_before=original,database_after=restored,
                    database_equal=True,fts_matches=1,sqlite_integrity='ok',sqlite_relationships=1,held_markers_unchanged=r.hold_state(holds)==before,
                    retained_new_writes=True,worker_effects=0,concurrent_writer_refused=True,exported_snapshot=True,off_host_restore=False,production_qualified=False,
                    duration_seconds=round(time.monotonic()-start,3),disk_growth_bytes=before_disk-shutil.disk_usage(ROOT).free,
                    peak_controller_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        r.write_new(ROOT/'synthetic-acceptance.json',r.encode(output))
    finally:
        state={}
        for name in NAMES:
            row=subprocess.run(['docker','inspect','--type','container',name],capture_output=True)
            if row.returncode==0:
                v=json.loads(row.stdout)[0]
                if v['State']['Running']:command(['docker','stop',name])
                v=json.loads(command(['docker','inspect','--type','container',name]))[0]
                state[name]={'id':v['Id'],'image':v['Image'],'running':v['State']['Running'],'oom_killed':v['State']['OOMKilled'],'network':v['HostConfig']['NetworkMode'],'ports':v['HostConfig']['PortBindings']}
        r.write_new(ROOT/'rehearsal-cleanup.json',r.encode(state))
    print(json.dumps(output))

if __name__=='__main__':main()
