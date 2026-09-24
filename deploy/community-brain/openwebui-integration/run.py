"""VM108 integration only. Private fixture authority is NOT an Infisical adapter."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import sys
import time
import urllib.request
import urllib.error

from service_renewal_policy import SPECS, IDENTITIES, PENDING, run as renew

ROOT=Path('/srv/dev-data/workspaces/cbm-openwebui-integration-20260920')
SOURCE=ROOT/'source'
PRIVATE=ROOT/'private'
COMPOSE=['docker','compose','-f',str(ROOT/'compose.yml')]
IMAGE='sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b'
OPENER=urllib.request.build_opener(urllib.request.ProxyHandler({}))


def command(args):
    p=subprocess.run(args,capture_output=True,text=True,timeout=180)
    if p.returncode:raise RuntimeError('development operation failed; output suppressed')
    return p.stdout.strip()


def atomic(path,value):
    p=path.with_suffix('.tmp');p.write_text(json.dumps(value,indent=2)+'\n');p.chmod(0o600);p.replace(path)


def container(service):return command(COMPOSE+['ps','-aq',service])
def address(service,port):
    row=json.loads(command(['docker','inspect',container(service)]))[0]
    networks=row['NetworkSettings']['Networks'];assert set(networks)=={'cbm-integration-dev_default'}
    return 'http://'+networks['cbm-integration-dev_default']['IPAddress']+':'+str(port)


def call(path,token=None,body=None):
    headers={'Content-Type':'application/json'}
    if token:headers['Authorization']='Bearer '+token
    req=urllib.request.Request(address('api',8090)+path,headers=headers,data=None if body is None else json.dumps(body).encode())
    try:
        with OPENER.open(req,timeout=30) as r:return r.status,json.load(r) if path!='/metrics' else r.read().decode()
    except urllib.error.HTTPError as e:return e.code,None


def ready_api():
    for _ in range(90):
        try:
            if call('/health')[0]==200:return
        except (OSError,ValueError):pass
        time.sleep(1)
    raise RuntimeError('development API readiness timeout')


def lib():
    spec=importlib.util.spec_from_file_location('rehearse',SOURCE/'rehearse.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    m.ROOT=ROOT;m.SOURCE=SOURCE;m.WEBUI=container('webui');m.BASE=address('webui',8080)
    m.RETRIEVAL='http://api:8090/retrieval/query'
    m.call.__defaults__=(None,None,m.BASE)
    sys.modules['rehearse']=m
    return m


def render(values):
    env={'CB_DATABASE_URL':'postgresql+psycopg://fixture@pg/integration',
         'CB_STORAGE_ROOT':'/state/files','CB_PIPELINE_CONFIG_DIR':'/state/config',
         'COMMUNITY_BRAIN_CONFIG_DIR':'/state/config','CB_CORPUS_ROOT':'/state/corpus',
         'LANCEDB_PATH':'/state/corpus/lancedb/nomic-v1','CB_CORPUS_SCOPE':'community-brain',
         'CB_OIDC_ISSUER':'https://fixture.invalid','CB_OIDC_AUDIENCE':'fixture',
         'CB_OIDC_CLIENT_ID':'fixture','CB_OIDC_JWKS_URL':'https://fixture.invalid/jwks',
         'CB_SERVICE_IDENTITIES':values[IDENTITIES],'CB_ENABLE_RETRIEVAL':'true',
         'COMMUNITY_BRAIN_DISTRIBUTION_MODE':'true','OLLAMA_BASE_URL':'http://provider:8999',
         'CB_ENABLE_MODEL_CALLS':'false','CB_ENABLE_NETWORK_PUBLICATION':'false',
         'CB_WEB_DIST':'/app/web/dist','CB_AUTOMATIC_PROCESSING':'false'}
    p=PRIVATE/'api.env';t=p.with_suffix('.tmp')
    assert all('\n' not in v and "'" not in v for v in env.values())
    t.write_text(''.join(k+"='"+v+"'\n" for k,v in env.items()));t.chmod(0o600);t.replace(p)


def setup():
    assert not PRIVATE.exists(),'existing private state: inspect before continuation'
    PRIVATE.mkdir(mode=0o700)
    values={};records=[];expiry=int(time.time())+7*86400
    for key,exp,subject,permissions in SPECS:
        values[key]=secrets.token_urlsafe(48);values[exp]=str(expiry)
        records.append({'subject':subject,'scope':'community-brain','permissions':permissions,
                        'expires_at':expiry,'sha256':hashlib.sha256(values[key].encode()).hexdigest()})
    values[IDENTITIES]=json.dumps(records)
    atomic(PRIVATE/'authority.json',values)
    atomic(PRIVATE/'clients.json',{key:values[key] for key,*_ in SPECS})
    atomic(PRIVATE/'credentials.json',{'email':'integration@example.invalid','password':secrets.token_urlsafe(32),
                                     'old':values[SPECS[0][0]],'new':values[SPECS[0][0]]})
    render(values)
    env={'WEBUI_SECRET_KEY':secrets.token_urlsafe(48),'WEBUI_AUTH':'true','ENABLE_SIGNUP':'true',
         'OFFLINE_MODE':'true','HF_HUB_OFFLINE':'1','TRANSFORMERS_OFFLINE':'1',
         'ENABLE_OLLAMA_API':'false','ENABLE_OPENAI_API':'true',
         'OPENAI_API_BASE_URL':'http://provider:8999/v1','OPENAI_API_KEY':secrets.token_urlsafe(24),
         'RAG_EMBEDDING_ENGINE':'ollama','OLLAMA_BASE_URL':'http://provider:8999',
         'ANONYMIZED_TELEMETRY':'false','DO_NOT_TRACK':'true','SCARF_NO_ANALYTICS':'true'}
    p=PRIVATE/'webui.env';p.write_text(''.join(k+'='+v+'\n' for k,v in env.items()));p.chmod(0o600)
    command(COMPOSE+['up','-d','pg','provider'])
    # Fresh volume ownership only; no existing fixture/production volume touched.
    command(COMPOSE+['run','--rm','--no-deps','--user','0:0','--cap-add','CHOWN','api','python','-c',
                     "import os;os.chown('/state',10001,10001)"])
    command(COMPOSE+['run','--rm','api','python','-B','/source/seed.py'])
    command(COMPOSE+['up','-d','api','webui']);ready_api();lib().ready()
    print('Isolated application and WebUI ready')


def webui_install():
    m=lib();m.ready();state=json.loads((PRIVATE/'credentials.json').read_text())
    marker=PRIVATE/'install-started';assert not marker.exists();marker.touch(mode=0o600)
    m.api('POST','/api/v1/auths/signup',{'name':'Integration fixture','email':state['email'],'password':state['password']})
    token=m.login(state)
    for fid,name in [('community_brain_filter','community_brain_filter.py'),('cbm_request026_probe','probe_action.py')]:
        m.api('POST','/api/v1/functions/create',{'id':fid,'name':fid,'content':(SOURCE/name).read_text(),'meta':{}},token)
    m.api('POST','/api/v1/functions/id/community_brain_filter/toggle',token=token)
    m.api('POST','/api/v1/functions/id/community_brain_filter/toggle/global',token=token)
    valves=m.api('GET','/api/v1/functions/id/community_brain_filter/valves',token=token)
    valves.update(retrieval_url=m.RETRIEVAL,api_key=state['old'])
    m.api('POST','/api/v1/functions/id/community_brain_filter/valves/update',valves,token)
    result=m.probe(token,state['old']);assert result['source_count']==1
    status,body=call('/retrieval/query',state['old'],{'question':'Synthetic migration question','top_k':1})
    assert status==200 and body['chunks'][0]['ground_truth']['chunk_id']=='integration-synthetic-001'
    assert call('/api/v1/jobs',state['old'])[0]==403
    assert call('/retrieval/query','unknown-token',{'question':'synthetic'})[0]==401
    atomic(ROOT/'real-retrieval.json',{'passed':True,'actual_api_factory':True,'actual_lancedb_fts':True,
        'actual_webui_filter_cache':True,'expected_source_id_verified':True,'embedding_provider':'deterministic isolated fixture',
        'external_calls':0,'production_changes':False})
    print('Real Community Brain retrieval through WebUI passed')


class Adapter:
    def __init__(self,fail=False):self.fail=fail;self.recreations=0
    def read(self):return json.loads((PRIVATE/'authority.json').read_text())
    def save(self,updates):atomic(PRIVATE/'authority.json',{**self.read(),**updates})
    def accept(self,values):
        render(values);command(COMPOSE+['up','-d','--no-deps','--force-recreate','api']);ready_api()
        row=json.loads(command(['docker','inspect',container('api')]))[0]
        assert row['Image']==IMAGE
        assert not any('/site-packages/' in x['Destination'] or x['Destination']=='/app/web/dist' for x in row['Mounts'])
        self.recreations+=1
    def verify_tokens(self,values,revoked=False):
        for key,_,_,_ in SPECS:
            path='/metrics' if key=='CB_METRICS_PROBE_TOKEN' else '/api/v1/me'
            body=None;expected=200
            if key=='CB_OPENWEBUI_RETRIEVAL_TOKEN':path='/retrieval/query';body={'question':'synthetic'}
            if key=='CB_PROD_MAC_COLLECTOR_TOKEN':expected=403
            assert call(path,values[key],body)[0]==(401 if revoked else expected)
    def inventory(self,values):
        clients=json.loads((PRIVATE/'clients.json').read_text())
        assert all(clients[k]==values[k] for k,*_ in SPECS)
        self.verify_tokens(values);self.cache(values['CB_OPENWEBUI_RETRIEVAL_TOKEN'])
    def cache(self,token):
        m=lib();state=json.loads((PRIVATE/'credentials.json').read_text())
        result=m.probe(m.login(state),token);assert result['source_count']==1
    def verify_overlap(self,journal):
        self.verify_tokens(journal['old']);self.verify_tokens(journal['updates'])
    def deliver(self,journal):
        m=lib();state=json.loads((PRIVATE/'credentials.json').read_text());token=m.login(state)
        valves=m.api('GET','/api/v1/functions/id/community_brain_filter/valves',token=token)
        key='CB_OPENWEBUI_RETRIEVAL_TOKEN'
        assert valves['api_key'] in (journal['old'][key],journal['updates'][key])
        assert valves['retrieval_url']==m.RETRIEVAL
        valves['api_key']=journal['updates'][key]
        m.api('POST','/api/v1/functions/id/community_brain_filter/valves/update',valves,token)
        self.cache(journal['updates'][key])
        if self.fail:
            self.fail=False;raise RuntimeError('synthetic lost delivery acknowledgment')
        atomic(PRIVATE/'clients.json',{k:journal['updates'][k] for k,*_ in SPECS})
    def verify_consumers(self,journal):
        clients=json.loads((PRIVATE/'clients.json').read_text())
        assert all(clients[k]==journal['updates'][k] for k,*_ in SPECS)
        self.verify_tokens(journal['updates']);self.cache(journal['updates']['CB_OPENWEBUI_RETRIEVAL_TOKEN'])
    def verify_revoked(self,journal):self.verify_tokens(journal['old'],True)


def renewal():
    assert (ROOT/'real-retrieval.json').exists()
    marker=PRIVATE/'renewal-started';assert not marker.exists();marker.touch(mode=0o600)
    adapter=Adapter(fail=True)
    try:renew(adapter,time.time(),force=True)
    except RuntimeError as error:assert str(error)=='synthetic lost delivery acknowledgment'
    else:raise AssertionError('lost acknowledgment not exercised')
    journal=json.loads(adapter.read()[PENDING]);assert journal['phase']=='overlap_verified'
    assert len(json.loads(adapter.read()[IDENTITIES]))==10
    adapter.verify_overlap(journal)
    result=renew(adapter,time.time());assert result['cycle']==journal['cycle']
    assert len(json.loads(adapter.read()[IDENTITIES]))==5
    state=json.loads((PRIVATE/'credentials.json').read_text())
    state['new']=adapter.read()['CB_OPENWEBUI_RETRIEVAL_TOKEN'];atomic(PRIVATE/'credentials.json',state)
    m=lib();m.docker('restart',m.WEBUI);m.ready();adapter.cache(state['new'])
    atomic(ROOT/'renewal.json',{'passed':True,'subjects':5,'lost_delivery_acknowledgment':True,
        'overlap_retained_and_verified':True,'same_generation_resumed':True,'old_credentials_rejected':True,
        'api_recreations':adapter.recreations,'stabilization_image_and_unoverlaid_modules_preserved':True,
        'new_cache_after_restart':True,'authority':'private development file fixture; not Infisical',
        'other_consumers':'development credential bundles; not actual Kuma/Prometheus/Mac collector',
        'production_renderer_validated':False,'production_changes':False})
    print('Five-identity policy and actual API/WebUI renewal passed; authority/other consumers are fixtures')



def data_module():
    lib()
    spec=importlib.util.spec_from_file_location('integration_data',SOURCE/'data_recovery.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def tree(path):
    result={}
    for p in sorted(path.rglob('*')):
        if p.is_symlink():
            assert p.resolve().is_relative_to(path.resolve()), 'link escapes fixture volume'
            result[str(p.relative_to(path))]={'type':'symlink','target':os.readlink(p)}
        elif p.is_file():result[str(p.relative_to(path))]={'type':'file','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    return result


def restore():
    assert (ROOT/'renewal.json').exists()
    marker=PRIVATE/'restore-started';assert not marker.exists();marker.touch(mode=0o600)
    # Existing Request026 data helper requires its prior acceptance marker.
    atomic(ROOT/'acceptance.json',{'integration_renewal_passed':True})
    data_module().main()
    vector_code="import chromadb; c=chromadb.PersistentClient(path='/app/backend/data/vector_db'); t=c.create_collection('integration_restore'); t.add(ids=['synthetic-vector'],embeddings=[[1.0,0.0,0.0]],documents=['Synthetic vector restore']); assert t.count()==1"
    command(['docker','exec',container('webui'),'python','-c',vector_code])
    command(COMPOSE+['stop','webui'])
    restore_volume()


def restore_volume():
    assert (PRIVATE/'restore-started').exists() and (ROOT/'data-recovery-acceptance.json').exists()
    assert not (PRIVATE/'webui-backup.tar').exists(), 'inspect existing backup before continuation'
    row=json.loads(command(['docker','inspect',container('webui')]))[0]
    assert row['State']['Status']=='exited'
    mount,=[m for m in row['Mounts'] if m['Destination']=='/app/backend/data']
    assert mount['Name']=='cbm-integration-dev_webui'
    original=Path(mount['Source']);before=tree(original)
    archive=PRIVATE/'webui-backup.tar'
    command(['tar','--numeric-owner','-C',str(original),'-cpf',str(archive),'.']);archive.chmod(0o600)
    restored='cbm-integration-dev_restored'
    assert subprocess.run(['docker','volume','inspect',restored],capture_output=True).returncode!=0
    command(['docker','volume','create',restored])
    target=Path(json.loads(command(['docker','volume','inspect',restored]))[0]['Mountpoint'])
    command(['tar','--numeric-owner','-C',str(target),'-xpf',str(archive)])
    assert tree(target)==before
    override=ROOT/'compose.restore.yml'
    override.write_text('services:\n  webui:\n    volumes: [restored:/app/backend/data]\nvolumes:\n  restored:\n    external: true\n    name: '+restored+'\n')
    signing_hash=hashlib.sha256((PRIVATE/'webui.env').read_bytes()).hexdigest()
    command(COMPOSE+['-f',str(override),'up','-d','--no-deps','--force-recreate','webui'])
    lib().ready();data_module().verify()
    verify_vector="import chromadb; c=chromadb.PersistentClient(path='/app/backend/data/vector_db'); t=c.get_collection('integration_restore'); assert t.count()==1; assert t.query(query_embeddings=[[1.0,0.0,0.0]],n_results=1)['ids']==[['synthetic-vector']]"
    command(['docker','exec',container('webui'),'python','-c',verify_vector])
    assert tree(original)==before
    assert hashlib.sha256((PRIVATE/'webui.env').read_bytes()).hexdigest()==signing_hash
    atomic(ROOT/'restore.json',{'passed':True,'fresh_volume':True,'files_hash_matched_before_start':len(before),
        'original_volume_unchanged':True,'external_signing_material_preserved':True,
        'login_chat_upload_models_prompts_verified':True,'chroma_query_verified':True,
        'actual_filter_real_backend_after_restore':True,'synthetic_data_only':True,'production_changes':False})
    print('Fresh-volume application and Chroma restore passed')


def load(label="load"):
    from concurrent.futures import ThreadPoolExecutor
    import threading
    assert (ROOT/'restore.json').exists()
    marker=PRIVATE/(label+'-started');assert not marker.exists();marker.touch(mode=0o600)
    samples=[];stop=threading.Event()
    def sample():
        while not stop.is_set():
            raw=command(['docker','stats','--no-stream','--format','{{json .}}',container('api'),container('webui')])
            stats=json.loads('['+raw.replace('}\n{','},{')+']')
            available=next(int(x.split()[1]) for x in Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemAvailable:'))
            samples.append({'available_kib':available,'containers':[{k:r[k] for k in ('Name','MemUsage','CPUPerc')} for r in stats]})
            stop.wait(1)
    thread=threading.Thread(target=sample);thread.start()
    values=json.loads((PRIVATE/'authority.json').read_text())
    token=values['CB_OPENWEBUI_RETRIEVAL_TOKEN']
    m=lib();state=json.loads((PRIVATE/'credentials.json').read_text());user=m.login(state)
    latencies=[]
    deadline=time.monotonic()+90
    def exercise(_):
        while time.monotonic()<deadline:
            start=time.monotonic()
            status,body=call('/retrieval/query',token,{'question':'Synthetic migration question'})
            assert status==200 and body['chunks'][0]['ground_truth']['chunk_id']=='integration-synthetic-001'
            assert m.probe(user,token)['source_count']==1
            latencies.append(time.monotonic()-start)
    try:
        with ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(exercise,range(3)))
    finally:stop.set();thread.join()
    assert samples
    rows=json.loads(command(['docker','inspect',container('api'),container('webui')]))
    assert all(not r['State']['OOMKilled'] and r['State']['Running'] for r in rows)
    atomic(ROOT/(label+'.json'),{'passed':True,'concurrent_clients':3,'request_pairs':len(latencies),
        'max_pair_seconds':max(latencies),'samples':samples,'oom_killed':False,
        'scope':'synthetic retrieval/filter load; pipeline overlap recorded separately',
        'production_scale_or_provider_latency_certified':False})
    print('Concurrent real retrieval/filter load passed')


def main():
    os.umask(0o077)
    assert socket.gethostname()=='community-brain-dev' and os.geteuid()==0 and Path('/srv/dev-data').is_mount()
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['setup','install','renewal','restore','restore-volume','load','load-extended','inspect'])
    args=parser.parse_args()
    if args.mode=='inspect':
        print(json.dumps({p.name:json.loads(p.read_text()) for p in ROOT.glob('*.json')}))
    else:{'setup':setup,'install':webui_install,'renewal':renewal,'restore':restore,'restore-volume':restore_volume,'load':load,'load-extended':lambda:load('load-extended')}[args.mode]()

if __name__=='__main__':main()
