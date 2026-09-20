"""Actual isolated monitoring clients and development service bundles."""
import json
import os
import secrets
import shlex
import time
from host import ROOT,PACKET,PRIVATE,COMPOSE,OPENER,atomic,command,container,address,call

MAPPINGS={
 'probes.env':{'CB_READ_PROBE_TOKEN':'CB_READ_PROBE_TOKEN','CB_METRICS_PROBE_TOKEN':'CB_METRICS_PROBE_TOKEN','CB_PROBE_EXPIRES_AT':'CB_PROBE_EXPIRES_AT'},
 'operator-client.env':{'CB_MANUAL_OPERATOR_TOKEN':'CB_PROD_MANUAL_OPERATOR_TOKEN','CB_MANUAL_OPERATOR_EXPIRES_AT':'CB_PROD_MANUAL_OPERATOR_EXPIRES_AT'},
 'collector-client.env':{'CB_COLLECTOR_TOKEN':'CB_PROD_MAC_COLLECTOR_TOKEN','CB_COLLECTOR_EXPIRES_AT':'CB_PROD_MAC_COLLECTOR_EXPIRES_AT'},
}

def bundles(values,old=None):
 for name,mapping in MAPPINGS.items():
  p=PRIVATE/name
  if old is not None:
   current=dict(x.split('=',1) for x in shlex.split(p.read_text()))
   assert all(current[k] in (old[src],values[src]) for k,src in mapping.items())
  atomic(p,''.join(k+"='"+values[src]+"'\n" for k,src in mapping.items()))

def kuma(payload):
 return json.loads(command(['docker','exec','-i',container('kuma'),'node','-e',(PACKET/'kuma.js').read_text()],payload,timeout=60))

def prom_token(value,old=None):
 p=PRIVATE/'prometheus/metrics-token'
 if old is not None:assert p.read_text() in (old,value)
 atomic(p,value,0o640);os.chown(p,0,65534)

def setup(values):
 marker=PRIVATE/'monitors-started';assert not marker.exists();marker.touch(mode=0o600)
 bundles(values)
 directory=PRIVATE/'prometheus';directory.mkdir(mode=0o750);directory.chmod(0o750);os.chown(directory,0,65534)
 prom_token(values['CB_METRICS_PROBE_TOKEN'])
 config={'global':{'scrape_interval':'5s'},'scrape_configs':[{'job_name':'cbm-request027-api','metrics_path':'/metrics','authorization':{'credentials_file':'/etc/prometheus/metrics-token'},'static_configs':[{'targets':['api:8090']}]}]}
 atomic(directory/'prometheus.json',json.dumps(config),0o640);os.chown(directory/'prometheus.json',0,65534)
 command(COMPOSE+['up','-d','prometheus','kuma'])
 for _ in range(120):
  try:
   with OPENER.open(address('kuma',3001),timeout=3) as r:
    if r.status==200:break
  except (OSError,ValueError):pass
  time.sleep(1)
 else:raise RuntimeError('development Kuma readiness timeout')
 password=secrets.token_urlsafe(32)
 atomic(PRIVATE/'kuma-admin.json',json.dumps({'username':'request027','password':password}))
 return resume_setup(values)

def resume_setup(values):
 # Reconcile the observed partial setup: private files and containers already
 # exist, but no user or monitor has been created. Do not replay setup().
 directory=PRIVATE/'prometheus';directory.chmod(0o750)
 command(COMPOSE+['up','-d','prometheus'])
 import urllib.request
 for _ in range(120):
  try:
   with OPENER.open(address('kuma',3001)+'/setup-database-info',timeout=3) as r:info=json.load(r)
   break
  except (OSError,ValueError):time.sleep(1)
 else:raise RuntimeError('development Kuma application readiness timeout')
 if info.get('needSetup'):
  assert not info.get('runningSetup')
  req=urllib.request.Request(address('kuma',3001)+'/setup-database',data=json.dumps({'dbConfig':{'type':'sqlite'}}).encode(),headers={'Content-Type':'application/json'})
  with OPENER.open(req,timeout=30) as r:assert json.load(r)['ok']
  time.sleep(5)
 # Socket.IO application readiness remains the authoritative gate.
 credentials=json.loads((PRIVATE/'kuma-admin.json').read_text())
 result=kuma({'mode':'setup',**credentials,'token':values['CB_READ_PROBE_TOKEN']})
 return {'actual_monitor_setup':True,'kuma':result,'partial_setup_reconciled':True}


def deliver(journal):
 old,new=journal['old'],journal['updates'];after=time.time()
 bundles(new,old)
 result=kuma({'mode':'deliver','old':old['CB_READ_PROBE_TOKEN'],'token':new['CB_READ_PROBE_TOKEN']})
 prom_token(new['CB_METRICS_PROBE_TOKEN'],old['CB_METRICS_PROBE_TOKEN'])
 command(['docker','exec',container('prometheus'),'promtool','check','config','/etc/prometheus/prometheus.json'])
 command(['docker','kill','--signal=HUP',container('prometheus')])
 return {'actual_consumers_delivered':True,'after':after,'kuma':result}

def verify(payload):
 values=payload['values'];after=payload['after']
 for name,mapping in MAPPINGS.items():
  p=PRIVATE/name;assert p.stat().st_mode&0o777==0o600
  current=dict(x.split('=',1) for x in shlex.split(p.read_text()))
  assert current=={k:values[v] for k,v in mapping.items()}
 # Consume the delivered bundle files, not merely the authority's input tokens.
 read=dict(x.split('=',1) for x in shlex.split((PRIVATE/'probes.env').read_text()))
 operator=dict(x.split('=',1) for x in shlex.split((PRIVATE/'operator-client.env').read_text()))
 collector=dict(x.split('=',1) for x in shlex.split((PRIVATE/'collector-client.env').read_text()))
 assert call('/api/v1/jobs',read['CB_READ_PROBE_TOKEN'])[0]==200
 assert call('/metrics',read['CB_METRICS_PROBE_TOKEN'])[0]==200
 assert call('/api/v1/jobs',operator['CB_MANUAL_OPERATOR_TOKEN'])[0]==200
 assert call('/api/v1/jobs',collector['CB_COLLECTOR_TOKEN'])[0]==403
 p=PRIVATE/'prometheus/metrics-token';assert p.read_text()==values['CB_METRICS_PROBE_TOKEN'] and p.stat().st_mode&0o777==0o640
 deadline=time.monotonic()+100
 while True:
  result=kuma({'mode':'verify','token':values['CB_READ_PROBE_TOKEN'],'old':values['CB_READ_PROBE_TOKEN']})
  with OPENER.open(address('prometheus',9090)+'/api/v1/targets',timeout=10) as r:data=json.load(r)
  rows=[x for x in data['data']['activeTargets'] if x['scrapePool']=='cbm-request027-api']
  from datetime import datetime
  fresh=len(rows)==1 and rows[0]['health']=='up' and datetime.fromisoformat(rows[0]['lastScrape'].replace('Z','+00:00')).timestamp()>=after
  beat=result['heartbeat']
  if beat and beat['status']==1 and beat['at']>=after and fresh:break
  if time.monotonic()>deadline:raise RuntimeError('fresh monitor acceptance missing; retain old acceptance')
  time.sleep(3)
 return {'bundle_permissions_and_values':True,'bundles_used_for_actual_api_probes':True,'collector_read_denied':True,'collector_upload_tested':False,'actual_kuma_fresh_up':True,'actual_prometheus_fresh_up':True}

def operations():return {'monitors-setup':setup,'monitors-resume':resume_setup,'consumers-deliver':deliver,'consumers-verify':verify}
