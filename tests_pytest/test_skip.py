import sys

import pytest

# pytestmark = [pytest.mark.smoke, pytest.mark.strtest]
# pytestmark = pytest.mark.skipif(sys.platform != 'darwin', reason='test will run only for Mac')
# pytest -v -k 'first' test_skip.py
@pytest.mark.skip("Test skip")
def test_first():
    assert 5 + 5 == 10

@pytest.mark.skip()
def test_second():
    assert 5 + 5 == 11

@pytest.mark.skipif(sys.version_info <= (3, 10, 7), reason='sys version is ' + str(sys.version_info))
def test_third():
    assert 9 // 5 == 1


@pytest.mark.skipif(pytest.__version__ < '8.5.0', reason="pytest version is lower then 8.5.0")
def test_forth():
    assert 9 // 5 == 1
