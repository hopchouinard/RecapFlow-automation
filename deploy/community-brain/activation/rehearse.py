"""Disposable VM108 activation rehearsal; no production data or provider access."""
import fcntl
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
from contextlib import ExitStack
from activate import Activation, Docker, atomic, command, digest, fingerprint, preserved, validate_plan

ROOT = Path('/srv/dev-data/workspaces/cbm-activation-validation-20260921')
SOURCE = Path(__file__).resolve().parent
IMAGE = 'sha256:6e7f43ebd7970f89ae9f1afe5d4d77b89448e188e4a580ff9e38bac923d5bc5b'
WEBUI = 'sha256:08046b9748558bc2747dd20c9c77fc0e6b05216b8ad33513e7a9152cea15b87b'
PG = 'sha256:4ef4dbc939d61acea57712655ddb4b4ab27419c913f94cca0cd57cb3ea3c2280'
NETWORK = 'cbm-activation-validation'
PREFIX = 'cbm-activation-validation-'
engine = Docker()


def expected(spec, service, port):
    binds = sorted([{'source': m['source'], 'target': m['target'], 'read_only': m['read_only']}
                    for m in spec.get('volumes', []) if m['type'] == 'bind'], key=lambda m: m['target'])
    volumes = [{'name': PREFIX+'webui-data', 'target': '/app/backend/data', 'read_only': False}] if service == 'webui' else []
    mapping = {'8090/tcp': [{'HostIp': '127.0.0.1', 'HostPort': '19929'}]} if service == 'api' else {}
    return {'service': service, 'container': spec['container_name'], 'image': spec['image'],
            'network': NETWORK, 'probe_port': port, 'health_timeout': 180,
            'runtime': {'memory': spec['mem_limit'], 'nano_cpus': int(spec['cpus']*1000000000),
                        'read_only_root': spec.get('read_only', False), 'user': spec.get('user', ''),
                        'command': spec.get('command', ['bash', 'start.sh']), 'ports': mapping,
                        'binds': binds, 'volumes': volumes}}


