import json,os,signal,subprocess,sys,tempfile,time,unittest
from pathlib import Path
from helper_contracts import Cycle,verify_sources
class Admission(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.mutex=self.root/'mutex';self.mutex.touch(mode=0o600)
 def tearDown(self):self.tmp.cleanup()
 def cycle(self,op,kind='manual'):return Cycle(self.root/'journal',self.mutex,op,kind,verify_sources())
 def test_direct_helper_requires_owned_mutex(self):
  c=self.cycle('direct')
  with self.assertRaises(ValueError):c.helper('copy-backup',lambda:None,lambda:{'fake':True})
 def test_uncertain_helper_blocks_all_kinds_and_cannot_replay(self):
  with self.cycle('uncertain') as c:
   with self.assertRaises(RuntimeError):c.helper('copy-backup',lambda:(_ for _ in ()).throw(RuntimeError('lost ack')),lambda:{})
  for kind in ('scheduler','manual','capture'):
   with self.assertRaises(ValueError):
    with self.cycle('next-'+kind,kind):pass
  self.assertTrue((self.root/'journal/uncertain/copy-backup.intent.json').exists())
 def test_real_process_kill_retains_common_intent(self):
  code="from helper_contracts import *\nimport time\nwith Cycle("+repr(str(self.root/'journal'))+","+repr(str(self.mutex))+",'killed','capture',verify_sources()) as c:\n c.helper('copy-backup',lambda:time.sleep(60),lambda:{'never':True})\n"
  p=subprocess.Popen([sys.executable,'-B','-c',code],cwd=Path(__file__).parent)
  try:
   for _ in range(100):
    if (self.root/'journal/killed/copy-backup.intent.json').exists():break
    time.sleep(.01)
   else:self.fail('intent missing')
   with self.assertRaises(BlockingIOError):
    with self.cycle('compete'):pass
   p.kill();p.wait(timeout=5)
   with self.assertRaises(ValueError):
    with self.cycle('scheduler','scheduler'):pass
  finally:
   if p.poll() is None:p.kill();p.wait()
 def test_resolved_cycle_allows_new_but_not_replay(self):
  with self.cycle('one') as c:c.helper('copy-backup',lambda:None,lambda:{'actual':'fixture'});c.finish()
  with self.cycle('two','scheduler') as c:c.finish()
  with self.assertRaises(FileExistsError):
   with self.cycle('one'):pass
 def test_retired_root_refuses_new_effect(self):
  (self.root/'retired.json').write_text('{}')
  with self.assertRaisesRegex(ValueError,'retired'):
   with self.cycle('retired'):pass
 def test_mutex_replacement_refused(self):
  with self.cycle('replace') as c:
   self.mutex.rename(self.root/'old');self.mutex.touch()
   with self.assertRaises(ValueError):c.check()
if __name__=='__main__':unittest.main()
