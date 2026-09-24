"""Bounded copy before existing21:00 local PBS; fail visibly, never change PBS."""
import datetime,json,pathlib,subprocess,shlex,hashlib,sys
from maintenance_policy import pre_window,validate_copy,next_pbs
ROOT=pathlib.Path(__file__).resolve().parent
STATE=pathlib.Path.home()/'.local/state/community-brain-management/pre-pbs-state.json'
now=datetime.datetime.now(datetime.timezone.utc)
rehearse=sys.argv[1:]==['--rehearse'];assert not sys.argv[1:] or rehearse
state=json.loads(STATE.read_text())
if not pre_window(now) and not rehearse:print('Outside pre-PBS window; existing freshness deadline retained');raise SystemExit(0)
def query():
    code="""import pathlib,hashlib,subprocess,json
p=sorted(pathlib.Path('/var/backups/community-brain').glob('*.dump'))[-1]
r=subprocess.run(['pg_restore','--list',str(p)],capture_output=True);assert r.returncode==0
s=subprocess.check_output(['systemctl','show','community-brain-db-backup.service','--property=ExecMainStatus','--value'],text=True).strip();assert s=='0'
print(json.dumps({'name':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'native_dump_exit_status':0}))
"""
    r=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','pchouinard@10.1.10.50','sudo python3 -c '+shlex.quote(code)],capture_output=True,text=True,timeout=25);assert r.returncode==0,'Completed dump inspection failed';return json.loads(r.stdout)
try:
    before=query();stamp=datetime.datetime.strptime(before['name'],'%Y%m%dT%H%M%SZ.dump').replace(tzinfo=datetime.timezone.utc)
    assert 0<=(now-stamp).total_seconds()<=7200,'Source dump stale'
    r=subprocess.run(['python3',str(ROOT/'copy-backup.py')],capture_output=True,text=True,timeout=150);assert r.returncode==0,'Bounded copy failed'
    copy=json.loads(r.stdout);after=query();assert before==after and pathlib.Path(copy['off_host_path']).name==before['name'] and copy['bytes']==before['bytes']
    finished=datetime.datetime.now(datetime.timezone.utc);due=validate_copy(now,finished,stamp,before['sha256'],after['sha256'],copy['sha256'],enforce_window=not rehearse)
    state.update(state='verified',checked_at=finished.isoformat(),next_due_epoch=due,last_success={'pbs_window':next_pbs(finished).isoformat(),'dump':before,'copy':copy},failure=None)
except Exception:
    state.update(state='failed',checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),failure='Pre-PBS source/copy/freshness verification failed; coverage unconfirmed')
finally:
    if rehearse:
        state['rehearsal_only']=True;state['scheduled_freshness_advanced']=False;STATE=STATE.with_name('pre-pbs-rehearsal.json')
    t=STATE.with_suffix('.tmp');t.write_text(json.dumps(state,indent=2)+'\n');t.chmod(0o600);t.replace(STATE)
print(json.dumps({k:v for k,v in state.items() if k!='last_success'}))
raise SystemExit(0 if state['state']=='verified' else 1)
