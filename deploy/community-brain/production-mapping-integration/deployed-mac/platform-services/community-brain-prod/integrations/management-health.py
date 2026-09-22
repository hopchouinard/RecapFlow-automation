"""Publish only backup/expiry metadata via the existing node-exporter textfile path."""
import datetime,json,pathlib,time
from secret_store import read,remote
from maintenance_policy import expiry_state
v=read();now=datetime.datetime.now(datetime.timezone.utc);identities=json.loads(v['CB_SERVICE_IDENTITIES']);assert len(identities) in (5,10)
records=[]
for i in identities:
    assert i['subject'] in ['community-brain-prod-read-probe','community-brain-prod-metrics-probe','community-brain-openwebui','community-brain-prod-mac-collector','community-brain-prod-manual-operator']
    records.append({'subject':i['subject'],'expires_at':i['expires_at'],'expires_utc':datetime.datetime.fromtimestamp(i['expires_at'],datetime.timezone.utc).isoformat(),'state':expiry_state(now,i['expires_at']),'owner':'Mac management; automatic seven-day Infisical renewal'})
state_root=pathlib.Path.home()/'.local/state/community-brain-management';backup=json.loads((state_root/'pre-pbs-state.json').read_text())
renewal_path=state_root/'service-renewal-status.json'
renewal=json.loads(renewal_path.read_text()) if renewal_path.exists() else {'state':'missing','checked_at':0}
renewal_failed=renewal.get('state') in ['failed','missing']
body=f'cbm_management_checked_at_seconds {now.timestamp()}\ncbm_backup_copy_valid_until_seconds {backup["next_due_epoch"]}\ncbm_backup_copy_failed {int(backup["state"]=="failed")}\n'
body+=f'cbm_service_renewal_failed {int(renewal_failed)}\ncbm_service_renewal_checked_at_seconds {renewal.get("checked_at",0)}\n'
for i in records:body+='cbm_service_identity_expires_at_seconds{subject="'+i['subject']+'"} '+str(i['expires_at'])+'\n'
public={'checked_at':now.isoformat(),'service_identities':records,'backup':{k:backup.get(k) for k in ['state','next_due_epoch','checked_at','failure']},'mac_offline_detection':'Prometheus metadata age alert after2h; overdue pre-PBS freshness alert before next window','automatic_renewal':True,'renewal':renewal}
code=r'''import pathlib,json,sys,os
d=json.load(sys.stdin);root=pathlib.Path('/var/lib/prometheus/node-exporter');assert root.is_dir();p=root/'community-brain-management.prom';t=p.with_suffix('.tmp');t.write_text(d['metrics']);t.chmod(0o644);t.replace(p)
r=pathlib.Path('/srv/community-brain/management-status');r.mkdir(mode=0o700,exist_ok=True);p=r/'maintenance.json';t=p.with_suffix('.tmp');t.write_text(json.dumps(d['public'],indent=2)+'\n');t.chmod(0o600);t.replace(p);print('Management metadata published')
'''
assert remote('pchouinard@10.1.30.21',code,{'metrics':body,'public':public}).strip()=='Management metadata published'
p=state_root/'identity-expiry-status.json';t=p.with_suffix('.tmp');t.write_text(json.dumps(public,indent=2)+'\n');t.chmod(0o600);t.replace(p)
print(json.dumps(public));raise SystemExit(1 if renewal_failed or any(r['state']!='ok' for r in records) or backup['state']=='failed' or now.timestamp()>backup['next_due_epoch'] else 0)
