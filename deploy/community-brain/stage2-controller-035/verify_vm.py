"""Read-only independent VM108 parity and preservation receipt."""
import json
from pathlib import Path
import sys
from common import DEV_ROOT,command,docker_fingerprint,docker_row,host_identity,read_json,sha,stable_bytes,verify_packet
from fixture_vm import controls,sql

BASELINE=('cbm-collector-development-proxy-1','cbm-live-development-api-1',
          'cbm-live-development-nats-1','cbm-live-development-postgres-1')

def inspect(packet_sha):
 packet=Path(__file__).resolve().parent
 parity=verify_packet(packet,packet_sha,owner_uid=0)
 fixture=read_json(DEV_ROOT/'fixture.json')
 plan=read_json(DEV_ROOT/'plan.json')
 inc=docker_row(fixture['incumbent_id'])
 pg=docker_row(fixture['postgres_id'])
 baseline={name:json.loads(command(['docker','inspect','--type','container',name],timeout=10))[0]['State']['Running'] for name in BASELINE}
 active=read_json(DEV_ROOT/'journal/active.json') if (DEV_ROOT/'journal/active.json').exists() else None
 result=read_json(DEV_ROOT/'journal'/active['attempt']/'result.json') if active and (DEV_ROOT/'journal'/active['attempt']/'result.json').exists() else None
 receipt={'schema':'cbm.stage2-vm108-parity/1','packet':parity,
          'plan_sha256':sha(stable_bytes(DEV_ROOT/'plan.json')),
          'plan_pin_matches':stable_bytes(DEV_ROOT/'plan.pin').decode().strip()==sha(stable_bytes(DEV_ROOT/'plan.json')),
          'host_matches':host_identity(DEV_ROOT,'synthetic-development')==fixture['host']==plan['host'],
          'controls_match_fixture':controls()==fixture['controls'],
          'controls_match_plan':controls()==plan['controls'],
          'incumbent_id_matches':inc['Id']==fixture['incumbent_id']==plan['incumbent_id'],
          'incumbent_fingerprint_matches':docker_fingerprint(inc)==fixture['incumbent_fingerprint']==plan['incumbent_fingerprint'],
          'incumbent_running':inc['State']['Running'],
          'postgres_id_matches':pg['Id']==fixture['postgres_id']==plan['postgres_id'],
          'postgres_running':pg['State']['Running'],
          'database_acl_matches_initial':sql("SELECT datacl::text FROM pg_database WHERE datname='fixture'")==fixture['database_acl_before'] if pg['State']['Running'] else False,
          'baseline_containers_running':baseline,
          'active_attempt':active['attempt'] if active else None,
          'active_result':result,
          'production_slots_null':len([v for v in plan['production_evidence'].values() if v is None]),
          'production_changes':False,'vm101_changes':False,'paid_provider_requests':0}
 return receipt

if __name__=='__main__':print(json.dumps(inspect(sys.argv[1]),sort_keys=True))
