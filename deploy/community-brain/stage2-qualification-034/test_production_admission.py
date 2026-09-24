"""Negative admission checks; no production effect or fixture credential."""
import copy,hashlib,importlib.util,json,tempfile,unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('production_admission',HERE/'production_admission.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
contract=json.loads(m.CONTRACT.read_text())

def fixture():
 plan={'phase':'protected-preservation','target':'community-brain-prod',
       'authorization':{'id':'test-only','scope':'separate-production-phase','expires_epoch':1500},
       'acceptance_deadline_epoch':1400,'production_execution_enabled':False,
       'machine_id':contract['machine_id'],'mount_uuid':contract['state_mount']['uuid'],
       'incumbent_id':contract['incumbent_id'],'incumbent_image':contract['incumbent_image'],
       'holds':{'paused':'a','attention':'b','boot':'c'},
       'locks':{'runner':'a','manual':'b','submission':'c'}}
 authority={'environment':'production','readback':True,'expires_epoch':1800}
 observed={key:plan[key] for key in ('machine_id','mount_uuid','incumbent_id','incumbent_image','holds','locks')}
 evidence={slot:{'scope':'production','accepted':True,'receipt_sha256':'a'*64} for slot in m.SLOTS}
 return plan,authority,observed,evidence

def seal(plan):return hashlib.sha256((json.dumps(plan,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()

class Admission(unittest.TestCase):
 def run_review(self,p,a,o,e):return m.review(p,a,o,e,now=1000,reviewed_plan_sha256=seal(p))
 def test_review_is_still_disabled(self):
  p,a,o,e=fixture();self.assertFalse(self.run_review(p,a,o,e)['production_execution_enabled'])
 def test_source_drift(self):
  p,a,o,e=fixture()
  with self.assertRaisesRegex(ValueError,'externally reviewed'):m.review(p,a,o,e,now=1000,reviewed_plan_sha256='0'*64)
 def test_exact_source_member_drift_and_extra_file(self):
  with tempfile.TemporaryDirectory() as temporary:
   root=Path(temporary)/'source';root.mkdir();(root/'controller.py').write_bytes(b'first')
   manifest=Path(temporary)/'manifest.json';manifest.write_text(json.dumps({'controller.py':m.digest(b'first')}))
   pin=m.digest(manifest.read_bytes())
   self.assertEqual(m.exact_tree(root,manifest,pin),1)
   (root/'controller.py').write_bytes(b'changed')
   with self.assertRaisesRegex(ValueError,'drift'):m.exact_tree(root,manifest,pin)
   (root/'controller.py').write_bytes(b'first');(root/'extra.py').write_bytes(b'extra')
   with self.assertRaisesRegex(ValueError,'member drift'):m.exact_tree(root,manifest,pin)
 def test_expiry(self):
  p,a,o,e=fixture();a['expires_epoch']=1401
  with self.assertRaisesRegex(ValueError,'authority'):self.run_review(p,a,o,e)
 def test_changed_host_or_hold(self):
  p,a,o,e=fixture();o['mount_uuid']='wrong'
  with self.assertRaisesRegex(ValueError,'mount'):self.run_review(p,a,o,e)
  p,a,o,e=fixture();o['holds']=copy.deepcopy(o['holds']);o['holds']['paused']='changed'
  with self.assertRaisesRegex(ValueError,'holds'):self.run_review(p,a,o,e)
 def test_missing_or_dev_slot(self):
  p,a,o,e=fixture();e.pop(m.SLOTS[-1])
  with self.assertRaisesRegex(ValueError,'21 evidence'):self.run_review(p,a,o,e)
  p,a,o,e=fixture();e[m.SLOTS[0]]['scope']='development'
  with self.assertRaisesRegex(ValueError,'nonproduction'):self.run_review(p,a,o,e)
 def test_production_enable_refused(self):
  p,a,o,e=fixture();p['production_execution_enabled']=True
  with self.assertRaisesRegex(ValueError,'cannot enable'):self.run_review(p,a,o,e)

if __name__=='__main__':unittest.main()
