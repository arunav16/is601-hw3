import pytest
from app.operations import Operations

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8), (-1, -1, -2), (0, 0, 0)
])
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2), (-1, -1, 0), (0, 5, -5)
])
def test_subtract(a, b, expected):
    assert Operations.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 15), (-1, -1, 1), (0, 5, 0)
])
def test_multiply(a, b, expected):
    assert Operations.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2), (-10, -2, 5), (9, 3, 3)
])
def test_divide(a, b, expected):
    assert Operations.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(5, 0)
