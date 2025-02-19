import subprocess

def run_calculator(args):
    """Helper function to run the calculator program via CLI and return output"""
    result = subprocess.run(["python", "main.py"] + args, capture_output=True, text=True)
    return result.stdout.strip()

def test_main_cli_addition():
    output = run_calculator(["5", "3", "add"])
    assert "The result of 5.0 add 3.0 is equal to 8.0" in output

def test_main_cli_subtraction():
    output = run_calculator(["9", "3", "subtract"])
    assert "The result of 9.0 subtract 3.0 is equal to 6.0" in output

def test_main_cli_multiplication():
    output = run_calculator(["4", "2", "multiply"])
    assert "The result of 4.0 multiply 2.0 is equal to 8.0" in output

def test_main_cli_division():
    output = run_calculator(["10", "2", "divide"])
    assert "The result of 10.0 divide 2.0 is equal to 5.0" in output

def test_main_cli_divide_by_zero():
    output = run_calculator(["8", "0", "divide"])
    assert "An error occurred: Cannot divide by zero" in output

def test_main_cli_invalid_operation():
    output = run_calculator(["9", "3", "unknown"])
    assert "Unknown operation: unknown" in output

def test_main_cli_invalid_number():
    output = run_calculator(["a", "3", "add"])
    assert "Invalid number input: a or 3 is not a valid number." in output

def test_main_cli_invalid_number_2():
    output = run_calculator(["5", "b", "subtract"])
    assert "Invalid number input: 5 or b is not a valid number." in output

def test_main_cli_missing_arguments():
    output = run_calculator(["5", "3"])
    assert "Usage: python main.py <num1> <num2> <operation>" in output

def test_main_cli_extra_arguments():
    output = run_calculator(["5", "3", "add", "extra"])
    assert "Usage: python main.py <num1> <num2> <operation>" in output
