import sys
import platform
import pytest


@pytest.mark.xfail(reason='known issue')
def test_first():
    letters = 'dfssdfsdfdsfsdfs'
    assert letters[100]


@pytest.mark.xfail(raises=IndexError, reason="Index error")
def test_second():
    letters = 'dfssdfsdfdsfsdfs'
    assert letters[100]


@pytest.mark.xfail(platform.system() == 'Linux', reason='works only for Mac')
# xfail works if condition is true
def test_third():
    print(platform.system())
    letters = 'dfssdfsdfdsfsdfs'
    assert letters[50]
