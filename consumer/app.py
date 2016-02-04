from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('my-topic',group_id='my-group',bootstrap_servers=['kafka:9092'])

while True:
  for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
  time.sleep(10)

