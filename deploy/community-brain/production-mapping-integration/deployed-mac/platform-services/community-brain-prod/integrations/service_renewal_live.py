"""Exact existing production consumers. No model calls or submission probes."""
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import time
import urllib.error
import urllib.request
from secret_store import read, save, remote
from manual_api_runtime import recreate
from manage import CTX
from service_renewal_policy import SPECS, IDENTITIES

VM = 'pchouinard@10.1.30.21'
ROOT = Path(__file__).resolve().parent
BASE = 'https://community-brain.patchoutech.lab'


def request(path, token, body=None):
    req = urllib.request.Request(BASE+path, headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'},
                                 data=None if body is None else json.dumps(body).encode())
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as response:
            return response.status
    except urllib.error.HTTPError as error:
        return error.code


def kube_script(code, payload):
    args = ['pct','exec','306','--','docker','exec','-i','platform-uptime-kuma','node','-e',code]
    p = subprocess.run(['ssh','-o','BatchMode=yes','-o','ConnectTimeout=8','root@10.1.10.4',shlex.join(args)],
                       input=json.dumps(payload),text=True,capture_output=True,timeout=60)
    if p.returncode:
        safe=[line for line in p.stderr.splitlines() if line.startswith('Kuma acknowledgment failed') or line == 'Kuma rotation failed; private output suppressed']
        print(json.dumps({'consumer':'kuma','returncode':p.returncode,'diagnostic':safe}),file=__import__('sys').stderr)
        raise RuntimeError('Kuma consumer operation failed; credentials suppressed')
    return json.loads(p.stdout.strip().splitlines()[-1])


KUMA_INSPECT = """
const fs=require('fs'),crypto=require('crypto');
const db=new(require('@louislam/sqlite3').Database)('/app/data/kuma.db');
db.get('SELECT headers,active,url,method FROM monitor WHERE id=31',[],(e,r)=>{
 if(e||!r)process.exit(1);
 const h=JSON.parse(r.headers),t=h.Authorization.replace(/^Bearer /,'');
 console.log(JSON.stringify({sha256:crypto.createHash('sha256').update(t).digest('hex'),active:r.active,url:r.url,method:r.method}));db.close();});
"""


