"""Disposable exact-module failure/race checks; never imports the live entry point."""
import datetime,json,pathlib,tempfile,types,unittest,unittest.mock,fcntl,os,subprocess,sys
import ownership_control as c
import mac_intake_policy as m
NOW=datetime.datetime.fromisoformat('2026-09-10T06:50:00+00:00')
class Tests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.tmp.name);self.effects=[]
  self.state={'request_id':c.ORIGINAL,'phase':'switched','guard_active':True,'mac_resume_allowed':False,'deadline_utc':'2026-09-11T01:30:00+00:00'}
  c.atomic_json(self.root/'state.json',self.state)
  ready={'request_id':c.REQUEST,'accepted_recovery_receipt_sha256':c.RECEIPT,'checked_at':NOW.isoformat(),'checks':{k:True for k in c.CHECKS}}
  c.atomic_json(self.root/'ownership-readiness007.json',ready)
  self.ctrl=c.Controller(self.root,types.SimpleNamespace(rollback=lambda force:self.effects.append(('rollback',force))),lambda:self.effects.append(('preflight',True)),lambda:NOW)
 def tearDown(self):self.tmp.cleanup()
 def test_before_commit_timer_boot_and_force_delegate(self):
  for force in [False,False,True]:self.ctrl.execute('rollback',force)
  self.assertEqual(self.effects,[('rollback',False),('rollback',False),('rollback',True)])
 def test_after_commit_all_entry_paths_are_noops(self):
  first=self.ctrl.execute('supersede');self.effects.clear()
  for command,force in [('rollback',False),('rollback',False),('rollback',True),('supersede',False),('status',False)]:self.assertEqual(self.ctrl.execute(command,force),first)
  self.assertEqual(self.effects,[])
 def test_failed_prerequisite_preserves_rollback(self):
  self.ctrl.verify_live=lambda:(_ for _ in []).throw(RuntimeError('fixture'))
  with self.assertRaises(RuntimeError):self.ctrl.execute('supersede')
  self.ctrl.execute('rollback',False);self.assertEqual(self.effects,[('rollback',False)])
 def test_failed_readiness_preserves_rollback(self):
  (self.root/'ownership-readiness007.json').unlink()
  with self.assertRaises(FileNotFoundError):self.ctrl.execute('supersede')
  self.ctrl.execute('rollback',False);self.assertEqual(self.effects,[('rollback',False)])
 def test_late_preflight_rejected(self):
  self.ctrl.now=lambda:c.LATEST_START
  with self.assertRaises(AssertionError):self.ctrl.execute('supersede')
  self.assertEqual(c.read_private(self.root/'state.json')['phase'],'switched')
 def test_crash_before_replace_keeps_old_semantics(self):
  with unittest.mock.patch.object(c.os,'replace',side_effect=OSError('crash')):
   with self.assertRaises(OSError):self.ctrl.execute('supersede')
  self.effects.clear();self.ctrl.execute('rollback',False);self.assertEqual(self.effects,[('rollback',False)])
 def test_crash_after_replace_retry_cannot_restore(self):
  original=c.atomic_json
  def crash(p,value):original(p,value);raise OSError('crash after commit')
  with unittest.mock.patch.object(c,'atomic_json',side_effect=crash):
   with self.assertRaises(OSError):self.ctrl.execute('supersede')
  self.effects.clear();self.assertEqual(self.ctrl.execute('rollback',True)['phase'],'superseded');self.assertEqual(self.effects,[])
 def test_missing_state_fails_closed(self):
  self.ctrl.execute('supersede');self.effects.clear();(self.root/'state.json').unlink()
  with self.assertRaises(FileNotFoundError):self.ctrl.execute('rollback',True)
  self.assertEqual(self.effects,[])
 def test_corrupt_state_fails_closed(self):
  self.ctrl.execute('supersede');self.effects.clear();(self.root/'state.json').write_text('{')
  with self.assertRaises(json.JSONDecodeError):self.ctrl.execute('rollback',True)
  self.assertEqual(self.effects,[])
 def test_missing_or_corrupt_terminal_record_fails_closed(self):
  state=self.ctrl.execute('supersede');self.effects.clear()
  for record in [None,{'request_id':'wrong'}]:
   v={**state};v.pop('ownership',None)
   if record is not None:v['ownership']=record
   c.atomic_json(self.root/'state.json',v)
   with self.assertRaises((KeyError,AssertionError)):self.ctrl.execute('rollback',True)
  self.assertEqual(self.effects,[])
 def test_lock_race_excludes_second_process(self):
  fd=os.open(self.root/'control.lock',os.O_CREAT|os.O_RDWR,0o600);fcntl.flock(fd,fcntl.LOCK_EX)
  try:
   script="import sys,types;from ownership_control import Controller\ntry:Controller(sys.argv[1],types.SimpleNamespace(rollback=lambda force:print('UNSAFE')),lambda:None).execute('supersede')\nexcept BlockingIOError:print('locked')"
   env={**os.environ,'PYTHONPATH':str(pathlib.Path(__file__).parent.resolve())}
   r=subprocess.run([sys.executable,'-c',script,str(self.root)],capture_output=True,text=True,env=env);self.assertEqual(r.returncode,0);self.assertEqual(r.stdout.strip(),'locked')
  finally:os.close(fd)
 def test_deadline_waits_for_transient_lock_then_runs_once(self):
  import time
  fd=os.open(self.root/'control.lock',os.O_CREAT|os.O_RDWR,0o600);fcntl.flock(fd,fcntl.LOCK_EX)
  script="import sys,types;from ownership_control import Controller;Controller(sys.argv[1],types.SimpleNamespace(rollback=lambda force:print('delegated')),lambda:None).execute('rollback',False)"
  env={**os.environ,'PYTHONPATH':str(pathlib.Path(__file__).parent.resolve())}
  process=subprocess.Popen([sys.executable,'-c',script,str(self.root)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env)
  try:
   time.sleep(0.1);self.assertIsNone(process.poll());os.close(fd);fd=None;stdout,stderr=process.communicate(timeout=3);self.assertEqual(process.returncode,0);self.assertEqual(stdout.strip(),'delegated')
  finally:
   if fd is not None:os.close(fd)
   if process.poll() is None:process.kill();process.wait()
 def test_lock_release_after_failure(self):
  with unittest.mock.patch.object(c,'read_private',side_effect=ValueError('fixture')):
   with self.assertRaises(ValueError):self.ctrl.execute('status')
  self.assertEqual(self.ctrl.execute('status')['phase'],'switched')
 def local(self):return {'request_id':m.ORIGINAL,'phase':'held','previous_enabled':True}
 def test_mac_unreachable_peer_never_resumes(self):
  with self.assertRaises(OSError):m.decide(self.local(),lambda:(_ for _ in []).throw(OSError()),lambda x:None,lambda:None,lambda v:self.effects.append('resume'))
  self.assertEqual(self.effects,[])
 def test_mac_observes_terminal_even_with_stale_local_restored(self):
  local={**self.local(),'phase':'restored'};remote=self.ctrl.execute('supersede');events=[]
  result=m.decide(local,lambda:remote,lambda d:events.append('saved'),lambda:events.append('disabled'),lambda v:events.append('resume'))
  self.assertEqual(result,'superseded');self.assertEqual(events,['saved','disabled'])
 def test_mac_terminal_ignores_stale_or_unreachable_peer(self):
  local={**self.local(),'phase':'superseded','ownership':self.ctrl.execute('supersede')['ownership']}
  def forbidden():raise AssertionError('must not read stale peer')
  result=m.decide(local,forbidden,lambda d:None,lambda:self.effects.append('disabled'),lambda v:self.effects.append('resume'))
  self.assertEqual(result,'superseded');self.assertEqual(self.effects[-1],'disabled')
 def test_mac_save_failure_never_resumes(self):
  remote=self.ctrl.execute('supersede');events=[]
  with self.assertRaises(OSError):m.decide(self.local(),lambda:remote,lambda d:(_ for _ in []).throw(OSError()),lambda:events.append('disabled'),lambda v:events.append('resume'))
  self.assertEqual(events,[])
 def test_mac_missing_terminal_record_fails_closed(self):
  local={**self.local(),'phase':'superseded'}
  with self.assertRaises(KeyError):m.decide(local,lambda:None,lambda d:None,lambda:None,lambda v:self.effects.append('resume'))
  self.assertEqual(self.effects,[])
 def test_mac_old_verified_rollback_still_restores_exact_saved_state(self):
  remote={'request_id':m.ORIGINAL,'phase':'restored','rollback_verified':True,'mac_resume_allowed':True};events=[]
  self.assertEqual(m.decide(self.local(),lambda:remote,lambda d:events.append('saved'),lambda:events.append('disabled'),lambda v:events.append(('resume',v))),'restored')
  self.assertEqual(events,[('resume',True),'saved'])
if __name__=='__main__':unittest.main()
