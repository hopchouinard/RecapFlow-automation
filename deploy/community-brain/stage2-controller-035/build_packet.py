"""Deterministic exact-member packet, with no secret or runtime state."""
import hashlib
import gzip
import json
from pathlib import Path
import re
import tarfile

SOURCE=Path(__file__).resolve().parent

def build(destination,revision,source=SOURCE):
 if not re.fullmatch(r'packet-v[1-9][0-9]*',revision):raise ValueError('bad packet revision')
 source=Path(source)
 destination=Path(destination)
 destination.mkdir(mode=0o700)
 files={str(p.relative_to(source)):p for p in source.rglob('*') if p.is_file() and not p.is_symlink()
        and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.name!='packet-manifest.json'}
 if not files or any(p.is_symlink() for p in source.rglob('*')):raise ValueError('linked/empty packet source')
 manifest={}
 for name,p in sorted(files.items()):
  target=destination/name
  target.parent.mkdir(parents=True,exist_ok=True)
  raw=p.read_bytes()
  target.write_bytes(raw)
  target.chmod(0o444)
  manifest[name]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
 raw=(json.dumps(manifest,sort_keys=True,separators=(',',':'))+'\n').encode()
 (destination/'packet-manifest.json').write_bytes(raw)
 (destination/'packet-manifest.json').chmod(0o444)
 return hashlib.sha256(raw).hexdigest()

def archive(packet,output):
 packet=Path(packet)
 with Path(output).open('wb') as raw:
  with gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0) as zipped:
   with tarfile.open(fileobj=zipped,mode='w',format=tarfile.PAX_FORMAT) as tar:
    for p in sorted(packet.rglob('*')):
     if not p.is_file():continue
     info=tarfile.TarInfo(str(p.relative_to(packet)))
     info.size=p.stat().st_size
     info.mtime=0
     info.uid=info.gid=0
     info.uname=info.gname=''
     info.mode=0o444
     with p.open('rb') as stream:tar.addfile(info,stream)
 return hashlib.sha256(Path(output).read_bytes()).hexdigest()
