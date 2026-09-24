"""Reviewed serving activation; never clears processing holds or restores data.

Run on the target host with an externally pinned plan. Source, compose, private
configuration and recovery receipts are bound by SHA256. No secret values are
written to the journal. An uncertain absent/stopped target requires reconciliation.
"""
import argparse
from contextlib import ExitStack
import fcntl
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import time
import urllib.request


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def atomic(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + '.tmp')
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w') as stream:
        json.dump(value, stream, sort_keys=True, indent=2)
        stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)
    fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try: os.fsync(fd)
    finally: os.close(fd)


def command(args):
    result = subprocess.run(args, capture_output=True, timeout=180)
    if result.returncode:
        raise RuntimeError('command failed; reconcile actual container state before retry')
    return result.stdout


class Docker:
    def inspect(self, name):
        result = subprocess.run(['docker', 'inspect', name], capture_output=True, timeout=20)
        if result.returncode:
            # Distinguish an absent container from a failed Docker daemon/query.
            command(['docker', 'info', '--format', '{{.ID}}'])
            if b'no such object' in result.stderr.lower() or b'no such container' in result.stderr.lower():
                return None
            raise RuntimeError('container inspection unavailable')
        return json.loads(result.stdout)[0]

    def stop(self, container):
        command(['docker', 'stop', '--time', '30', container])

    def start(self, container):
        command(['docker', 'start', container])

    def create(self, plan, service):
        command(['docker', 'compose', '-f', plan['compose'], 'up', '-d',
                 '--no-deps', '--no-build', '--pull', 'never', service['service']])

    def health(self, row, target):
        network = row['NetworkSettings']['Networks'][target['network']]
        url = 'http://' + network['IPAddress'] + ':' + str(target['probe_port']) + '/health'
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        deadline = time.monotonic() + target.get('health_timeout', 120)
        while time.monotonic() < deadline:
            try:
                with opener.open(url, timeout=3) as response:
                    if response.status == 200:
                        return
            except (OSError, ValueError):
                pass
            time.sleep(1)
        raise RuntimeError('candidate health failed; rollback or reconcile before proceeding')


def fingerprint(row):
    # Hash configuration without exposing environment values in receipts.
    value = {k: row[k] for k in ('Id', 'Image', 'Config', 'HostConfig')}
    value['Mounts'] = sorted(row['Mounts'], key=lambda mount: mount['Destination'])
    return digest(json.dumps(value, sort_keys=True).encode())


def validate_runtime(row, target):
    if not row or row['Image'] != target['image']:
        raise ValueError('unexpected runtime image')
    host = row['HostConfig']
    actual = {
        'memory': host['Memory'], 'nano_cpus': host['NanoCpus'],
        'read_only_root': host['ReadonlyRootfs'], 'user': row['Config']['User'],
        'command': row['Config']['Cmd'], 'ports': host['PortBindings'] or {},
        'binds': sorted([{'source': m['Source'], 'target': m['Destination'], 'read_only': not m['RW']}
                         for m in row['Mounts'] if m['Type'] == 'bind'], key=lambda m: m['target']),
        'volumes': sorted([{'name': m['Name'], 'target': m['Destination'], 'read_only': not m['RW']}
                           for m in row['Mounts'] if m['Type'] == 'volume'], key=lambda m: m['target']),
    }
    if actual != target['runtime'] or set(row['NetworkSettings']['Networks']) != {target['network']}:
        raise ValueError('runtime deviates from reviewed bindings')


def preserved(plan):
    values = {}
    for name in plan['holds']:
        path = Path(name)
        if path.is_symlink() or not path.is_file():
            raise ValueError('required preserved hold missing or symlinked')
        stat = path.stat()
        values[name] = {'sha256': digest(path.read_bytes()), 'mode': stat.st_mode & 0o777,
                        'inode': stat.st_ino, 'device': stat.st_dev}
    return values


def validate_plan(plan, expected):
    raw = Path(plan).read_bytes()
    if digest(raw) != expected:
        raise ValueError('plan identity mismatch')
    value = json.loads(raw)
    if value['schema'] != 1 or value['phase'] != 'serving-only':
        raise ValueError('unsupported activation phase')
    if value['hostname'] not in ('community-brain-dev', 'community-brain-prod'):
        raise ValueError('unsupported target host')
    if socket.gethostname() != value['hostname'] or os.geteuid() != 0:
        raise ValueError('target host/root mismatch')
    root = Path(value['state_root'])
    if value['hostname'] == 'community-brain-prod':
        if str(root) != '/srv/community-brain':
            raise ValueError('production state boundary mismatch')
    elif not root.is_relative_to('/srv/dev-data/workspaces'):
        raise ValueError('development state boundary mismatch')
    locks = [str(root/'automation/runner.lock'), str(root/'files/.manual-worker.lock'), str(root/'files/.submission.lock')]
    holds = [str(root/'automation'/n) for n in ('paused', 'attention.json', 'boot-state.json')]
    if value['locks'] != locks or value['holds'] != holds:
        raise ValueError('ordered locks/holds mismatch')
    if not value['candidates'] or len({x['container'] for x in value['candidates']}) != len(value['candidates']):
        raise ValueError('invalid candidate set')
    if value['incumbent']['container'] in {x['container'] for x in value['candidates']}:
        raise ValueError('incumbent cannot be replaced in place')
    required = {value['compose'], str(Path(__file__).resolve()), value['recovery_receipt']}
    if not required <= set(value['files']):
        raise ValueError('unbound source/compose/recovery evidence')
    for name, sha in value['files'].items():
        p = Path(name)
        if not p.is_absolute() or p.is_symlink() or digest(p.read_bytes()) != sha:
            raise ValueError('bound input changed')
    compose = json.loads(Path(value['compose']).read_text())
    for target in value['candidates']:
        spec = compose['services'][target['service']]
        if spec['container_name'] != target['container'] or spec['image'] != target['image']:
            raise ValueError('compose target mismatch')
        for env in spec.get('env_file', []):
            if env not in value['files']:
                raise ValueError('private environment not bound')
    recovery = json.loads(Path(value['recovery_receipt']).read_text())
    if recovery.get('verified') is not True or recovery.get('state_root') != str(root):
        raise ValueError('paired recovery receipt required')
    if value['hostname'] == 'community-brain-prod':
        if any(recovery.get(key) is not True for key in
               ('webui_restore_verified', 'signing_material_verified', 'off_host_backup_verified')):
            raise ValueError('protected production restoration evidence incomplete')
    return value


