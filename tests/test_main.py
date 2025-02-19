import pytest 
from main import main

def test_main_addition(monkeypatch, capsys):
    """Test command-line execution for addition."""
    monkeypatch.setattr('sys.argv', ['main.py', '5', '3', 'add'])
    main()
    captured = capsys.readouterr()
    assert "The result of 5.0 add 3.0 is equal to 8.0" in captured.out

def test_main_subtraction(monkeypatch, capsys):
    """Test command-line execution for subtraction."""
    monkeypatch.setattr('sys.argv', ['main.py', '10', '2', 'subtract'])
    main()
    captured = capsys.readouterr()
    assert "The result of 10.0 subtract 2.0 is equal to 8.0" in captured.out

def test_main_multiplication(monkeypatch, capsys):
    """Test command-line execution for multiplication."""
    monkeypatch.setattr('sys.argv', ['main.py', '4', '5', 'multiply'])
    main()
    captured = capsys.readouterr()
    assert "The result of 4.0 multiply 5.0 is equal to 20.0" in captured.out

def test_main_division(monkeypatch, capsys):
    """Test command-line execution for division."""
    monkeypatch.setattr('sys.argv', ['main.py', '20', '4', 'divide'])
    main()
    captured = capsys.readouterr()
    assert "The result of 20.0 divide 4.0 is equal to 5.0" in captured.out

def test_main_divide_by_zero(monkeypatch, capsys):
    """Test command-line handling of division by zero."""
    monkeypatch.setattr('sys.argv', ['main.py', '1', '0', 'divide'])
    main()
    captured = capsys.readouterr()
    assert "An error occurred: Cannot divide by zero" in captured.out

def test_main_invalid_operation(monkeypatch, capsys):
    """Test handling of an invalid operation."""
    monkeypatch.setattr('sys.argv', ['main.py', '9', '3', 'unknown'])
    main()
    captured = capsys.readouterr()
    assert "Unknown operation: unknown" in captured.out

def test_main_invalid_number(monkeypatch, capsys):
    """Test invalid number input handling."""
    monkeypatch.setattr('sys.argv', ['main.py', 'a', '3', 'add'])
    main()
    captured = capsys.readouterr()
    assert "Invalid number input: a or 3 is not a valid number." in captured.out

def test_main_invalid_number_2(monkeypatch, capsys):
    """Test another invalid number input scenario."""
    monkeypatch.setattr('sys.argv', ['main.py', '5', 'b', 'subtract'])
    main()
    captured = capsys.readouterr()
    assert "Invalid number input: 5 or b is not a valid number." in captured.out
