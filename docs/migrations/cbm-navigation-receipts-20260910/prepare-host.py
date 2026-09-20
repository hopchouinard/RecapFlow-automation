"""Request010: preserve current controls and prepare one API-only static mount."""
import pathlib,hashlib,json,subprocess,os,shutil,datetime
os.umask(0o077)
root=pathlib.Path('/srv/community-brain');base=root/'workspaces/manual-20260910';ui=root/'workspaces/cbm-navigation-20260910';backup=root/'artifacts/cbm-navigation-20260910';backup.mkdir(mode=0o700)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(p):
 d={}
 for f in sorted(p.rglob('*')):
  assert not f.is_symlink()
  if f.is_file():d[str(f.relative_to(p))]={'bytes':f.stat().st_size,'sha256':sha(f)}
 return d
runtime=json.loads((base/'runtime-manifest.json').read_text());assert len(runtime)==14
for n,h in runtime.items():assert sha(base/n)==h
for n in ['compose.production-manual.yml','runtime-manifest.json','production-staging/manual_host.py']:
 dest=backup/'before'/n;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(base/n,dest)
x=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0]
(backup/'api-inspect.private.json').write_text(json.dumps(x));shutil.copy2('/etc/community-brain-production/api.env',backup/'api.env.before')
subprocess.run(['docker','cp','community-brain-production-staging-api-1:/app/web/dist',str(backup/'old-dist')],check=True,capture_output=True)
old=manifest(backup/'old-dist');new=json.loads((ui/'frontend-manifest.json').read_text());expected=json.loads(pathlib.Path('/srv/community-brain/handoff/requests/CBM-NAVIGATION-20260910-010/documents/cbm-navigation-manifest.json').read_text());assert new==expected and manifest(ui/'dist')==new
for n,h in old.items():
 if not n.startswith('assets/'):continue
 target=ui/'dist'/n
 if target.exists():assert sha(target)==h['sha256'],'Colliding old asset differs'
 else:target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(backup/'old-dist'/n,target)
for f in (ui/'dist').rglob('*'):f.chmod(0o755 if f.is_dir() else 0o644)
combined=manifest(ui/'dist');(ui/'effective-frontend-manifest.json').write_text(json.dumps(combined,indent=2)+'\n')
old_overlay=(base/'compose.production-manual.yml').read_text();assert old_overlay.count('    volumes:')==1
old_static='/srv/community-brain/workspaces/cbm-archive-ui-20260910/dist:/app/web/dist:ro';assert old_overlay.count(old_static)==1
new_overlay=old_overlay.replace(old_static,'/srv/community-brain/workspaces/cbm-navigation-20260910/dist:/app/web/dist:ro')
def atomic(p,s):
 t=p.with_name('.'+p.name+'.010.tmp');t.write_text(s);t.chmod(0o600);t.replace(p)
atomic(base/'compose.production-manual.yml',new_overlay);runtime['compose.production-manual.yml']=sha(base/'compose.production-manual.yml');atomic(base/'runtime-manifest.json',json.dumps(runtime,indent=2)+'\n')
state={n:manifest(root/n) for n in ['corpus','config','files','meeting-archive-20260910']};(backup/'data-manifest-before.json').write_text(json.dumps(state,sort_keys=True))
r={'request_id':'CBM-NAVIGATION-20260910-010','prepared_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'private_backup':str(backup),'old_assets':old,'new_assets':new,'effective_assets':combined,'before_runtime_manifest_sha256':sha(backup/'before/runtime-manifest.json'),'after_runtime_manifest_sha256':sha(base/'runtime-manifest.json'),'effective_frontend_manifest_sha256':sha(ui/'effective-frontend-manifest.json'),'data_manifest_sha256':sha(backup/'data-manifest-before.json'),'api_not_recreated_yet':True}
(backup/'preparation.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