class Activation:
    def __init__(self, plan, identity, journal, engine=None):
        self.plan, self.identity, self.path = plan, identity, Path(journal)
        self.engine = engine or Docker()
        self.state = json.loads(self.path.read_text()) if self.path.exists() else None
        if self.state and self.state['plan_sha256'] != identity:
            raise ValueError('journal belongs to another plan')

    def save(self):
        atomic(self.path, self.state)

    def unchanged(self):
        if preserved(self.plan) != self.state['holds']:
            raise ValueError('processing holds changed; no action permitted')
        row = self.engine.inspect(self.plan['incumbent']['container'])
        if not row or fingerprint(row) != self.state['incumbent_fingerprint']:
            raise ValueError('incumbent recovery container changed')
        return row

    def begin(self):
        if self.state: return
        row = self.engine.inspect(self.plan['incumbent']['container'])
        if not row or row['Id'] != self.plan['incumbent']['id'] or not row['State']['Running']:
            raise ValueError('incumbent before-state mismatch')
        if fingerprint(row) != self.plan['incumbent']['fingerprint']:
            raise ValueError('incumbent before-state drift')
        if any(self.engine.inspect(x['container']) for x in self.plan['candidates']):
            raise ValueError('candidate exists without activation journal')
        self.engine.health(row, self.plan['incumbent'])
        self.state = {'plan_sha256': self.identity, 'phase': 'prepared',
                      'incumbent_fingerprint': fingerprint(row), 'holds': preserved(self.plan),
                      'candidate_intents': {}, 'candidate_ids': {}}
        self.save()

    def activate(self):
        self.begin(); incumbent = self.unchanged()
        if self.state['phase'] in ('rolling_back', 'rolled_back'):
            raise ValueError('rollback is terminal; new reviewed plan required')
        if self.state['phase'] == 'prepared':
            self.state['phase'] = 'stopping_incumbent'; self.save()
            self.engine.stop(incumbent['Id'])
        elif self.state['phase'] == 'stopping_incumbent' and incumbent['State']['Running']:
            raise RuntimeError('uncertain stop; reconcile rather than replay')
        if self.engine.inspect(incumbent['Id'])['State']['Running']:
            raise RuntimeError('incumbent still owns serving endpoint')
        for target in self.plan['candidates']:
            self.unchanged()
            name = target['container']; row = self.engine.inspect(name)
            if name not in self.state['candidate_intents']:
                if row: raise ValueError('unowned candidate appeared')
                self.state['candidate_intents'][name] = True; self.save()
                self.engine.create(self.plan, target)
                row = self.engine.inspect(name)
            elif not row or not row['State']['Running']:
                raise RuntimeError('uncertain candidate effect; no replay')
            validate_runtime(row, target)
            if name in self.state['candidate_ids'] and row['Id'] != self.state['candidate_ids'][name]:
                raise ValueError('candidate identity changed')
            self.state['candidate_ids'][name] = row['Id']; self.save()
            self.engine.health(row, target)
        self.unchanged()
        self.state['phase'] = 'active'; self.save()
        return {'phase': 'active', 'processing_holds_preserved': True}

    def rollback(self):
        if not self.state: raise ValueError('no activation to roll back')
        incumbent = self.unchanged()
        self.state['phase'] = 'rolling_back'; self.save()
        for target in reversed(self.plan['candidates']):
            row = self.engine.inspect(target['container'])
            if target['container'] not in self.state['candidate_intents']:
                if row: raise ValueError('unowned rollback target')
                continue
            if not row: raise RuntimeError('uncertain absent candidate; reconcile first')
            validate_runtime(row, target)
            expected_id = self.state['candidate_ids'].get(target['container'])
            if expected_id and row['Id'] != expected_id: raise ValueError('replacement changed')
            if row['State']['Running']: self.engine.stop(row['Id'])
        if not incumbent['State']['Running']:
            self.engine.start(incumbent['Id'])
        self.engine.health(self.engine.inspect(incumbent['Id']), self.plan['incumbent'])
        self.unchanged()
        self.state['phase'] = 'rolled_back'; self.save()
        return {'phase': 'rolled_back', 'replacement_data_retained': True,
                'processing_holds_preserved': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=['activate', 'rollback'])
    parser.add_argument('plan'); parser.add_argument('expected_plan_sha256'); parser.add_argument('journal')
    args = parser.parse_args()
    plan = validate_plan(args.plan, args.expected_plan_sha256)
    with ExitStack() as stack:
        for name in plan['locks']:
            fd = os.open(name, os.O_RDWR | os.O_NOFOLLOW)
            stack.callback(os.close, fd)
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            if os.fstat(fd).st_ino != os.stat(name).st_ino:
                raise ValueError('lock inode changed')
        controller = Activation(plan, args.expected_plan_sha256, args.journal)
        print(json.dumps(getattr(controller, args.operation)()))


if __name__ == '__main__':
    main()
