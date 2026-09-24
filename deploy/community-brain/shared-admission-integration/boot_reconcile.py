"""Fail-closed boot hook for the retained active owner; no capture replay."""
import fcntl,json,os,re,subprocess,sys,time,secrets
from pathlib import Path
import common as c
r=c.r

def reconcile(packet_sha):
    packet=Path(__file__).resolve().parent;c.packet(packet,packet_sha)
    if c.machine_id()=='' or __import__('socket').gethostname()!='community-brain-dev':raise ValueError('VM108 only')
    if (c.ROOT/'retired.json').exists():raise ValueError('retired synthetic root cannot restart')
    fd=os.open(c.ROOT/'boot.lock',os.O_RDWR|os.O_NOFOLLOW)
    try:
        fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
        record={'schema':1,'boot_id':c.boot_id(),'machine_id':c.machine_id(),'controller_packet_sha256':packet_sha,'admission_open':False,'at':time.time()}
        c.atom(c.ROOT/'boot-admission.json',record)
        active=c.ROOT/'active.json';recovered=None
        if active.exists():
            value=json.loads(r.stable_bytes(active));opid=value['operation_id']
            if not re.fullmatch('r032-[a-z0-9-]+',opid):raise ValueError('foreign retained owner')
            spec_path=c.ROOT/'operations'/opid/'spec.json';raw=r.stable_bytes(spec_path)
            if r.sha(raw)!=value['spec_sha256']:raise ValueError('retained owner specification changed')
            spec=json.loads(raw);source=r.no_links(spec['packet'])
            if source.parent!=c.ROOT or spec['operation']!=str(c.ROOT/'operations'/opid):raise ValueError('foreign retained source/path')
            c.packet(source,spec['packet_sha256'])
            challenge=secrets.token_hex(32)
            observed=json.loads(c.command(['/usr/bin/python3','-B',str(source/'target.py'),'observe',str(spec_path),value['spec_sha256'],challenge],timeout=25))
            proof=observed['proof'];final=observed['finalizer']
            safe=(observed['challenge']==challenge and observed['target_spec_sha256']==value['spec_sha256'] and observed['machine_id']==c.machine_id() and observed['current_boot_id']==c.boot_id() and proof['spec_sha256']==c.admission.digest(c.admission_spec(spec)) and proof['incumbent_id']==spec['incumbent']['id'] and proof['holds_sha256']==c.admission.digest(spec['hold_bindings']) and proof['healthy'] is True and proof['service_inactive'] is True and proof['state'] in ('completed','aborted_restored') and final.get('verified') is True and final.get('boot_id')==c.boot_id() and final.get('spec_sha256')==value['spec_sha256'] and observed['writer_controls_restored'] is True)
            if safe:
                recovered={'boot_id':c.boot_id(),'machine_id':c.machine_id()};record['owner_action']='fresh_current_owner_verification_only'
            else:
                # Exact retained implementation reconciles state, never capture effects.
                result=c.command(['/usr/bin/python3','-B',str(source/'target.py'),'startup',str(spec_path),value['spec_sha256']],timeout=25)
                recovered=json.loads(result);record['owner_action']='retained_owner_state_reconciliation'
            if recovered['boot_id']!=c.boot_id() or recovered['machine_id']!=c.machine_id():raise ValueError('retained recovery boot mismatch')
        elif any((c.ROOT/'operations').iterdir()):raise ValueError('orphan operations require explicit reconciliation')
        record.update(admission_open=True,recovered_operation=None if recovered is None else opid,at=time.time())
        c.atom(c.ROOT/'boot-admission.json',record)
        r.write_new(c.ROOT/('boot-reconciliation-'+str(time.time_ns())+'.json'),r.encode(record))
        return record
    finally:os.close(fd)

if __name__=='__main__':print(json.dumps(reconcile(sys.argv[1])))
