"""Isolated synthetic retrieval/model-list fixture. Never performs inference."""
import hashlib
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

CONTROL = Path('/state/control.json')


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def reply(self, status, value):
        raw = json.dumps(value).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path == '/v1/models':
            self.reply(200, {'object': 'list', 'data': [
                {'id': 'cbm-synthetic-model', 'object': 'model', 'owned_by': 'request026-fixture'}
            ]})
        elif self.path == '/health':
            self.reply(200, {'fixture': True})
        else:
            self.reply(404, {'error': 'fixture route absent'})

    def do_POST(self):
        body = self.rfile.read(int(self.headers.get('Content-Length', '0')))
        if self.path != '/retrieval/query':
            self.reply(403, {'error': 'inference and other writes prohibited'})
            return
        control = json.loads(CONTROL.read_text())
        digest = hashlib.sha256(self.headers.get('X-API-Key', '').encode()).hexdigest()
        if digest not in control['accepted_sha256']:
            self.reply(401, {'error': 'development credential rejected'})
            return
        value = json.loads(body)
        if not isinstance(value.get('question'), str):
            self.reply(422, {'error': 'question required'})
            return
        self.reply(200, {'chunks': [{
            'ground_truth': {'chunk_id': 'request026:synthetic:001',
                             'session_id': 'request026-synthetic',
                             'source_file': 'synthetic.txt',
                             'session_date': '2026-09-20',
                             'full_text': 'Synthetic migration acceptance sentence.'},
            'derived_metadata': {'speakers_spoke': ['Fixture'], 'topic_label': 'Migration test'},
            'provenance': {'fixture': True}, 'similarity': 1.0
        }]})


if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0', 8999), Handler).serve_forever()
