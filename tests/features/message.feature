Feature: Message
  
  Scenario: User can view messages that have been sent to the message service from the www-api
    Given a message is sent with the text of "test message"
    And I wait "10" seconds for the message to populate from kafka to redis
    When I make a request to the "/messages/list" URL
    Then I should see "test message" in the json response
