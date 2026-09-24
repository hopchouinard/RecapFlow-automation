"""One-shot concurrent synthetic capacity trial on isolated VM108 state."""
import concurrent.futures
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import statistics
import subprocess
import tarfile
import threading
import time
from host import ROOT, PRIVATE, COMPOSE, call, lib, atomic, command
from validation_host import submit, launch, data

DURATION = 75
CLIENTS = 3
LATENCY_LIMIT_MS = 2000
MIN_AVAILABLE_KIB = 524288


def token(name, key):
    values = dict(x.split('=', 1) for x in shlex.split((PRIVATE / name).read_text()))
    return values[key]


def available():
    for line in Path('/proc/meminfo').read_text().splitlines():
        if line.startswith('MemAvailable:'):
            return int(line.split()[1])
    raise ValueError('MemAvailable missing')


def oom_kills():
    for line in Path('/proc/vmstat').read_text().splitlines():
        if line.startswith('oom_kill '):
            return int(line.split()[1])
    raise ValueError('kernel OOM counter missing')


def stats():
    rows=[]
    raw=command(['docker','stats','--no-stream','--format','{{json .}}'],timeout=20)
    for line in raw.splitlines():
        row=json.loads(line)
        if row['Name'].startswith('cbm-r034-'):
            rows.append({'name':row['Name'],'memory':row['MemUsage'].split(' / ')[0],
                         'cpu_percent':float(row['CPUPerc'].strip('%'))})
    return rows


def load_client(kind, end, barrier, read, webui, webui_token, retrieval):
    barrier.wait()
    durations=[];failures=0
    while time.monotonic()<end:
        start=time.monotonic()
        try:
            if kind=='api':
                assert call('/retrieval/query',read,{'question':'synthetic stage2 capacity'})[0]==200
            else:
                assert webui.probe(webui_token,retrieval)['source_count']==1
        except Exception:
            failures+=1
        durations.append((time.monotonic()-start)*1000)
    return {'kind':kind,'requests':len(durations),'failures':failures,'latencies_ms':durations}


def worker(barrier, operator):
    barrier.wait();start=time.monotonic()
    job=submit({'CB_PROD_MANUAL_OPERATOR_TOKEN':operator},'2026-09-15')
    stages=[]
    for stage in ('processing','indexing'):
        selection=launch(['inspect',job,stage,'1'])['selection']
        result=launch(['execute',selection]);assert result['state']=='succeeded'
        stages.append(stage)
    proof=data()
    assert proof['fts']['num_unindexed_rows']==0
    return {'started':start,'ended':time.monotonic(),'job_id':job,'stages':stages,
            'fts_indexed_rows':proof['fts']['num_indexed_rows']}


def restore(barrier):
    barrier.wait();start=time.monotonic()
    root=ROOT/'capacity-restore';root.mkdir(mode=0o700)
    dump=root/'database.sql'
    with dump.open('xb') as output:
        p=subprocess.run(COMPOSE+['exec','-T','pg','pg_dump','-U','fixture','--no-owner','integration'],
                         stdout=output,stderr=subprocess.PIPE,timeout=90)
        assert p.returncode==0
    command(COMPOSE+['exec','-T','pg','createdb','-U','fixture','integration_capacity_034'])
    with dump.open('rb') as source:
        p=subprocess.run(COMPOSE+['exec','-T','pg','psql','-U','fixture','-d','integration_capacity_034',
                              '-v','ON_ERROR_STOP=1'],stdin=source,capture_output=True,timeout=90)
        assert p.returncode==0
    with tarfile.open(root/'state.tar','w') as tar:
        for name in ('files','config','corpus','meeting-archive','automation','automation-public'):
            tar.add(ROOT/'state'/name,arcname=name)
    files=0
    with tarfile.open(root/'state.tar') as tar:
        members=tar.getmembers()
        tar.extractall(root/'restored',filter='data')
        for member in members:
            if member.isfile():
                source=ROOT/'state'/member.name
                target=root/'restored'/member.name
                assert hashlib.sha256(source.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest()
                files+=1
    return {'started':start,'ended':time.monotonic(),
            'dump_sha256':hashlib.sha256(dump.read_bytes()).hexdigest(),
            'state_files_verified':files,'separate_database':'integration_capacity_034'}


def main(_):
    marker=ROOT/'capacity-trial-intent'
    assert not marker.exists();marker.touch(mode=0o600)
    assert not (ROOT/'state/automation/paused').exists()
    read=token('probes.env','CB_READ_PROBE_TOKEN')
    operator=token('operator-client.env','CB_MANUAL_OPERATOR_TOKEN')
    webui=lib()
    webui.ready()
    from host import address,OPENER
    with OPENER.open(address('webui',8080)+'/health',timeout=10) as response:assert response.status==200
    assert call('/api/v1/me',read)[0]==200
    webui_token=webui.login(json.loads((PRIVATE/'credentials.json').read_text()))
    retrieval=webui.api('GET','/api/v1/functions/id/community_brain_filter/valves',token=webui_token)['api_key']
    before_oom=oom_kills();before_available=available();begin=time.monotonic()
    end=begin+DURATION;barrier=threading.Barrier(CLIENTS+2)
    samples=[];results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=CLIENTS+2) as pool:
        futures=[pool.submit(load_client,'api' if i<2 else 'webui',end,barrier,read,webui,webui_token,retrieval)
                 for i in range(CLIENTS)]
        futures.append(pool.submit(worker,barrier,operator))
        futures.append(pool.submit(restore,barrier))
        while any(not future.done() for future in futures):
            samples.append({'available_kib':available(),'containers':stats(),'at':time.monotonic()-begin})
            time.sleep(2)
        for future in futures:results.append(future.result())
    after_oom=oom_kills()
    client_results=results[:CLIENTS];w,r=results[CLIENTS:]
    latency=sorted(x for result in client_results for x in result['latencies_ms'])
    assert latency
    p95=latency[math.ceil(.95*len(latency))-1]
    overlap=max(0,min(w['ended'],r['ended'],end)-max(w['started'],r['started'],begin))
    min_available=min(x['available_kib'] for x in samples)
    peak_cpu=max((row['cpu_percent'] for sample in samples for row in sample['containers']),default=0)
    receipt={'schema':'cbm.stage2-capacity/1','profile':{'clients':CLIENTS,'duration_seconds':DURATION,
             'api_clients':2,'webui_clients':1,'worker':'actual synthetic processing and indexing',
             'restore':'separate PostgreSQL database and state tar','baseline_vm_kib':4004576,
             'p95_limit_ms':LATENCY_LIMIT_MS,'minimum_available_kib':MIN_AVAILABLE_KIB},
             'before_available_kib':before_available,'min_available_kib':min_available,
             'headroom_fraction':round(min_available/4004576,3),'kernel_oom_kills_delta':after_oom-before_oom,
             'peak_container_cpu_percent':peak_cpu,'request_pairs':sum(x['requests'] for x in client_results),
             'request_failures':sum(x['failures'] for x in client_results),
             'p95_latency_ms':round(p95,1),'max_latency_ms':round(latency[-1],1),
             'worker':w,'restore':r,'four_way_overlap_seconds':round(overlap,1),
             'actual_concurrent_acceptance':overlap>=1 and min_available>=MIN_AVAILABLE_KIB
                 and after_oom==before_oom and p95<=LATENCY_LIMIT_MS
                 and all(x['failures']==0 for x in client_results)}
    atomic(ROOT/'capacity-acceptance.json',json.dumps(receipt,indent=2))
    return receipt
