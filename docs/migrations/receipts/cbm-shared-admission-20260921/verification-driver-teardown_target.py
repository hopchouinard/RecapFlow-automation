import sys,json,time
from pathlib import Path
ROOT=Path('/srv/dev-data/workspaces/cbm-shared-admission-20260921-032');sys.path.insert(0,str(ROOT/'packet-v6'));import common as c
expected=json.loads(sys.stdin.read());owned={row['id']:row['name'] for row in expected['fixtures']}
for v in json.loads((ROOT/'database-bindings.json').read_bytes()).values():owned[v['id']]=v['name']
for op in expected['operations']:
 state=c.command(['systemctl','show','cbm-r032-'+op['operation_id']+'.service','--property=ActiveState','--value']).decode().strip();assert state in ('inactive','failed')
# Explicit retirement closes candidate boot and admission before stopping fixtures.
if not (ROOT/'retired.json').exists():c.r.write_new(ROOT/'retired.json',c.r.encode({'at':time.time(),'reason':'Request032 verification complete; retained synthetic fixtures stopped; no replay','owner':'home.servers'}))
else:assert json.loads((ROOT/'retired.json').read_bytes())['owner']=='home.servers'
record=json.loads((ROOT/'boot-admission.json').read_bytes());record.update(admission_open=False,reason='retired after verification');c.atom(ROOT/'boot-admission.json',record)
rows=[]
for ident,name in owned.items():
 row=c.inspect(ident);assert row['Name'].lstrip('/')==name and name.startswith('cbm-r032-')
 if row['State']['Running']:c.command(['docker','stop','--time','2',ident],timeout=8)
 after=c.inspect(ident);assert not after['State']['Running'];rows.append({'id':ident,'name':name,'running':False,'removed':False,'data_retained':True})
units=json.loads(c.command(['systemctl','list-units','--all','--output=json','cbm-r032-start-*']))
unit_results=[]
for unit in units:
 name=unit['unit'];assert name.startswith('cbm-r032-start-') and name.endswith('.service')
 result=__import__('subprocess').run(['systemctl','stop',name],capture_output=True)
 prop=__import__('subprocess').run(['systemctl','show',name,'--property=ActiveState,LoadState'],capture_output=True,text=True)
 values=dict(x.split('=',1) for x in prop.stdout.splitlines() if '=' in x)
 assert values.get('ActiveState') in ('inactive','failed') or values.get('LoadState')=='not-found',values
 unit_results.append({'unit':name,'properties':values,'stop_returncode':result.returncode,'dependency_unloaded_transient_unit':values.get('LoadState')=='not-found'})
print(json.dumps({'at':time.time(),'containers':rows,'count':len(rows),'startup_units':unit_results,'scope':'Request032 IDs verified against pre-teardown fixture audit and database bindings','preexisting_containers_touched':False,'data_deleted':False,'retired_marker':str(ROOT/'retired.json'),'all_attempts_and_packets_retained':True}))
