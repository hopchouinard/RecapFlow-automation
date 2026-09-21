"""Compile complete bindings from existing evidence; never infer restore success."""
import json
from pathlib import Path
import time
from activate import digest, preserved, fingerprint, Docker, atomic


def packet_files(root, expected):
    root = Path(root)
    manifest = root / 'packet-manifest.json'
    if root.is_symlink() or digest(manifest.read_bytes()) != expected:
        raise ValueError('sealed packet identity mismatch')
    entries = json.loads(manifest.read_text())
    actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    if actual != set(entries) | {'packet-manifest.json'}:
        raise ValueError('sealed packet file set mismatch')
    result = {str(manifest): expected}
    for name, item in entries.items():
        p = root / name
        if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):
            raise ValueError('unsafe packet member')
        if p.stat().st_size != item['bytes'] or digest(p.read_bytes()) != item['sha256']:
            raise ValueError('sealed packet bytes changed')
        result[str(p)] = item['sha256']
    return result


def evidence_files(path, state_root, packet_sha):
    """Accept the actual paired-restore schema, not a caller-supplied true flag."""
    path = Path(path)
    receipt = json.loads(path.read_text())
    required = ('restore_equal', 'webui_restore_integrity')
    if any(receipt.get(k) is not True for k in required):
        raise ValueError('actual paired restore evidence missing')
    if receipt.get('packet_manifest') != packet_sha or not receipt.get('restored_files'):
        raise ValueError('recovery packet/state binding missing')
    trees = ('files','config','corpus','meeting-archive','automation','automation-public','manual-approvals')
    for base in (Path(state_root), path.parent/'restored'):
        actual = {str(p.relative_to(base)) for name in trees for p in (base/name).rglob('*') if p.is_file()}
        if actual != set(receipt['restored_files']):
            raise ValueError('recovery state file set changed')
    files = {str(path): digest(path.read_bytes())}
    for name, sha in receipt['restored_files'].items():
        for base in (Path(state_root), path.parent / 'restored'):
            p = base / name
            if p.is_symlink() or not p.resolve().is_relative_to(base.resolve()) or digest(p.read_bytes()) != sha:
                raise ValueError('recovery state drift')
            files[str(p)] = sha
    db = path.parent / 'database.sql'
    if digest(db.read_bytes()) != receipt['database_sha256']:
        raise ValueError('recovery database artifact drift')
    for name in ('database.sql', 'state.tar', 'private-runtime.tar', 'webui.tar',
                 'before.json', 'restored-observation.json'):
        p = path.parent / name
        files[str(p)] = digest(p.read_bytes())
    before = json.loads((path.parent / 'before.json').read_text())
    after = json.loads((path.parent / 'restored-observation.json').read_text())
    for value in (before, after):
        for job in value['jobs']:
            job['stages'].sort(key=lambda stage: stage['name'])
    if before != after:
        raise ValueError('restored database observation differs')
    return files


def compile_plan(spec, output):
    """Spec is operator-reviewed metadata. Private values never enter the plan."""
    if Path(output).exists():
        raise ValueError('plan is immutable; use a fresh name')
    if spec['hostname'] != 'community-brain-dev':
        raise ValueError('production compilation disabled pending protected evidence')
    files = packet_files(spec['packet'], spec['packet_sha256'])
    for packet, expected in spec.get('additional_packets', {}).items():
        files.update(packet_files(packet, expected))
    recovery_packet = spec.get('recovery_packet_sha256', spec['packet_sha256'])
    if recovery_packet not in {spec['packet_sha256'], *spec.get('additional_packets', {}).values()}:
        raise ValueError('original recovery packet must remain sealed and bound')
    files.update(evidence_files(spec['recovery_receipt'], spec['state_root'], recovery_packet))
    receipt = json.loads(Path(spec['recovery_receipt']).read_text())
    signing = Path(spec['state_root']).parent/'private/webui.env'
    if digest(signing.read_bytes()) != receipt['signing_environment_sha256']:
        raise ValueError('external signing environment changed since recovery')
    compose = json.loads(Path(spec['compose']).read_text())
    inputs = {spec['compose'], *spec['configuration_files']}
    for target in spec['candidates']:
        service = compose['services'][target['service']]
        inputs.update(service.get('env_file', []))
        for mount in service.get('volumes', []):
            if isinstance(mount, dict) and mount['type'] == 'bind' and Path(mount['source']).is_file():
                inputs.add(mount['source'])
    for name in inputs:
        p = Path(name)
        if not p.is_absolute() or p.is_symlink() or not p.is_file():
            raise ValueError('missing configuration binding')
        files[name] = digest(p.read_bytes())
    engine = Docker()
    from activate import command
    resolved = json.loads(command(['docker', 'compose', '-f', spec['compose'], 'config', '--format', 'json']))
    spec = json.loads(json.dumps(spec))
    for target in spec['candidates']:
        image = json.loads(command(['docker', 'image', 'inspect', target['image']]))[0]
        environment = dict(item.split('=', 1) for item in image['Config'].get('Env', []))
        environment.update(resolved['services'][target['service']].get('environment', {}))
        target['environment_sha256'] = digest(json.dumps(sorted(k+'='+str(v) for k,v in environment.items())).encode())
        target['cap_drop'] = ['ALL']
        target['security_opt'] = ['no-new-privileges:true']
    row = engine.inspect(spec['incumbent']['container'])
    if not row or not row['State']['Running']:
        raise ValueError('running incumbent required')
    value = dict(spec, schema=2, phase='serving-only', files=files,
                 created_at=time.time(), expires_at=min(time.time()+4*3600, spec['deadline_epoch']))
    value['incumbent'] = dict(spec['incumbent'], id=row['Id'], fingerprint=fingerprint(row))
    value['hold_bindings'] = preserved(value)
    # Explicit volume identity and actual restored content are required.
    volumes = {}
    for name in spec['external_webui_volumes']:
        info = json.loads(command(['docker', 'volume', 'inspect', name]))[0]
        volumes[name] = digest(json.dumps(info, sort_keys=True).encode())
    if not volumes:
        raise ValueError('external WebUI volume binding required')
    value['volume_bindings'] = volumes
    atomic(output, value)
    return digest(Path(output).read_bytes())


def validate_bindings(value):
    if time.time() >= value['expires_at']:
        raise ValueError('plan is stale; review current state')
    bound = packet_files(value['packet'], value['packet_sha256'])
    for packet, expected in value.get('additional_packets', {}).items():
        bound.update(packet_files(packet, expected))
    if any(value['files'].get(p) != sha for p, sha in bound.items()):
        raise ValueError('incomplete packet bindings')
    if preserved(value) != value['hold_bindings']:
        raise ValueError('compiled processing holds changed')
    from activate import command
    for name, expected in value['volume_bindings'].items():
        row = json.loads(command(['docker', 'volume', 'inspect', name]))[0]
        if digest(json.dumps(row, sort_keys=True).encode()) != expected:
            raise ValueError('external WebUI volume identity changed')
