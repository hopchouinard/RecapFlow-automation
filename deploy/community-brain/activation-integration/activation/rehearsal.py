"""Fresh Request029 host fixture; all content and authority are development-only."""
import copy
import hashlib
import json
import os
from pathlib import Path
import shlex
import sqlite3
import subprocess
import sys
import tarfile
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import host
from activate import Docker, atomic, command, digest, fingerprint, preserved
from plan import compile_plan

ROOT = host.ROOT
PACKET = host.PACKET
ENGINE = Docker()


def case_dir(case):
    return ROOT/('activation-'+case+'-'+PACKET.name)


def safe_link(target, linkname, root):
    if Path(linkname).is_absolute() or not (target.parent/linkname).resolve().is_relative_to(root.resolve()):
        raise ValueError('recovery symlink escapes disposable volume')
    target.parent.mkdir(parents=True,exist_ok=True)
    target.symlink_to(linkname)


def runtime(spec, service, network, volume):
    mounts = spec.get('volumes', [])
    binds = sorted([{'source': m['source'], 'target': m['target'], 'read_only': m['read_only']}
                    for m in mounts if isinstance(m, dict) and m['type'] == 'bind'], key=lambda m:m['target'])
    volumes = [] if service == 'api' else [{'name': volume, 'target': '/app/backend/data', 'read_only':False}]
    ports = {'8090/tcp':[{'HostIp':'127.0.0.1','HostPort':'19930'}]} if service == 'api' else {}
    return {'service':service,'container':spec['container_name'],'image':spec['image'],
            'network':network,'probe_port':8090 if service=='api' else 8080,'health_timeout':600 if service=='webui' else 90,
            'runtime':{'memory':spec['mem_limit'],'nano_cpus':int(spec['cpus']*1000000000),
                       'read_only_root':spec.get('read_only',False),'user':spec.get('user','0:0'),
                       'command':spec.get('command',['bash','start.sh']),'ports':ports,
                       'binds':binds,'volumes':volumes}}


def prepare(case):
    if case not in ('normal','readiness','partial'):
        raise ValueError('unknown disposable case')
    directory=case_dir(case);directory.mkdir(mode=0o700)
    descriptor=json.loads((PACKET/'descriptor.json').read_text())
    volume='cbm-r029-'+case+'-webui-'+PACKET.name
    command(['docker','volume','create','--label','cbm.request=029',volume])
    mountpoint=Path(json.loads(command(['docker','volume','inspect',volume]))[0]['Mountpoint'])
    # Restore the verified stopped-volume backup into a NEW external volume.
    with tarfile.open(ROOT/'paired-recovery/webui.tar') as archive:
        for member in archive:
            relative=Path(member.name).relative_to('webui')
            target=mountpoint/relative
            if member.isdir():target.mkdir(exist_ok=True,parents=True)
            elif member.isfile():
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(archive.extractfile(member).read());os.chmod(target,member.mode)
            elif member.issym():safe_link(target,member.linkname,mountpoint)
            else:raise ValueError('unsupported recovery member')
    with sqlite3.connect('file:'+str(mountpoint/'webui.db')+'?mode=ro',uri=True) as db:
        assert db.execute('pragma integrity_check').fetchone()==('ok',)
    actual=copy.deepcopy(json.loads((ROOT/'compose.json').read_text()))
    compose={'name':'cbm-r029-'+case,'services':{},'networks':{'default':{'external':True,'name':descriptor['network']}},
             'volumes':{'webui':{'external':True,'name':volume}}}
    for service in ('api','webui'):
        spec=copy.deepcopy(actual['services'][service])
        spec['container_name']='cbm-r029-'+case+'-'+service
        spec['networks']={'default':{'aliases':[service]}}
        if service=='webui':
            spec['user']='0:0'
            spec['volumes']=[{'type':'volume','source':'webui','target':'/app/backend/data','read_only':False}]
        compose['services'][service]=spec
    compose_path=directory/'compose.json';atomic(compose_path,compose)
    (ROOT/'activation-operations').mkdir(mode=0o700,exist_ok=True)
    (ROOT/'activation-journals').mkdir(mode=0o700,exist_ok=True)
    spec={'hostname':'community-brain-dev','state_root':str(ROOT/'state'),
          'packet':str(PACKET),'packet_sha256':os.environ['CBM_PACKET_SHA256'],
          'compose':str(compose_path),'recovery_receipt':str(ROOT/'paired-recovery/manifest.json'),
          'configuration_files':[str(p) for p in sorted((ROOT/'private').rglob('*')) if p.is_file()
                                 and p.suffix in ('.env','.pem','.crt','.conf')],
          'locks':[str(ROOT/'state'/n) for n in ('automation/runner.lock','files/.manual-worker.lock','files/.submission.lock')],
          'holds':[str(ROOT/'state/automation'/n) for n in ('paused','attention.json','boot-state.json')],
          'incumbent':{'container':'cbm-r029-api','network':descriptor['network'],'probe_port':8090},
          'candidates':[runtime(compose['services'][s],s,descriptor['network'],volume) for s in ('api','webui')],
          'external_webui_volumes':[volume],'deadline_epoch':1790020800}
    provider_packet=Path(actual['services']['provider']['volumes'][0].split(':')[0]).parent
    spec['additional_packets']={str(provider_packet):digest((provider_packet/'packet-manifest.json').read_bytes())}
    recovery_sha=json.loads((ROOT/'paired-recovery/manifest.json').read_text())['packet_manifest']
    recovery_packets=[p for p in ROOT.glob('packet-v*') if p.is_dir() and digest((p/'packet-manifest.json').read_bytes())==recovery_sha]
    if len(recovery_packets)!=1:raise ValueError('original recovery packet unavailable')
    spec['additional_packets'][str(recovery_packets[0])]=recovery_sha
    spec['recovery_packet_sha256']=recovery_sha
    spec['configuration_files'] += [str(ROOT/'compose.json'),str(ROOT/'development-loopback.py')]
    if case=='readiness':
        spec['candidates'][0].update(probe_port=9,health_timeout=2)
    if case=='partial':
        spec['candidates'][1].update(probe_port=9,health_timeout=2)
    plan=directory/'plan.json'
    identity=compile_plan(spec,plan)
    value={'case':case,'plan':str(plan),'sha256':identity,'journal':str(ROOT/'activation-journals'/(case+'.json')),
           'restored_external_webui_volume':volume,'source_packet':spec['packet_sha256']}
    atomic(directory/'identity.json',value)
    return value