class Adapter:
    def __init__(self, lease): self.lease = lease; self.monitor_after = time.time()-120
    def read(self): self.lease.check(); return read()
    def save(self, updates): self.lease.check(); save(updates); self.lease.check()

    def accept(self, values):
        self.lease.check()
        current = json.loads(remote(VM, "import json,subprocess;d=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0];e=dict(x.split('=',1) for x in d['Config']['Env']);print(json.dumps({'identities':json.loads(e['CB_SERVICE_IDENTITIES']),'healthy':d['State']['Health']['Status']=='healthy'}))"))
        if current != {'identities':json.loads(values[IDENTITIES]),'healthy':True}:
            recreate(values)
        self.lease.check()

    def inventory(self, values):
        """Verify all known active consumers against the exact current authority."""
        self.check_consumers(values)
        self.verify_tokens(values)

    def verify_tokens(self, values, expected=200):
        for key, _, _, _ in SPECS:
            path = '/metrics' if key == 'CB_METRICS_PROBE_TOKEN' else '/api/v1/me'
            body = None
            status = expected
            if key == 'CB_OPENWEBUI_RETRIEVAL_TOKEN':
                path, body = '/retrieval/query', {'question':'community','top_k':1}
            if key == 'CB_PROD_MAC_COLLECTOR_TOKEN' and expected == 200:
                # Recognized credential with deliberately forbidden read scope;
                # anonymous/revoked credentials instead return 401. No upload.
                status = 403
            assert request(path, values[key], body) == status, 'Service identity authentication failed'
        if expected == 200:
            for key, _, _, _ in SPECS:
                path = '/api/v1/jobs' if key == 'CB_METRICS_PROBE_TOKEN' else '/metrics'
                assert request(path, values[key]) == 403, 'Cross-scope denial failed'
            assert request('/api/v1/jobs',values['CB_PROD_MAC_COLLECTOR_TOKEN']) == 403
            assert request('/api/v1/jobs',values['CB_PROD_MANUAL_OPERATOR_TOKEN']) == 200
            assert request('/retrieval/query',values['CB_OPENWEBUI_RETRIEVAL_TOKEN'],{'question':'community','top_k':1}) == 200

    def verify_overlap(self, journal):
        self.verify_tokens(journal['old'])
        self.verify_tokens(journal['updates'])

    def check_consumers(self, values):
        p = Path.home()/'Library/Application Support/CommunityBrainProduction/collector.json'
        config = json.loads(p.read_text())
        assert config['token'] == values['CB_PROD_MAC_COLLECTOR_TOKEN']
        assert config['expires_at'] == int(values['CB_PROD_MAC_COLLECTOR_EXPIRES_AT'])
        assert config['enabled'] and p.stat().st_mode & 0o777 == 0o600
        code = r'''import pathlib,shlex,sys,json,hashlib
d=json.load(sys.stdin);root=pathlib.Path('/etc/community-brain-production')
for filename,mapping in [('probes.env',{'CB_READ_PROBE_TOKEN':'CB_READ_PROBE_TOKEN','CB_METRICS_PROBE_TOKEN':'CB_METRICS_PROBE_TOKEN','CB_PROBE_EXPIRES_AT':'CB_PROBE_EXPIRES_AT'}),('manual-preparation/operator-client.env',{'CB_MANUAL_OPERATOR_TOKEN':'CB_PROD_MANUAL_OPERATOR_TOKEN','CB_MANUAL_OPERATOR_EXPIRES_AT':'CB_PROD_MANUAL_OPERATOR_EXPIRES_AT'}),('manual-preparation/collector-client.env',{'CB_COLLECTOR_TOKEN':'CB_PROD_MAC_COLLECTOR_TOKEN','CB_COLLECTOR_EXPIRES_AT':'CB_PROD_MAC_COLLECTOR_EXPIRES_AT'})]:
 p=root/filename;assert p.stat().st_mode&0o777==0o600
 v=dict(x.split('=',1) for x in shlex.split(p.read_text()))
 assert all(v[k]==d[src] for k,src in mapping.items()),'Client bundle mismatch'
print('verified')
'''
        bundle_keys={key for spec in SPECS[1:] for key in spec[:2]}
        assert remote(VM,code,{k:values[k] for k in bundle_keys}).strip() == 'verified'
        webui = r'''import subprocess,json
code="import sqlite3,json,hashlib; c=sqlite3.connect('file:/app/backend/data/webui.db?mode=ro',uri=True);r=c.execute(\"select valves,is_active,is_global from function where id='community_brain_filter'\").fetchone();v=json.loads(r[0]);print(json.dumps({'sha256':hashlib.sha256(v['api_key'].encode()).hexdigest(),'url':v['retrieval_url'],'active':r[1],'global':r[2]}))"
r=subprocess.run(['docker','exec','open-webui','python','-c',code],capture_output=True,text=True);assert r.returncode==0;print(r.stdout)
'''
        info = json.loads(remote('n8n-automation',webui))
        assert info == {'sha256':hashlib.sha256(values['CB_OPENWEBUI_RETRIEVAL_TOKEN'].encode()).hexdigest(),
                        'url':BASE+'/retrieval/query','active':1,'global':1}
        kuma = kube_script(KUMA_INSPECT,{})
        assert kuma['sha256'] == hashlib.sha256(values['CB_READ_PROBE_TOKEN'].encode()).hexdigest()
        assert kuma['active'] == 1 and kuma['url'] == BASE+'/retrieval/query' and kuma['method'] == 'POST'
        prom = json.loads(remote('monitoring-stack',"import pathlib,hashlib,json;p=pathlib.Path('/opt/monitoring-stack/config/prometheus/community-brain-private/metrics-token');print(json.dumps({'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mode':p.stat().st_mode&0o777}))"))
        assert prom == {'sha256':hashlib.sha256(values['CB_METRICS_PROBE_TOKEN'].encode()).hexdigest(),'mode':0o640}
        self.lease.check()

    def deliver(self, journal):
        self.lease.check()
        self.monitor_after = time.time()
        old, new = journal['old'],journal['updates']
        p = Path.home()/'Library/Application Support/CommunityBrainProduction/collector.json'
        config = json.loads(p.read_text())
        assert config['token'] in (old['CB_PROD_MAC_COLLECTOR_TOKEN'],new['CB_PROD_MAC_COLLECTOR_TOKEN'])
        config.update(token=new['CB_PROD_MAC_COLLECTOR_TOKEN'],expires_at=int(new['CB_PROD_MAC_COLLECTOR_EXPIRES_AT']))
        tmp=p.with_name('.collector.renewal.tmp');tmp.write_text(json.dumps(config,indent=2)+'\n');tmp.chmod(0o600);tmp.replace(p)
        code=r'''import sys,json,pathlib,shlex,os
d=json.load(sys.stdin);root=pathlib.Path('/etc/community-brain-production')
for name,mapping in [('probes.env',{'CB_READ_PROBE_TOKEN':'CB_READ_PROBE_TOKEN','CB_METRICS_PROBE_TOKEN':'CB_METRICS_PROBE_TOKEN','CB_PROBE_EXPIRES_AT':'CB_PROBE_EXPIRES_AT'}),('manual-preparation/operator-client.env',{'CB_MANUAL_OPERATOR_TOKEN':'CB_PROD_MANUAL_OPERATOR_TOKEN','CB_MANUAL_OPERATOR_EXPIRES_AT':'CB_PROD_MANUAL_OPERATOR_EXPIRES_AT'}),('manual-preparation/collector-client.env',{'CB_COLLECTOR_TOKEN':'CB_PROD_MAC_COLLECTOR_TOKEN','CB_COLLECTOR_EXPIRES_AT':'CB_PROD_MAC_COLLECTOR_EXPIRES_AT'})]:
 p=root/name;v=dict(x.split('=',1) for x in shlex.split(p.read_text()))
 assert all(v[k] in [d['old'][src],d['updates'][src]] for k,src in mapping.items())
 v.update({k:d['updates'][src] for k,src in mapping.items()})
 assert all("'" not in x and '\n' not in x for x in v.values())
 t=p.with_name('.'+p.name+'.renewal');t.write_text(''.join(k+"='"+x+"'\n" for k,x in v.items()));t.chmod(0o600);t.replace(p)
print('delivered')
'''
        bundle_keys={key for spec in SPECS[1:] for key in spec[:2]}
        payload={part:{k:journal[part][k] for k in bundle_keys} for part in ['old','updates']}
        assert remote(VM,code,payload).strip() == 'delivered'
        # Existing authenticated Open WebUI API updates the live filter cache.
        script=(ROOT/'renewal_webui_control.py').read_text()
        outer="SCRIPT="+repr(script)+"\n"+r'''import subprocess,sys,json
d=json.load(sys.stdin)
r=subprocess.run(['docker','exec','-i','open-webui','python','-c',SCRIPT],input=json.dumps(d),capture_output=True,text=True,timeout=90)
assert r.returncode==0,'OpenWebUI delivery failed'
result=json.loads(r.stdout);assert result['retrieval_status']=='ok' and result['context_emitted']
print(json.dumps({'live_app_process':result['live_app_process'],'retrieval_status':result['retrieval_status'],'context_emitted':result['context_emitted']}))
'''
        result=json.loads(remote('n8n-automation',outer,{'mode':'set','url':BASE+'/retrieval/query','token':new['CB_OPENWEBUI_RETRIEVAL_TOKEN']}))
        assert result['live_app_process'] and result['context_emitted']
        kuma_script=(ROOT/'renewal_kuma.js').read_text()
        kube_script(kuma_script,{'old':old['CB_READ_PROBE_TOKEN'],'token':new['CB_READ_PROBE_TOKEN'],'cycle':journal['cycle']})
        prom=r'''import pathlib,sys,json,os,subprocess
d=json.load(sys.stdin);p=pathlib.Path('/opt/monitoring-stack/config/prometheus/community-brain-private/metrics-token')
assert p.read_text() in [d['old'],d['token']]
if p.read_text()!=d['token']:
 t=p.with_name('.metrics-token.renewal');t.write_text(d['token']);os.chown(t,0,65534);t.chmod(0o640);t.replace(p)
subprocess.run(['docker','exec','prometheus','promtool','check','config','/etc/prometheus/prometheus.yml'],check=True,capture_output=True)
subprocess.run(['docker','kill','--signal=HUP','prometheus'],check=True,capture_output=True)
print('delivered')
'''
        assert remote('monitoring-stack',prom,{'old':old['CB_METRICS_PROBE_TOKEN'],'token':new['CB_METRICS_PROBE_TOKEN']}).strip()=='delivered'
        self.lease.check()

    def verify_consumers(self, journal):
        self.check_consumers(journal['updates'])
        self.verify_tokens(journal['updates'])
        deadline=time.monotonic()+100
        while True:
            self.lease.check()
            kuma=kube_script("const db=new(require('@louislam/sqlite3').Database)('/app/data/kuma.db');db.get('SELECT status,time FROM heartbeat WHERE monitor_id=31 ORDER BY id DESC LIMIT 1',[],(e,r)=>{if(e||!r)process.exit(1);console.log(JSON.stringify({status:r.status,at:Date.parse(r.time+'Z')/1000}));db.close();});",{})
            prom=json.loads(remote('monitoring-stack',"import urllib.request,json,datetime;r=json.load(urllib.request.urlopen('http://127.0.0.1:9090/api/v1/targets',timeout=10));print(json.dumps([{'health':t['health'],'at':datetime.datetime.fromisoformat(t['lastScrape'].replace('Z','+00:00')).timestamp()} for t in r['data']['activeTargets'] if t['scrapePool']=='community-brain-prod-api']))"))
            if kuma['status']==1 and kuma['at']>=self.monitor_after and len(prom)==1 and prom[0]['health']=='up' and prom[0]['at']>=self.monitor_after:
                break
            if time.monotonic()>=deadline:
                raise RuntimeError('Fresh consumer monitoring acceptance not observed; old acceptance retained')
            time.sleep(3)

    def verify_revoked(self, journal):
        self.verify_tokens(journal['old'],401)
