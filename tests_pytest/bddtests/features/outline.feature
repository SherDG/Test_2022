@outline
Feature: Check outline

  Scenario Outline: Adding to a set
    Given a set with <start> elements
    When add <deposit> elements to the set
    When remove <withdraw> elements to the set
    Then  the set should have <final> elements

    Examples:
    | start | deposit | withdraw | final |
    |    1  |    3    |   2      |   2   |
    |    2  |    1    |   2      |   1   |