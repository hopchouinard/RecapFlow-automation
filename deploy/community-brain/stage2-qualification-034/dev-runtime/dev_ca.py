"""Issue one short-lived development NATS leaf through the existing Step CA.

Private key material stays in the local 0700 request state and never enters a
receipt or source packet. This does not change a production listener or secret.
"""
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile

os.umask(0o077)
STATE = Path.home() / '.local/state/community-brain-management/request034'
NAME = 'nats'


def ca(args):
    command = ['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=8', 'traefik',
               shlex.join(['sudo', '-n', 'docker', 'exec', 'step-ca', *args])]
    result = subprocess.run(command, capture_output=True, timeout=45)
    if result.returncode:
        raise RuntimeError('Step CA development leaf operation failed; private output suppressed')
    return result.stdout


def main():
    STATE.mkdir(mode=0o700, parents=True, exist_ok=True)
    assert STATE.stat().st_mode & 0o777 == 0o700
    certificate, key = STATE / 'nats.crt', STATE / 'nats.key'
    assert not certificate.exists() and not key.exists(), 'existing development leaf: reconcile first'
    directory = ca(['mktemp', '-d', '/tmp/cbm-r034-nats.XXXXXXXX']).decode().strip()
    assert directory.startswith('/tmp/cbm-r034-nats.') and '\n' not in directory
    try:
        ca(['step', 'ca', 'certificate', NAME, directory + '/cert.pem', directory + '/key.pem',
            '--san', NAME, '--provisioner', 'admin@patchoutech.lab',
            '--password-file', '/home/step/secrets/password',
            '--ca-url', 'https://localhost:9000', '--root', '/home/step/certs/root_ca.crt',
            '--not-after', '24h'])
        leaf = ca(['cat', directory + '/cert.pem'])
        secret = ca(['cat', directory + '/key.pem'])
        root = ca(['cat', '/home/step/certs/root_ca.crt'])
        intermediate = ca(['cat', '/home/step/certs/intermediate_ca.crt'])
    finally:
        ca(['rm', '-rf', directory])
    with tempfile.TemporaryDirectory() as temporary:
        leaf_file = Path(temporary) / 'leaf.pem'
        root_file = Path(temporary) / 'root.pem'
        intermediate_file = Path(temporary) / 'intermediate.pem'
        key_file = Path(temporary) / 'key.pem'
        leaf_file.write_bytes(leaf)
        root_file.write_bytes(root)
        intermediate_file.write_bytes(intermediate)
        key_file.write_bytes(secret)
        subprocess.run(['openssl', 'verify', '-CAfile', str(root_file), '-untrusted',
                        str(intermediate_file), str(leaf_file)],
                       check=True, capture_output=True)
        detail = subprocess.run(['openssl', 'x509', '-in', str(leaf_file), '-noout',
                                 '-text'], check=True, capture_output=True).stdout.decode()
        assert 'DNS:' + NAME in detail, 'issued leaf hostname mismatch'
        cert_pub = subprocess.run(['openssl', 'x509', '-in', str(leaf_file), '-pubkey', '-noout'],
                                  check=True, capture_output=True).stdout
        key_pub = subprocess.run(['openssl', 'pkey', '-in', str(key_file), '-pubout'],
                                 check=True, capture_output=True).stdout
        assert cert_pub == key_pub, 'private key mismatch'
        dates = subprocess.run(['openssl', 'x509', '-in', str(leaf_file), '-noout',
                                '-startdate', '-enddate'], check=True, capture_output=True).stdout.decode().splitlines()
    for path, contents in ((certificate, leaf + intermediate), (key, secret),
                           (STATE / 'ca-root.crt', root)):
        with path.open('xb') as output:
            output.write(contents)
        path.chmod(0o600)
    receipt = {'issued_for': NAME, 'issuer': 'existing Step CA',
               'development_only': True, 'certificate_sha256': hashlib.sha256(leaf).hexdigest(),
               'fullchain_sha256': hashlib.sha256(leaf + intermediate).hexdigest(),
               'root_sha256': hashlib.sha256(root).hexdigest(),
               'validity': dates, 'chain_verified': True, 'key_pair_verified': True,
               'production_listener_changed': False}
    (STATE / 'ca-issuance.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
