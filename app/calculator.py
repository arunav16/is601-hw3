from app.operations import Operations
from app.calculations import CalculationsHistory

class Calculator:
    """A simple calculator using Operations and history management."""

    def __init__(self):
        self.result = None

    def perform_operation(self, operation, a, b):
        """Executes the given operation and stores it in history."""
        
        operations_map = {
            "add": Operations.add,
            "subtract": Operations.subtract,
            "multiply": Operations.multiply,
            "divide": Operations.divide
        }

        if operation not in operations_map:
            raise ValueError("Invalid operation")

        self.result = operations_map[operation](a, b)
        CalculationsHistory.add_calculation(operation, a, b, self.result)
        return self.result

    def get_last_result(self):
        return self.result
