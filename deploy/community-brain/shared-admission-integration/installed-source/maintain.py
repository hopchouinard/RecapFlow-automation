"""Existing Mac LaunchAgent entry: minute checkpoints plus retained hourly work."""
import datetime
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import threading

ROOT=Path(__file__).resolve().parent
STATE=Path.home()/'.local/state/community-brain-management'
AUTOMATIC=ROOT/'platform-services/community-brain-prod/automatic-recovery'
sys.path.insert(0,str(AUTOMATIC))
from checkpoint_acceptance import atomic
from monitor_status import publish


def hourly_due(now,last,local_clock):
    # The existing20:45 local pre-PBS call remains independent of last-hour time.
    minute_start=now-local_clock.second-local_clock.microsecond/1000000
    scheduled=local_clock.hour==20 and local_clock.minute==45 and last<minute_start
    return now-last>=3600 or scheduled


def main():
    os.umask(0o077);STATE.mkdir(mode=0o700,exist_ok=True)
    with (STATE/'scheduler.lock').open('a') as lock:
        try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:return {'state':'another_management_cycle_running'}
        status={}
        now=time.time();schedule=STATE/'automatic-scheduler.json'
        previous=json.loads(schedule.read_text()) if schedule.exists() else {}
        if hourly_due(now,previous.get('last_hourly_attempt',0),datetime.datetime.now()):
            # Persist the attempt before launching legacy maintenance to avoid
            # repeating side effects after an uncertain scheduler interruption.
            previous['last_hourly_attempt']=now;atomic(schedule,previous)
            try:
                result=subprocess.run([sys.executable,str(ROOT/'maintain-hourly.py')],capture_output=True,timeout=1000,env={**os.environ,'CBM_SCHEDULER_LOCK_HELD':'1'})
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
                result=subprocess.run([sys.executable,str(AUTOMATIC/'consumer.py')],capture_output=True,text=True,timeout=1200)
            finally:
                stopping.set();thread.join(timeout=35)
            if result.returncode:raise RuntimeError('checkpoint consumer failed')
            status['automatic']=json.loads(result.stdout)
            status['monitoring']=publish()
        except Exception:
            status['automatic']={'state':'reconciliation_required'}
            try:status['monitoring']=publish(failed=True)
            except Exception:status['monitoring']={'state':'unavailable'}
        status['checked_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        atomic(STATE/'automatic-maintenance-status.json',status)
        return status


if __name__=='__main__':
    value=main();print(json.dumps(value))
    raise SystemExit(1 if value.get('automatic',{}).get('state')=='reconciliation_required' or value.get('hourly') in ('failed','timed_out') else 0)
