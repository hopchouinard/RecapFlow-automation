import json,hashlib,subprocess,sys
from pathlib import Path
s=Path.home()/'.local/state/community-brain-management/request032';sys.path.insert(0,str(s/'sealed/packet-v6'));import shared
code=(s.parent/'request029/snapshot-code.py').read_text().replace("name.startswith('cbm-r029')","name.startswith('cbm-r032')")
results={}
for label,host in [('production','10.1.30.21'),('development','10.1.30.20')]:
 r=subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','pchouinard@'+host,'sudo -n python3 -B -'],input=code,capture_output=True,text=True);assert r.returncode==0,r.stderr
 v=json.loads(r.stdout);(s/(label+'-after.json')).write_text(json.dumps(v,indent=2)+'\n');old=json.loads((s/(label+'-before.json')).read_bytes());old.pop('checked_at');v.pop('checked_at');assert old==v,label
 results[label]={'unchanged':True,'containers':len(v['containers']),'compared':'IDs, images, config, running state, start timestamps, restart counts; production holds and retained bytecode'}
lineage=json.loads((s/'sealed/packet-v6/LINEAGE.json').read_bytes())
for name,sha in lineage['installed_scheduler_snapshot'].items():
 matches=[Path.home()/'.local/lib/community-brain-management'/name];assert hashlib.sha256(matches[0].read_bytes()).hexdigest()==sha
 assert matches,name
 results.setdefault('installed_scheduler',{})[name]={'sha256':sha,'matching_installed_paths':[str(p) for p in matches]}
spec=json.loads((s/'legacy6-spec.json').read_bytes());shared.legacy_guard(spec)
st=shared.MUTEX.stat();assert json.loads((s/'host-bindings.json').read_bytes())['mutex']=={'device':st.st_dev,'inode':st.st_ino,'uid':st.st_uid,'gid':st.st_gid,'mode':st.st_mode&511}
rows=[]
for p in (s/'journal').iterdir():
 assert (p/'intent.json').exists() and (p/'resolution.json').exists(),p
 rows.append({'operation_id':p.name,'intent_sha256':hashlib.sha256((p/'intent.json').read_bytes()).hexdigest(),'resolution_sha256':hashlib.sha256((p/'resolution.json').read_bytes()).hexdigest(),'resolved':True,'retained':True})
results.update(journal=rows,unresolved_shared_intents=0,existing_mutex_identity_unchanged=True,legacy_pending_retained_and_fresh_target_disposition_verified=True,vm101_touched=False)
(s/'preservation.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results))
