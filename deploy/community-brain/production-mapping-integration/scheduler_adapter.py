"""Installed scheduler algorithm under one existing, continuously owned mutex."""
import contextlib
from helper_contracts import MAC,verify_sources

def run(cycle):
 cycle.check()
 source=(MAC/'maintain.py').read_text()
 before="with (STATE/'scheduler.lock').open('a') as lock:"
 acquire='fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)'
 if source.count(before)!=1 or source.count(acquire)!=1:raise ValueError('installed scheduler lock seam changed')
 source=source.replace(before,'with SHARED_LOCK() as lock:').replace(acquire,'CHECK_SHARED_LOCK(lock)')
 @contextlib.contextmanager
 def lock():
  cycle.check();yield cycle.fd;cycle.check()
 def check(fd):
  if fd!=cycle.fd:raise ValueError('foreign mutex descriptor')
  cycle.check()
 namespace={'__file__':str(MAC/'maintain.py'),'__name__':'candidate_scheduler','SHARED_LOCK':lock,'CHECK_SHARED_LOCK':check}
 exec(compile(source,str(MAC/'maintain.py'),'exec'),namespace)
 return namespace['main']()
