import pytest
from app.calculator import Calculator
from app.calculations import CalculationsHistory

def test_calculator_operations():
    calc = Calculator()
    
    assert calc.perform_operation("add", 2, 3) == 5
    assert calc.perform_operation("subtract", 7, 2) == 5
    assert calc.perform_operation("multiply", 4, 3) == 12
    assert calc.perform_operation("divide", 10, 2) == 5

def test_calculation_history():
    CalculationsHistory.clear_history()
    
    calc = Calculator()
    calc.perform_operation("add", 1, 1)
    calc.perform_operation("multiply", 2, 2)
    
    history = CalculationsHistory.get_history()
    
    assert len(history) == 2
    assert history[0].operation == "add"
    assert history[1].operation == "multiply"

def test_clear_history():
    CalculationsHistory.clear_history()
    assert len(CalculationsHistory.get_history()) == 0
