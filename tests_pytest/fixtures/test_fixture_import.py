# Fixtures imported form conftest.py
import pytest


def test_check_items(setup_list_import):
    del setup_list_import[-1]
    print(setup_list_import)
    assert setup_list_import == pytest.cites


def test_check_items2(setup_list_import_factory):
    new_list = setup_list_import_factory()
    del new_list[-1]
    # del setup_list_import[-1]
    # print(setup_list_import);
    # assert setup_list_import == pytest.cites
    assert new_list == pytest.cites


def test_check_items3(setup_list_import_factory):
    new_list = setup_list_import_factory()
    new_list.remove('tretret')
    assert new_list == pytest.cites


month = ['december', 'january']


def test_check_requests(setup_list_import3):
    # assert 'april' in setup_list_import3
    assert len(setup_list_import3) == 3


def test_check_factory(factory_fixture):
    assert type(factory_fixture('list')) == list
    assert type(factory_fixture('tuple')) == tuple


def test_fixtures_params(params_fixture):
    assert (type(params_fixture)) in [tuple, list]


def test_fixtures_params2(params_fixture, params_fixture2):
    if params_fixture2 == 'access':
        assert (type(params_fixture)) in [tuple, list]
    elif params_fixture2 == 'slice':
        assert (type(params_fixture)) in [tuple, list]
