import os
import json
import flask
import redis
from flask import request
from utils import crossdomain

app = flask.Flask(__name__)
app.redis = redis.StrictRedis(host='redis')

@app.route('/')
def index():
  return 'Woo it works!'

@app.route('/messages/list')
@crossdomain(origin='*')
def messages_list():
  messages = app.redis.lrange("messages", 0, -1)
  return flask.jsonify(messages=messages)
