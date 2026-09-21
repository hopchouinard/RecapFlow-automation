"""Compatibility entry point for the real, verified automatic launcher."""
import json,os,sys
from automation import tick
if __name__=='__main__':
 os.environ['CBM_PACKET_SHA256']=sys.argv[1]
 print(json.dumps(tick(sys.argv[1])))
