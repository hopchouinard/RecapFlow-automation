"""Read-only request008 comparison against privately preserved predeployment state."""
import pathlib,hashlib,json,subprocess,datetime
root=pathlib.Path('/srv/community-brain');backup=root/'artifacts/cbm-dark-mode-20260910'
def manifest(p):
 d={}
 for f in sorted(p.rglob('*')):
  assert not f.is_symlink()
  if f.is_file():d[str(f.relative_to(p))]={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
 return d
assert {n:manifest(root/n) for n in ['corpus','config','files']}==json.loads((backup/'data-manifest-before.json').read_text())
old=json.loads((backup/'api-inspect.private.json').read_text());x=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0]
assert old['Config']['Image']==x['Config']['Image']
assert set(old['Config']['Env'])==set(x['Config']['Env'])
oldmounts={m['Destination']:(m['Source'],m['RW']) for m in old['Mounts']};mounts={m['Destination']:(m['Source'],m['RW']) for m in x['Mounts']}
assert mounts.pop('/app/web/dist')==('/srv/community-brain/workspaces/cbm-dark-mode-20260910/dist',False);assert mounts==oldmounts
assert x['State']['Health']['Status']=='healthy'
assert set(subprocess.check_output(['docker','ps','--format','{{.Names}}'],text=True).splitlines())=={'community-brain-production-staging-api-1','community-brain-alloy'}
print(json.dumps({'request_id':'CBM-DARK-MODE-20260910-008','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_files_corpus_config_unchanged':True,'backend_image_unchanged':True,'entire_api_environment_unchanged':True,'only_mount_change':'read-only /app/web/dist','original_mounts_unchanged':True,'only_api_alloy_running':True,'healthy':True}))
