import pathlib,tarfile,tempfile,shutil,json,hashlib,datetime
p=pathlib.Path('/var/backups/community-brain/meeting-archive-009/archive-and-controls.tar.gz')
with tempfile.TemporaryDirectory(prefix='.verify009-',dir=p.parent) as tmp:
 root=pathlib.Path(tmp)
 with tarfile.open(p,'r:gz') as t:
  members=t.getmembers()
  for m in members:
   n=pathlib.PurePosixPath(m.name);assert not n.is_absolute() and '..' not in n.parts and (m.isfile() or m.isdir())
   dest=root/m.name
   if m.isdir():dest.mkdir(parents=True,exist_ok=True)
   else:
    dest.parent.mkdir(parents=True,exist_ok=True)
    with t.extractfile(m) as src,dest.open('xb') as out:shutil.copyfileobj(src,out)
 archive=root/'meeting-archive-20260910';raw=(archive/'manifest.json').read_bytes();assert hashlib.sha256(raw).hexdigest()=='3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00';d=json.loads(raw);entries={a['id']:a for m in d['meetings'] for a in m['artifacts']};assert len(d['meetings'])==87 and len(entries)==481
 assert {p.name for p in (archive/'files').iterdir()}==set(entries)
 for n,h in entries.items():
  b=(archive/'files'/n).read_bytes();assert len(b)==h['bytes'] and hashlib.sha256(b).hexdigest()==h['sha256']
 ui=root/'workspaces/cbm-archive-ui-20260910';manifest=json.loads((ui/'effective-runtime-manifest.json').read_text())
 for n,h in manifest.items():
  b=(ui/n).read_bytes();assert len(b)==h['bytes'] and hashlib.sha256(b).hexdigest()==h['sha256']
print(json.dumps({'request_id':'CBM-MEETING-ARCHIVE-20260910-009','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'private_offhost_archive_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'isolated_restore_files':481,'meetings':87,'restored_packet_files':len(manifest),'safe_tar_members':len(members),'temporary_extraction_removed':True,'database_queue_provider_access':False}))