def setup(resume=False):
    if socket.gethostname() != 'community-brain-dev' or os.geteuid() != 0:
        raise ValueError('VM108 root only')
    os.umask(0o077)
    private, state = ROOT/'private', ROOT/'state'
    if not resume:
        private = ROOT/'private'; private.mkdir(mode=0o700)  # Never replay setup.
        state = ROOT/'state'
        for name in ['files','config','corpus','meeting-archive','automation-public','automation']:
            p = state/name; p.mkdir(parents=True); os.chown(p,10001,10001)
        for name in ('automation/runner.lock','files/.manual-worker.lock','files/.submission.lock'):
            (state/name).touch(mode=0o600)
        for name in ('paused','attention.json','boot-state.json'):
            (state/'automation'/name).write_text(json.dumps({'reconciled':False,'reason':'synthetic activation hold'}))
        (state/'files/synthetic-preserved.txt').write_text('Keep the prior synthetic artifact.\n')
        token = secrets.token_urlsafe(32)
        identities = [{'sha256':digest(token.encode()),'expires_at':time.time()+7200,
                       'subject':'activation-fixture','scope':'community-brain','permissions':['jobs:read','artifacts:read']}]
        api_env = {'CB_DATABASE_URL':'postgresql+psycopg://fixture@pg/activation',
                   'CB_STORAGE_ROOT':'/state/files','CB_PIPELINE_CONFIG_DIR':'/state/config',
                   'CB_CORPUS_ROOT':'/state/corpus','CB_OIDC_ISSUER':'https://fixture.invalid',
                   'CB_OIDC_AUDIENCE':'fixture','CB_OIDC_CLIENT_ID':'fixture','CB_OIDC_JWKS_URL':'https://fixture.invalid/jwks',
                   'CB_SERVICE_IDENTITIES':json.dumps(identities),'CB_CORPUS_SCOPE':'community-brain',
                   'CB_AUTOMATIC_PROCESSING':'true','CB_AUTOMATION_ROOT':'/state/automation-public',
                   'CB_ENABLE_MODEL_CALLS':'false','CB_ENABLE_NETWORK_PUBLICATION':'false',
                   'PYTHONDONTWRITEBYTECODE':'1'}
        (private/'api.env').write_text(''.join(k+'='+v+'\n' for k,v in api_env.items()))
        (private/'token').write_text(token)
        web_env = {'WEBUI_SECRET_KEY':secrets.token_urlsafe(48),'WEBUI_AUTH':'true','ENABLE_SIGNUP':'false',
                   'OFFLINE_MODE':'true','HF_HUB_OFFLINE':'1','TRANSFORMERS_OFFLINE':'1',
                   'ENABLE_OLLAMA_API':'false','ENABLE_OPENAI_API':'false','RAG_EMBEDDING_ENGINE':'ollama',
                   'ANONYMIZED_TELEMETRY':'false','DO_NOT_TRACK':'true','SCARF_NO_ANALYTICS':'true'}
        (private/'webui.env').write_text(''.join(k+'='+v+'\n' for k,v in web_env.items()))
        (private/'ca.pem').write_bytes(Path('/etc/ssl/certs/ca-certificates.crt').read_bytes())
        command(['docker','network','create','--internal',NETWORK])
        command(['docker','volume','create',PREFIX+'webui-data'])
        command(['docker','run','-d','--name',PREFIX+'pg','--network',NETWORK,'--network-alias','pg',
                 '--memory','192m','--tmpfs','/var/lib/postgresql','-e','POSTGRES_USER=fixture',
                 '-e','POSTGRES_DB=activation','-e','POSTGRES_HOST_AUTH_METHOD=trust',PG])
        for _ in range(60):
            p = subprocess.run(['docker','exec',PREFIX+'pg','pg_isready','-U','fixture','-d','activation'],capture_output=True)
            if p.returncode == 0: break
            time.sleep(1)
    else:
        if (ROOT/'plan-v3.json').exists() or (ROOT/'candidate.json').exists():
            raise ValueError('setup has progressed past the schema boundary')
        count = command(['docker','exec',PREFIX+'pg','psql','-U','fixture','-d','activation','-Atc',
                         "select count(*) from information_schema.tables where table_schema = 'public'"])
        if count.strip() != b'0': raise ValueError('schema exists; reconcile before resume')
    command(['docker','run','--rm','--network',NETWORK,'--env-file',str(private/'api.env'),IMAGE,
             'python','-B','-c',"import os; from sqlalchemy import create_engine; from community_brain.jobs.models import Base; Base.metadata.create_all(create_engine(os.environ['CB_DATABASE_URL']))"])
    backup = ROOT/'recovery'; backup.mkdir(mode=0o700)
    (backup/'database.sql').write_bytes(command(['docker','exec',PREFIX+'pg','pg_dump','-U','fixture','activation']))
    (backup/'synthetic-preserved.txt').write_bytes((state/'files/synthetic-preserved.txt').read_bytes())
    # Verify the snapshot by restoring it into a distinct disposable DB.
    command(['docker','exec',PREFIX+'pg','createdb','-U','fixture','restore_check'])
    p = subprocess.run(['docker','exec','-i',PREFIX+'pg','psql','-v','ON_ERROR_STOP=1','-U','fixture','restore_check'],
                       input=(backup/'database.sql').read_bytes(),capture_output=True)
    if p.returncode: raise RuntimeError('development recovery verification failed')
    atomic(backup/'receipt.json', {'verified':True,'state_root':str(state),'synthetic_only':True,
                                 'database_sha256':digest((backup/'database.sql').read_bytes()),
                                 'artifact_sha256':digest((backup/'synthetic-preserved.txt').read_bytes())})
    mounts = [{'type':'bind','source':str(state/n),'target':'/state/'+n,'read_only':n!='files'}
              for n in ('files','config','corpus','meeting-archive','automation-public')]
    mounts.append({'type':'bind','source':str(private/'ca.pem'),'target':'/run/certs/ca-bundle.pem','read_only':True})
    api = {'container_name':PREFIX+'api','image':IMAGE,'read_only':True,'user':'10001:10001',
           'cap_drop':['ALL'],'security_opt':['no-new-privileges:true'],'tmpfs':['/tmp:uid=10001,gid=10001'],
           'volumes':mounts,'env_file':[str(private/'api.env')],'mem_limit':2147483648,'cpus':2,
           'ports':['127.0.0.1:19929:8090'],
           'command':['python','-B','-m','uvicorn','community_brain.jobs.runtime:app','--factory',
                      '--host','0.0.0.0','--port','8090','--no-access-log']}
    webui = {'container_name':PREFIX+'webui','image':WEBUI,'user':'0:0','env_file':[str(private/'webui.env')],
             'mem_limit':1610612736,'cpus':1.5,'cap_drop':['ALL'],'security_opt':['no-new-privileges:true'],
             'volumes':[{'type':'volume','source':'webui','target':'/app/backend/data','read_only':False}]}
    compose = {'name':'cbm-activation-candidate','services':{'api':api,'webui':webui},
               'networks':{'default':{'external':True,'name':NETWORK}},
               'volumes':{'webui':{'external':True,'name':PREFIX+'webui-data'}}}
    atomic(ROOT/'candidate.json',compose)
    old = json.loads(json.dumps(compose));old['name']='cbm-activation-incumbent'
    old['services']={'api':{**api,'container_name':PREFIX+'incumbent'}}
    atomic(ROOT/'incumbent.json',old)
    command(['docker','compose','-f',str(ROOT/'incumbent.json'),'up','-d','--no-build','--pull','never'])
    baseline = engine.inspect(PREFIX+'incumbent');engine.health(baseline,{'network':NETWORK,'probe_port':8090})
    files = [SOURCE/'activate.py',ROOT/'candidate.json',private/'api.env',private/'webui.env',private/'ca.pem',backup/'receipt.json']
    plan = {'schema':1,'phase':'serving-only','hostname':'community-brain-dev','state_root':str(state),
            'compose':str(ROOT/'candidate.json'),'recovery_receipt':str(backup/'receipt.json'),
            'files':{str(p):digest(p.read_bytes()) for p in files},
            'locks':[str(state/n) for n in ('automation/runner.lock','files/.manual-worker.lock','files/.submission.lock')],
            'holds':[str(state/'automation'/n) for n in ('paused','attention.json','boot-state.json')],
            'incumbent':{'container':PREFIX+'incumbent','id':baseline['Id'],'fingerprint':fingerprint(baseline),
                         'network':NETWORK,'probe_port':8090},
            'candidates':[expected(api,'api',8090),expected(webui,'webui',8080)]}
    atomic(ROOT/'plan-v3.json',plan)
    print(json.dumps({'setup':True,'plan_sha256':digest((ROOT/'plan-v3.json').read_bytes())}))


