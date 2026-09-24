import copy
import multiprocessing
import os
from pathlib import Path
import signal
import tempfile
import time
import unittest
import admission as a

class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.journal=self.root/'journal';self.journal.mkdir()
        self.lock=self.root/'scheduler.lock';self.lock.touch()
        self.gate=a.Gate(self.journal,self.lock)
        self.spec=dict(scope='synthetic-development',kind='capture',operation_id='capture-test001',owner_id='forge-test001',packet_sha256='1'*64,target='community-brain-dev',incumbent_id='2'*64,holds_sha256='3'*64,deadline_epoch=time.time()+60)
    def proof(self):
        return dict(spec_sha256=a.digest(self.spec),state='aborted_restored',incumbent_id=self.spec['incumbent_id'],holds_sha256=self.spec['holds_sha256'],target=self.spec['target'],observed_epoch=time.time(),boot_id='12345678-1234-1234-1234-123456789abc',finalizer_seen=True,service_inactive=True,healthy=True)
    def test_all_entry_points_share_unresolved_barrier(self):
        with self.gate.locked():
            self.gate.begin(self.spec)
            for kind in ('scheduler','manual','capture'):
                with self.subTest(kind=kind),self.assertRaises(ValueError):
                    self.gate.begin({**self.spec,'kind':kind,'operation_id':kind+'-test002'})
    def test_fresh_recovery_after_deadline_resolves_without_replay(self):
        self.spec['deadline_epoch']=time.time()+.02
        with self.gate.locked():
            self.gate.begin(self.spec);time.sleep(.03)
            self.gate.reconcile(self.spec,self.proof)
            self.assertEqual(self.gate.unresolved(),[])
            with self.assertRaises(ValueError):self.gate.begin(self.spec)
    def test_foreign_stale_unhealthy_and_unresolved_readbacks_refused(self):
        changes=[{'state':'uncertain'},{'healthy':False},{'finalizer_seen':False},{'service_inactive':False},{'spec_sha256':'4'*64},{'holds_sha256':'4'*64},{'incumbent_id':'4'*64},{'observed_epoch':time.time()-60},{'observed_epoch':float('nan')},{'boot_id':''},{'target':'community-brain-prod'},{'extra':True}]
        with self.gate.locked():
            self.gate.begin(self.spec)
            for change in changes:
                with self.subTest(change=change),self.assertRaises(ValueError):
                    self.gate.reconcile(self.spec,lambda:{**self.proof(),**change})
                self.assertEqual(self.gate.unresolved(),[self.spec['operation_id']])
    def test_no_lock_no_production_no_expired_dispatch(self):
        with self.assertRaises(ValueError):self.gate.begin(self.spec)
        with self.gate.locked():
            for change in ({'scope':'production'},{'target':'community-brain-prod'},{'deadline_epoch':0}):
                with self.assertRaises(ValueError):self.gate.begin({**self.spec,**change})
        self.assertEqual(list(self.journal.iterdir()),[])
    def test_partial_intent_and_unknown_member_block(self):
        p=self.journal/'capture-partial';p.mkdir()
        with self.gate.locked():
            with self.assertRaises(ValueError):self.gate.begin(self.spec)
            (p/'unexpected').touch()
            with self.assertRaises(ValueError):self.gate.unresolved()
    def test_mutex_replacement_detected_before_effect(self):
        with self.assertRaises(ValueError):
            with self.gate.locked():
                self.lock.rename(self.root/'retained.lock');self.lock.touch()
                self.gate.begin(self.spec)
        self.assertEqual(list(self.journal.iterdir()),[])
    def test_callback_failure_never_replayed(self):
        calls=[]
        def dispatch():calls.append('effect');raise RuntimeError('lost reply')
        with self.gate.locked():
            with self.assertRaises(RuntimeError):self.gate.invoke(self.spec,dispatch,self.proof)
            with self.assertRaises(ValueError):self.gate.invoke(self.spec,dispatch,self.proof)
        self.assertEqual(calls,['effect'])
    def test_real_owner_kill_blocks_fresh_process_until_readback(self):
        ready=self.root/'ready'
        def child():
            with a.Gate(self.journal,self.lock).locked() as gate:
                gate.begin(self.spec);ready.touch();time.sleep(30)
        proc=multiprocessing.get_context('fork').Process(target=child);proc.start()
        try:
            limit=time.monotonic()+5
            while not ready.exists() and time.monotonic()<limit:time.sleep(.01)
            self.assertTrue(ready.exists())
            with self.assertRaises(BlockingIOError):
                with self.gate.locked():pass
            os.kill(proc.pid,signal.SIGKILL);proc.join(5);self.assertFalse(proc.is_alive())
            with a.Gate(self.journal,self.lock).locked() as recovered:
                with self.assertRaises(ValueError):recovered.begin({**self.spec,'kind':'scheduler','operation_id':'scheduler-next'})
                recovered.reconcile(self.spec,self.proof)
                recovered.begin({**self.spec,'kind':'scheduler','operation_id':'scheduler-next'})
        finally:
            if proc.is_alive():proc.kill();proc.join()
    def test_symlink_journal_and_missing_mutex_refused(self):
        alias=self.root/'alias';alias.symlink_to(self.journal)
        with self.assertRaises(ValueError):a.Gate(alias,self.lock)
        self.lock.unlink()
        with self.assertRaises(FileNotFoundError):
            with self.gate.locked():pass
        self.assertFalse(self.lock.exists())

if __name__=='__main__':unittest.main()
