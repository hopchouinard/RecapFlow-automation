"""External-pin plan compiler. Production evidence is deliberately fail-closed."""
import json
import os
from pathlib import Path
import sys
import time
from common import DEV_ROOT,PROD_ROOT,create,replace,encode,file_identity,host_identity,read_json,sha,verify_packet,docker_row,docker_fingerprint
from fixture_vm import controls

SLOTS=tuple(json.loads(Path(__file__).with_name('evidence-slots.json').read_text()))
# A receipt schema must have a semantic verifier, not merely accepted:true.
PRODUCTION_VALIDATORS={}

def validate_production_evidence(evidence,now=None):
 now=time.time() if now is None else now
 if not isinstance(evidence,dict) or set(evidence)!=set(SLOTS):raise ValueError('production evidence slot set incomplete')
 for name in SLOTS:
  item=evidence[name]
  if not isinstance(item,dict) or not item.get('receipt_sha256') or not item.get('schema') or not item.get('member_hashes') or not item.get('observations') or not item.get('scope') or not item.get('capture_id') or not item.get('expires_at'):
   raise ValueError('production evidence absent or incomplete: '+name)
  if item['scope']!='production' or item['expires_at']<=now:raise ValueError('production evidence scope/expiry: '+name)
  validator=PRODUCTION_VALIDATORS.get(name)
  if validator is None:raise ValueError('semantic production validator unimplemented: '+name)
  validator(item)
 raise ValueError('production approval authority not enrolled')

def compile_dev(packet_sha,owner):
 if owner!='pchouinard':raise ValueError('rollback owner must be explicit')
 root=DEV_ROOT
 host=host_identity(root,'synthetic-development')
 packet=Path(__file__).resolve().parent
 verify_packet(packet,packet_sha,owner_uid=0)
 fixture=read_json(root/'fixture.json')
 if fixture['host']!=host or fixture['controls']!=controls():raise ValueError('fixture/controls drift')
 inc=docker_row(fixture['incumbent_id'])
 pg=docker_row(fixture['postgres_id'])
 if docker_fingerprint(inc)!=fixture['incumbent_fingerprint'] or not inc['State']['Running'] or not pg['State']['Running']:
  raise ValueError('incumbent or DB drift')
 source=file_identity(root/'state/corpus/source.txt')
 config=file_identity(root/'state/config/profile.json')
 authority={'scope':'synthetic-development','generation':'r035-synthetic-only','expires_at':int(time.time())+1800,
            'protected_preservation':False,'serving':True,'processing_resume':False,'paid_provider_calls':False}
 plan={'schema':'cbm.stage2-plan/1','scope':'synthetic-development','packet_manifest_sha256':packet_sha,
       'host':host,'fixture_sha256':sha(encode(fixture)),'source':source,'config':config,
       'incumbent_id':fixture['incumbent_id'],'incumbent_image':fixture['incumbent_image'],
       'incumbent_fingerprint':fixture['incumbent_fingerprint'],'postgres_id':fixture['postgres_id'],
       'postgres_image':fixture['postgres_image'],'controls':fixture['controls'],
       'authority':authority,'operation':'synthetic_serving_recovery','rollback_owner':owner,
       'private_destinations':[str(root/'journal')],
       'deadlines_seconds':{'stop':20,'db':20,'work':30,'restore':60,'overall':150},
       'production_evidence':{name:None for name in SLOTS}}
 if (root/'plan.json').exists():
  active=read_json(root/'journal/active.json')
  result=root/'journal'/active['attempt']/'result.json'
  if not result.exists() or not read_json(result).get('serving_restored'):
   raise ValueError('unresolved prior attempt blocks plan revision')
  prior=(root/'plan.json').read_bytes()
  create(root/'journal'/('retired-plan-'+sha(prior)+'.json'),prior)
  replace(root/'plan.json',encode(plan))
  replace(root/'plan.pin',sha(encode(plan)).encode()+b'\n')
 else:
  create(root/'plan.json',encode(plan))
  create(root/'plan.pin',sha(encode(plan)).encode()+b'\n')
 return {'plan_sha256':sha(encode(plan)),'authority_expires_at':authority['expires_at'],
         'production_slots_null':len(SLOTS),'external_pin_required':True}

def validate_live(plan,now=None):
 now=time.time() if now is None else now
 if plan['scope']!='synthetic-development':raise ValueError('plan scope mismatch')
 if now>=plan['authority']['expires_at'] or not plan['authority']['serving']:
  raise ValueError('serving authority expired or denied')
 if plan['authority']['protected_preservation'] or plan['authority']['processing_resume']:
  raise ValueError('dev authorities must remain separated')
 if host_identity(DEV_ROOT,'synthetic-development')!=plan['host'] or controls()!=plan['controls']:
  raise ValueError('host/control drift')
 if file_identity(DEV_ROOT/'state/corpus/source.txt')!=plan['source'] or file_identity(DEV_ROOT/'state/config/profile.json')!=plan['config']:
  raise ValueError('source/config drift')
 inc=docker_row(plan['incumbent_id'])
 if inc['Image']!=plan['incumbent_image'] or docker_fingerprint(inc)!=plan['incumbent_fingerprint']:
  raise ValueError('exact incumbent drift')
 pg=docker_row(plan['postgres_id'])
 if pg['Image']!=plan['postgres_image']:raise ValueError('DB drift')
 return plan

def load_pinned(expected,packet_sha):
 if sha(Path(DEV_ROOT/'plan.json').read_bytes())!=expected or (DEV_ROOT/'plan.pin').read_text().strip()!=expected:
  raise ValueError('external plan pin mismatch')
 plan=read_json(DEV_ROOT/'plan.json')
 if plan['packet_manifest_sha256']!=packet_sha:raise ValueError('plan packet mismatch')
 return validate_live(plan)

if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='compile':print(json.dumps(compile_dev(sys.argv[2],sys.argv[3])))
 elif mode=='production-check':
  host_identity(PROD_ROOT,'production')
  validate_production_evidence(read_json(sys.argv[2]))
 else:raise SystemExit(2)
