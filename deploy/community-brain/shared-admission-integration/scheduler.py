"""Candidate derived from the exact installed maintain.py snapshot.

Retains hourly scheduling, intent-before-hourly, bounded work, heartbeat and status
flow. Effects are redirected to sealed VM108 fixtures; deployed helpers are never
imported or invoked. One shared admission wraps the complete management cycle.
"""
import datetime,json,os,sys,time,threading,subprocess
from pathlib import Path
import shared
import common as c
ROOT=Path(__file__).resolve().parent
STATE=shared.STATE/'scheduler'
atomic=c.atom

def publish(failed=False):
    value={'at':time.time(),'scope':'candidate-synthetic-only','failed':failed}
    atomic(STATE/'monitor.json',value);return value

def hourly_due(now,last,local_clock):
    # The existing20:45 local pre-PBS call remains independent of last-hour time.
    minute_start=now-local_clock.second-local_clock.microsecond/1000000
    scheduled=local_clock.hour==20 and local_clock.minute==45 and last<minute_start
    return now-last>=3600 or scheduled


def cycle(s):
    STATE.mkdir(mode=0o700,exist_ok=True)
    atomic(STATE/(s['operation_id']+'-scheduler-spec.json'),s)
    status={}
    now=time.time();schedule=STATE/'automatic-scheduler.json'
    previous=json.loads(schedule.read_text()) if schedule.exists() else {}
    if hourly_due(now,previous.get('last_hourly_attempt',0),datetime.datetime.now()):
        # Persist the attempt before launching legacy maintenance to avoid
        # repeating side effects after an uncertain scheduler interruption.
        previous['last_hourly_attempt']=now;atomic(schedule,previous)
        try:
            result=subprocess.run([sys.executable,'-B',str(ROOT/'scheduler_helpers.py'),'hourly',str(STATE/(s['operation_id']+'-scheduler-spec.json'))],capture_output=True,timeout=25)
            status['hourly']='passed' if result.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:status['hourly']='timed_out'
    else:status['hourly']='not_due'
    try:
        publish()
        stopping=threading.Event()
        def heartbeat():
            while not stopping.wait(30):
                try:publish()
                except Exception:pass  # Existing server-side age alert remains authoritative.
        thread=threading.Thread(target=heartbeat,daemon=True);thread.start()
        try:
            shared.dispatch(s)
        finally:
            stopping.set();thread.join(timeout=35)
        status['automatic']={'dispatch_finished':True,'authoritative_readback':'required by outer shared gate'}
        status['monitoring']=publish()
    except Exception:
        status['automatic']={'state':'reconciliation_required'}
        try:status['monitoring']=publish(failed=True)
        except Exception:status['monitoring']={'state':'unavailable'}
    status['checked_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    atomic(STATE/'automatic-maintenance-status.json',status)
    return status

def main():
    mode,path=sys.argv[1:]
    if mode not in ('dispatch','reconcile'):raise ValueError('unknown mode')
    return shared.execute('scheduler',path,action=cycle,reconcile=mode=='reconcile')

if __name__=='__main__':print(json.dumps(main()))
