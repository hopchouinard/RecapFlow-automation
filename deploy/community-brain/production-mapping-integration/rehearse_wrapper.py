import json,os,subprocess,sys
from pathlib import Path
from helper_contracts import Cycle,HERE,verify_sources,write_new,sha

def run(root,mutex):
 root=Path(root);root.mkdir(mode=0o700);bin=root/'bin';bin.mkdir();log=root/'calls.jsonl';cli=bin/'infisical'
 cli.write_text('#!'+sys.executable+'\nimport sys,json\nfrom pathlib import Path\np=Path('+repr(str(log))+')\nwith p.open("a") as f:f.write(json.dumps(sys.argv[1:3])+"\\n")\nprint("SYNTHETIC-AUTHORITY" if sys.argv[1]=="login" else "{\\"folders\\":[{\\"name\\":\\"applications\\"},{\\"name\\":\\"community-brain\\"}]}")\n');cli.chmod(0o700)
 envfile=root/'synthetic.env';envfile.write_text('INFISICAL_API_URL=http://127.0.0.1:9\nINFISICAL_PROJECT_ID=synthetic\nINFISICAL_UNIVERSAL_AUTH_CLIENT_ID=synthetic\nINFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET=SYNTHETIC-ONLY\n');envfile.chmod(0o600)
 env={**os.environ,'PATH':str(bin)+':'+os.environ['PATH'],'INFISICAL_ENV_FILE':str(envfile),'INFISICAL_MANIFEST_PATH':str(HERE/'deployed-mac/platform-services/infisical/homelab-secret-authority.yaml'),'CBM_SCOPE':'synthetic-development','CBM_DEVELOPMENT_ROOT':str(root)}
 args=['/bin/bash',str(HERE/'candidate/run.sh'),'copy-backup.py'];denied=subprocess.run(args,env=env,capture_output=True);assert denied.returncode!=0 and not log.exists()
 with Cycle(root/'journal',mutex,root.name+'-wrapper','manual',verify_sources()) as c:
  env.update(CBM_ADMISSION_FD=str(c.fd),CBM_ADMISSION_INTENT=str(c.op/'intent.json'))
  def execute():
   p=subprocess.run(args,env=env,pass_fds=(c.fd,),capture_output=True,text=True);assert p.returncode==0,p.stderr;assert 'SYNTHETIC-ONLY' not in p.stdout+p.stderr
  def readback():
   calls=[json.loads(x) for x in log.read_text().splitlines()];assert all('create' not in x for x in calls)
   target=root/'effect-copy-backup/hosts/pchouinard@10.1.30.21/srv/community-brain/db-backups';files=list(target.glob('*.dump'));assert len(files)==1
   return {'authority_calls':calls,'copy_sha256':sha(files[0].read_bytes()),'folder_creation':False,'guard_preceded_login':True}
  c.helper('copy-backup',execute,readback);c.finish()
 write_new(root/'wrapper-receipt.json',{'actual_bash_and_infisical_library':True,'authority_cli':'explicit synthetic CLI fixture','no_capability_refused_before_login':True,'no_folder_creation':True,'actual_copy_writer_ran':True,'production_invoked':False});print('wrapper checks passed')
if __name__=='__main__':run(*sys.argv[1:])
