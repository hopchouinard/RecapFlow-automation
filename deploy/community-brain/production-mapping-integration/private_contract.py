"""Metadata/content envelope contract; never authorizes a protected transfer."""
import hashlib,json,os,stat,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'recovery-core'))
import recovery
COMPONENTS={'database','files','config','corpus','meeting-archive','automation','automation-public','manual-approvals','runtime-config','webui-volume','webui-signing','mac-management'}

def inspect_components(components,signing_digest):
 if set(components)!=COMPONENTS:raise ValueError('exact private component membership required')
 trees={name:recovery.tree(path) for name,path in sorted(components.items())}
 key=Path(components['webui-signing'])/'webui_secret_key'
 if recovery.sha(recovery.stable_bytes(key))!=signing_digest:raise ValueError('original signing digest mismatch; never regenerate')
 return {'schema':'cbm.private-components/2','components':trees,'signing_sha256':signing_digest,'metadata_policy':'numeric uid/gid, mode and mtime_ns; relative contained symlinks; roots and empty directories; reject xattrs/ACLs, hardlinks, absolute/escaping/broken links, special files and privileged bits','production_execution_enabled':False}

def verify_restore(before,after):
 if before!=after:raise ValueError('private restore differs; originals and failed attempt retained')
 return {'component_membership_equal':True,'metadata_and_bytes_equal':True,'signing_equal':True,'offline_only':True,'session_browser_accepted':False,'production_qualified':False}

def validate_destination(binding,observed):
 required={'machine_id','mount_uuid','parent','child','owner_uid','mode','minimum_free_bytes','retention','network','production_transfer_authorized'}
 if set(binding)!=required or binding['production_transfer_authorized'] is not False:raise ValueError('proposal only')
 if binding['machine_id']!=observed['machine_id'] or binding['mount_uuid']!=observed['mount_uuid'] or binding['parent']!=observed['parent']:raise ValueError('private destination identity changed')
 if observed['available_bytes']<binding['minimum_free_bytes'] or observed['child_exists']:raise ValueError('capacity or exclusive destination boundary')
 if binding['owner_uid']!=0 or binding['mode']!=0o700 or binding['network']!='none':raise ValueError('private root/isolation required')
 if not Path(binding['child']).is_relative_to(binding['parent']):raise ValueError('escaping destination')
 return {'metadata_preflight':True,'transfer_authorized':False}
