"""VM108 loopback-only health relay for Docker's unpublished internal network.

Docker on this host records PortBindings on internal networks without opening
the host listener. This explicit test relay verifies the sole running port owner;
it is not production ingress and never permits ambiguity or external egress.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import socket
import subprocess
import urllib.request
import urllib.error

ALLOWED = {'cbm-r029-api', 'cbm-r029-normal-api', 'cbm-r029-readiness-api', 'cbm-r029-partial-api'}
PORTS = {'8090/tcp': [{'HostIp':'127.0.0.1','HostPort':'19930'}]}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path not in ('/health','/api/v1/me'):
            self.send_error(404); return
        try:
            ids=subprocess.run(['docker','ps','-q'],capture_output=True,check=True,text=True,timeout=10).stdout.split()
            rows=json.loads(subprocess.run(['docker','inspect',*ids],capture_output=True,check=True,text=True,timeout=10).stdout)
            owners=[r for r in rows if r['Name'].lstrip('/') in ALLOWED and r['State']['Running']
                    and r['HostConfig']['PortBindings']==PORTS]
            if len(owners)!=1:raise ValueError('ambiguous or absent serving owner')
            row=owners[0]
            network=row['NetworkSettings']['Networks']
            if set(network)!={'cbm-r029_default'}:raise ValueError('unexpected network')
            opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
            try:
                result=opener.open('http://'+network['cbm-r029_default']['IPAddress']+':8090'+self.path,timeout=5)
            except urllib.error.HTTPError as error:
                result=error
            raw=result.read()
            self.send_response(result.status)
            self.send_header('Content-Type','application/json')
            self.send_header('X-CBM-Container-Id',row['Id'])
            self.send_header('Content-Length',str(len(raw)))
            self.end_headers();self.wfile.write(raw)
        except Exception:
            self.send_error(503,'Serving owner unavailable')


if __name__=='__main__':
    if socket.gethostname()!='community-brain-dev':raise ValueError('development only')
    ThreadingHTTPServer(('127.0.0.1',19930),Handler).serve_forever()
