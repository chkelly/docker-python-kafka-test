import os
import json
import flask
from kafka import KafkaProducer
from flask import request

app = flask.Flask(__name__)

#Setup for JSON
PRODUCER = KafkaProducer(bootstrap_servers=['kafka:9092'])

@app.route('/')
def index():
  return 'Woo it works!'

@app.route('/message/new',methods=['POST'])
def alert():
  request_data = request.get_json()
  message = str(request_data['message'])
  PRODUCER.send('my-topic', message)
  return('',204)
