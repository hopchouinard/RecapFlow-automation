"""Synthetic hourly helper: authenticated read-only health, never production jobs."""
import json,sys,subprocess
import shared
if __name__=='__main__':
    mode,path=sys.argv[1:]
    if mode!='hourly':raise ValueError('only synthetic hourly health supported')
    s=shared.load(path,'scheduler')
    p=subprocess.run(shared.command(s,'health'),capture_output=True,timeout=20)
    if p.returncode or json.loads(p.stdout)!={'healthy':True}:raise RuntimeError('synthetic hourly health failed')
    print(json.dumps({'hourly_health':'passed','production_helpers_invoked':False}))
