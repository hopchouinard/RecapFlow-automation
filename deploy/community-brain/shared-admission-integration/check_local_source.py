"""Actual subprocess refusal for changed or extra sealed Mac source members."""
import json,shutil,subprocess,sys,time
from pathlib import Path
import shared,common as c

if __name__=='__main__':
    path=Path(sys.argv[1]);s=shared.load(path,'manual');root=shared.STATE/('source-negatives-'+str(time.time_ns()));root.mkdir(mode=0o700)
    results=[]
    for kind in ('changed','extra','bytecode'):
        copy=root/kind;shutil.copytree(Path(__file__).parent,copy)
        if kind=='changed':
            p=copy/'manual.py';p.chmod(0o600);p.write_text(p.read_text()+'\n# deliberate synthetic source drift\n')
        else:(copy/('extra.py' if kind=='extra' else 'unlisted.pyc')).write_bytes(b'synthetic unlisted source member')
        p=subprocess.run([sys.executable,'-B',str(copy/'manual.py'),'dispatch',str(path)],capture_output=True,text=True)
        assert p.returncode!=0 and ('source differs' in p.stderr or 'unknown local source member' in p.stderr)
        results.append({'case':kind,'rejected_before_admission':True,'returncode':p.returncode})
    value={'cases':results,'negative_count':len(results),'retained_path':str(root)}
    c.atom(shared.STATE/(s['operation_id']+'-source-checks.json'),value);print(json.dumps(value))
