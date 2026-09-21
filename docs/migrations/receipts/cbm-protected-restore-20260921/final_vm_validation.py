import pathlib,sys,json,io,hashlib,subprocess,socket
root=pathlib.Path('/srv/dev-data/workspaces/cbm-protected-restore-20260921-030')
sys.path.insert(0,str(root/'source-v6'))
import recovery as r,transport
assert socket.gethostname()=='community-brain-dev'
source=root/'attempt04/synthetic-source';out=root/'final-validation';out.mkdir(mode=0o700)
locks=[source/'controls'/n for n in ['runner.lock','manual.lock','submission.lock']]
holds=[source/'controls'/n for n in ['paused','attention.json','boot-state.json','checkpoint-needed.json']]
before=r.hold_state(holds)
with r.quiet(locks,holds):
 h=r.capture({p.name:p for p in source.iterdir()},out/'capture','cbm-r030-final-v6',{'hold_bindings':before,'writer_exclusion':'all Request030 PostgreSQL sources stopped'})
 stream=io.BytesIO();transport.pack(out/'capture',h,stream);stream.seek(0)
 transfer=transport.receive(stream,out/'received',h,8*1024*1024)
 receipt=r.restore(out/'received',h,out/'restored')
 assert r.hold_state(holds)==before
 prior=json.loads((root/'attempt04/synthetic-acceptance.json').read_text())
 assert r.sha((out/'restored/database/database.dump').read_bytes())==r.sha((root/'attempt04/independent-restore/database/database.dump').read_bytes())
 webui=root/'webui-session-a02/capture';web=json.loads((root/'webui-session-a02/webui-session-acceptance.json').read_text())
 r.validate_bundle(webui,web['capture_manifest_sha256'])
 webrestore=r.restore(webui,web['capture_manifest_sha256'],out/'webui-preservation')
 result={'scope':'synthetic-development','source_revision':'source-v6','manifest_sha256':h,'transfer':transfer,'restore':receipt,'held_markers_equal':r.hold_state(holds)==before,'database_dump_equals_independently_restored_attempt04':True,'database_acceptance_receipt_sha256':r.sha((root/'attempt04/synthetic-acceptance.json').read_bytes()),'webui_restore':webrestore,'source_hashes':{p.name:r.sha(p.read_bytes()) for p in (root/'source-v6').iterdir() if p.is_file()},'off_host_transfer_performed':False,'production_qualified':False}
 r.write_new(out/'acceptance.json',r.encode(result))
print(json.dumps(result))
