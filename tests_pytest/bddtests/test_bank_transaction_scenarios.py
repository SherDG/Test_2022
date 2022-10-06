from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
from os.path import dirname, abspath
import pytest

featureFileDir = 'features'
featureFile = 'bank_transaction.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


# print('Path: ' + str(FEATURE_FILE))

def pytest_configure():
    pytest.AMT = 0


scenarios(FEATURE_FILE)
# @scenario(FEATURE_FILE, "Money deposit")
# def test_money_deposit():
#     print('End of test')
#     pass



@given("the account balance is 100")
def current_balance():
    pytest.AMT = 100


@when('the client deposit 100')
def deposit_money():
    pytest.AMT += 100


@then('the account balance is 200')
def check_balance():
    assert pytest.AMT == 200


#
# @scenario(FEATURE_FILE, "Remove account")
# def test_remove_account():
#     pass


@given('a set of accounts of 2', target_fixture='accounts_set')
def current_accounts():
    accounts_set = {'first', 'second'}
    return accounts_set


@when('remove an account')
def remove_account(accounts_set):
    accounts_set.pop()


@then('a set of accounts of 1')
def check_accounts_set(accounts_set):
    assert len(accounts_set) == 1
