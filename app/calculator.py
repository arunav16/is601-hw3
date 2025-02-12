# app/calculator.py
from app.operations import Operations

class Calculator:
    """A simple REPL-based calculator using Operations class."""

    def __init__(self):
        """Initialize the calculator."""
        self.operations = Operations()

    def add(self, a, b):
        """Perform addition."""
        return self.operations.add(a, b)

    def subtract(self, a, b):
        """Perform subtraction."""
        return self.operations.subtract(a, b)

    def multiply(self, a, b):
        """Perform multiplication."""
        return self.operations.multiply(a, b)

    def divide(self, a, b):
        """Perform division with error handling."""
        return self.operations.divide(a, b)

    def start(self):
        """Run the calculator REPL."""
        print("Simple Calculator (Type 'exit' to quit)")
        while True:
            try:
                expr = input("Enter operation (e.g., 2 + 2): ").strip()
                if expr.lower() == "exit":
                    print("Exiting calculator.")
                    break
                
                # Tokenizing user input
                tokens = expr.split()
                if len(tokens) != 3:
                    print("Invalid input format. Use format: <num1> <operator> <num2>")
                    continue
                
                a, op, b = tokens
                a, b = float(a), float(b)

                # Mapping operators to functions
                operations_map = {
                    "+": self.add,
                    "-": self.subtract,
                    "*": self.multiply,
                    "/": self.divide
                }

                if op in operations_map:
                    result = operations_map[op](a, b)
                    print(f"Result: {result}")
                else:
                    print("Unsupported operation.")

            except ValueError:
                print("Invalid number format. Please enter valid numbers.")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
            except Exception as e:
                print(f"Unexpected error: {e}")
