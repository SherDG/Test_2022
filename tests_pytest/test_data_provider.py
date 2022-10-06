import pytest
from tests_pytest.utils.util import get_data


@pytest.mark.parametrize('a,b,c,d', get_data())
def test_data_from_utils(a,b,c,d):
    print(d)
