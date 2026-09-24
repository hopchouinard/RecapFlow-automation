"""External-provider fixture only; real selected worker, queue, DB and locks."""
import os,json,sys
from contextlib import nullcontext
from pathlib import Path
from unittest.mock import patch
import manual_worker
from profiles import development
from fixtures import fake_model,_mock_ollama_embed,_fake_extract_response
from community_brain.processing.pipeline import OutcomeUnknown

def main():
    development(json.loads(Path('/packet/descriptor.json').read_text()))
    if os.environ['CB_RUNTIME_PROFILE']!='development':raise ValueError('synthetic provider forbidden outside development')
    def model(request):
        with (Path(os.environ['CB_STORAGE_ROOT'])/'synthetic-provider.jsonl').open('a') as f:
            f.write(json.dumps({'expect':request['expect'],'outcome':os.environ['CB_SYNTHETIC_OUTCOME']})+'\n');f.flush();os.fsync(f.fileno())
        if os.environ['CB_SYNTHETIC_OUTCOME']=='uncertain':raise OutcomeUnknown('synthetic uncertain provider outcome')
        return fake_model(request)
    class Fathom:
        def __init__(self,*args):pass
        def close(self):pass
        def fetch(self,identity):return 'Selected synthetic Fathom transcript'
    with patch.object(manual_worker,'ManualProvider',lambda key:model),patch.object(manual_worker,'SelectedFathom',Fathom),patch.object(manual_worker,'audited_indexing',lambda *a:nullcontext()),patch('community_brain.ingestion.embedding.ollama.Client.embed',side_effect=_mock_ollama_embed),patch('community_brain.ingestion.embedding.ollama.embed',side_effect=_mock_ollama_embed),patch('community_brain.ingestion.extractor._call_llm',side_effect=_fake_extract_response),patch('community_brain.ingestion.session_extractor._call_llm',side_effect=_fake_extract_response):
        manual_worker.main()
if __name__=='__main__':main()
