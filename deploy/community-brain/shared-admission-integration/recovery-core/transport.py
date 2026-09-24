"""Private stream framing; no SSH launch, remote command or unrestricted extraction."""
import os
from pathlib import Path
import re
import tarfile
import recovery as r


def pack(bundle, expected, output, scope='synthetic-development'):
    bundle=Path(bundle)
    r.validate_bundle(bundle,expected,scope)
    with tarfile.open(fileobj=output,mode='w|') as tar:
        for p in sorted(bundle.rglob('*')):
            if p.is_file():
                info=tar.gettarinfo(str(p),arcname=str(p.relative_to(bundle)))
                if not info.isfile():raise ValueError('nonregular transport member')
                info.mode=0o600;info.uid=0;info.gid=0;info.uname='';info.gname=''
                with p.open('rb') as f:tar.addfile(info,f)


def receive(stream,destination,expected,byte_ceiling,scope='synthetic-development'):
    if not isinstance(byte_ceiling,int) or not 1<=byte_ceiling<=20*1024**3:
        raise ValueError('invalid transport byte ceiling')
    destination=r.no_links(destination)
    destination.mkdir(mode=0o700)
    (destination/'blobs').mkdir(mode=0o700)
    seen=set();total=0
    with tarfile.open(fileobj=stream,mode='r|') as tar:
        for m in tar:
            if not m.isfile() or not (m.name in {'intent.json','manifest.json','capture-complete.json'} or re.fullmatch('blobs/[0-9a-f]{64}',m.name)):
                raise ValueError('unsafe transport member')
            if m.name in seen:raise ValueError('duplicate transport member')
            seen.add(m.name);total+=m.size
            if total>byte_ceiling:raise ValueError('transport byte ceiling exceeded')
            p=destination/m.name
            fd=os.open(p,os.O_CREAT|os.O_EXCL|os.O_WRONLY|os.O_NOFOLLOW,0o600)
            with os.fdopen(fd,'wb') as out:
                incoming=tar.extractfile(m);left=m.size
                while left:
                    b=incoming.read(min(1024*1024,left))
                    if not b:raise ValueError('truncated transport member')
                    out.write(b);left-=len(b)
                out.flush();os.fsync(out.fileno())
    for p in [destination/'blobs',destination]:
        fd=os.open(p,os.O_RDONLY)
        try:os.fsync(fd)
        finally:os.close(fd)
    value=r.validate_bundle(destination,expected,scope)
    return {'capture_id':value['capture_id'],'manifest_sha256':expected,'bytes':total,
            'members':len(seen),'destination':str(destination),'scope':scope}
