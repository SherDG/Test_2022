from pytest_bdd import scenario, scenarios, given, when, then, parser, parsers
from pathlib import Path
from os.path import dirname, abspath
import pytest

featureFileDir = 'features'
featureFile = 'parametrize.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


# print('FEATURE_FILE: '+str(FEATURE_FILE))


scenarios(FEATURE_FILE)



@given("a set with 3 elements", target_fixture="cont")
def get_set():
    countries = {'USA', 'Ukraine', 'Canada'}
    return countries


@when('add 2 elements to the set')
def add_to_set(cont):
    cont.add('UK')
    cont.add('Germany')


# IF USE {count:d} for 5 in this test then it passed to the second and broke it
@then(parsers.parse('the set should have {len_final:d} elements'))
def check_set(cont, len_final):
    print(cont)
    # print(count)
    assert len(cont) == len_final



@given(parsers.parse('countries set with {count:d} elements'), target_fixture="dict2")
def existing_set(count):
    return dict(start=count, substracted=0)


@when(parsers.parse('remove {count:d} element from the set'))
def remove_one(dict2, count):
    # print(setup_set1)
    dict2['substracted'] += count
    dict2['start'] -= count
    print('dict2')
    print(dict2)
    return dict2


@then(parsers.parse('set will have {count:d} elements'))
def check_final_set(dict2, count):
    # assert dict1['start'] == count
    assert dict2['substracted'] == 3
