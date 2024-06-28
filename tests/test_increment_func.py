import pytest
import logging

logger = logging.getLogger()


def increment(x):
    return x + 1


@pytest.mark.parametrize('numbers', [
    [5, 6],
    [3, 4],
    [11, 12],
    [11, 13]
])
def test_increment_func(numbers):
    addend, func_sum = numbers
    assert increment(addend) == func_sum


@pytest.mark.parametrize('addend', [3, 4, 7, 9])
def test_increment_func2(addend):
    expected_sum = addend
    expected_sum += 1
    assert increment(addend) == expected_sum
