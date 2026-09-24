"""Seed only an empty disposable integration volume/database with synthetic data."""
import os
from pathlib import Path
import lancedb
from sqlalchemy import create_engine
from community_brain.jobs.models import Base
from community_brain.ingestion.schema import Chunk, pyarrow_table_schema
from community_brain.query.fts_lifecycle import ensure_fts_index

root=Path('/state')
assert os.environ['CB_DATABASE_URL']=='postgresql+psycopg://fixture@pg/integration'
assert not (root/'seeded').exists()
(root/'files').mkdir();(root/'config').mkdir();(root/'corpus').mkdir()
(root/'config/speaker-aliases.yaml').write_text('version: "x"\naliases: {}\npending: []\n')
text='Synthetic migration question. This is isolated Community Brain retrieval acceptance.'
chunk=Chunk(schema_version='1.1',chunk_id='integration-synthetic-001',session_id='2026-09-20',
 session_date='2026-09-20',session_title='Synthetic integration',content_type='prepared_transcript',
 source_file='synthetic.txt',chunk_index=0,total_chunks_in_source=1,speakers_spoke=['Fixture'],
 speakers_mentioned=[],entities=[],keywords=['migration'],topic_label='Migration',session_themes=[],
 speech_acts=[],stance=None,certainty='asserted',chunk_local_markers=[],corpus_derived_markers=[],
 corpus_markers_computed_at=None,has_question=True,has_answer=True,has_unresolved_question=False,
 has_insight=False,decisions=[],action_items=[],external_refs=[],references_prior=False,
 extraction_model='fixture',extraction_prompt_version='fixture',extraction_status='success',
 extraction_error=None,extracted_at=None,embed_text=text,full_text=text,bm25_text=text,
 embedding=[1.0]+[0.0]*767)
table=lancedb.connect(str(root/'corpus/lancedb/nomic-v1')).create_table('chunks',data=[chunk.to_arrow_dict()],schema=pyarrow_table_schema())
ensure_fts_index(table)
Base.metadata.create_all(create_engine(os.environ['CB_DATABASE_URL']))
(root/'seeded').write_text('synthetic only\n')
print('Synthetic schema, corpus and FTS initialized')
