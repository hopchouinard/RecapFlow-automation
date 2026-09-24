"""Checked queue binding shared by selected and bounded workers."""
import json
import os
from pathlib import Path
import ssl
from profiles import validate


def binding(env):
 descriptor=json.loads(Path('/packet/descriptor.json').read_text())
 validate(descriptor);q=descriptor['queue']
 expected={'CB_RUNTIME_PROFILE':descriptor['profile'],'CB_NATS_URL':q['url'],
 'CB_NATS_STREAM':q['stream'],'CB_NATS_SUBJECT':q['subject'],'CB_NATS_INBOX':q['inbox']}
 if any(env.get(k)!=v for k,v in expected.items()):raise ValueError('queue/profile mismatch')
 if not all(env.get(k) for k in q['credential_keys']):raise ValueError('queue credentials required')
 if descriptor['profile']=='development' and env['CB_NATS_USER']!='cbm-request034-worker':raise ValueError('wrong development principal')
 if env.get('CB_ENABLE_NETWORK_PUBLICATION')!='false':raise ValueError('publication must stay disabled')
 return q


def connection_options(env):
 q=binding(env)
 return {'servers':q['url'],'user':env['CB_NATS_USER'],'password':env['CB_NATS_PASSWORD'],
 'tls':ssl.create_default_context(cafile=q['ca_file']),'tls_handshake_first':q['tls_handshake_first'],
 'inbox_prefix':q['inbox'].encode(),'allow_reconnect':False,'connect_timeout':10}
