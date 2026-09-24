"""Actual admitted DML, DDL and sequence sessions terminated by writer closure."""
import json,subprocess,sys,time,select
from pathlib import Path
import common as c
import catalog
r=c.r

def run(path,sha):
    s=c.load_spec(path,sha,check_time=False);op=Path(s['operation']);fixture=Path(s['fixture']);container=s['database']['source']['id']
    work=fixture/'concurrent-clients';work.mkdir(mode=0o700);processes=[]
    cases=[('dml','cbm_runtime',"BEGIN;UPDATE app.jobs SET state='uncommitted_should_rollback' WHERE id=1;SELECT 'READY';"),
           ('ddl','cbm_ddl',"BEGIN;SET ROLE cbm_owner;CREATE TABLE app.uncommitted_should_rollback(id int);SELECT 'READY';"),
           ('sequence','cbm_runtime',"BEGIN;SELECT CASE WHEN nextval('app.jobs_id_seq')>0 THEN 'READY' END;")]
    try:
        for label,role,query in cases:
            p=subprocess.Popen(['docker','exec','-i','-e','PGAPPNAME=cbm-r032-test-'+label,container,'psql','-X','-qAt','-U',role,'-d','cbm_app','-v','ON_ERROR_STOP=1'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            p.stdin.write(query+'\n');p.stdin.flush()
            limit=time.monotonic()+8;seen=[]
            while time.monotonic()<limit:
                if select.select([p.stdout],[],[],.1)[0]:
                    line=p.stdout.readline().strip();seen.append(line)
                    if line=='READY':break
                if p.poll() is not None:raise ValueError('pre-admission writer could not connect')
            else:raise ValueError('writer readiness timeout')
            processes.append((label,p,seen))
        r.write_new(work/'ready.json',r.encode({'clients':[x[0] for x in processes],'at':time.time()}))
        limit=time.time()+100
        while not (op/'writer-admission-closed.json').exists():
            if time.time()>limit:raise ValueError('capture never closed writer admission')
            time.sleep(.1)
        results=[]
        for label,p,seen in processes:
            try:p.stdin.write('COMMIT;\nSELECT 1;\n');p.stdin.flush()
            except BrokenPipeError:pass
            p.wait(timeout=8);assert p.returncode!=0
            results.append({'kind':label,'connected_before_close':True,'actual_backend_terminated':True,'client_returncode':p.returncode,'ready_output':seen})
        assert catalog.sql(container,"SELECT state FROM app.jobs WHERE id=1;")=='held'
        assert catalog.sql(container,"SELECT count(*) FROM pg_tables WHERE schemaname='app' AND tablename='uncommitted_should_rollback';")=='0'
        value={'clients':results,'dml_rolled_back':True,'ddl_rolled_back':True,'sequence_is_nontransactional_and_captured_after_termination':True,'at':time.time()}
        r.write_new(work/'result.json',r.encode(value));print(json.dumps(value))
    finally:
        for _,p,_ in processes:
            if p.poll() is None:
                p.stdin.close()
                try:p.wait(timeout=3)
                except subprocess.TimeoutExpired:p.kill();p.wait()

if __name__=='__main__':run(*sys.argv[1:])
