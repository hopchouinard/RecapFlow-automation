"""Retained synthetic integration fixture; VM108 only, exclusive workspace."""
import io
import json
from pathlib import Path
import socket
import sys
import time
import operation
import receipt
import recovery as r
import transport


def main():
    root=r.no_links(sys.argv[1])
    if socket.gethostname()!='community-brain-dev' or not root.is_relative_to(Path('/srv/dev-data/workspaces')):
        raise ValueError('VM108 development workspace required')
    root.mkdir(mode=0o700)
    source=root/'source';source.mkdir();(source/'empty').mkdir()
    (source/'data').write_text('synthetic retained request031 fixture\n')
    (source/'link').symlink_to('data')
    lock=root/'existing.lock';lock.touch();hold=root/'paused';hold.write_text('paused\n')
    before=r.tree(source);holds=r.hold_state([hold])
    spec=dict(scope='synthetic-development',deadline_epoch=time.time()+120,
              max_seconds=60,locks=[str(lock)],holds=[str(hold)])
    r.write_new(root/'spec.json',r.encode(spec))
    def action():
        digest=r.capture({'state':source},root/'bundle','cbm-r031-forge-synthetic',{'holds':holds})
        stream=io.BytesIO();transport.pack(root/'bundle',digest,stream);stream.seek(0)
        transport.receive(stream,root/'received',digest,byte_ceiling=1024*1024)
        r.restore(root/'received',digest,root/'restored')
        return receipt.verify(root/'received',digest,root/'restored')
    result=operation.run(root/'operation',spec,action)
    assert operation.readback(root/'operation',spec)==result
    assert r.tree(source)==before and r.hold_state([hold])==holds
    try:operation.run(root/'operation',spec,lambda:None)
    except FileExistsError:pass
    else:raise AssertionError('replay accepted')
    summary=dict(operation=result,source_unchanged=True,holds_unchanged=True,
                 duplicate_refused=True,external_calls=0,production_execution=False)
    r.write_new(root/'summary.json',r.encode(summary))
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__':main()
