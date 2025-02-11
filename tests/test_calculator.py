# tests/test_calculator.py

import pytest
from app.calculator import calculator

def test_calculator_exit(monkeypatch, capsys):
    """Test if the calculator exits correctly when 'exit' is typed."""
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator()
    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out
