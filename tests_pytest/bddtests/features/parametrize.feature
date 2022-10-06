Feature: Check parametrization

  Scenario: Adding to a set
    Given a set with 3 elements
    When add 2 elements to the set
    Then  the set should have 5 elements

  @remove
  Scenario: Substruct from a set
    Given countries set with 3 elements
    When remove 1 element from the set
    And remove 2 element from the set
    Then  set will have 0 elements