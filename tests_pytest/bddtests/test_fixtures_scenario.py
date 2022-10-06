from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
from os.path import dirname, abspath
import pytest

featureFileDir = 'features'
featureFile = 'fixtures.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


# print(FEATURE_FILE)
# scenarios(FEATURE_FILE)


@scenario(FEATURE_FILE, "Adding to a set")
def test_money_deposit():
    print('End of test')
    pass


@pytest.fixture()
def setup_set():
    countries = {'USA', 'Ukraine', 'Canada'}
    # countries = {}
    # countries = []
    return countries


@given("a set with 3 elements", target_fixture='setup_set1')
def get_set(setup_set):
    if len(setup_set) == 0:
        pytest.xfail('The set is empty')
    elif len(setup_set) > 3:
        pytest.xfail('The set is longer then 3')
    else:
        return setup_set


@when('add 2 elements to the set')
def add_to_set(setup_set1):
    setup_set1.add('UK')
    setup_set1.add('Germany')


@then('the set should have 5 elements')
def check_set(setup_set1):
    # print(setup_set1)
    assert len(setup_set1) == 5


@given('get test data')
def get_data(setup_set):
    print('Background')
    # print(setup_set)
    if not isinstance(setup_set, set):
        pytest.xfail('The type of data is not SET')


@given('check if the set is not empty')
def get_data(setup_set):
    print('Background1')
    if len(setup_set) == 0:
        pytest.xfail('The set is empty')
