"""Fresh Request028 data only. Private authority values never enter receipts."""
import base64,hashlib,json,os,time
from pathlib import Path
from host import ROOT,PRIVATE,PACKET,atomic,command,COMPOSE
from profiles import profile

def private_files(values):
 state=ROOT/'state'
 for name in ['files','config','corpus','meeting-archive','meeting-archive/files','automation-public','automation','automation/checkpoints','manual-approvals']:
  path=state/name;path.mkdir(parents=True,exist_ok=True,mode=0o755 if name not in ('automation','automation/checkpoints','manual-approvals') else 0o700)
  if name not in ('automation','automation/checkpoints','manual-approvals'):path.chmod(0o755)
  if name in ('files','config','corpus'):os.chown(path,10001,10001)
 (state/'automation/paused').write_text('disposable Request028 bootstrap hold\n')
 atomic(state/'automation/boot-state.json',json.dumps({'boot_id':Path('/proc/sys/kernel/random/boot_id').read_text().strip(),'reconciled':False}))
 atomic(state/'automation-public/checkpoints.json',json.dumps({'checkpoints':{},'management_attention':False}),0o644)
 raw=b'Request028 synthetic archive. No production data.\n';digest=hashlib.sha256(raw).hexdigest()
 atomic(state/'meeting-archive/files'/digest,raw.decode(),0o644)
 manifest={'scope':'community-brain','meetings':[{'date':'2026-09-09','artifacts':[{'id':digest,'name':'synthetic.txt','bytes':len(raw),'sha256':digest}]}]}
 atomic(state/'meeting-archive/manifest.json',json.dumps(manifest),0o644)
 cert=base64.b64decode(values['CB_DEV_NATS_CERT_B64']).decode();key=base64.b64decode(values['CB_DEV_NATS_KEY_B64']).decode()
 atomic(PRIVATE/'queue-ca.pem',cert,0o644);atomic(PRIVATE/'ca-bundle.pem',cert,0o644)
 atomic(PRIVATE/'nats/server.crt',cert,0o644);atomic(PRIVATE/'nats/server.key',key)
 q=profile('development')['queue']
 config={'port':4222,'jetstream':{'store_dir':'/data'},'tls':{'cert_file':'/config/server.crt','key_file':'/config/server.key','handshake_first':True},
 'authorization':{'users':[{'user':values['CB_DEV_NATS_ADMIN_USER'],'password':values['CB_DEV_NATS_ADMIN_PASSWORD']},
 {'user':values['CB_NATS_USER'],'password':values['CB_NATS_PASSWORD'],'permissions':{'publish':[q['subject'],'$JS.API.>','$JS.ACK.>'],'subscribe':[q['inbox']+'.>']}}]}}
 atomic(PRIVATE/'nats/server.conf',json.dumps(config))
 for name,keys in [('worker.env',['CB_NATS_USER','CB_NATS_PASSWORD']),('provider.env',['CB_SYNTHETIC_PROVIDER_TOKEN']),('queue-admin.env',['CB_DEV_NATS_ADMIN_USER','CB_DEV_NATS_ADMIN_PASSWORD'])]:
  assert all("'" not in values[k] and '\n' not in values[k] for k in keys)
  atomic(PRIVATE/name,''.join(k+"='"+values[k]+"'\n" for k in keys))

def seed():
 from run import container_args,worker_environment,invoke,read_env
 for _ in range(60):
  try:command(COMPOSE+['exec','-T','pg','pg_isready','-U','fixture','-d','integration']);break
  except RuntimeError:time.sleep(1)
 else:raise RuntimeError('fresh PostgreSQL not ready')
 args=container_args(indexing=True)
 args+=['-v',str(ROOT/'state')+':/state:rw']
 invoke(args,worker_environment(),['python','-B','/packet/fixture/seed.py'],log=PRIVATE/'seed.log')
 queue()

def queue():
 from run import container_args,worker_environment,invoke,read_env
 import shlex
 admin=dict(x.split('=',1) for x in shlex.split((PRIVATE/'queue-admin.env').read_text()))
 env=worker_environment();env.update(read_env('worker.env'));env.update(admin)
 result=invoke(container_args(),env,['python','-B','/packet/fixture/queue_setup.py'],log=PRIVATE/'queue-setup.log')
 atomic(ROOT/'queue-acceptance.json',result.decode())


def resume_setup(values):
 assert (ROOT/'state/seeded').read_text()=='synthetic only\n'
 queue()
 command(COMPOSE+['up','-d','api','webui'])
 from host import ready_api,holds
 ready_api()
 return {'api_ready':True,'webui_started':True,'seed_preserved':True,'holds':holds()}