def exercise():
    identity = digest((ROOT/'plan-v3.json').read_bytes())
    plan = validate_plan(ROOT/'plan-v3.json',identity)
    initial_holds = preserved(plan)
    cli = ['python3','-B',str(SOURCE/'activate.py')]
    args = [str(ROOT/'plan-v3.json'),identity,str(ROOT/'journal-v3.json')]
    with open(plan['locks'][0],'r+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        blocked = subprocess.run([*cli,'activate',*args],capture_output=True)
        if blocked.returncode == 0 or (ROOT/'journal-v3.json').exists():raise AssertionError('runner lock did not exclude activation')
    class LostAcknowledgment(Docker):
        def create(self, plan, target):
            super().create(plan,target)
            raise RuntimeError('synthetic lost acknowledgment after Docker creation')
    with ExitStack() as stack:
        for name in plan['locks']:
            f = stack.enter_context(open(name,'r+'));fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
        try: Activation(plan,identity,ROOT/'journal-v3.json',LostAcknowledgment()).activate()
        except RuntimeError as error:
            if str(error)!='synthetic lost acknowledgment after Docker creation':raise
        else: raise AssertionError('failure injection missing')
    candidate_before = engine.inspect(plan['candidates'][0]['container'])['Id']
    result = json.loads(command([*cli,'activate',*args]))
    if engine.inspect(plan['candidates'][0]['container'])['Id'] != candidate_before: raise AssertionError('uncertain create was replayed')
    ids = {t['container']:engine.inspect(t['container'])['Id'] for t in plan['candidates']}
    command([*cli,'activate',*args])
    if ids != {t['container']:engine.inspect(t['container'])['Id'] for t in plan['candidates']}:raise AssertionError('duplicate activation recreated targets')
    api = engine.inspect(plan['candidates'][0]['container']);ip=api['NetworkSettings']['Networks'][NETWORK]['IPAddress']
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    request = urllib.request.Request('http://'+ip+':8090/api/v1/me',headers={'Authorization':'Bearer '+(ROOT/'private/token').read_text()})
    with opener.open(request) as response:
        if response.status!=200:raise AssertionError('authenticated API failed')
    try:opener.open('http://'+ip+':8090/api/v1/me')
    except urllib.error.HTTPError as error:
        if error.code!=401:raise
    else:raise AssertionError('anonymous API unexpectedly accepted')
    command(['docker','exec',plan['candidates'][1]['container'],'python','-B','-c',"from pathlib import Path; Path('/app/backend/data/activation-preserved.txt').write_text('synthetic post-activation write')"])
    result_rollback=json.loads(command([*cli,'rollback',*args]))
    command(['docker','run','--rm','--network','none','-v',PREFIX+'webui-data:/restore:ro',IMAGE,'python','-B','-c',"from pathlib import Path; assert Path('/restore/activation-preserved.txt').read_text()=='synthetic post-activation write'"])
    if preserved(plan)!=initial_holds:raise AssertionError('holds changed')
    if (ROOT/'state/files/synthetic-preserved.txt').read_bytes()!=(ROOT/'recovery/synthetic-preserved.txt').read_bytes():raise AssertionError('prior artifact changed')
    original=engine.inspect(plan['incumbent']['container'])
    if original['Id']!=plan['incumbent']['id'] or not original['State']['Running']:raise AssertionError('incumbent recovery failed')
    evidence={'passed':True,'activation':result,'rollback':result_rollback,'runner_lock_exclusion':True,
              'lost_acknowledgment_no_recreate':True,'duplicate_activation_no_recreate':True,
              'actual_api_authentication':True,'anonymous_api_denied':True,'actual_webui_health':True,
              'post_activation_webui_write_preserved':True,'same_incumbent_container_restored':True,
              'plan_sha256':identity,'synthetic_data_only':True,'production_changed':False}
    atomic(ROOT/'result.json',evidence);print(json.dumps(evidence))


if __name__=='__main__':
    {'setup':setup,'resume-setup':lambda:setup(True),'exercise':exercise}[sys.argv[1]]()
