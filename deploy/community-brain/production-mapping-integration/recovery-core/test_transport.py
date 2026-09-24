import sys
from unittest.mock import patch
import io
from pathlib import Path
import tarfile
import tempfile
import unittest
import recovery as r
import transport as t

class TransportTests(unittest.TestCase):
    def setUp(self):
        # Unit fixtures model Linux metadata. Real VM108 tests use os.listxattr.
        if sys.platform == 'darwin':
            metadata_patch=patch.object(r,'extended_names',return_value=[])
            metadata_patch.start();self.addCleanup(metadata_patch.stop)
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name).resolve();self.source=self.root/'source';self.source.mkdir();(self.source/'private').write_bytes(b'synthetic')
        self.bundle=self.root/'bundle';self.h=r.capture({'state':self.source},self.bundle,'synthetic-transport',{})
        self.stream=io.BytesIO();t.pack(self.bundle,self.h,self.stream);self.stream.seek(0)
    def test_verified_round_trip_and_refused_replay(self):
        target=self.root/'receiver';v=t.receive(self.stream,target,self.h,1024*1024)
        self.assertEqual(v['capture_id'],'synthetic-transport')
        r.restore(target,self.h,self.root/'restored')
        self.assertEqual(r.tree(self.source),r.tree(self.root/'restored/state'))
        self.stream.seek(0)
        with self.assertRaises(FileExistsError):t.receive(self.stream,target,self.h,1024*1024)
    def test_budget_failure_retains_partial_destination(self):
        with self.assertRaises(ValueError):t.receive(self.stream,self.root/'receiver',self.h,1)
        self.assertTrue((self.root/'receiver').exists())
    def test_malicious_link_refused(self):
        s=io.BytesIO()
        with tarfile.open(fileobj=s,mode='w') as tar:
            m=tarfile.TarInfo('manifest.json');m.type=tarfile.SYMTYPE;m.linkname='/etc/passwd';tar.addfile(m)
        s.seek(0)
        with self.assertRaises(ValueError):t.receive(s,self.root/'receiver',self.h,100000)
        self.assertFalse((self.root/'receiver/manifest.json').exists())
    def test_traversal_refused(self):
        s=io.BytesIO()
        with tarfile.open(fileobj=s,mode='w') as tar:
            m=tarfile.TarInfo('../escaped');m.size=1;tar.addfile(m,io.BytesIO(b'x'))
        s.seek(0)
        with self.assertRaises(ValueError):t.receive(s,self.root/'receiver',self.h,100000)
        self.assertFalse((self.root/'escaped').exists())
    def test_wrong_external_digest_refused(self):
        with self.assertRaises(ValueError):t.receive(self.stream,self.root/'receiver','0'*64,100000)
    def test_incomplete_stream_refused(self):
        with self.assertRaises((ValueError,tarfile.TarError)):
            t.receive(io.BytesIO(self.stream.getvalue()[:900]),self.root/'receiver',self.h,100000)

if __name__=='__main__':unittest.main()
