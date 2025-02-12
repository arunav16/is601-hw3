from app.calculator import Calculator
from app.calculations import CalculationsHistory

def perform_calculation(operation, num1, num2):
    """Performs the requested operation using the Calculator class."""
    calc = Calculator()
    return calc.perform_operation(operation, num1, num2)

def display_history():
    """Displays past calculations."""
    history = CalculationsHistory.get_history()
    print("\nCalculation History:" if history else "\nNo calculations in history yet.")
    for calc in history:
        print(calc)

def process_input(user_input):
    """Processes user input and executes the appropriate function."""
    actions = {
        "history": display_history,
        "clear": CalculationsHistory.clear_history,
        "exit": lambda: exit("Exiting calculator. Goodbye!")
    }

    if user_input in actions:
        actions[user_input]()
        return

    try:
        operation, num1, num2 = user_input.split()
        num1, num2 = float(num1), float(num2)
        result = perform_calculation(operation, num1, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Format: <operation> <num1> <num2> (e.g., add 5 3)")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

def main():
    print("\nWelcome to the Python CLI Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'history' to view past calculations, 'clear' to reset history, or 'exit' to quit.")

    while True:
        process_input(input("\nEnter operation and numbers: ").strip().lower())

if __name__ == "__main__":
    main()
