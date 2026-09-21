"""Negative adapter validation using fresh SSH observations, never fixture success flags."""
import copy,json,secrets,subprocess,sys,time
from pathlib import Path
import shared
import common as c

def check(path):
    s=shared.load(path,json.loads(Path(path).read_bytes())['kind']);challenge=secrets.token_hex(32)
    p=subprocess.run(shared.command(s,'observe',challenge),capture_output=True,timeout=25);assert p.returncode==0
    v=json.loads(p.stdout);shared.verify_observation(s,challenge,v)
    cases={
      'stale_challenge':lambda x:x.update(challenge='0'*64),
      'foreign_target_spec':lambda x:x.update(target_spec_sha256='0'*64),
      'foreign_source':lambda x:x.update(packet_sha256='0'*64),
      'foreign_machine':lambda x:x.update(machine_id='foreign'),
      'changed_incumbent_config':lambda x:x.update(incumbent_fingerprint='0'*64),
      'unknown_acceptance_flag':lambda x:x.update(accepted=True),
      'missing_startup':lambda x:x.update(startup=None),
      'stale_startup_boot':lambda x:x['startup'].update(boot_id='00000000-0000-0000-0000-000000000000'),
      'foreign_startup_owner':lambda x:x['startup'].update(spec_sha256='0'*64),
      'stale_finalizer_boot':lambda x:x['finalizer'].update(boot_id='00000000-0000-0000-0000-000000000000'),
      'missing_finalizer':lambda x:x.update(finalizer={}),
      'unrestored_writers':lambda x:x.update(writer_controls_restored=False),
      'stale_proof':lambda x:x['proof'].update(observed_epoch=time.time()-60),
      'future_proof':lambda x:x['proof'].update(observed_epoch=time.time()+60),
      'foreign_owner_proof':lambda x:x['proof'].update(spec_sha256='0'*64),
      'foreign_incumbent':lambda x:x['proof'].update(incumbent_id='0'*64),
      'changed_holds':lambda x:x['proof'].update(holds_sha256='0'*64),
      'production_target':lambda x:x['proof'].update(target='community-brain-prod'),
      'unhealthy':lambda x:x['proof'].update(healthy=False),
      'service_active':lambda x:x['proof'].update(service_inactive=False),
      'uncertain':lambda x:x['proof'].update(state='uncertain')}
    results=[]
    for name,mutate in cases.items():
        x=copy.deepcopy(v);mutate(x)
        try:shared.verify_observation(s,challenge,x)
        except ValueError:results.append({'case':name,'rejected':True})
        else:raise AssertionError(name)
    denied=subprocess.run(['ssh','-o','ControlMaster=no','-o','ControlPath=none','-o','UserKnownHostsFile=/dev/null','-o','GlobalKnownHostsFile=/dev/null',*shared.command(s,'observe',challenge)[1:]],capture_output=True,timeout=15)
    assert denied.returncode!=0 and b'Host key verification failed' in denied.stderr
    results.append({'case':'unknown_ssh_host_key','rejected':True,'actual_connection_refused':True})
    out={'observation_origin':'fresh challenged SSH with StrictHostKeyChecking=yes; no receipt-file input in entry points','positive_live_readback_verified':True,'cases':results,'negative_count':len(results),'target_spec_sha256':v['target_spec_sha256'],'actual_kernel_boot_id':v['current_boot_id']}
    c.atom(shared.STATE/(s['operation_id']+'-readback-checks.json'),out);print(json.dumps(out))

if __name__=='__main__':check(sys.argv[1])
