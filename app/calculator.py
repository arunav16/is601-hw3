from .operations import Operations

class Calculation:
    """Stores individual calculations."""
    def __init__(self, a, b, operation, result):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = result

class Calculator:
    """Handles multiple calculations with history."""
    history = []

    @classmethod
    def perform_operation(cls, a, b, operation):
        try:
            a, b = float(a), float(b)
            if operation == "add":
                result = Operations.add(a, b)
            elif operation == "subtract":
                result = Operations.subtract(a, b)
            elif operation == "multiply":
                result = Operations.multiply(a, b)
            elif operation == "divide":
                result = Operations.divide(a, b)
            else:
                return f"Unknown operation: {operation}"
            
            calc = Calculation(a, b, operation, result)
            cls.history.append(calc)
            return f"The result of {a} {operation} {b} is equal to {result}"
        
        except ValueError:
            return f"Invalid number input: {a} or {b} is not a valid number."
        except ZeroDivisionError as e:
            return f"An error occurred: {e}"

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history = []
