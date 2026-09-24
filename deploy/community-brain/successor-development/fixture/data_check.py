"""Read durable fixture outcomes through the real Store and LanceDB."""
import json,os,sys
from pathlib import Path
from sqlalchemy import select
from sqlalchemy.orm import Session
from community_brain.jobs.runtime import make_store
from community_brain.jobs.models import Job,Stage,Outbox
import lancedb
store=make_store()
if sys.argv[1]=='excluded':
 identity={'meeting_id':'request028-excluded','local_date':'2026-09-08','started_at':'2026-09-08T22:00:00Z','timezone':'America/Toronto','provider':'manual'}
 source=store.add_source('community-brain','request028-excluded','transcript','Excluded synthetic source')
 job,_=store.accept('community-brain','fixture','request028-excluded',{'identity':identity,'mode':'transcript_backfill','sources':{'transcript':str(source)}})
 print(json.dumps({'excluded_job':str(job)}))
else:
 with Session(store.engine) as session:
  jobs=[]
  for j in session.scalars(select(Job)):
   stages=session.scalars(select(Stage).where(Stage.job_id==j.id)).all()
   outbox=session.scalars(select(Outbox).where(Outbox.stage_id.in_([s.id for s in stages]))).all()
   jobs.append({'id':str(j.id),'meeting_id':j.identity['meeting_id'],'indexing':j.indexing,'processing':j.processing,'stages':[{'name':s.name,'attempts':s.attempts,'state':s.state} for s in stages],'outbox_sent':sum(e.sent_at is not None for e in outbox)})
 table=lancedb.connect(str(Path(os.environ['CB_CORPUS_ROOT'])/'lancedb/nomic-v1')).open_table('chunks')
 stats=table.index_stats('bm25_text_idx')
 print(json.dumps({'jobs':sorted(jobs,key=lambda j:j['id']),'rows':table.count_rows(),'fts':{k:stats[k] for k in ('num_indexed_rows','num_unindexed_rows')}}))
