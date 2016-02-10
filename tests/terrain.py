from lettuce import *
import redis

@before.each_feature
def scrub_redis(self):
  redis_conn = redis.StrictRedis(host='redis')
  redis_conn.flushall()
