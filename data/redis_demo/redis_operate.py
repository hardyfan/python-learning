import redis
from redis_config import REDIS_HOST, REDIS_PORT

pool = redis.ConnectionPool(host=REDIS_HOST,
                            port=REDIS_PORT,
                            db='4',
                            decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 设置字符串
r.set('name1', 'hardy1', ex=60*60)
# r.set('gender', 'male')
print(r.get('name1'))
print(r.get('gender'))

# 设置列表
r.lpush('Zarten', 1, 2, 3, 4, 5)
r.lpush('Zarten', 6)
print(r.llen('Zarten'))
print(r.lrange('Zarten', 2, 3))

# 设置hash值,一小时内有效
r.hmset('environments', {'rain_snow': '0', 'wend': 13})
print(r.hgetall('environments'))


