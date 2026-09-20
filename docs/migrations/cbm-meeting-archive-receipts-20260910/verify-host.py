"""Read-only request008 comparison against privately preserved predeployment state."""
import pathlib,hashlib,json,subprocess,datetime
root=pathlib.Path('/srv/community-brain');backup=root/'artifacts/cbm-meeting-archive-20260910'
def manifest(p):
 d={}
 for f in sorted(p.rglob('*')):
  assert not f.is_symlink()
  if f.is_file():d[str(f.relative_to(p))]={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
 return d
assert {n:manifest(root/n) for n in ['corpus','config','files']}==json.loads((backup/'data-manifest-before.json').read_text())
old=json.loads((backup/'api-inspect.private.json').read_text());x=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0]
assert old['Config']['Image']==x['Config']['Image']
before=dict(v.split('=',1) for v in old['Config']['Env']);after=dict(v.split('=',1) for v in x['Config']['Env'])
assert after.pop('CB_MEETING_ARCHIVE_ROOT')=='/state/meeting-archive'
assert after.pop('CB_MEETING_ARCHIVE_SHA256')=='3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00'
assert json.loads(after.pop('CB_HIDDEN_JOB_IDS'))==['f6e9abed-e862-4eb7-a231-e98467adcaba','91d77409-afed-4625-97cb-748c8b637991']
assert before==after
oldmounts={m['Destination']:(m['Source'],m['RW']) for m in old['Mounts']};mounts={m['Destination']:(m['Source'],m['RW']) for m in x['Mounts']}
assert mounts.pop('/app/web/dist')==('/srv/community-brain/workspaces/cbm-archive-ui-20260910/dist',False);oldmounts.pop('/app/web/dist')
assert mounts.pop('/state/meeting-archive')==('/srv/community-brain/meeting-archive-20260910',False)
for n in ['api.py','runtime.py','archive.py']:
 assert mounts.pop('/app/community-brain/.venv/lib/python3.11/site-packages/community_brain/jobs/'+n)==('/srv/community-brain/workspaces/cbm-archive-ui-20260910/'+n,False)
assert mounts==oldmounts
assert x['State']['Health']['Status']=='healthy'
assert set(subprocess.check_output(['docker','ps','--format','{{.Names}}'],text=True).splitlines())=={'community-brain-production-staging-api-1','community-brain-alloy'}
print(json.dumps({'request_id':'CBM-MEETING-ARCHIVE-20260910-009','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'all_files_corpus_config_unchanged':True,'backend_image_unchanged':True,'only_three_reviewed_public_env_additions':True,'auth_environment_unchanged':True,'mount_changes':'reviewed read-only static/module/archive mounts','original_mounts_unchanged':True,'only_api_alloy_running':True,'healthy':True}))
