"""Actual successor-mapped live Adapter against local HTTP and consumer fixtures."""
import contextlib,hashlib,http.server,importlib.util,json,sys,threading,time,types
from pathlib import Path
from unittest.mock import patch
from helper_contracts import HERE,INTEGRATIONS,canonical,sha,write_new
from rehearse_helpers import Environment,module

def run(root):
 root=Path(root);root.mkdir(mode=0o700);env=Environment(root);policy=env.policy;env.accepted=json.loads(env.values[policy.IDENTITIES]);state={'webui':env.values['CB_OPENWEBUI_RETRIEVAL_TOKEN'],'kuma':env.values['CB_READ_PROBE_TOKEN']};calls=[]
 class HTTP(http.server.BaseHTTPRequestHandler):
  def log_message(self,*args):pass
  def do_GET(self):self.answer()
  def do_POST(self):self.rfile.read(int(self.headers.get('Content-Length',0)));self.answer()
  def answer(self):
   token=self.headers.get('Authorization','').removeprefix('Bearer ');r=next((r for r in env.accepted if r['sha256']==sha(token.encode()) and r['expires_at']>time.time()),None)
   permission='/metrics'==self.path and 'metrics:read' or '/retrieval/query'==self.path and 'retrieval:read' or '/api/v1/jobs'==self.path and 'jobs:read' or 'jobs:read'
   status=401 if r is None else 200 if permission in r['permissions'] else 403
   self.send_response(status);self.end_headers();self.wfile.write(b'{}')
 server=http.server.ThreadingHTTPServer(('127.0.0.1',0),HTTP);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
 collector=env.home/'Library/Application Support/CommunityBrainProduction/collector.json';collector.parent.mkdir(parents=True);collector.write_text(json.dumps({'token':env.values['CB_PROD_MAC_COLLECTOR_TOKEN'],'expires_at':int(env.values['CB_PROD_MAC_COLLECTOR_EXPIRES_AT']),'enabled':True}));collector.chmod(0o600)
 host='pchouinard@10.1.30.21';etc=env.root/'hosts'/host/'etc/community-brain-production';(etc/'manual-preparation').mkdir(parents=True)
 mappings=[('probes.env',{'CB_READ_PROBE_TOKEN':'CB_READ_PROBE_TOKEN','CB_METRICS_PROBE_TOKEN':'CB_METRICS_PROBE_TOKEN','CB_PROBE_EXPIRES_AT':'CB_PROBE_EXPIRES_AT'}),('manual-preparation/operator-client.env',{'CB_MANUAL_OPERATOR_TOKEN':'CB_PROD_MANUAL_OPERATOR_TOKEN','CB_MANUAL_OPERATOR_EXPIRES_AT':'CB_PROD_MANUAL_OPERATOR_EXPIRES_AT'}),('manual-preparation/collector-client.env',{'CB_COLLECTOR_TOKEN':'CB_PROD_MAC_COLLECTOR_TOKEN','CB_COLLECTOR_EXPIRES_AT':'CB_PROD_MAC_COLLECTOR_EXPIRES_AT'})]
 for name,m in mappings:
  p=etc/name;p.write_text(''.join(k+"='"+env.values[v]+"'\n" for k,v in m.items()));p.chmod(0o600)
 prom=env.root/'hosts/monitoring-stack/opt/monitoring-stack/config/prometheus/community-brain-private/metrics-token';prom.parent.mkdir(parents=True);prom.write_text(env.values['CB_METRICS_PROBE_TOKEN']);prom.chmod(0o640)
 def remote(target,code,payload=None):
  calls.append({'host':target,'code_sha256':sha(code.encode())})
  if target=='n8n-automation':raise AssertionError('legacy consumer dependency')
  if "'identities':" in code:return json.dumps({'identities':env.accepted,'healthy':True})
  if "'valves" in code or 'select valves,' in code:return json.dumps({'sha256':sha(state['webui'].encode()),'url':live.BASE+'/retrieval/query','active':1,'global':1})
  if code.startswith('SCRIPT='):
   assert "'community-brain-successor-webui'" in code
   state['webui']=payload['token'];return json.dumps({'live_app_process':True,'retrieval_status':'ok','context_emitted':True})
  if "'/api/v1/targets'" in code or '/api/v1/targets' in code:return json.dumps([{'health':'up','at':time.time()}])
  if 'metrics-token' in code and payload is None:return json.dumps({'sha256':sha(prom.read_bytes()),'mode':prom.stat().st_mode&511})
  if 'metrics-token' in code:
   assert prom.read_text() in (payload['old'],payload['token']);prom.write_text(payload['token']);return 'delivered'
  return env.execute_remote(target,code,payload)
 def recreate(values):
  # Consumer API endpoint double; actual Adapter.accept decides whether to call.
  env.accepted=json.loads(values[policy.IDENTITIES]);(root/'accepted-api.json').write_text(json.dumps(env.accepted))
 def kuma(code,payload):
  if payload:
   assert state['kuma'] in (payload['old'],payload['token']);state['kuma']=payload['token'];return {'ok':True}
  if 'heartbeat' in code:return {'status':1,'at':time.time()}
  return {'sha256':sha(state['kuma'].encode()),'active':1,'url':live.BASE+'/retrieval/query','method':'POST'}
 lease=types.SimpleNamespace(check=lambda:None)
 modules={'secret_store':types.SimpleNamespace(read=lambda:dict(env.values),save=env.save_authority,remote=remote),'candidate.manual_runtime':types.SimpleNamespace(recreate=recreate),'manage':types.SimpleNamespace(CTX=None),'service_renewal_policy':policy}
 try:
  with patch.dict(sys.modules,modules),patch.object(Path,'home',return_value=env.home):
   live=module(HERE/'candidate/service_renewal_live.py','candidate_live');live.BASE='http://127.0.0.1:'+str(server.server_port);live.kube_script=kuma;live.ROOT=INTEGRATIONS
   adapter=live.Adapter(lease);adapter.inventory(env.values);before=dict(env.values);result=policy.run(adapter,time.time(),force=True);assert result['state']=='completed';adapter.inventory(env.values);adapter.verify_tokens(before,401)
   assert all(c['host']!='n8n-automation' for c in calls)
   # Changed actual consumer file is detected before another renewal.
   v=json.loads(collector.read_bytes());original=v['token'];v['token']='SYNTHETIC-TAMPER';collector.write_text(json.dumps(v))
   try:adapter.inventory(env.values)
   except AssertionError:pass
   else:raise AssertionError('changed collector accepted')
   v['token']=original;collector.write_text(json.dumps(v));adapter.inventory(env.values)
  receipt={'actual_successor_adapter_executed':True,'actual_renewal_policy_executed':True,'local_http_auth_and_scope_probes':True,'consumer_changed_bytes_rejected':True,'old_tokens_rejected_after_final_authority':True,'legacy_calls':0,'calls':calls,'external_services':'local protocol fixtures; no live CA/Infisical/Kuma/WebUI/Prometheus acceptance','manual_renderer_boundary':'fixture; separate sealed renderer preflight required','production_invoked':False,'candidate_source_sha256':sha((HERE/'candidate/service_renewal_live.py').read_bytes())}
  write_new(root/'renewal-live-receipt.json',receipt);print(json.dumps(receipt))
 finally:server.shutdown();server.server_close();thread.join()
if __name__=='__main__':run(sys.argv[1])
