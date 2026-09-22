"""Fresh Infisical API-only render using the reviewed manual Compose overlay."""
import json
from secret_store import remote

def recreate(values):
    api={'CB_DATABASE_URL':values['CB_RUNTIME_DATABASE_URL'],'CB_SERVICE_IDENTITIES':values['CB_SERVICE_IDENTITIES']}
    api.update({k:values[k] for k in ['CB_OIDC_ISSUER','CB_OIDC_AUDIENCE','CB_OIDC_CLIENT_ID','CB_OIDC_JWKS_URL']})
    code=r'''import pathlib,sys,json,os,shlex,hashlib,subprocess,time
sys.dont_write_bytecode=True
os.umask(0o077);api=json.load(sys.stdin);root=pathlib.Path('/etc/community-brain-production');p=root/'api.env'
base=pathlib.Path('/srv/community-brain/workspaces/manual-20260910');manifest=json.loads((base/'runtime-manifest.json').read_text())
assert hashlib.sha256((base/'runtime-manifest.json').read_bytes()).hexdigest()=='cf22ff3ce1c026e8edc24cb8ef34bef1e38f69d19edbbb6ae31bd41c4ce29d11'
for n,h in manifest.items():assert not (base/n).is_symlink() and hashlib.sha256((base/n).read_bytes()).hexdigest()==h
ui=pathlib.Path('/srv/community-brain/workspaces/cbm-archive-ui-20260910')
assert hashlib.sha256((ui/'effective-runtime-manifest.json').read_bytes()).hexdigest()=='28344346dd6e8e3e87bef4021b009cf6d756f098f1866006fe598a15a4024600'
assets=json.loads((ui/'effective-runtime-manifest.json').read_text())
assert {str(p.relative_to(ui)) for p in ui.rglob('*') if p.is_file() and p.name not in ['runtime-manifest.json','effective-runtime-manifest.json']}==set(assets)
for n,h in assets.items():
 asset=ui/n;assert not asset.is_symlink() and asset.is_file()
 assert asset.stat().st_size==h['bytes'] and hashlib.sha256(asset.read_bytes()).hexdigest()==h['sha256'],n
archive=pathlib.Path('/srv/community-brain/meeting-archive-20260910')
assert hashlib.sha256((archive/'manifest.json').read_bytes()).hexdigest()=='3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00'
catalog=json.loads((archive/'manifest.json').read_text());assert catalog['scope']=='community-brain' and len(catalog['meetings'])==87
entries={a['id']:a for m in catalog['meetings'] for a in m['artifacts']};assert len(entries)==481
assert {p.name for p in (archive/'files').iterdir()}==set(entries)
for n,h in entries.items():
 f=archive/'files'/n;assert not f.is_symlink() and f.is_file() and f.stat().st_size==h['bytes'] and hashlib.sha256(f.read_bytes()).hexdigest()==h['sha256'],n
frontend=pathlib.Path('/srv/community-brain/workspaces/cbm-workspace-recovery-20260917-frontend')
assert hashlib.sha256((frontend/'effective-frontend-manifest.json').read_bytes()).hexdigest()=='564a565276db86eda41352ce7f490f1d8fcc548ecc26a468795b6d03243b15ee'
static=json.loads((frontend/'effective-frontend-manifest.json').read_text())
assert {str(p.relative_to(frontend/'dist')) for p in (frontend/'dist').rglob('*') if p.is_file()}==set(static)
for n,h in static.items():
 f=frontend/'dist'/n;assert not f.is_symlink() and f.is_file() and f.stat().st_size==h['bytes'] and hashlib.sha256(f.read_bytes()).hexdigest()==h['sha256'],n
packet=pathlib.Path('/srv/community-brain/workspaces/cbm-workspace-recovery-20260917-effective-r020')
assert hashlib.sha256((packet/'effective-manifest.json').read_bytes()).hexdigest()=='e3ba6ed250d64881f2d6d1c3bcf70b0515e90ab1f23fe0ca1133cf9d4400fabd'
effective=json.loads((packet/'effective-manifest.json').read_text())['files']
assert {str(p.relative_to(packet)) for p in packet.rglob('*') if p.is_file() and p.name!='effective-manifest.json'}==set(effective)
for n,h in effective.items():
 f=packet/n;assert not f.is_symlink() and f.stat().st_size==h['bytes'] and hashlib.sha256(f.read_bytes()).hexdigest()==h['sha256']
sys.path.insert(0,str(packet));from automatic_host import publish_checkpoint_status
publish_checkpoint_status()
public=pathlib.Path('/srv/community-brain/automation-public')
assert public.stat().st_uid==0 and public.stat().st_mode&0o777==0o755
assert (public/'checkpoints.json').stat().st_uid==0 and (public/'checkpoints.json').stat().st_mode&0o777==0o644
old={k:shlex.split(v)[0] for k,v in (line.split('=',1) for line in p.read_text().splitlines() if line and not line.startswith('#'))}
assert {k:v for k,v in old.items() if k!='CB_SERVICE_IDENTITIES'}=={k:v for k,v in api.items() if k!='CB_SERVICE_IDENTITIES'}
sys.path.insert(0,str(base/'production-staging'));from manual_host import validate_identities
validate_identities(api)
assert all(isinstance(v,str) and not any(c in v for c in ["'",'\n','\r']) for v in api.values())
t=root/'.api.manual-renewal';t.write_text(''.join(k+"='"+v+"'\n" for k,v in api.items()));t.chmod(0o600);t.replace(p)
r=subprocess.run(['python3',str(base/'production-staging/manual_host.py'),'api-up'],capture_output=True,text=True)
assert r.returncode==0,'Manual API recreation failed; inspect private manual-api-up.log'
for attempt in range(30):
 probe=subprocess.run(['docker','exec','community-brain-production-staging-api-1','python','-c',"import urllib.request;urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=1)"],capture_output=True)
 if probe.returncode==0:break
 time.sleep(1)
else:raise RuntimeError('Manual API health readiness failed')
print('Manual API recreated with fresh authoritative identities and verified overlay')
'''
    assert remote('pchouinard@10.1.30.21',code,api).strip().startswith('Manual API recreated')

if __name__=='__main__':
    from secret_store import read
    recreate(read())
    print('Manual API recreated; run TLS/auth/health/cue and actual WebUI checks before acceptance')
