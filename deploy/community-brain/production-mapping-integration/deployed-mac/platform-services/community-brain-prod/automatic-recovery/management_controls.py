"""Capture current Mac renderer/scheduler code and scoped Authentik policy only.

No Infisical bootstrap file, SSH key or management login is copied to a VM.
"""
import hashlib
import json
import os
from pathlib import Path
import tarfile
import tempfile
from checkpoint_acceptance import atomic
from transport import PVE, VM

from human_access import APPS, HUMANS, mapping_expression, policy_expression

AUTH_CODE = ('APPS=' + repr(APPS) + '\nHUMANS=' + repr(HUMANS) + '\nMAPPINGS=' + repr({s:mapping_expression(s) for s in APPS}) + '\nPOLICIES=' + repr({s:policy_expression(s) for s in APPS}) + '\n') + "\nimport json,hashlib\nfrom authentik.providers.oauth2.models import ScopeMapping,OAuth2Provider\nfrom authentik.core.models import Application,User,Group\nfrom authentik.policies.models import PolicyBinding\nfrom authentik.policies.expression.models import ExpressionPolicy\nresult={'request_id':'CBM-AKADMIN-20260917-018','humans':{},'apps':{}}\nfor pk,uuid in HUMANS.items():\n u=User.objects.get(pk=pk);assert u.is_active and str(u.uuid)==uuid\n assert u.username==({6:'pchouinard',4:'akadmin'}[pk])\n result['humans'][str(pk)]={'username':u.username,'uuid':str(u.uuid),'active':u.is_active}\nfor slug,expected in APPS.items():\n p=OAuth2Provider.objects.get(pk=expected['provider']);a=Application.objects.get(slug=slug)\n assert a.provider_id==p.pk and a.policy_engine_mode=='all'\n m=ScopeMapping.objects.get(pk=expected['mapping']);assert m.expression==MAPPINGS[slug] and m.scope_name=='profile'\n assert list(OAuth2Provider.objects.filter(property_mappings=m).values_list('pk',flat=True))==[p.pk]\n g=Group.objects.get(pk=expected['group']);assert g.name==expected['group_name'] and not g.is_superuser\n members=sorted(g.users.values_list('pk',flat=True));assert members==[4,6]\n bindings=list(PolicyBinding.objects.filter(target=a).order_by('order'))\n enabled=[b for b in bindings if b.enabled];assert len(enabled)==2\n group_bindings=[b for b in enabled if str(b.group_id)==str(g.pk) and b.policy_id is None and b.user_id is None]\n human_bindings=[b for b in enabled if b.policy_id is not None and b.group_id is None and b.user_id is None]\n assert len(group_bindings)==len(human_bindings)==1 and all(not b.negate and not b.failure_result for b in enabled)\n policy=ExpressionPolicy.objects.get(pk=human_bindings[0].policy_id)\n assert policy.expression==POLICIES[slug]\n assert list(PolicyBinding.objects.filter(policy=policy).values_list('target_id',flat=True))==[a.pk]\n result['apps'][slug]={'provider_id':p.pk,'client_id':p.client_id,'application_id':str(a.pk),'mapping_id':str(m.pk),'expression':m.expression,'scope_name':m.scope_name,'policy_id':str(policy.pk),'policy_expression':policy.expression,'group_id':str(g.pk),'group_members':members,'bindings':[{'pk':str(b.pk),'group_id':str(b.group_id) if b.group_id else None,'policy_id':str(b.policy_id) if b.policy_id else None,'user_id':b.user_id,'enabled':b.enabled,'order':b.order,'negate':b.negate,'failure_result':b.failure_result} for b in bindings]}\nprint(json.dumps(result,default=str))\n"


def auth(transport):
    code = "SCRIPT=" + repr(AUTH_CODE) + "\n" + r'''
import subprocess,json
r=subprocess.run(['pct','exec','301','--','docker','exec','platform-auth-server','ak','shell','-c',SCRIPT],capture_output=True,text=True,timeout=45)
assert r.returncode==0
value=json.loads(r.stdout.strip().splitlines()[-1]);print(json.dumps(value))
'''
    return transport.json(PVE, code, timeout=60)


