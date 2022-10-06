@bddparam
Feature: Bank Transaction
  Test deposit transaction

  @moneyDeposit
  Scenario: Money deposit
    Given the account balance is 100
    When the client deposit 100
    Then  the account balance is 200

  Scenario: Remove account
    Given a set of accounts of 2
    When remove an account
    Then a set of accounts of 1