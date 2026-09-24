"""Exercise actual restored evidence with retained, separately named negative copies."""
import copy,json,shutil,sys,time
from pathlib import Path
import common as c
import database as db
import candidate
r=c.r

def check(spec_path,sha,template_path):
    s=c.load_spec(spec_path,sha,check_time=False);op=Path(s['operation'])
    result=json.loads(r.stable_bytes(op/'worker-result.json'));manifest=result['manifest_sha256']
    evidence=op/'evidence';positive=db.verify_evidence(evidence,s,manifest)
    template=json.loads(r.stable_bytes(Path(template_path)))
    prep=candidate.prepare(template,evidence,s,manifest)
    root=op/'negative-evidence';root.mkdir(mode=0o700)
    receipt=json.loads(r.stable_bytes(evidence/'database-receipt.json'))
    cases=[]
    def case(name,edit=None,spec_edit=None,digest=None):
        dst=root/name;shutil.copytree(evidence,dst)
        local=copy.deepcopy(s);v=copy.deepcopy(receipt)
        if edit:edit(dst,v)
        if spec_edit:spec_edit(local)
        c.atom(dst/'database-receipt.json',v)
        try:db.verify_evidence(dst,local,digest or manifest)
        except (ValueError,KeyError,FileNotFoundError,TypeError) as exc:
            cases.append({'case':name,'rejected':True,'exception':type(exc).__name__});return
        raise AssertionError('negative accepted: '+name)
    case('missing_before',lambda d,v:(d/'before.json').unlink())
    case('extra_file',lambda d,v:(d/'unexpected').write_text('extra'))
    case('unknown_acceptance_flag',lambda d,v:v.update(database_accepted=True))
    case('production_scope',lambda d,v:v.update(scope='production'))
    case('production_spec',spec_edit=lambda s:s.update(scope='production'))
    for key in ('owner_id','operation_id','capture_id','packet_sha256','manifest_sha256'):
        case('mixed_'+key,lambda d,v,k=key:v.update({k:'wrong-attempt'}))
    case('external_manifest_mismatch',digest='0'*64)
    case('dump_digest',lambda d,v:v['dump'].update(sha256='0'*64))
    case('dump_extra_flag',lambda d,v:v['dump'].update(accepted=True))
    case('before_digest',lambda d,v:v.update(before_sha256='0'*64))
    case('after_digest',lambda d,v:v.update(after_sha256='0'*64))
    case('foreign_restore',lambda d,v:v.update(restored=str(op/'other')))
    case('old_observation',lambda d,v:v.update(observed_before=s['deadlines']['prepare_by']-601))
    case('future_observation',lambda d,v:v.update(observed_after=s['deadlines']['validate_by']+1))
    case('stale_deadline',lambda d,v:v.update(deadline_epoch=1),lambda s:s['deadlines'].update(validate_by=1))
    case('same_database_server',lambda d,v:v.update(destination_identity=copy.deepcopy(v['source_identity'])))
    case('forged_server_system_id',lambda d,v:v['destination_identity'].update(system_identifier='forged'))
    case('unknown_server_flag',lambda d,v:v['destination_identity'].update(accepted=True))
    case('missing_server_field',lambda d,v:v['destination_identity'].pop('version'))
    def after_change(field):
        def edit(d,v):
            a=json.loads(r.stable_bytes(d/'after.json'))
            if field=='tables':a[field]['jobs']['rows']+=1
            elif field=='sequences':next(iter(a[field].values()))['last_value']+=1
            elif field=='relationships':a[field]['unknown_attempts']=0
            elif field=='file_references':a[field][0]['sha256']='0'*64
            elif field=='schema':a[field]['indexes']=[]
            elif field=='unknown':a['accepted']=True
            c.atom(d/'after.json',a);v['after_sha256']=r.sha(r.stable_bytes(d/'after.json'))
        return edit
    for field in ('tables','sequences','relationships','file_references','schema','unknown'):case('canonical_'+field,after_change(field))
    # Independent shape checks ensure even matching observations cannot add flags.
    before=json.loads(r.stable_bytes(evidence/'before.json'))
    for field in ('schema','tables','sequences','relationships'):
        v=copy.deepcopy(before)
        if field=='schema':v[field]['accepted']=True
        elif field=='relationships':v[field]['accepted']=True
        else:next(iter(v[field].values()))['accepted']=True
        try:db.validate_observation(v)
        except ValueError:cases.append({'case':'unknown_nested_'+field,'rejected':True})
        else:raise AssertionError(field)
    for change in ('filled_slot','enabled'):
        t=copy.deepcopy(template)
        if change=='enabled':t['deployable']=True
        else:t['required_evidence'][next(iter(t['required_evidence']))]=positive
        try:candidate.prepare(t,evidence,s,manifest)
        except ValueError:cases.append({'case':'candidate_'+change,'rejected':True})
        else:raise AssertionError(change)
    out={'positive':positive,'candidate':prep,'negative_cases':cases,'negative_count':len(cases),'retained_negative_path':str(root),'at':time.time()}
    r.write_new(op/'evidence-checks.json',r.encode(out));print(json.dumps(out))

if __name__=='__main__':check(*sys.argv[1:])
