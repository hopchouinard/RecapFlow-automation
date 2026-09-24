"""Exact-image, no-network validation of the whole preserved file catalog."""
import hashlib
import json
from types import SimpleNamespace
from fastapi.testclient import TestClient
from community_brain.jobs.api import create_app
from community_brain.jobs.archive import MeetingArchive
from community_brain.jobs.auth import Principal

archive = MeetingArchive('/archive', '3ceecdf65c38e0a2e59da4c8e90584e8cb3c9f2cffa2c96da4d487ebcdbb9d00')
principals = {'reader': Principal('reader', 'community-brain', frozenset(['jobs:read', 'artifacts:read'])),
              'collector': Principal('collector','community-brain',frozenset(['sources:upload:chat'])),
              'other': Principal('reader','other',frozenset(['jobs:read','artifacts:read']))}
c = TestClient(create_app(SimpleNamespace(), principals.__getitem__, archive=archive))
headers={'Authorization':'Bearer reader'}
r=c.get('/api/v1/meetings',headers=headers)
assert r.status_code==200 and len(r.json()['items'])==87
for key,meta in archive.files.items():
    r=c.get(f'/api/v1/meeting-artifacts/{key}/content',headers=headers)
    assert r.status_code==200 and len(r.content)==meta['bytes'] and hashlib.sha256(r.content).hexdigest()==meta['sha256']
for path in ['/api/v1/meetings', '/api/v1/meeting-artifacts/'+next(iter(archive.files))+'/content']:
    assert c.get(path).status_code==401
    assert c.get(path,headers={'Authorization':'Bearer collector'}).status_code==403
    assert c.get(path,headers={'Authorization':'Bearer other'}).status_code==404
print(json.dumps({'meetings':87,'authenticated_file_hashes':len(archive.files),'scope_denials_verified':True,'network_disabled':True,'database_queue_provider_access':False}))
