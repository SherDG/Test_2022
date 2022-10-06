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

@pytest.fixture()
def get_set():
    return {'USA', 'Ukraine', 'Canada'}

@pytest.fixture()
def get_dict():
    return dict(start=0, substracted=0)



@given("a set with 3 elements")
def check_start_set(get_set):
    assert len(get_set) == 3


@when(parsers.parse('add {len_test:d} elements to the set'))
def add_to_set(get_set, len_test):
    assert 2 == len_test
    get_set.add('UK')
    get_set.add('Germany')


@then(parsers.cfparse('the set should have {len_final:d} elements'))
def check_set(get_set, len_final):
    # print('get_set3')
    # print(get_set)
    assert len(get_set) == len_final
    # assert len(get_set) == len


@given(parsers.parse('countries set with {count:d} elements'))
def existing_set(get_dict, count):
    print('dict')
    print(get_dict)
    get_dict['start'] += count
    print('dict2')
    print(get_dict)
    return get_dict


@when(parsers.parse('remove {count:d} element from the set'))
def remove_one(get_dict, count):
    # print(setup_set1)
    get_dict['substracted'] += count
    get_dict['start'] -= count
    print('dict3')
    print(get_dict)
    return get_dict


@then(parsers.parse('set will have {count:d} elements'))
def check_final_dict(get_dict, count):
    print("get_dict4")
    print(get_dict)
    assert get_dict['start'] == count
    assert get_dict['substracted'] == 3
