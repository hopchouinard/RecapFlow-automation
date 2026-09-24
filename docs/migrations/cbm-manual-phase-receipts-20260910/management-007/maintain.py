import subprocess,pathlib,datetime,json
root=pathlib.Path(__file__).resolve().parent
status={}
def task(name,args,timeout):
 try:
  r=subprocess.run(args,capture_output=True,text=True,timeout=timeout)
  status[name]='passed' if r.returncode==0 else 'failed: inspect private management status'
 except subprocess.TimeoutExpired:status[name]='timed out: coverage unconfirmed'
helpers=root/'platform-services/community-brain-prod/integrations'
task('pre-pbs-copy',['python3',str(helpers/'pre-pbs-copy.py')],210)
task('legacy-intake-ownership',['/usr/bin/python3',str(root/'mac-intake.py'),'poll'],45)
for script in ['provision-nats-tls.py','renew-app-tls.py','copy-backup.py','management-health.py']:
 task(script,['/bin/bash',str(helpers/'run.sh'),script],180)
ok=all(v=='passed' for v in status.values())
status['checked_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=pathlib.Path.home()/'.local/state/community-brain-management/maintenance-status.json'
t=p.with_suffix('.tmp');t.write_text(json.dumps(status,indent=2)+'\n');t.chmod(0o600);t.replace(p)
print(json.dumps(status))
raise SystemExit(0 if ok else 1)
