import pytest
from app.calculator import Calculator

def test_add():
    assert Calculator.perform_operation(5, 3, "add") == "The result of 5.0 add 3.0 is equal to 8.0"

def test_subtract():
    assert Calculator.perform_operation(10, 2, "subtract") == "The result of 10.0 subtract 2.0 is equal to 8.0"

def test_multiply():
    assert Calculator.perform_operation(4, 5, "multiply") == "The result of 4.0 multiply 5.0 is equal to 20.0"

def test_divide():
    assert Calculator.perform_operation(20, 4, "divide") == "The result of 20.0 divide 4.0 is equal to 5.0"

def test_divide_by_zero():
    assert Calculator.perform_operation(1, 0, "divide") == "An error occurred: Cannot divide by zero"

@pytest.mark.parametrize("a, b, operation, expected", [
    ("9", "3", "unknown", "Unknown operation: unknown"),
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.")
])
def test_invalid_input(a, b, operation, expected):
    assert Calculator.perform_operation(a, b, operation) == expected

def test_generated_data(test_data):
    a, b, operation, expected = test_data
    assert Calculator.perform_operation(a, b, operation) == f"The result of {float(a)} {operation} {float(b)} is equal to {float(expected)}"
