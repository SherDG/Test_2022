import pytest
from functools import reduce
import operator


@pytest.mark.parametrize('test_input', [54, 24, 32])
def test_first(test_input):
    assert test_input < 50


data = [
    ([2, 3, 4], 'sum', 9),
    ([2, 3, 4], 'prod', 24)
]


@pytest.mark.parametrize('a,b,c', data)
def test_second(a, b, c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert reduce(operator.mul, a, 1) == c

#
# def test_third():
#     assert 9 // 5 == 1