def check(case, phase, after):
    from consumers import verify
    value=json.loads((case_dir(case)/'plan.json').read_text())
    original_container=host.container
    if phase=='active':
        def container(service):
            return next((x['container'] for x in value['candidates'] if x['service']==service),original_container(service))
        host.container=container
    elif phase!='rolled_back':raise ValueError('unknown phase')
    # Actual authenticated app/filter calls read credentials privately on VM108.
    env=lambda name:dict(x.split('=',1) for x in shlex.split((ROOT/'private'/name).read_text()))
    read=env('probes.env');operator=env('operator-client.env');collector=env('collector-client.env')
    m=host.lib();credentials=json.loads((ROOT/'private/credentials.json').read_text());token=m.login(credentials)
    valves=m.api('GET','/api/v1/functions/id/community_brain_filter/valves',token=token)
    values={**read,'CB_PROD_MANUAL_OPERATOR_TOKEN':operator['CB_MANUAL_OPERATOR_TOKEN'],
            'CB_PROD_MANUAL_OPERATOR_EXPIRES_AT':operator['CB_MANUAL_OPERATOR_EXPIRES_AT'],
            'CB_PROD_MAC_COLLECTOR_TOKEN':collector['CB_COLLECTOR_TOKEN'],
            'CB_PROD_MAC_COLLECTOR_EXPIRES_AT':collector['CB_COLLECTOR_EXPIRES_AT'],
            'CB_OPENWEBUI_RETRIEVAL_TOKEN':valves['api_key']}
    tokens=host.verify_tokens(values)
    assert host.call('/api/v1/me')[0]==401
    assert m.probe(token,values['CB_OPENWEBUI_RETRIEVAL_TOKEN'])['source_count']==1
    # Existing global filter and real application process, no synthetic cache substitution.
    monitor=verify({'values':values,'after':after})
    assert preserved(value)==value['hold_bindings']
    current=ENGINE.inspect(host.container('api'))
    assert current['HostConfig']['PortBindings']=={'8090/tcp':[{'HostIp':'127.0.0.1','HostPort':'19930'}]}
    result={'case':case,'phase':phase,'authenticated_subjects':tokens,'anonymous_rejected':True,
            'live_openwebui_filter':True,'synthetic_source_count':1,'monitors':monitor,
            'monitor_after':after,'holds_preserved':True,'api_container_id':current['Id'],
            'port_binding':current['HostConfig']['PortBindings'],'packet_sha256':value['packet_sha256']}
    atomic(case_dir(case)/(phase+'-acceptance.json'),result)
    return result


def write_webui(case):
    value=json.loads((case_dir(case)/'plan.json').read_text())
    name=value['candidates'][1]['container']
    # Use the actual application API for a retained chat write.
    old=host.container
    host.container=lambda service:name if service=='webui' else old(service)
    m=host.lib();token=m.login(json.loads((ROOT/'private/credentials.json').read_text()))
    chat=m.api('POST','/api/v1/chats/new',{'chat':{'title':'Request029 synthetic retained write','messages':[]}},token)
    chat_id=chat['id']
    result={'chat_id':chat_id,'synthetic_only':True,'volume':value['external_webui_volumes'][0]}
    atomic(case_dir(case)/'new-write.json',result)
    return result


def retained(case):
    value=json.loads((case_dir(case)/'plan.json').read_text())
    info=json.loads(command(['docker','volume','inspect',value['external_webui_volumes'][0]]))[0]
    write=json.loads((case_dir(case)/'new-write.json').read_text())
    with sqlite3.connect('file:'+str(Path(info['Mountpoint'])/'webui.db')+'?mode=ro',uri=True) as db:
        assert db.execute('pragma integrity_check').fetchone()==('ok',)
        assert db.execute('select id from chat where id=?',(write['chat_id'],)).fetchone()==(write['chat_id'],)
    incumbent=ENGINE.inspect(value['incumbent']['container'])
    assert incumbent['Id']==value['incumbent']['id'] and incumbent['State']['Running']
    assert fingerprint(incumbent)==value['incumbent']['fingerprint']
    result={'actual_new_webui_chat_retained':True,'same_incumbent_id':True,'same_incumbent_configuration':True,
            'holds_preserved':preserved(value)==value['hold_bindings']}
    atomic(case_dir(case)/'retained-write.json',result)
    return result


if __name__=='__main__':
    from runtime_contract import load
    load(os.environ['CBM_PACKET_SHA256'])
    mode,case=sys.argv[1:3]
    if mode=='prepare':result=prepare(case)
    elif mode=='check':result=check(case,sys.argv[3],float(sys.argv[4]))
    elif mode=='write':result=write_webui(case)
    elif mode=='retained':result=retained(case)
    else:raise ValueError('unknown rehearsal operation')
    print(json.dumps(result))
