"""Actual inherited budget helper with synthetic transports, zero provider calls."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

class Unknown(Exception):pass
class Response:
    def __init__(self,body):self.body=body
    def raise_for_status(self):pass
    def json(self):return self.body

class BudgetTests(unittest.TestCase):
    def setUp(self):
        self.allow={'limit':5,'limit_reset':'weekly','limit_remaining':5,'is_management_key':False,'include_byok_in_limit':True}
        self.http=types.ModuleType('httpx');self.calls=0
        self.http.get=lambda *a,**k:Response({'data':self.allow})
        def post(*a,**k):self.calls+=1;return Response({'usage':{'synthetic':True}})
        self.http.post=post
        llm=types.SimpleNamespace(httpx=self.http,LLMOutcomeUnknown=Unknown,OPENROUTER_URL='https://openrouter.ai/api/v1/chat/completions')
        cb=types.ModuleType('community_brain');cb.llm=llm
        self.patch=patch.dict(sys.modules,{'httpx':self.http,'community_brain':cb});self.patch.start();self.addCleanup(self.patch.stop)
        spec=importlib.util.spec_from_file_location('subject',Path(__file__).with_name('indexing_budget.py'));self.m=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.m)
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.journal=Path(self.tmp.name)/'journal.jsonl'
        self.store=types.SimpleNamespace(storage=types.SimpleNamespace(put=lambda data:('synthetic-response','synthetic-sha',len(data))))
    def test_invalid_allowances_fail_closed(self):
        for field,value in [('limit',10),('limit_remaining',0),('limit_remaining',float('nan')),('limit_reset','monthly'),('is_management_key',True),('include_byok_in_limit',False)]:
            old=self.allow[field];self.allow[field]=value
            with self.assertRaises(Unknown):self.m.allowance('synthetic')
            self.allow[field]=old
        self.assertEqual(self.calls,0)
    def test_allowance_transport_failure_is_unknown(self):
        self.http.get=lambda *a,**k:(_ for _ in ()).throw(TimeoutError())
        with self.assertRaises(Unknown):self.m.allowance('synthetic')
        self.assertEqual(self.calls,0)
    def test_ceiling_prevents_second_request_and_restores_transport(self):
        original=self.http.post
        with self.m.audited_indexing(self.store,'synthetic',self.journal,ceiling=1):
            self.http.post(self.m.llm.OPENROUTER_URL,json={'model':'synthetic'})
            with self.assertRaises(Unknown):self.http.post(self.m.llm.OPENROUTER_URL,json={'model':'synthetic'})
        self.assertEqual(self.calls,1);self.assertIs(self.http.post,original)
        self.assertEqual([json.loads(x)['state'] for x in self.journal.read_text().splitlines()],['exercise','intent','response'])
    def test_wrong_endpoint_has_no_request(self):
        with self.m.audited_indexing(self.store,'synthetic',self.journal):
            with self.assertRaises(Unknown):self.http.post('https://unexpected.invalid',json={'model':'synthetic'})
        self.assertEqual(self.calls,0)
    def test_unknown_response_retains_intent_and_refuses_reopening(self):
        self.http.post=lambda *a,**k:(_ for _ in ()).throw(TimeoutError())
        with self.m.audited_indexing(self.store,'synthetic',self.journal):
            with self.assertRaises(Unknown):self.http.post(self.m.llm.OPENROUTER_URL,json={'model':'synthetic'})
        self.assertEqual([json.loads(x)['state'] for x in self.journal.read_text().splitlines()],['exercise','intent'])
        with self.assertRaises(FileExistsError):
            with self.m.audited_indexing(self.store,'synthetic',self.journal):pass
    def test_allowance_rechecked_before_each_call(self):
        with self.m.audited_indexing(self.store,'synthetic',self.journal):
            self.http.post(self.m.llm.OPENROUTER_URL,json={'model':'synthetic'})
            self.allow['limit_remaining']=0
            with self.assertRaises(Unknown):self.http.post(self.m.llm.OPENROUTER_URL,json={'model':'synthetic'})
        self.assertEqual(self.calls,1)

if __name__=='__main__':unittest.main()
