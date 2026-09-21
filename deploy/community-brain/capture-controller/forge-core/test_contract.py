import copy
from pathlib import Path
import sys
import unittest
from contract import reconcile

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.template={'deployable':False,'production_execution_enabled':False,'required_evidence':{'protected_restore':None}}
        self.receipt={'schema':'cbm.restore-receipt/1','scope':'synthetic-development','production_qualified':False,'capture_id':'synthetic-030','manifest_sha256':'0'*64}
    def test_development_never_completes_production_slot(self):
        t=copy.deepcopy(self.template);result=reconcile(t,self.receipt)
        self.assertEqual(t,self.template);self.assertFalse(result['production_compilation_enabled']);self.assertEqual(result['missing_slots'],['protected_restore'])
    def test_relabelled_receipt_rejected(self):
        self.receipt['scope']='production'
        with self.assertRaises(ValueError):reconcile(self.template,self.receipt)
    def test_enabled_template_rejected(self):
        self.template['production_execution_enabled']=True
        with self.assertRaises(ValueError):reconcile(self.template,self.receipt)
    def test_prefilled_flag_rejected(self):
        self.template['required_evidence']['protected_restore']=True
        with self.assertRaises(ValueError):reconcile(self.template,self.receipt)

if __name__=='__main__':unittest.main()
