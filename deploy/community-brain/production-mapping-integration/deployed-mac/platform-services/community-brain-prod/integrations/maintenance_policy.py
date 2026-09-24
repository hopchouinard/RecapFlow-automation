"""Pure timing/expiry rules for existing Mac maintenance; no credential mutation."""
import datetime
from zoneinfo import ZoneInfo
ZONE=ZoneInfo('America/Toronto')
def next_pbs(now):
    local=now.astimezone(ZONE);target=local.replace(hour=21,minute=0,second=0,microsecond=0)
    if local>=target:target+=datetime.timedelta(days=1)
    return target
def pre_window(now):
    local=now.astimezone(ZONE)
    return local.hour==20 and 40<=local.minute<55
def validate_copy(now,finished,dump_time,sha_before,sha_after,copy_sha,enforce_window=True):
    assert not enforce_window or (pre_window(now) and pre_window(finished)),'Outside bounded pre-PBS window'
    assert 0<=(finished-dump_time).total_seconds()<=7200,'Missing or stale completed dump'
    assert sha_before==sha_after==copy_sha,'Source/copy checksum mismatch'
    assert (next_pbs(finished)-finished.astimezone(ZONE)).total_seconds()>=300,'Insufficient time before PBS'
    return (next_pbs(finished)+datetime.timedelta(days=1)-datetime.timedelta(minutes=5)).timestamp()
def expiry_state(now,expiry):
    remaining=expiry-now.timestamp()
    return 'expired' if remaining<=0 else 'critical_24h' if remaining<=86400 else 'warning_72h' if remaining<=259200 else 'ok'
