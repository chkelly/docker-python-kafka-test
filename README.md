# Summary
This app demonstrates a few concepts..
* Rapid prototyping with Docker
* Kafka
* A simple producer (message-api)
* A simple consumer (consumer) that does something with the messages (stores them in redis)
* A simple www-api that reads from redis and returns this data via JSON
* A simple web page (using harp to serve the static assets) which uses jquery to display a list of messages from the www-api
* Running of Integration tests

This is not meant to ever leave a developers laptop...

# Running the demo

Checkout this repo and just run `docker-compose up -d`.

## Sending messages to the message API

Fire off an event with something like....

`curl -X POST -H "Content-Type: application/json" -d '{"message":"This is a test message!"}' http://192.168.99.100:8081/message/news`

## View the consumer doing its thing...

Tail the logs of the consumer process

## View list of messages stored in redis from www-api

`curl 192.168.99.100:8080/messages/list`

## View list of messages stored in redis from website

`open http://192.168.99.100:9000`

## Running the tests

### Integration tests
1. First start all services via `docker-compose up -d`
1. Give the system a minute or so to converge and such. Kafka needs to start up and register itself with zookeeper.
1. Run the integration tests with the following command `docker-compose run tests lettuce`


