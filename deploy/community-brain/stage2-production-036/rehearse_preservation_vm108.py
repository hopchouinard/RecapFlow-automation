"""Fresh VM108-only Request030 adapter rehearsal, with no private content."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import time

import preservation

ROOT = Path('/srv/dev-data/workspaces/cbm-stage2-production-20260924-036')
MOUNT_UUID = '4a18b6bd-e3d7-40c7-b310-add6598c9438'


def main():
    if socket.gethostname() != 'community-brain-dev' or os.geteuid() != 0:
        raise ValueError('VM108 root only')
    observed = subprocess.run(['findmnt', '-no', 'UUID', '/srv/dev-data'],
                              check=True, capture_output=True, timeout=8).stdout.decode().strip()
    if observed != MOUNT_UUID or ROOT.exists():
        raise ValueError('wrong mount or reused fixture')
    lib = Path(sys.argv[1])
    expected = sys.argv[2]
    if hashlib.sha256(lib.read_bytes()).hexdigest() != expected:
        raise ValueError('Request030 library hash mismatch')
    spec = importlib.util.spec_from_file_location('request030_recovery', lib)
    recovery = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(recovery)
    ROOT.mkdir(mode=0o700)
    source = ROOT / 'source'
    source.mkdir(mode=0o700)
    (source / 'empty').mkdir(mode=0o700)
    (source / 'corpus.bin').write_bytes(b'Request036 synthetic corpus\n')
    hold = ROOT / 'paused'
    hold.write_bytes(b'synthetic processing pause\n')
    lock = ROOT / 'runner.lock'
    lock.write_bytes(b'')
    receipt = preservation.local_preservation(recovery,
        components={'corpus': source}, locks=[lock], holds=[hold],
        bundle=ROOT / 'capture', restored=ROOT / 'restored',
        capture_id='cbm-stage2-production-dev-036',
        deadline_epoch=time.time() + 120)
    (ROOT / 'receipt.json').write_text(json.dumps(receipt, sort_keys=True, indent=2) + '\n')
    print(json.dumps({'capture_id': receipt['capture_id'],
                      'manifest_sha256': receipt['manifest_sha256'],
                      'restore_equal': receipt['restore_receipt']['tree_comparison'],
                      'production_qualified': False}, sort_keys=True))


if __name__ == '__main__':
    main()
