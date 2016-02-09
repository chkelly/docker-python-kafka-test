from kafka import KafkaProducer
from datetime import datetime
import time

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

while True:
  message = "This is message sent from python client " + str(datetime.now().time())
  producer.send("my-topic", message)
  print message
  time.sleep(5)
