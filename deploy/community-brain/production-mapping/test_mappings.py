import copy,json
from pathlib import Path
import unittest
import mappings as m

class MappingTests(unittest.TestCase):
    def setUp(self):
        self.profile=json.loads((Path(__file__).parent/'observed-profile.json').read_text())
        self.census=dict(schema='cbm.metadata-census/1',application_rows_read=False,observations={**copy.deepcopy(self.profile['observations']),'identity':[{'read_only':'on'}]})
    def test_actual_profile_accepts_no_sequences_without_certifying_restore(self):
        self.assertFalse(any(r['kind']=='S' for r in self.profile['observations']['relations']))
        v=m.compare_catalog(self.census,self.profile)
        self.assertTrue(v['compatible_observed_metadata']);self.assertFalse(v['restore_qualified'])
    def test_schema_extension_role_table_and_acl_drift_detected(self):
        for key in ('schemas','extensions','application_roles','relations','default_acls'):
            v=copy.deepcopy(self.census);v['observations'][key].append({'unexpected':'object'})
            with self.subTest(key=key):self.assertEqual(m.compare_catalog(v,self.profile)['differences'],[key])
    def test_unknown_coverage_or_writable_census_rejected(self):
        extra=copy.deepcopy(self.census);extra['observations']['extra']=[]
        missing=copy.deepcopy(self.census);missing['observations'].pop('relations')
        for v in (extra,missing):
            with self.assertRaises(ValueError):m.compare_catalog(v,self.profile)
        self.census['observations']['identity'][0]['read_only']='off'
        with self.assertRaises(ValueError):m.compare_catalog(self.census,self.profile)
    def rows(self):
        return {name:dict(source_path=path,source_sha256='1'*64,effects=['synthetic fixture effect'],admission='shared-journal-before-effect',unknown_outcome='retain-and-readback-no-replay',recovery='synthetic fixture readback',dev_receipt_sha256='2'*64,legacy_dependency=False) for name,path in m.HELPERS.items()}
    def test_helper_shapes_do_not_enable_execution(self):
        self.assertFalse(m.validate_helper_mappings(self.rows())['production_execution_enabled'])
    def test_missing_helper_proof_and_legacy_dependency_refused(self):
        for key,val in [('source_sha256',None),('dev_receipt_sha256',''),('legacy_dependency',True),('unknown_outcome','retry'),('effects',[])]:
            rows=self.rows();rows['pre-pbs-copy'][key]=val
            with self.subTest(key=key),self.assertRaises(ValueError):m.validate_helper_mappings(rows)
        rows=self.rows();rows.pop('checkpoint-consumer')
        with self.assertRaises(ValueError):m.validate_helper_mappings(rows)

if __name__=='__main__':unittest.main()
