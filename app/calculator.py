# app/calculator.py

from app.operations import Operations

def add_numbers(num1, num2):
    return Operations.add(num1, num2)

def subtract_numbers(num1, num2):
    return Operations.subtract(num1, num2)

def multiply_numbers(num1, num2):
    return Operations.multiply(num1, num2)

def divide_numbers(num1, num2):
    return Operations.divide(num1, num2)

# Dictionary to map operators to functions
operations_map = {
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
    "/": divide_numbers
}

def calculator():
    print("Simple Calculator - Type 'exit' to quit.")

    while True:
        try:
            expression = input("Enter operation (e.g., 2 + 3): ").strip()

            if expression.lower() == "exit":
                print("Exiting calculator. Goodbye!")
                break

            parts = expression.split()
            if len(parts) != 3:
                print("Invalid input format. Use format: number operator number")
                continue

            num1, operator, num2 = parts
            num1, num2 = float(num1), float(num2)

            # Fetch the corresponding function from the dictionary
            operation_function = operations_map.get(operator)

            if operation_function:
                result = operation_function(num1, num2)
                print(f"Result: {result}")
            else:
                print("Invalid operator. Use +, -, *, or /.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
