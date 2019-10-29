import redis
from redis_config import REDIS_HOST, REDIS_PORT

pool = redis.ConnectionPool(host=REDIS_HOST,
                            port=REDIS_PORT,
                            decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('name', 'hardy')
r.set('gender', 'male')

print(r.get('name'))
print(r.get('gender'))
