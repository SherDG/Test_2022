from pytest_bdd import scenario, scenarios, given, when, then, parser, parsers
from pathlib import Path
from os.path import dirname, abspath
import pytest

featureFileDir = 'features'
featureFile = 'outline.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


@scenario(FEATURE_FILE, "Adding to a set")
def test_set():
    print('End of test')
    pass


@pytest.fixture()
def setup_set():
    countries = {'USA', 'Ukraine', 'Canada'}
    return countries


@given(parsers.parse("a set with {start:d} elements"), target_fixture='setup_set1')
def get_set(setup_set, start):
    if len(setup_set) == 0:
        pytest.xfail('The set is empty')
    elif len(setup_set) > 3:
        pytest.xfail('The set is longer then 3')
    else:
        return dict(start=start)


@when(parsers.parse('add {deposit:d} elements to the set'))
def add_to_set(setup_set1, deposit):
    setup_set1["deposit"] = deposit


@when(parsers.parse('remove {withdraw:d} elements to the set'))
def remove_from_set(setup_set1, withdraw):
    setup_set1["withdraw"] = withdraw


@then(parsers.parse('the set should have {final:d} elements'))
def check_set(setup_set1, final):
    # print(setup_set1)
    # print(count)
    assert setup_set1["start"] + setup_set1["deposit"] - setup_set1["withdraw"] == final
