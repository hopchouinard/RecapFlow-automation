"""Development-only common admission journal. No remote dispatch or production CLI.

All entry points must use the same existing mutex and journal. Intent precedes
any effect; only fresh authoritative readback resolves it. Expiry is not success.
"""
from contextlib import contextmanager
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import stat
import time


def encode(v):
    return (json.dumps(v,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()


def digest(v):
    return hashlib.sha256(encode(v)).hexdigest()


def path(p):
    p=Path(p).absolute()
    if any(x.is_symlink() for x in [p,*p.parents]):raise ValueError('linked journal path')
    return p


def read(p):
    fd=os.open(path(p),os.O_RDONLY|os.O_NOFOLLOW)
    with os.fdopen(fd,'rb') as f:
        s=os.fstat(f.fileno())
        if not stat.S_ISREG(s.st_mode) or s.st_nlink!=1:raise ValueError('unsafe journal member')
        return json.load(f)


def create(p,v):
    fd=os.open(path(p),os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,'wb') as f:f.write(encode(v));f.flush();os.fsync(f.fileno())
    sync(p.parent)


def sync(p):
    fd=os.open(p,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)


def validate(spec):
    keys={'scope','kind','operation_id','owner_id','packet_sha256','target','incumbent_id','holds_sha256','deadline_epoch'}
    if set(spec)!=keys or spec['scope']!='synthetic-development' or spec['target']!='community-brain-dev':raise ValueError('development specification required')
    if spec['kind'] not in ('scheduler','manual','capture'):raise ValueError('unknown entry point')
    for k in ('operation_id','owner_id'):
        if not isinstance(spec[k],str) or not re.fullmatch('[a-z0-9][a-z0-9-]{7,100}',spec[k]):raise ValueError('invalid owner/operation')
    for k in ('packet_sha256','holds_sha256','incumbent_id'):
        if not isinstance(spec[k],str) or not re.fullmatch('[0-9a-f]{64}',spec[k]):raise ValueError('invalid binding')
    if type(spec['deadline_epoch']) not in (int,float) or not math.isfinite(spec['deadline_epoch']):raise ValueError('invalid deadline')


class Gate:
    def __init__(self,root,mutex):
        self.root=path(root);self.mutex=path(mutex)
        # Provisioning is explicit; never replace or create installed controls.
        if not self.root.is_dir():raise ValueError('journal must already exist')
        self.owned=False

    @contextmanager
    def locked(self):
        if self.owned:raise ValueError('nested admission refused')
        fd=os.open(self.mutex,os.O_RDWR|os.O_NOFOLLOW)
        try:
            s=os.fstat(fd)
            if not stat.S_ISREG(s.st_mode) or s.st_nlink!=1:raise ValueError('unsafe mutex')
            fcntl.flock(fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
            self.owned=True
            self.fd=fd;self.identity=(s.st_dev,s.st_ino)
            self.check()
            yield self
            self.check()
        finally:self.owned=False;os.close(fd)

    def check(self):
        if not self.owned:raise ValueError('existing common mutex required')
        s=path(self.mutex).stat()
        if (s.st_dev,s.st_ino)!=self.identity:raise ValueError('mutex replaced')

    def unresolved(self):
        self.check();pending=[]
        for p in sorted(self.root.iterdir()):
            path(p)
            if not p.is_dir() or not re.fullmatch('[a-z0-9][a-z0-9-]{7,100}',p.name):raise ValueError('unknown journal entry')
            members={x.name for x in p.iterdir()}
            if not members<= {'intent.json','resolution.json'}:raise ValueError('partial or unknown journal member')
            if 'intent.json' not in members:pending.append(p.name);continue
            spec=read(p/'intent.json');validate(spec)
            if spec['operation_id']!=p.name:raise ValueError('foreign intent')
            if 'resolution.json' not in members:pending.append(p.name);continue
            result=read(p/'resolution.json')
            if set(result)!={'spec_sha256','readback','resolved_epoch'} or result['spec_sha256']!=digest(spec):raise ValueError('foreign resolution')
            self.proof(spec,result['readback'],result['resolved_epoch'])
        return pending

    def begin(self,spec):
        self.check();validate(spec)
        if self.unresolved():raise ValueError('unresolved operation; authoritative readback required')
        if spec['deadline_epoch']<=time.time():raise ValueError('expired dispatch')
        p=path(self.root/spec['operation_id']);p.mkdir(mode=0o700);sync(self.root)
        # A crash before intent fsync leaves a directory that blocks ALL callers.
        create(p/'intent.json',spec)
        return digest(spec)

    def proof(self,spec,value,now):
        keys={'spec_sha256','state','incumbent_id','holds_sha256','target','observed_epoch','boot_id','finalizer_seen','service_inactive','healthy'}
        if set(value)!=keys:raise ValueError('incomplete authoritative readback')
        if value['spec_sha256']!=digest(spec) or any(value[k]!=spec[k] for k in ('incumbent_id','holds_sha256','target')):raise ValueError('foreign readback')
        if value['state'] not in ('completed','aborted_restored'):raise ValueError('unresolved target')
        if any(value[k] is not True for k in ('finalizer_seen','service_inactive','healthy')):raise ValueError('unsafe target')
        t=value['observed_epoch']
        if type(t) not in (int,float) or not math.isfinite(t) or not 0<=now-t<=15:raise ValueError('stale readback')
        if not isinstance(value['boot_id'],str) or not re.fullmatch('[0-9a-f-]{36}',value['boot_id']):raise ValueError('missing current boot identity')

    def reconcile(self,spec,observe):
        self.check();validate(spec)
        p=path(self.root/spec['operation_id'])
        if read(p/'intent.json')!=spec:raise ValueError('foreign pending owner')
        if (p/'resolution.json').exists():raise ValueError('already resolved')
        # Callback must obtain fresh target state; no local receipt substitution.
        value=observe();now=time.time();self.check();self.proof(spec,value,now)
        create(p/'resolution.json',dict(spec_sha256=digest(spec),readback=value,resolved_epoch=now))
        return value

    def invoke(self,spec,dispatch,observe):
        """Common scheduler/manual/capture facade. Caller owns this gate's lock."""
        self.begin(spec)
        dispatch()  # Failure or lost caller leaves unresolved intent, never redispatch.
        return self.reconcile(spec,observe)
