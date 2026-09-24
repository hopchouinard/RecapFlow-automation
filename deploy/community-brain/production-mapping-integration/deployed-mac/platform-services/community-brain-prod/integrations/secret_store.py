"""Private Infisical persistence helpers. Never return secret values to logs."""
from manage import PROJECT
import subprocess,os,json,tempfile
from pathlib import Path
BASE=['--projectId',PROJECT,'--env','prod','--path','/applications/community-brain','--domain',os.environ['INFISICAL_API_URL'],'--token',os.environ['INFISICAL_TOKEN'],'--silent']
def cli(args):
 r=subprocess.run(['infisical']+args+BASE,capture_output=True,text=True)
 if r.returncode:raise RuntimeError('Infisical failed; private output suppressed')
 return r.stdout
def read():
 entries=json.loads(cli(['secrets','--output','json','--include-imports=false','--expand=false']))
 if isinstance(entries,dict):entries=entries.get('secrets',entries.get('data',[]))
 return {e['secretKey']:e['secretValue'] for e in (entries or [])}
def save(values):
 with tempfile.TemporaryDirectory() as d:
  p=Path(d)/'values.env';fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
  with os.fdopen(fd,'w') as f:
   for k,v in values.items():
    assert isinstance(v,str) and "'" not in v and '\n' not in v
    f.write(k+"='"+v+"'\n")
  cli(['secrets','set','--file',str(p)])
 check=read();assert all(check[k]==v for k,v in values.items())
def remote(host,code,payload=None):
 import shlex
 r=subprocess.run(['ssh','-o','BatchMode=yes',host,'sudo python3 -c '+shlex.quote(code)],input=None if payload is None else json.dumps(payload),text=True,capture_output=True)
 if r.returncode:raise RuntimeError('Remote management operation failed; private output suppressed')
 return r.stdout
