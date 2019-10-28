from datetime import datetime, timedelta, timezone

now = datetime.now()
print('now = ', now)
print('type(now) = ',type(now))

dt = datetime(2017,12,28,16,49)
print('dt = ', dt)
print('datetime -> timestamp:', dt.timestamp())

ts = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(ts))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(ts))

cday = datetime.strptime('2017-12-28 16:58:02','%Y-%m-%d %H:%M:%S')
print('strptime =',cday)
print('strftime =',cday.strftime('%a, %b %d %H:%M'))

print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =',cday-timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2,hours=12))

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)


