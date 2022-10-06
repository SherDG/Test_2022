import pytest


@pytest.fixture()
def setup_list():
    print('\n init setup. \n')
    cites = ['fdsfsd', 'fdsfsd23', 'fdsf1']
    return cites


def test_check_items(setup_list):
    print (setup_list);
    assert setup_list[0] == 'fdsfsd'


@pytest.mark.usefixtures('setup_list')
def test_check_items():
    assert 1 == 1

#
# def test_third():
#     assert 9 // 5 == 1
