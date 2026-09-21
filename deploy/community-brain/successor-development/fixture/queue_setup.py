"""Provision only the isolated queue; exercise real TLS and credential rejection."""
import asyncio,json,os,ssl
import nats
from nats.js.api import ConsumerConfig
from queue_binding import binding,connection_options

async def main():
 q=binding(os.environ);assert q['stream']=='CBM_REQUEST028'
 options=connection_options(os.environ)
 admin={**options,'user':os.environ['CB_DEV_NATS_ADMIN_USER'],'password':os.environ['CB_DEV_NATS_ADMIN_PASSWORD']}
 nc=await nats.connect(**admin);js=nc.jetstream()
 await js.add_stream(name=q['stream'],subjects=[q['subject']])
 await js.add_consumer(q['stream'],ConsumerConfig(durable_name=q['consumer'],filter_subject=q['subject'],ack_policy='explicit'))
 await nc.close()
 good=await nats.connect(**options);assert (await good.jetstream().stream_info(q['stream'])).config.subjects==[q['subject']];await good.close()
 rejected=[]
 for name,change in [('wrong_password',{'password':'deliberately-invalid'}),('untrusted_tls',{'tls':ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)})]:
  try:
   bad=await nats.connect(**{**options,**change,'max_reconnect_attempts':0})
   if not bad.is_connected:raise ConnectionError('connection rejected')
   await bad.close()
  except Exception:rejected.append(name)
  else:raise AssertionError('queue accepted invalid authority')
 for key,badvalue in [('CB_NATS_URL','tls://platform-events.patchoutech.lab:4223'),('CB_NATS_STREAM','COMMUNITY_BRAIN_PROD'),('CB_NATS_SUBJECT','cbm.prod.jobs.stage.ready.v1'),('CB_NATS_INBOX','_INBOX.cbm_prod_worker')]:
  try:binding({**os.environ,key:badvalue})
  except ValueError:rejected.append(key)
  else:raise AssertionError('profile mismatch accepted')
 print(json.dumps({'actual_tls_authenticated':True,'stream':q['stream'],'subject':q['subject'],'inbox':q['inbox'],'negative_checks':rejected,'external_calls':0}))
asyncio.run(main())
