"""Actual-profile PostgreSQL development capture under common admission."""
import json,sys,time
from pathlib import Path
from helper_contracts import Cycle,verify_sources,write_new,sha
from rehearse_database import run,ROOT

def capture(label):
 with Cycle(ROOT/'capture-journal',ROOT/'fixture-mutex',label,'capture',verify_sources()) as c:
  write_new(c.op/'database-capture.intent.json',{'scope':'synthetic-actual-schema','deadline':time.time()+180,'source_sha256':c.source_sha})
  run(label)
  receipt=json.loads((ROOT/(label+'-database-receipt.json')).read_bytes())
  c.check();write_new(c.op/'database-capture.receipt.json',receipt);c.receipts['database-capture']=receipt;c.finish()
if __name__=='__main__':capture(sys.argv[1])
