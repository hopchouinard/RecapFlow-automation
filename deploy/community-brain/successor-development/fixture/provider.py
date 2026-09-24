"""Only deterministic embedding and model-list fixtures; never retrieval/inference."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_): pass
    def reply(self, status, body):
        raw=json.dumps(body).encode()
        self.send_response(status);self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(raw)));self.end_headers();self.wfile.write(raw)
    def do_GET(self):
        if self.path=='/v1/models':
            self.reply(200,{'data':[{'id':'cbm-synthetic-model','object':'model','owned_by':'fixture'}]})
        else:self.reply(404,{'code':'absent'})
    def do_POST(self):
        body=json.loads(self.rfile.read(int(self.headers.get('Content-Length','0'))) or '{}')
        if self.path=='/api/embed':
            values=body['input'];values=[values] if isinstance(values,str) else values
            self.reply(200,{'model':'nomic-embed-text','embeddings':[[1.0]+[0.0]*767 for _ in values]})
        else:self.reply(403,{'code':'inference_and_retrieval_not_provided'})

if __name__=='__main__':ThreadingHTTPServer(('0.0.0.0',8999),Handler).serve_forever()
