class Calculation:
    """Represents a single calculation operation."""
    
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def __repr__(self):
        return f"{self.operation}({self.a}, {self.b}) = {self.result}"


class CalculationsHistory:
    """Manages calculation history using class methods and instance methods."""
    
    history = []

    @classmethod
    def add_calculation(cls, operation, a, b, result):
        calc = Calculation(operation, a, b, result)
        cls.history.append(calc)

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()
