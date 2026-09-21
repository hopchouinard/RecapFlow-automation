import sys
from unittest.mock import patch
import copy
import fcntl
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import recovery as r


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        # Unit fixtures model Linux metadata. Real VM108 tests use os.listxattr.
        if sys.platform == 'darwin':
            metadata_patch=patch.object(r,'extended_names',return_value=[])
            metadata_patch.start();self.addCleanup(metadata_patch.stop)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root/'original'
        self.source.mkdir()
        (self.source/'empty').mkdir()
        (self.source/'data').write_bytes(b'private synthetic bytes')
        (self.source/'data').chmod(0o640)
        (self.source/'link').symlink_to('data')
        self.bundle = self.root/'bundle'
        self.dest = self.root/'restored'
    def capture(self):
        return r.capture({'state':self.source},self.bundle,'synthetic-request030',{})
    def mutate_manifest(self, function):
        v=json.loads((self.bundle/'manifest.json').read_text());function(v)
        b=r.encode(v);(self.bundle/'manifest.json').write_bytes(b)
        h=r.sha(b);(self.bundle/'capture-complete.json').write_bytes(r.encode({'manifest_sha256':h}))
        return h
    def test_round_trip_preserves_empty_directories_links_and_original(self):
        before=r.tree(self.source);h=self.capture()
        result=r.restore(self.bundle,h,self.dest)
        self.assertEqual(before,r.tree(self.dest/'state'))
        self.assertEqual(before,r.tree(self.source))
        self.assertFalse(result['production_qualified'])
        self.assertIsNone(result['database_acceptance'])
    def test_capture_never_overwrites_uncertain_attempt(self):
        self.capture()
        with self.assertRaises(FileExistsError):self.capture()
    def test_restore_never_overwrites_uncertain_destination(self):
        h=self.capture();self.dest.mkdir()
        with self.assertRaises(FileExistsError):r.restore(self.bundle,h,self.dest)
    def test_escape_source_link_refused(self):
        (self.source/'escape').symlink_to('../outside');(self.root/'outside').touch()
        with self.assertRaises(ValueError):self.capture()
    def test_hardlink_refused(self):
        os.link(self.source/'data',self.source/'hard')
        with self.assertRaises(ValueError):self.capture()
    def test_special_file_refused(self):
        os.mkfifo(self.source/'fifo')
        with self.assertRaises(ValueError):self.capture()
    def test_corrupt_blob_refused_before_destination_creation(self):
        h=self.capture();next((self.bundle/'blobs').iterdir()).write_bytes(b'corrupt')
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
        self.assertFalse(self.dest.exists())
    def test_blob_directory_symlink_refused(self):
        h=self.capture();(self.bundle/'blobs').rename(self.root/'elsewhere');(self.bundle/'blobs').symlink_to(self.root/'elsewhere')
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
    def test_duplicate_component_source_refused(self):
        with self.assertRaises(ValueError):r.capture({'one':self.source,'two':self.source},self.bundle,'synthetic-request030',{})
    def test_extended_metadata_refused(self):
        with patch.object(r,'extended_names',return_value=['user.synthetic']):
            with self.assertRaises(ValueError):self.capture()

    def test_unpinned_manifest_refused(self):
        self.capture()
        with self.assertRaises(ValueError):r.restore(self.bundle,'0'*64,self.dest)
    def test_missing_completion_refused(self):
        h=self.capture();(self.bundle/'capture-complete.json').unlink()
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
    def test_traversal_manifest_refused(self):
        self.capture();h=self.mutate_manifest(lambda v:v['components']['state'][1].update(path='../escape'))
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
    def test_link_escape_manifest_refused(self):
        self.capture();h=self.mutate_manifest(lambda v:next(x for x in v['components']['state'] if x['kind']=='symlink').update(target='../../outside'))
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
    def test_foreign_scope_refused(self):
        self.capture();h=self.mutate_manifest(lambda v:v.update(scope='production'))
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
    def test_extra_blob_refused(self):
        h=self.capture();(self.bundle/'blobs'/'unlisted').touch()
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.dest)
    def test_restore_over_original_refused(self):
        h=self.capture()
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.source/'replacement')
    def test_linked_destination_ancestor_refused(self):
        h=self.capture();(self.root/'alias').symlink_to(self.root,target_is_directory=True)
        with self.assertRaises(ValueError):r.restore(self.bundle,h,self.root/'alias'/'x')
    def test_busy_lock_refuses_before_capture_and_preserves_holds(self):
        lock=self.root/'lock';lock.touch();hold=self.root/'paused';hold.write_text('paused')
        before=r.hold_state([hold])
        with lock.open('r+') as f:
            fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)
            with self.assertRaises(BlockingIOError):
                with r.quiet([lock],[hold]):self.capture()
        self.assertEqual(before,r.hold_state([hold]));self.assertFalse(self.bundle.exists())
    def test_missing_lock_not_created(self):
        with self.assertRaises(FileNotFoundError):
            with r.quiet([self.root/'absent'],[]):pass
        self.assertFalse((self.root/'absent').exists())
    def test_hold_drift_detected_without_repair(self):
        hold=self.root/'paused';hold.write_text('before')
        with self.assertRaises(ValueError):
            with r.quiet([],[hold]):hold.write_text('changed')
        self.assertEqual(hold.read_text(),'changed')
    def test_changed_lock_identity_detected(self):
        lock=self.root/'lock';lock.touch()
        with self.assertRaises(ValueError):
            with r.quiet([lock],[]):lock.rename(self.root/'retained');lock.touch()
    def test_source_drift_retains_incomplete_attempt(self):
        real=r.tree;calls=0
        def changing(*a,**kw):
            nonlocal calls
            calls+=1
            if calls==2:(self.source/'data').write_text('changed')
            return real(*a,**kw)
        with patch.object(r,'tree',changing):
            with self.assertRaises(ValueError):self.capture()
        self.assertTrue((self.bundle/'intent.json').exists())
        self.assertFalse((self.bundle/'capture-complete.json').exists())

if __name__=='__main__':unittest.main()
