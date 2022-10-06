Feature: Check fixtures

  Background: setup data for test
    Given get test data
    And check if the set is not empty

  @add1
  Scenario: Adding to a set
    Given a set with 3 elements
    When add 2 elements to the set
    Then  the set should have 5 elements