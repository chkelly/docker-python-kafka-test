from lettuce import *
import requests
import json
import time

@step(u'Given a message is sent with the text of "(.*)"')
def given_a_message_is_sent(step, message):
    payload = {'message':message}
    r = requests.post('http://message-api:5000/message/new',json=payload)
    if r.status_code == 204:
      assert True

@step(u'And I wait "(.*)" seconds for the message to populate from kafka to redis')
def sleep_for_variable_seconds(step,seconds):
    time.sleep(float(seconds))
    assert True

@step(u'I make a request to the "(.*)" URL')
def make_request_to_url(step, url):
    r = requests.get('http://www-api:5000/messages/list')
    world.response = r.text
    if r.status_code == 200:
      assert True

@step(u'I should see "(.*)" in the json response')
def i_should_see(step, text):
    assert text in world.response
