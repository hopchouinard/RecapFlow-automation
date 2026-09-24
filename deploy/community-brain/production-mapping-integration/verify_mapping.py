import hashlib,json,sys
from pathlib import Path
from helper_contracts import canonical,verify_sources
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'forge'))
from mappings import validate_helper_mappings
v=json.loads((HERE/'helper-mappings.json').read_bytes());proof=json.loads((HERE/'evidence/helper-algorithm-receipts.json').read_bytes())
result=validate_helper_mappings(v)
for name,row in v.items():
 assert hashlib.sha256((HERE/'deployed-mac'/row['source_path']).read_bytes()).hexdigest()==row['source_sha256']
 assert hashlib.sha256(canonical(proof[name])).hexdigest()==row['dev_receipt_sha256']
 assert proof[name]['source_sha256']==row['source_sha256']
result.update(independent_source_and_receipt_bytes_verified=True,helper_count=len(v),executing_source_sha256=verify_sources(),production_execution_enabled=False)
print(json.dumps(result))
