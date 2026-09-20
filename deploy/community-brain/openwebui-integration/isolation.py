"""Read-only network acceptance for this exact VM108 fixture."""
import errno
import json
import os
import socket
import subprocess
import run as r

assert socket.gethostname()=='community-brain-dev' and os.geteuid()==0
network=json.loads(r.command(['docker','network','inspect','cbm-integration-dev_default']))[0]
assert network['Internal']
rows=json.loads(r.command(['docker','inspect',*[r.container(s) for s in ('api','webui','provider','pg')]]))
assert all(set(row['NetworkSettings']['Networks'])=={'cbm-integration-dev_default'} for row in rows)
assert all(not row['HostConfig'].get('PortBindings') for row in rows)
script="import socket; s=socket.socket();s.settimeout(1);print(s.connect_ex(('203.0.113.1',443)))"
result=subprocess.run(['docker','exec',r.container('api'),'python','-c',script],capture_output=True,text=True)
assert result.returncode==0 and int(result.stdout.strip())==errno.ENETUNREACH
r.atomic(r.ROOT/'isolation.json',{'internal_network':True,'no_published_ports':True,
 'only_isolated_network_attached':True,'api_external_route_unreachable':True,
 'scope':'candidate network and documentation-address route probe; not packet capture'})
print('Isolation checks passed')
