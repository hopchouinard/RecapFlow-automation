"""Read-only negative matrix against actual VM108 identities and held files."""
import copy
import json
from pathlib import Path
import time
from common import DEV_ROOT,read_json,verify_packet
from plan import SLOTS,validate_live,validate_production_evidence

def refused(label,call):
 try:call()
 except (ValueError,KeyError,TypeError,RuntimeError) as exc:return {'refused':True,'reason':str(exc)}
 raise AssertionError(label+' unexpectedly accepted')

def main():
 plan=read_json(DEV_ROOT/'plan.json')
 packet=Path(__file__).resolve().parent
 packet_sha=plan['packet_manifest_sha256']
 verified=verify_packet(packet,packet_sha,owner_uid=0)
 assert validate_live(plan)==plan
 checks={}
 altered=copy.deepcopy(plan);altered['source']['sha256']='0'*64
 checks['source_drift']=refused('source',lambda:validate_live(altered))
 altered=copy.deepcopy(plan);altered['controls']['holds']['automation/paused']['sha256']='0'*64
 checks['hold_drift']=refused('hold',lambda:validate_live(altered))
 altered=copy.deepcopy(plan);altered['host']['mount_uuid']='0'*36
 checks['volume_identity_drift']=refused('volume',lambda:validate_live(altered))
 altered=copy.deepcopy(plan);altered['authority']['expires_at']=time.time()-1
 checks['authority_expiry']=refused('authority',lambda:validate_live(altered))
 altered=copy.deepcopy(plan);altered['incumbent_id']='0'*64
 checks['foreign_incumbent']=refused('incumbent',lambda:validate_live(altered))
 checks['production_null_21']=refused('null evidence',lambda:validate_production_evidence({x:None for x in SLOTS}))
 fake={x:{'receipt_sha256':'f'*64,'schema':'fake','member_hashes':{'x':'f'*64},
          'observations':['accepted:true'],'scope':'production','capture_id':'fake','expires_at':time.time()+100}
       for x in SLOTS}
 checks['generic_accepted_envelopes']=refused('generic accepted',lambda:validate_production_evidence(fake))
 return {'schema':'cbm.stage2-negative-matrix/1','scope':'synthetic-development',
         'packet':verified,'live_baseline_passed':True,'checks':checks,
         'actual_mount_changed':False,'actual_hold_changed':False,'actual_source_changed':False}

if __name__=='__main__':print(json.dumps(main(),sort_keys=True))
