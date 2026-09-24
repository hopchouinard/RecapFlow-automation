"""Infisical candidate boundary. Exact user-authorized development folder; no file-authority fallback."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
from uuid import UUID

PROJECT = 'a508e594-7686-43a1-9b0f-cafa8b348ad4'
ENVIRONMENT = 'prod'
DEVELOPMENT_PATH = '/development/community-brain-dev/request027'



class Authority:
    def __init__(self, project, environment, path, lease):
        UUID(project)
        if (project, environment, path) != (PROJECT, ENVIRONMENT, DEVELOPMENT_PATH):
            raise ValueError('exact authorized Request027 development folder required')
        self.project, self.environment, self.path, self.lease = project, environment, path, lease

    def cli(self, args):
        self.lease.check()
        result = subprocess.run(['infisical', *args, '--projectId', self.project,
            '--env', self.environment, '--path', self.path,
            '--domain', os.environ['INFISICAL_API_URL'],
            '--token', os.environ['INFISICAL_TOKEN'], '--silent'],
            capture_output=True, text=True, timeout=30)
        self.lease.check()
        if result.returncode:
            raise RuntimeError('development Infisical operation failed; reconcile persisted state')
        return result.stdout

    def read(self):
        entries = json.loads(self.cli(['secrets', '--output', 'json',
                                      '--include-imports=false', '--expand=false']))
        if isinstance(entries, dict):
            entries = entries.get('secrets', entries.get('data', []))
        return {entry['secretKey']: entry['secretValue'] for entry in entries or []}

    def save(self, updates):
        # Preserve the deployed read/save/read equality contract. A lost response
        # does not authorize a retry: first reconcile by reading the actual store.
        before = self.read()
        if not updates or any(not key.startswith('CB_') for key in updates):
            raise ValueError('unexpected secret name')
        if any(not isinstance(value, str) or any(c in value for c in ("'", '\n', '\r'))
               for value in updates.values()):
            raise ValueError('unsafe secret serialization')
        with tempfile.TemporaryDirectory(prefix='cbm-r027-') as temporary:
            path = Path(temporary) / 'values.env'
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            with os.fdopen(fd, 'w') as stream:
                stream.write(''.join(key + "='" + value + "'\n" for key, value in updates.items()))
            self.cli(['secrets', 'set', '--file', str(path)])
        after = self.read()
        if after != {**before, **updates}:
            raise RuntimeError('authority verification mismatch; preserve overlap and reconcile')
