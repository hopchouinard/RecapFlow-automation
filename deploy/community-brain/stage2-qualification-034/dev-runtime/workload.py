import os,sys,json,fcntl,secrets,subprocess,tempfile
from pathlib import Path
from uuid import uuid4
source=Path(__file__).resolve().parent
sys.path[:0]=[str(source),str(source/'incumbent')]
from manager import Adapter,LOCAL
from lease_supervisor import LeaseSupervisor
from transport import command
from profiles import DEV_HOST,DEV_ROOT
mode=os.environ['CBM_R034_MODE']
assert mode in ('validate-manual','validate-checkpoint','validate-automatic','validate-uncertain','data-inspect')
identity=json.loads((LOCAL/'packet-identity.json').read_text())
with (LOCAL/'isolated-scheduler.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 job,nonce=str(uuid4()),secrets.token_hex(32)
 with LeaseSupervisor(command(DEV_HOST,['python3','-B',identity['remote_path']+'/incumbent/quiet_window.py',DEV_ROOT+'/state',job,nonce,'60']),job,nonce,interval=3,reply_timeout=20) as lease:
  values=Adapter(lease,identity).read()
 # Lease released deliberately before invoking real workers. Mac scheduler remains locked.
 wrapper='import sys,runpy,json,traceback\nsys.path.insert(0,sys.argv[1]);sys.argv=[sys.argv[1]+"/host.py",*sys.argv[2:]]\ntry:runpy.run_path(sys.argv[0],run_name="__main__")\nexcept Exception as e:print(json.dumps({"adapter_error":type(e).__name__,"frames":[{"file":f.filename.rsplit("/",1)[-1],"line":f.lineno} for f in traceback.extract_tb(e.__traceback__)]}))'
 p=subprocess.run(command(DEV_HOST,['python3','-B','-c',wrapper,identity['remote_path'],identity['manifest_sha256'],mode]),input=json.dumps(values),capture_output=True,text=True,timeout=1000)
 assert p.returncode==0,'SSH failed; reconcile outcome'
 result=json.loads(p.stdout)
 if 'adapter_error' in result:raise RuntimeError(json.dumps(result))
 (LOCAL/(mode+'-acceptance.json')).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))
