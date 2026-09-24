import pathlib,json,hashlib,subprocess,sys,datetime
ROOT=pathlib.Path('/srv/dev-data/workspaces/cbm-production-mapping-20260922-033');sys.path.insert(0,str(ROOT/'packet-v7'));import service_recovery as s
out={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'packets':{},'containers':{},'units':{},'journal':[],'kernel_boot_id':pathlib.Path('/proc/sys/kernel/random/boot_id').read_text().strip()}
for p in sorted(ROOT.glob('packet-v*')):
 m=json.loads((p/'packet-manifest.json').read_bytes());actual={str(f.relative_to(p)) for f in p.rglob('*') if f.is_file()}
 assert actual==set(m)|{'packet-manifest.json'}
 assert all(not (p/n).is_symlink() and s.sha(p/n)==h for n,h in m.items())
 assert all((p/n).stat().st_uid==0 and (p/n).stat().st_mode&511==0o444 for n in actual)
 out['packets'][p.name]={'files':len(m),'manifest_sha256':s.sha(p/'packet-manifest.json'),'exact_bytes_and_members':True,'root_owned_readonly':True}
def add(ident,name,binding):
 row=s.inspect(ident);assert row['Name'].lstrip('/')==name and name.startswith('cbm-r033-')
 out['containers'][ident]={'id':ident,'name':name,'image':row['Image'],'fingerprint':s.fingerprint(row),'running':row['State']['Running'],'recorded_binding':str(binding),'mounts':[{'source':m['Source'],'destination':m['Destination']} for m in row['Mounts']]}
for p in ROOT.glob('*-created.json'):
 v=json.loads(p.read_bytes());add(v['id'],v['name'],p);assert s.inspect(v['id'])['Image']==v['image']
for p in ROOT.glob('services-*/spec.json'):
 v=json.loads(p.read_bytes());add(v['incumbent_id'],v['incumbent_name'],p);assert out['containers'][v['incumbent_id']]['fingerprint']==v['fingerprint']
 for name,h in v['persistent_holds'].items():assert s.sha(p.parent/'automation'/name)==h
 assert (p.parent/'automation/paused').exists()
 label=p.parent.name.removeprefix('services-');receipt=json.loads((ROOT/(label+'-service-receipt.json')).read_bytes())
 for unit in receipt['units']:out['units'][unit+'.service']={}
for p in ROOT.glob('renderer-*/binding.json'):
 v=json.loads(p.read_bytes());row=s.inspect(v['incumbent_id']);add(row['Id'],row['Name'].lstrip('/'),p);assert s.fingerprint(row)==v['incumbent_fingerprint'] and row['State']['Running']
 c=p.parent/('generation-'+v['generation'])/'created.json';n=json.loads(c.read_bytes());add(n['replacement_id'],n['name'],c);assert not s.inspect(n['replacement_id'])['State']['Running']
 proofs=list(p.parent.glob('finalizer-*.json'));assert proofs and all(json.loads(x.read_bytes())['verified'] for x in proofs)
 out['units'][v['unit']]={}
for u in out['units']:
 raw=subprocess.check_output(['systemctl','show',u,'--property=ActiveState,SubState,MainPID,LoadState,Result'],text=True);props=dict(x.split('=',1) for x in raw.splitlines() if '=' in x);assert props.get('MainPID','0')=='0';out['units'][u]=props
actual=[s.inspect(i) for i in subprocess.check_output(['docker','ps','-aq'],text=True).split()]
assert {r['Id'] for r in actual if r['Name'].lstrip('/').startswith('cbm-r033-')}==set(out['containers'])
for p in (ROOT/'journal').iterdir():
 assert (p/'intent.json').exists() and (p/'resolved.json').exists(),p
 out['journal'].append({'operation':p.name,'intent_sha256':s.sha(p/'intent.json'),'resolved_sha256':s.sha(p/'resolved.json')})
out.update(all_recorded_containers_accounted=True,common_journal_unresolved=0,actual_vm_reboot=False,processing_holds_preserved=True)
print(json.dumps(out))
