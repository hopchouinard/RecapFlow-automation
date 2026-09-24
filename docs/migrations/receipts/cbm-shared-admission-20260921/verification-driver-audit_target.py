import sys,json,time,hashlib,subprocess,os
from pathlib import Path
ROOT=Path('/srv/dev-data/workspaces/cbm-shared-admission-20260921-032')
sys.path.insert(0,str(ROOT/'packet-v6'))
import common as c
out={'checked_at_epoch':time.time(),'operations':[],'packets':{},'production_effects':False}
for packet in sorted(ROOT.glob('packet-v*')):
 raw=(packet/'packet-manifest.json').read_bytes();manifest=json.loads(raw);sha=hashlib.sha256(raw).hexdigest();c.packet(packet,sha)
 out['packets'][packet.name]={'manifest_sha256':sha,'files':len(manifest),'exact_bytes_and_members':True,'all_files_root_owned_readonly':all((packet/n).stat().st_uid==0 and (packet/n).stat().st_mode&511==292 for n in [*manifest,'packet-manifest.json'])}
for op in sorted((ROOT/'operations').iterdir()):
 spec=json.loads((op/'spec.json').read_bytes());row=c.verify_incumbent(spec)
 unit='cbm-r032-'+spec['operation_id']+'.service'
 props=c.command(['systemctl','show',unit,'--property=ActiveState,Result,MainPID,ExecMainStatus,RuntimeMaxUSec,TimeoutStopUSec,KillMode,Restart']).decode()
 properties=dict(x.split('=',1) for x in props.splitlines() if '=' in x)
 assert properties['ActiveState'] in ('inactive','failed'),unit
 v={'operation_id':spec['operation_id'],'owner_id':spec['owner_id'],'path':str(op),'spec_sha256':hashlib.sha256((op/'spec.json').read_bytes()).hexdigest(),'packet':spec['packet'],'packet_sha256':spec['packet_sha256'],'incumbent_id':row['Id'],'incumbent_name':row['Name'].lstrip('/'),'incumbent_running_before_teardown':row['State']['Running'],'incumbent_configuration_equal':True,'holds_equal':c.r.hold_state(spec['holds'])==spec['hold_bindings'],'unit':properties,'deadlines':spec['deadlines'],'stop_intent_present':(op/'stop-intent.json').exists(),'retained_files':{},'private_data_retained_on_vm108':True}
 for n in ('dispatch-intent.json','stop-intent.json','serving-restored.json','terminal.json','finalizer.json','recovery-unresolved.json','refusal.json','worker-result.json','capture-ready.json','fence-released.json'):
  p=op/n
  if p.exists():v['retained_files'][n]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'value':json.loads(p.read_bytes())}
 if 'terminal.json' in v['retained_files']:
  t=v['retained_files']['terminal.json']['value'];v['terminal_state']=t['state'];v['within_serving_deadline']=t.get('serving_restored_at',0)<=spec['deadlines']['serving_by']
  assert t['state'] in ('completed','aborted_restored') and v['holds_equal'] and v['incumbent_running_before_teardown'] and v['within_serving_deadline']
 else:
  raise AssertionError('unresolved target operation')
 out['operations'].append(v)
out['operation_count']=len(out['operations']);out['no_active_operations']=True
out['kernel_boot_id']=c.boot_id()
out['boot_admission']=json.loads((ROOT/'boot-admission.json').read_bytes())
out['prepared_specs']=len(list((ROOT/'specs').glob('*.json')))
out['fixtures']=[]
for fixture in sorted((ROOT/'fixtures').iterdir()):
 name='cbm-r032-inc-'+fixture.name
 row=c.inspect(name)
 assert any(m['Source']==str(fixture/'state') and m['Destination']=='/srv/state' for m in row['Mounts'])
 out['fixtures'].append({'name':name,'id':row['Id'],'fixture':str(fixture),'fingerprint':c.fingerprint(row),'running':row['State']['Running'],'created_binding':(fixture/'incumbent-created.json').exists(),'has_spec':any(json.loads(p.read_bytes())['fixture']==str(fixture) for p in (ROOT/'specs').glob('*.json'))})
print(json.dumps(out))
