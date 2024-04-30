import pytest


@pytest.mark.skip
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.hello
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.this
def test_less():
    num = 100
    assert num < 200
