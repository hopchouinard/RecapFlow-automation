from secret_store import read,save
import subprocess,shlex,json,base64,tempfile
from pathlib import Path
v=read()
def ssh(host,args,input=None):
 r=subprocess.run(['ssh','-o','BatchMode=yes',host,shlex.join(args)],input=input,capture_output=True,text=True)
 if r.returncode:raise RuntimeError('TLS management step failed; private output suppressed')
 return r.stdout
ck='CB_NATS_TLS_FULLCHAIN_B64';pk='CB_NATS_TLS_KEY_B64'
renew=ck not in v
if not renew:
 with tempfile.NamedTemporaryFile() as f:
  f.write(base64.b64decode(v[ck]));f.flush()
  renew=subprocess.run(['openssl','x509','-checkend','43200','-noout','-in',f.name],capture_output=True).returncode!=0
if renew:
 ca=lambda args:ssh('traefik',['sudo','docker','exec','step-ca']+args)
 directory=ca(['mktemp','-d','/tmp/cbm-prod-nats.XXXXXXXX']).strip()
 try:
  ca(['step','ca','certificate','platform-events.patchoutech.lab',directory+'/cert.pem',directory+'/key.pem','--san','platform-events.patchoutech.lab','--provisioner','admin@patchoutech.lab','--password-file','/home/step/secrets/password','--ca-url','https://localhost:9000','--root','/home/step/certs/root_ca.crt','--not-after','24h'])
  save({ck:base64.b64encode(ca(['cat',directory+'/cert.pem']).encode()).decode(),pk:base64.b64encode(ca(['cat',directory+'/key.pem']).encode()).decode()})
 finally:ca(['rm','-rf',directory])
v=read()
code=r'''import pathlib,subprocess,json,sys,base64
v=json.load(sys.stdin)
root=pathlib.Path('/opt/platform-services/compose/community-brain-nats-tls');root.mkdir(mode=0o700,exist_ok=True)
tls=root/'tls';tls.mkdir(mode=0o700,exist_ok=True)
for name,key in [('fullchain.pem','CB_NATS_TLS_FULLCHAIN_B64'),('key.pem','CB_NATS_TLS_KEY_B64')]:
 p=tls/(name+'.new');p.write_bytes(base64.b64decode(v[key]));p.chmod(0o600);p.replace(tls/name)
conf=root/'nginx.conf';conf.write_text('pid /tmp/nginx.pid;\nevents {}\nstream { server { listen 10.1.10.54:4223 ssl; ssl_certificate /run/tls/fullchain.pem; ssl_certificate_key /run/tls/key.pem; allow 10.1.30.21; deny all; proxy_pass 10.1.10.54:4222; proxy_timeout 1h; } }\n')
compose=root/'compose.yaml';compose.write_text('services:\n  tls:\n    image: nginx@sha256:72ba65eb42c10344912a84ff42408db7d34f2feb642204570ab8fc5ffd29f1d3\n    container_name: community-brain-nats-tls\n    network_mode: host\n    restart: unless-stopped\n    read_only: true\n    tmpfs: [/tmp]\n    mem_limit: 64m\n    volumes:\n      - ./nginx.conf:/etc/nginx/nginx.conf:ro\n      - ./tls:/run/tls:ro\n    entrypoint: [nginx]\n    command: [-g, "daemon off;"]\n')
args=['docker','compose','-f',str(compose)]
subprocess.run(args+['run','--rm','tls','-t'],check=True,capture_output=True)
subprocess.run(args+['up','-d'],check=True,capture_output=True)
subprocess.run(['docker','exec','community-brain-nats-tls','nginx','-s','reload'],check=True,capture_output=True)
print(json.dumps({'tls_listener':'platform-events.patchoutech.lab:4223','source_allowlist':['10.1.30.21'],'legacy_listener_unchanged':True,'required_client_options':{'tls_handshake_first':True,'inbox_prefix':'_INBOX.cbm_prod_worker'},'certificate_authority':'Infisical homelab/prod /applications/community-brain','renewal_method':'Mac scheduled renderer, renew below 12h remaining, 24h leaf lifetime'}))
'''
result=ssh('root@10.1.10.4',['pct','exec','304','--','python3','-c',code],json.dumps({ck:v[ck],pk:v[pk]}))
Path(__file__).with_name('nats-tls.json').write_text(result);print(result)
