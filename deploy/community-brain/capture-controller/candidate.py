"""Preparation-only component contract. No production adapter or execution path."""
import database

def prepare(template, evidence, specification, manifest_sha256):
    if template.get('deployable') is not False or template.get('production_execution_enabled') is not False:
        raise ValueError('production execution must remain disabled')
    slots=template['required_evidence']
    if len(slots)!=21 or any(v is not None for v in slots.values()):
        raise ValueError('all 21 production slots must remain empty')
    verified=database.verify_evidence(evidence,specification,manifest_sha256)
    return {'schema':'cbm.capture-preparation/1','scope':'synthetic-development',
            'component_database_verification':verified,'required_evidence':dict(slots),
            'deployable':False,'production_execution_enabled':False,
            'production_compiler_enabled':False,'production_controller_enabled':False,
            'adapter_installed':False,'remaining_gate':'Separate production authority and validators for every evidence slot; no development-to-production substitution.'}
