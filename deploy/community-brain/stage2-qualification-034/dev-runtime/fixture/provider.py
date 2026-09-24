"""Deterministic model-list, embedding and synthetic chat; no external provider."""
import json
import time
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
        elif self.path=='/v1/chat/completions':
            assert body['model']=='cbm-synthetic-model'
            answer='Request034 synthetic model response. No paid provider or production data.'
            base={'id':'chatcmpl-cbm-r034','object':'chat.completion','created':int(time.time()),
                  'model':'cbm-synthetic-model'}
            if body.get('stream'):
                self.send_response(200)
                self.send_header('Content-Type','text/event-stream')
                self.send_header('Cache-Control','no-cache')
                self.end_headers()
                for delta,finish in [({'role':'assistant','content':answer},None),({},'stop')]:
                    chunk={**base,'object':'chat.completion.chunk',
                           'choices':[{'index':0,'delta':delta,'finish_reason':finish}]}
                    self.wfile.write(('data: '+json.dumps(chunk)+'\n\n').encode())
                self.wfile.write(b'data: [DONE]\n\n')
                self.wfile.flush()
            else:
                self.reply(200,{**base,'choices':[{'index':0,'message':{'role':'assistant',
                            'content':answer},'finish_reason':'stop'}],
                            'usage':{'prompt_tokens':0,'completion_tokens':0,'total_tokens':0}})
        else:self.reply(403,{'code':'inference_and_retrieval_not_provided'})

if __name__=='__main__':ThreadingHTTPServer(('0.0.0.0',8999),Handler).serve_forever()
