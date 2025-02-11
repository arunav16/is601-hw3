# tests/test_operations.py

import pytest
from app.operations import Operations

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (-2, -4, -6),
    (0, 7, 7)
])
def test_add(a, b, expected):
    assert Operations.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-2, -4, 2),
    (0, 7, -7)
])
def test_subtract(a, b, expected):
    assert Operations.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 15),
    (-2, -4, 8),
    (0, 7, 0)
])
def test_multiply(a, b, expected):
    assert Operations.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-8, -4, 2),
    (7, 1, 7)
])
def test_divide(a, b, expected):
    assert Operations.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(10, 0)
