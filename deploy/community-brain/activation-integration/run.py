"""Shared host contract. Every operation verifies the externally pinned packet."""
import json,os,shlex,subprocess,time,uuid
from pathlib import Path
from runtime_contract import load
from profiles import API_IMAGE
HERE=Path(__file__).resolve().parent
IMAGE=API_IMAGE

def contract():return load(os.environ['CBM_PACKET_SHA256'])

def read_env(name):
    value=contract()
    if name not in {'api.env','worker.env','webui.env',value['provider']['acquisition_file'],value['provider']['model_file']}:raise ValueError('unexpected private environment')
    p=Path(value['private'])/name
    assert not p.is_symlink() and p.stat().st_mode&0o777==0o600
    return dict(x.split('=',1) for x in shlex.split(p.read_text()))

def worker_environment():
    value=contract();q=value['queue']
    return {'PATH':os.defpath,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':'/packet:/packet/workers:/packet/fixture/worker_support',
      'CB_DATABASE_URL':read_env('api.env')['CB_DATABASE_URL'],'CB_STORAGE_ROOT':'/state/files',
      'CB_PIPELINE_CONFIG_DIR':'/state/config','COMMUNITY_BRAIN_CONFIG_DIR':'/state/config','CB_CORPUS_ROOT':'/state/corpus',
      'CB_ENABLE_NETWORK_PUBLICATION':'false','CB_RUNTIME_PROFILE':value['profile'],
      'CB_NATS_URL':q['url'],'CB_NATS_STREAM':q['stream'],'CB_NATS_SUBJECT':q['subject'],'CB_NATS_INBOX':q['inbox'],
      'OLLAMA_BASE_URL':value['provider']['ollama_url'],'SSL_CERT_FILE':'/run/certs/ca-bundle.pem'}

def container_args(*,indexing=False):
    v=contract();root=v['root']
    args=['docker','run','--rm','--read-only','--network',v['network'],'--tmpfs','/tmp:uid=10001,gid=10001',
      '--user','10001:10001','--cap-drop','ALL','--security-opt','no-new-privileges',
      '--memory',str(v['worker_memory']),'--cpus',str(v['worker_cpus']),
      '-v',str(HERE)+':/packet:ro','-v',root+'/files:/state/files:rw',
      '-v',root+'/config:/state/config:'+('rw' if indexing else 'ro'),
      '-v',root+'/corpus:/state/corpus:'+('rw' if indexing else 'ro'),
      '-v',next(m['source'] for m in v['api_mounts'] if m['target']=='/run/certs/ca-bundle.pem')+':/run/certs/ca-bundle.pem:ro']
    if v['profile']=='development':args+=['-v',v['private']+'/queue-ca.pem:/run/certs/queue-ca.pem:ro']
    return args

def invoke(args,env,command,*,timeout=240,log=None):
    for key in env:
        if key!='PATH':args+=['-e',key]
    args+=[IMAGE,*command]
    evidence=Path(contract()['runtime_evidence']);evidence.mkdir(mode=0o700,exist_ok=True)
    cidfile=evidence/(str(uuid.uuid4())+'.cid');args[2:2]=['--cidfile',str(cidfile)]
    process=subprocess.Popen(args,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    observed=None
    for _ in range(100):
        if cidfile.exists() and cidfile.read_text().strip():
            probe=subprocess.run(['docker','inspect',cidfile.read_text().strip()],capture_output=True,timeout=10)
            if probe.returncode==0:
                row=json.loads(probe.stdout)[0]
                observed={'id':row['Id'],'image':row['Image'],'command':row['Config']['Cmd'],
                  'memory':row['HostConfig']['Memory'],'nano_cpus':row['HostConfig']['NanoCpus'],
                  'read_only_root':row['HostConfig']['ReadonlyRootfs'],'user':row['Config']['User'],
                  'mounts':[{'source':m['Source'],'target':m['Destination'],'read_only':not m['RW']} for m in row['Mounts']],
                  'network':row['HostConfig']['NetworkMode'],'packet_manifest':os.environ['CBM_PACKET_SHA256']}
                cidfile.with_suffix('.json').write_text(json.dumps(observed,sort_keys=True));break
        if process.poll() is not None:break
        time.sleep(0.1)
    try:stdout,stderr=process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill();process.communicate()
        raise RuntimeError('worker response timeout; reconcile durable outcome and container before any replay')
    if log is not None:Path(log).write_bytes(stderr)
    if process.returncode:raise RuntimeError('scoped worker failed; inspect private diagnostic and durable outcome')
    if observed is None:raise RuntimeError('worker effect completed without runtime evidence; reconcile before replay')
    return stdout
