"""Mac-issued private leaf, persisted in Infisical before delivery to Traefik."""
from secret_store import read,save,remote
import base64,subprocess,shlex,tempfile,json
from pathlib import Path
v=read();ck='CB_APP_TLS_FULLCHAIN_B64';pk='CB_APP_TLS_KEY_B64';renew=ck not in v
if not renew:
 with tempfile.NamedTemporaryFile() as f:
  f.write(base64.b64decode(v[ck]));f.flush()
  renew=subprocess.run(['openssl','x509','-checkend','43200','-noout','-in',f.name],capture_output=True).returncode!=0
if renew:
 def ca(args):
  r=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','traefik',shlex.join(['sudo','docker','exec','step-ca']+args)],capture_output=True,text=True)
  if r.returncode:raise RuntimeError('CA operation failed; private output suppressed')
  return r.stdout
 d=ca(['mktemp','-d','/tmp/cbm-prod-app.XXXXXXXX']).strip()
 try:
  ca(['step','ca','certificate','community-brain.patchoutech.lab',d+'/cert.pem',d+'/key.pem','--san','community-brain.patchoutech.lab','--provisioner','admin@patchoutech.lab','--password-file','/home/step/secrets/password','--ca-url','https://localhost:9000','--root','/home/step/certs/root_ca.crt','--not-after','24h'])
  save({ck:base64.b64encode(ca(['cat',d+'/cert.pem']).encode()).decode(),pk:base64.b64encode(ca(['cat',d+'/key.pem']).encode()).decode()})
 finally:ca(['rm','-rf',d])
v=read()
code=r'''import pathlib,json,sys,base64,datetime
v=json.load(sys.stdin);root=pathlib.Path('/mnt/HDD_2TB_Main/traefik/dynamic/community-brain-private');root.mkdir(mode=0o700,exist_ok=True)
for name,key in [('fullchain.pem','CB_APP_TLS_FULLCHAIN_B64'),('key.pem','CB_APP_TLS_KEY_B64')]:
 p=root/(name+'.new');p.write_bytes(base64.b64decode(v[key]));p.chmod(0o600);p.replace(root/name)
p=pathlib.Path('/mnt/HDD_2TB_Main/traefik/dynamic/community-brain-tls.yml')
s='tls:\n  certificates:\n    - certFile: /etc/traefik/dynamic/community-brain-private/fullchain.pem\n      keyFile: /etc/traefik/dynamic/community-brain-private/key.pem\n'
s+='# rendered '+datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n'
t=p.with_suffix('.new');t.write_text(s);t.chmod(0o644);t.replace(p)
print('App certificate delivered')
'''
assert remote('traefik',code,{ck:v[ck],pk:v[pk]}).strip()=='App certificate delivered'
print(json.dumps({'certificate':'community-brain.patchoutech.lab','renewed':renew,'authority':'Infisical','private_path':'/mnt/HDD_2TB_Main/traefik/dynamic/community-brain-private','renew_below_remaining_hours':12,'lifetime_hours':24}))
