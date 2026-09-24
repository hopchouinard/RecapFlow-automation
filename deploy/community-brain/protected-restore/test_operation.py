import json
import multiprocessing
import os
from pathlib import Path
import signal
import tempfile
import time
import unittest
import operation as op
import receipt
import recovery as r
import transport
import io


class OperationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name).resolve()
        self.lock=self.root/'lock'; self.lock.touch()
        self.hold=self.root/'paused'; self.hold.write_text('paused')
        self.spec=dict(scope='synthetic-development',deadline_epoch=time.time()+30,
                       max_seconds=10,locks=[str(self.lock)],holds=[str(self.hold)])
        self.directory=self.root/'operation'
    def test_success_readback_duplicate_and_binding(self):
        result=op.run(self.directory,self.spec,lambda: {'verified':True})
        self.assertEqual(result,op.readback(self.directory,self.spec))
        with self.assertRaises(FileExistsError):op.run(self.directory,self.spec,lambda: self.fail('replay'))
        with self.assertRaises(ValueError):op.readback(self.directory,{**self.spec,'max_seconds':9})
    def test_deadline_retains_partial_and_holds(self):
        self.spec['max_seconds']=0.05
        before=r.hold_state([self.hold])
        def action():
            (self.root/'partial').write_text('retain'); time.sleep(2)
        with self.assertRaises(op.Interrupted):op.run(self.directory,self.spec,action)
        self.assertEqual(op.readback(self.directory,self.spec)['state'],'uncertain')
        self.assertTrue((self.root/'partial').exists()); self.assertEqual(before,r.hold_state([self.hold]))
        with r.quiet([self.lock],[self.hold]):pass
    def test_signal_and_kill_readback_no_replay(self):
        for sig in (signal.SIGTERM,signal.SIGKILL):
            directory=self.root/str(sig)
            ready=self.root/('ready'+str(sig))
            def action():
                ready.touch(); time.sleep(20)
            process=multiprocessing.get_context('fork').Process(target=op.run,args=(directory,self.spec,action))
            process.start()
            try:
                until=time.monotonic()+5
                while not ready.exists() and time.monotonic()<until:time.sleep(.01)
                self.assertTrue(ready.exists())
                self.assertEqual(op.readback(directory,self.spec)['state'],'running')
                os.kill(process.pid,sig); process.join(5)
                self.assertFalse(process.is_alive())
                self.assertEqual(op.readback(directory,self.spec)['state'],'uncertain')
                with self.assertRaises(FileExistsError):op.run(directory,self.spec,lambda:None)
                with r.quiet([self.lock],[self.hold]):pass
            finally:
                if process.is_alive():process.kill();process.join()
    def test_expired_and_production_refused_before_intent(self):
        for change in ({'deadline_epoch':0},{'scope':'authorized-private-preservation'},{'max_seconds':float('nan')}):
            with self.assertRaises(ValueError):op.run(self.directory,{**self.spec,**change},lambda:None)
            self.assertFalse(self.directory.exists())
    def test_hold_drift_never_repairs_or_completes(self):
        with self.assertRaises(ValueError):op.run(self.directory,self.spec,lambda:self.hold.write_text('drift'))
        self.assertEqual(op.readback(self.directory,self.spec)['state'],'uncertain')
        self.assertEqual(self.hold.read_text(),'drift')


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name).resolve(); source=self.root/'source';source.mkdir()
        (source/'empty').mkdir();(source/'data').write_text('synthetic')
        (source/'link').symlink_to('data')
        self.bundle=self.root/'bundle';self.dest=self.root/'restored'
        self.digest=r.capture({'state':source},self.bundle,'synthetic-request031',{})
        stream=io.BytesIO();transport.pack(self.bundle,self.digest,stream);stream.seek(0)
        received=self.root/'received';transport.receive(stream,received,self.digest,byte_ceiling=1024*1024)
        self.bundle=received;r.restore(self.bundle,self.digest,self.dest)
    def test_stream_restore_verified_without_acceptance_substitution(self):
        result=receipt.verify(self.bundle,self.digest,self.dest)
        self.assertFalse(result['production_qualified']);self.assertIsNone(result['database_acceptance'])
    def test_drift_and_extra_members_refused(self):
        (self.dest/'state'/'data').write_text('changed')
        with self.assertRaises(ValueError):receipt.verify(self.bundle,self.digest,self.dest)
    def test_receipt_flags_cannot_certify_restore(self):
        path=self.dest/'restore-receipt.json';value=json.loads(path.read_text())
        value['production_qualified']=True;path.write_bytes(r.encode(value))
        with self.assertRaises(ValueError):receipt.verify(self.bundle,self.digest,self.dest)
    def test_extra_top_level_member_refused(self):
        (self.dest/'extra').touch()
        with self.assertRaises(ValueError):receipt.verify(self.bundle,self.digest,self.dest)
    def test_capture_identity_mismatch_refused(self):
        path=self.bundle/'intent.json';value=json.loads(path.read_text())
        value['capture_id']='wrong-capture';path.write_bytes(r.encode(value))
        with self.assertRaises(ValueError):receipt.verify(self.bundle,self.digest,self.dest)

if __name__=='__main__':unittest.main()
