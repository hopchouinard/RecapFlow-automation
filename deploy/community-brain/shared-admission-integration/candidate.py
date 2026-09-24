"""Preparation only; never turns synthetic evidence into production authorization."""
import database

def prepare(template,evidence,spec,manifest):
    if template.get('deployable') is not False or template.get('production_execution_enabled') is not False or len(template['required_evidence'])!=21 or any(v is not None for v in template['required_evidence'].values()):raise ValueError('all production gates must remain disabled and empty')
    verified=database.verify_evidence(evidence,spec,manifest)
    return {'schema':'cbm.shared-admission-preparation/1','scope':'synthetic-development','database_verification':verified,'required_evidence':dict(template['required_evidence']),'deployable':False,'production_execution_enabled':False,'production_compiler_enabled':False,'production_controller_enabled':False,'adapter_installed':False}
