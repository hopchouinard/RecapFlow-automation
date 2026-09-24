"""Synthetic-only exported snapshot and table write fence; no worker effects."""
from contextlib import contextmanager
import re
import select
import socket
import subprocess


@contextmanager
def fence(container, tables):
    if socket.gethostname()!='community-brain-dev' or not re.fullmatch('cbm-r030-pg-source-a[0-9]+',container):
        raise ValueError('only fresh Request030 synthetic database allowed')
    if not tables or any(not re.fullmatch('[a-z_]+',t) for t in tables):
        raise ValueError('invalid table allowlist')
    p=subprocess.Popen(['docker','exec','-i',container,'psql','-X','-qAt','-U','fixture','-d','fixture','-v','ON_ERROR_STOP=1'],
                       stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1)
    try:
        p.stdin.write("BEGIN ISOLATION LEVEL REPEATABLE READ; SET LOCAL lock_timeout='5s'; LOCK TABLE "+','.join('public.'+t for t in tables)+" IN SHARE MODE; SELECT pg_export_snapshot();\n")
        p.stdin.flush()
        ready,_,_=select.select([p.stdout],[],[],10)
        if not ready:raise ValueError('snapshot fence timed out')
        snapshot=p.stdout.readline().strip()
        if not re.fullmatch('[0-9A-Fa-f]+-[0-9A-Fa-f]+-[0-9]+',snapshot):
            raise ValueError('snapshot fence not acquired')
        yield snapshot
    finally:
        if p.poll() is None:
            try:p.stdin.write('ROLLBACK;\n');p.stdin.flush();p.stdin.close();p.wait(timeout=10)
            except (BrokenPipeError,subprocess.TimeoutExpired):p.kill();p.wait()
