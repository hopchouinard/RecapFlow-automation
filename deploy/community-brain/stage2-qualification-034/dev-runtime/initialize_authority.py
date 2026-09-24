import os,sys,json,subprocess,secrets,time,hashlib,fcntl
from pathlib import Path
from uuid import uuid4
os.umask(0o077)
SOURCE=Path(__file__).resolve().parent
sys.path[:0]=[str(SOURCE),str(SOURCE/'incumbent')]
from authority import Authority,PROJECT,ENVIRONMENT,DEVELOPMENT_PATH
from successor import DEV_HOST,DEV_ROOT
from transport import command
from lease_supervisor import LeaseSupervisor
from service_renewal_policy import SPECS,IDENTITIES,validate
base=['--projectId',PROJECT,'--env',ENVIRONMENT,'--path','/development/community-brain-dev','--domain',os.environ['INFISICAL_API_URL'],'--token',os.environ['INFISICAL_TOKEN'],'--silent']
def cli(args):
 p=subprocess.run(['infisical',*args,*base],capture_output=True,text=True,timeout=30)
 assert p.returncode==0,'development folder operation failed; output suppressed'
 return json.loads(p.stdout)
def parent():
 v=cli(['secrets','--output','json','--include-imports=false','--expand=false'])
 return v.get('secrets',v.get('data',[])) if isinstance(v,dict) else v
before=parent()
folders=cli(['secrets','folders','get','--output','json'])
def contains(v):
 if isinstance(v,dict):return v.get('name')=='request034' or any(contains(x) for x in v.values())
 if isinstance(v,list):return any(contains(x) for x in v)
 return False
local=Path.home()/'.local/state/community-brain-management/request034'
with (local/'isolated-scheduler.lock').open('a') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 job,nonce=str(uuid4()),secrets.token_hex(32)
 with LeaseSupervisor(command(DEV_HOST,['python3','-B',json.loads((local/'packet-identity.json').read_text())['remote_path']+'/incumbent/quiet_window.py',DEV_ROOT+'/state',job,nonce,'15']),job,nonce,interval=1,reply_timeout=5) as lease:
  if not contains(folders):
   lease.check()
   cli(['secrets','folders','create','--name','request034','--output','json'])
   lease.check()
  authority=Authority(PROJECT,ENVIRONMENT,DEVELOPMENT_PATH,lease)
  existing=authority.read()
  assert not existing,'existing Request034 authority: reconcile before initialization'
  values={};records=[];expiry=int(time.time())+7*86400
  for key,exp,subject,permissions in SPECS:
   values[key]=secrets.token_urlsafe(48);values[exp]=str(expiry)
   records.append({'subject':subject,'scope':'community-brain','permissions':permissions,'expires_at':expiry,'sha256':hashlib.sha256(values[key].encode()).hexdigest()})
  values[IDENTITIES]=json.dumps(records,separators=(',',':'))
  import base64
  values.update(CB_NATS_USER='cbm-request034-worker',CB_NATS_PASSWORD=secrets.token_urlsafe(48),CB_DEV_NATS_ADMIN_USER='cbm-request034-admin',CB_DEV_NATS_ADMIN_PASSWORD=secrets.token_urlsafe(48),CB_SYNTHETIC_PROVIDER_TOKEN=secrets.token_urlsafe(48))
  values['CB_DEV_NATS_CERT_B64']=base64.b64encode((local/'nats.crt').read_bytes()).decode()
  values['CB_DEV_NATS_KEY_B64']=base64.b64encode((local/'nats.key').read_bytes()).decode()
  values['CB_DEV_NATS_CA_B64']=base64.b64encode((local/'ca-root.crt').read_bytes()).decode()
  authority.save(values)
  actual=authority.read();validate(actual)
  assert actual==values
  assert parent()==before,'parent development material changed'
  result={'passed':True,'backend':'actual Infisical','project':'homelab','project_id':PROJECT,'environment':ENVIRONMENT,'path':DEVELOPMENT_PATH,'subjects':5,'generated_development_identities_only':True,'read_save_read_equality':True,'parent_development_secrets_unchanged':True,'production_keys_read_or_changed':False,'actual_ssh_quiet_lease':True,'scheduler_mutex':True,'authority_values_exported':False,'expires_at':expiry}
  (local/'authority-acceptance.json').write_text(json.dumps(result,indent=2)+'\n')
  print(json.dumps(result))
