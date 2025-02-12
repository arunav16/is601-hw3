# tests/test_calculator.py
import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(5, 3) == 8

def test_subtract(calculator):
    assert calculator.subtract(10, 4) == 6

def test_multiply(calculator):
    assert calculator.multiply(6, 7) == 42

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
