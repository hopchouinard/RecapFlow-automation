from pathlib import Path
import json,hashlib,subprocess,sys,datetime
s=Path.home()/'.local/state/community-brain-management/request033';p=s/'sealed/packet-v7';out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
code=(s.parent/'request029/snapshot-code.py').read_text().replace("name.startswith('cbm-r029')","name.startswith('cbm-r033')")
for label,host in [('production','10.1.30.21'),('development','10.1.30.20')]:
 r=subprocess.run(['ssh','-o','BatchMode=yes','pchouinard@'+host,'sudo -n python3 -B -'],input=code,capture_output=True,text=True);assert r.returncode==0,r.stderr
 v=json.loads(r.stdout);(s/(label+'-after.json')).write_text(json.dumps(v,indent=2)+'\n');before=json.loads((s/(label+'-before.json')).read_bytes());before.pop('checked_at');v.pop('checked_at');assert before==v,label
 out[label]={'unchanged':True,'baseline_containers':len(v['containers']),'compared':'exact IDs, images, configurations, running state, start times and restart counts; production held control bytes and retained old bytecode'}
for name,h in json.loads((p/'deployed-manifest.json').read_bytes()).items():assert hashlib.sha256((Path.home()/'.local/lib/community-brain-management'/name).read_bytes()).hexdigest()==h,name
out['installed_mac_source_files_unchanged']=len(json.loads((p/'deployed-manifest.json').read_bytes()))
rows=json.loads((p/'remote-source-manifest.json').read_bytes());out['remote_source_files_unchanged']=0
for host in sorted({v['host'] for v in rows.values()}):
 expected={v['original_path']:v['sha256'] for v in rows.values() if v['host']==host};code="from pathlib import Path\nimport hashlib,json\nv="+repr(expected)+"\nassert all(hashlib.sha256(Path(n).read_bytes()).hexdigest()==h for n,h in v.items())\nprint(json.dumps({'verified':len(v)}))"
 r=subprocess.run(['ssh','-o','BatchMode=yes',host,'python3 -B -' if host.startswith('root@') else 'sudo -n python3 -B -'],input=code,text=True,capture_output=True);assert r.returncode==0,r.stderr;out['remote_source_files_unchanged']+=json.loads(r.stdout)['verified']
sys.path.insert(0,str(p));import legacy_admission;out['legacy']=legacy_admission.check(s.parent/'scheduler.lock')
out['mac_common_journal']=[]
for x in (s/'journal').iterdir():
 assert (x/'intent.json').exists() and (x/'resolved.json').exists(),x
 out['mac_common_journal'].append({'operation':x.name,'intent_sha256':hashlib.sha256((x/'intent.json').read_bytes()).hexdigest(),'resolved_sha256':hashlib.sha256((x/'resolved.json').read_bytes()).hexdigest()})
code="import json,subprocess,pathlib\nr=json.loads(subprocess.check_output(['docker','inspect','83358b76e0544437bd8947ba9a7be94d9fba59559a6dc56bd3c1c0110fb8a33c']))[0]\nprint(json.dumps({'container_id':r['Id'],'image':r['Image'],'running':r['State']['Running'],'mounts':r['Mounts'],'machine_id':pathlib.Path('/etc/machine-id').read_text().strip()}))"
r=subprocess.run(['ssh','-o','BatchMode=yes','n8n-automation','sudo -n python3 -B -'],input=code,text=True,capture_output=True);assert r.returncode==0;v=json.loads(r.stdout);old=json.loads((s/'legacy-private-bindings.json').read_bytes());assert all(v[k]==old[k] for k in v);out['vm101_webui']=v;out['vm101_read_only_metadata_only']=True
(s/'preservation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
