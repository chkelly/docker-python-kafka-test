from kafka import KafkaConsumer
import redis
import time

consumer = KafkaConsumer('my-topic',group_id='my-group',bootstrap_servers=['kafka:9092'])
redis_conn = redis.StrictRedis(host='redis')

while True:
  for message in consumer:
    redis_conn.lpush("messages",message.value)
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
  time.sleep(10)

