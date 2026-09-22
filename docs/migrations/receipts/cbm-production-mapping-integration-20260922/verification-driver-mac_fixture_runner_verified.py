"""Explicit Linux-metadata model for five immutable Forge receipt fixtures on Mac.

This process-local test adaptation does not change the preservation library or
claim arbitrary Mac metadata is captured. A separate unpatched test proves refusal.
"""
import sys,tempfile,subprocess,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path('/Users/pchouinard/.local/state/community-brain-management/request033/sealed/packet-v7')
sys.path.insert(0,str(ROOT/'recovery-core'))
import recovery,test_operation

class NativeMetadataBoundary(unittest.TestCase):
    def test_actual_mac_extended_metadata_is_still_refused(self):
        with tempfile.TemporaryDirectory() as raw:
            root=Path(raw).resolve();source=root/'source';source.mkdir()
            p=source/'synthetic';p.write_text('synthetic metadata rejection')
            subprocess.run(['/usr/bin/xattr','-w','org.patchoutech.synthetic','fixture-only',str(p)],check=True,capture_output=True)
            self.assertIn('org.patchoutech.synthetic',[x.decode() if isinstance(x,bytes) else x for x in recovery.extended_names(p)])
            with self.assertRaisesRegex(ValueError,'extended metadata unsupported'):
                recovery.capture({'state':source},root/'bundle','synthetic-mac-boundary',{})

def main():
    if sys.platform!='darwin':raise ValueError('explicit Mac fixture runner only')
    original=test_operation.ReceiptTests.setUp
    def synthetic_linux_metadata(self):
        adaptation=patch.object(recovery,'extended_names',return_value=[])
        adaptation.start();self.addCleanup(adaptation.stop)
        original(self)
    test_operation.ReceiptTests.setUp=synthetic_linux_metadata
    suite=unittest.defaultTestLoader.discover(str(ROOT/'recovery-core'),pattern='test_*.py')
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(NativeMetadataBoundary))
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print('Explicit adaptation: five ReceiptTests model Linux metadata; native refusal tested separately.')
    return result.wasSuccessful()

if __name__=='__main__':raise SystemExit(0 if main() else 1)
