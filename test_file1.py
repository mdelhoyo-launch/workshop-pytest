import pytest


def func(x):
    return x + 1


@pytest.mark.xfail
def test_answer():
    assert func(3) == 5


@pytest.mark.hello
def test_answer2():
    assert func(6) == 7
