"""One-time request009 preservation and reviewed API overlay preparation."""
import pathlib,json,hashlib,subprocess,shutil,os,datetime
os.umask(0o077);root=pathlib.Path('/srv/community-brain');base=root/'workspaces/manual-20260910';ui=root/'workspaces/cbm-archive-ui-20260910';data=root/'meeting-archive-20260910';backup=root/'artifacts/cbm-meeting-archive-20260910';backup.mkdir(mode=0o700)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(p):
 d={}
 for f in sorted(p.rglob('*')):
  assert not f.is_symlink()
  if f.is_file():d[str(f.relative_to(p))]={'bytes':f.stat().st_size,'sha256':sha(f)}
 return d
assert sha(data/'manifest.json')=='3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00';archive=json.loads((data/'manifest.json').read_text());assert archive['scope']=='community-brain' and len(archive['meetings'])==87
entries={a['id']:a for m in archive['meetings'] for a in m['artifacts']};assert len(entries)==481
assert {p.name for p in (data/'files').iterdir()}==set(entries)
for n,h in entries.items():
 p=data/'files'/n;assert not p.is_symlink() and p.is_file() and p.stat().st_size==h['bytes'] and sha(p)==h['sha256']
packet=json.loads(pathlib.Path('/srv/community-brain/handoff/requests/CBM-MEETING-ARCHIVE-20260910-009/documents/cbm-archive-ui-manifest.json').read_text())
for n,h in packet.items():assert (ui/n).stat().st_size==h['bytes'] and sha(ui/n)==h['sha256']
runtime=json.loads((base/'runtime-manifest.json').read_text());assert len(runtime)==14
for n,h in runtime.items():assert sha(base/n)==h
for n in ['compose.production-manual.yml','runtime-manifest.json','production-staging/manual_host.py']:
 p=backup/'before'/n;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(base/n,p)
x=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0];(backup/'api-inspect.private.json').write_text(json.dumps(x));shutil.copy2('/etc/community-brain-production/api.env',backup/'api.env.before')
old=root/'workspaces/cbm-dark-mode-20260910/dist';old_assets=manifest(old)
for n,h in old_assets.items():
 if n.startswith('assets/'):
  p=ui/'dist'/n
  if p.exists():assert sha(p)==h['sha256']
  else:shutil.copy2(old/n,p)
for parent in [data,ui]:
 for p in [parent,*parent.rglob('*')]:
  assert not p.is_symlink();p.chmod(0o755 if p.is_dir() else 0o644)
effective={n:{'bytes':(ui/n).stat().st_size,'sha256':sha(ui/n)} for n in packet}
for n,h in manifest(ui/'dist').items():effective['dist/'+n]=h
(ui/'effective-runtime-manifest.json').write_text(json.dumps(effective,indent=2)+'\n');(ui/'effective-runtime-manifest.json').chmod(0o644)
s=(base/'compose.production-manual.yml').read_text();oldbind='/srv/community-brain/workspaces/cbm-dark-mode-20260910/dist:/app/web/dist:ro';assert s.count(oldbind)==1
s=s.replace(oldbind,str(ui)+'/dist:/app/web/dist:ro');s=s.replace('    environment:\n','    environment:\n      CB_MEETING_ARCHIVE_ROOT: /state/meeting-archive\n      CB_MEETING_ARCHIVE_SHA256: 3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00\n      CB_HIDDEN_JOB_IDS: \'["f6e9abed-e862-4eb7-a231-e98467adcaba","91d77409-afed-4625-97cb-748c8b637991"]\'\n')
s+='      - '+str(data)+':/state/meeting-archive:ro\n'
for n in ['api.py','runtime.py','archive.py']:s+='      - '+str(ui/n)+':/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs/'+n+':ro\n'
def atomic(p,s):
 t=p.with_name('.'+p.name+'.009.tmp');t.write_text(s);t.chmod(0o600);t.replace(p)
atomic(base/'compose.production-manual.yml',s);runtime['compose.production-manual.yml']=sha(base/'compose.production-manual.yml');atomic(base/'runtime-manifest.json',json.dumps(runtime,indent=2)+'\n')
state={n:manifest(root/n) for n in ['corpus','config','files']};(backup/'data-manifest-before.json').write_text(json.dumps(state,sort_keys=True))
r={'request_id':'CBM-MEETING-ARCHIVE-20260910-009','prepared_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_manifest_sha256':sha(data/'manifest.json'),'archive_meetings':87,'archive_files_verified':481,'old_assets':old_assets,'effective_packet':effective,'before_runtime_manifest_sha256':sha(backup/'before/runtime-manifest.json'),'after_runtime_manifest_sha256':sha(base/'runtime-manifest.json'),'effective_packet_manifest_sha256':sha(ui/'effective-runtime-manifest.json'),'private_backup':str(backup)}
(backup/'preparation.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