def host(transport):
    code = r'''
import subprocess,json,pathlib,hashlib
r=subprocess.run(['crontab','-l'],capture_output=True,text=True);assert r.returncode in (0,1)
container=json.loads(subprocess.check_output(['docker','inspect','community-brain-production-staging-api-1']))[0]
mounts=sorted([{'source':m['Source'],'destination':m['Destination'],'rw':m['RW']} for m in container['Mounts']],key=lambda m:m['destination'])
print(json.dumps({'root_crontab':r.stdout,'image':container['Config']['Image'],'mounts':mounts,
'environment_sha256':hashlib.sha256(json.dumps(sorted(container['Config']['Env'])).encode()).hexdigest(),
'state_mount':json.loads(subprocess.check_output(['findmnt','-J','-T','/srv/community-brain/artifacts','-o','TARGET,SOURCE,FSTYPE']))}))
'''
    return transport.json(VM, code)


def capture(directory, job, transport):
    directory = Path(directory)
    library = Path.home() / ".local/lib/community-brain-management"
    integrations = "platform-services/community-brain-prod/integrations/"
    names = ["maintain.py", "maintain-hourly.py", "mac-intake.py", "mac_intake_policy.py",
             "platform-services/scripts/lib/infisical.sh",
             "platform-services/infisical/homelab-secret-authority.yaml"]
    names += [integrations + name for name in ("management-health.py", "manage.py", "provision-nats-tls.py",
              "copy-backup.py", "maintenance_policy.py", "run.sh", "pre-pbs-copy.py", "secret_store.py",
              "manual_api_runtime.py", "renew-app-tls.py", "renew-service-tokens.py",
              "service_renewal_policy.py", "service_renewal_live.py", "renewal_webui_control.py", "renewal_kuma.js")]
    automatic = library / "platform-services/community-brain-prod/automatic-recovery"
    names += [str(p.relative_to(library)) for p in automatic.glob("*.py") if not p.name.startswith("test_") and "rehearsal" not in p.name]
    files = {}
    for name in names:
        p = library / name
        if p.is_symlink() or not p.is_file():
            raise ValueError("missing active management control")
        data = p.read_bytes()
        files["library/" + name] = data
    agent = Path.home() / "Library/LaunchAgents/lab.patchoutech.community-brain-management.plist"
    files["launch-agent.plist"] = agent.read_bytes()
    policy = auth(transport)
    files["authentik-policy.json"] = (json.dumps(policy, sort_keys=True, indent=2) + "\n").encode()
    summary = {"job_id": job, "files": {name: {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)} for name, data in sorted(files.items())},
               "bootstrap_credentials_included": False}
    archive = directory / "management-controls.tar.gz"
    with tempfile.TemporaryDirectory(prefix="cbm-controls-") as temporary:
        base = Path(temporary)
        for name, data in files.items():
            p = base / name
            p.parent.mkdir(parents=True, mode=0o700, exist_ok=True)
            p.write_bytes(data)
            p.chmod(0o600)
        with archive.open("xb") as stream:
            os.fchmod(stream.fileno(), 0o600)
            with tarfile.open(fileobj=stream, mode="w:gz") as tar:
                for name in sorted(files):
                    tar.add(base / name, arcname=name, recursive=False)
            stream.flush()
            os.fsync(stream.fileno())
    # Verify all actual members after writing, not just a generated manifest.
    with tarfile.open(archive, "r:gz") as tar:
        assert {m.name for m in tar} == set(files)
        for member in tar.getmembers():
            assert member.isfile() and member.mode == 0o600
            data = tar.extractfile(member).read()
            assert data == files[member.name]
    atomic(directory / "management-controls.json", summary)
    atomic(directory / "host-controls.json", {"job_id": job, "host": host(transport), "auth": policy})
    return summary
