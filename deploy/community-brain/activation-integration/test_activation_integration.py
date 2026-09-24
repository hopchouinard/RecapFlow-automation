"""Failure boundaries added by Request029; no live effects."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).parent/'activation'))
from plan import packet_files, evidence_files, validate_bindings
from activate import digest, preserved, validate_runtime, validate_plan
from management import invoke, unresolved


class Boundaries(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/'source.py').write_text('print("sealed")\n')
        entries={'source.py':{'bytes':(self.root/'source.py').stat().st_size,
                            'sha256':digest((self.root/'source.py').read_bytes())}}
        (self.root/'packet-manifest.json').write_text(json.dumps(entries))
        self.sha=digest((self.root/'packet-manifest.json').read_bytes())

    def test_extra_bytecode_rejected(self):
        packet_files(self.root,self.sha)
        (self.root/'source.pyc').write_bytes(b'bytecode')
        with self.assertRaises(ValueError):packet_files(self.root,self.sha)

    def test_source_and_manifest_drift_rejected(self):
        (self.root/'source.py').write_text('different bytes')
        with self.assertRaises(ValueError):packet_files(self.root,self.sha)
        with self.assertRaises(ValueError):packet_files(self.root,'0'*64)

    def test_true_flag_does_not_manufacture_restore_evidence(self):
        path=self.root/'receipt.json';path.write_text(json.dumps({'verified':True,'restore_equal':True}))
        with self.assertRaises(ValueError):evidence_files(path,self.root,self.sha)

    def test_compiled_holds_cannot_drift_before_first_effect(self):
        files=packet_files(self.root,self.sha)
        hold=self.root.parent/(self.root.name+'-hold')
        hold.write_text('held');self.addCleanup(hold.unlink)
        value={'packet':str(self.root),'packet_sha256':self.sha,'files':files,'holds':[str(hold)],
               'expires_at':10**12,'volume_bindings':{}}
        value['hold_bindings']=preserved(value)
        validate_bindings(value)
        hold.write_text('changed')
        with self.assertRaises(ValueError):validate_bindings(value)

    def test_stale_plan_refused(self):
        with self.assertRaises(ValueError):validate_bindings({'expires_at':0})

    def test_uncertain_mac_intent_is_not_dispatched_again(self):
        path=self.root/'intent.json';path.write_text('{"state":"intended"}')
        with patch('management.subprocess.Popen') as spawn, patch('management._owns_mutex', True):
            with self.assertRaises(FileExistsError):invoke('host','remote','directory',{},path)
            spawn.assert_not_called()

    def test_runtime_environment_drift_rejected(self):
        row={'Image':'pinned','HostConfig':{},'Config':{'Env':['SECRET=different']}}
        target={'image':'pinned','environment_sha256':digest(json.dumps(['SECRET=expected']).encode())}
        with self.assertRaisesRegex(ValueError,'environment'):validate_runtime(row,target)

    def test_pending_outcome_blocks_a_fresh_operation_id(self):
        intent=self.root/'old-intent.json';intent.write_text('{}')
        (self.root/'activation-pending.json').write_text(json.dumps({'intent':str(intent)}))
        self.assertTrue(unresolved(self.root))
        with patch('management._owns_mutex',True),patch('management.subprocess.Popen') as spawn:
            with self.assertRaisesRegex(RuntimeError,'unresolved'):
                invoke('host','remote','fresh-directory',{},self.root/'fresh-intent.json')
            spawn.assert_not_called()

    def test_production_host_still_cannot_activate(self):
        value={'schema':2,'phase':'serving-only','hostname':'community-brain-prod','state_root':'/srv/community-brain'}
        p=self.root/'production.json';p.write_text(json.dumps(value))
        with patch('activate.socket.gethostname',return_value='community-brain-prod'),patch('activate.os.geteuid',return_value=0):
            with self.assertRaisesRegex(ValueError,'production serving execution is disabled'):
                validate_plan(p,digest(p.read_bytes()))

    def test_restored_cache_link_is_contained(self):
        from rehearsal import safe_link
        target=self.root/'nested/link'
        safe_link(target,'../source.py',self.root)
        self.assertEqual(target.read_bytes(),(self.root/'source.py').read_bytes())
        with self.assertRaises(ValueError):safe_link(self.root/'escape','../../outside',self.root)


if __name__=='__main__':unittest.main()
