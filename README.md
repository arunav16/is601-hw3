# Python Calculator

## Overview
This is a simple Python-based calculator that supports basic arithmetic operations. The `Operations` class provides static methods for addition, subtraction, multiplication, and division.

---

## Features
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Exception Handling**: Prevents division by zero by raising an error.
- **Object-Oriented Design**: Encapsulated operations using a class with static methods.
=======
# Python Calculator Project

## Overview
This Python calculator project provides a command-line interface for performing basic arithmetic operations, including addition, subtraction, multiplication, and division. The calculator also includes error handling for invalid inputs and operations. Additionally, the project utilizes the **Faker** library to generate test data for testing purposes.

## Specifications

### Functional Requirements
1. **Basic Operations**:
    - **Addition**: Computes the sum of two numbers.
    - **Subtraction**: Computes the difference between two numbers.
    - **Multiplication**: Computes the product of two numbers.
    - **Division**: Computes the quotient of two numbers with error handling for division by zero.

2. **Error Handling**:
    - Raises a `ValueError` if either input is a non-numeric string.
    - Handles division by zero with a specific error message.
    - Handles unknown operations with a specific error message.

3. **History Management**:
    - Maintains a history of calculations performed during the session.

4. **Test Data Generation**:
    - Utilizes the **Faker** library to generate realistic test data for testing various scenarios, ensuring robustness in handling different inputs.

### Non-Functional Requirements
1. **Usability**: The command-line interface should be user-friendly and provide clear output for operations and errors.
2. **Performance**: The calculations should be performed in a reasonable time frame (sub-second).
3. **Testing**: The code should include unit tests for all functionalities, using the Faker library to generate test data.

## Use Cases

### Use Case 1: Addition
- **Input**: `5`, `3`, `add`
- **Expected Output**: `The result of 5.0 add 3.0 is equal to 8.0`

### Use Case 2: Subtraction
- **Input**: `10`, `2`, `subtract`
- **Expected Output**: `The result of 10.0 subtract 2.0 is equal to 8.0`

### Use Case 3: Multiplication
- **Input**: `4`, `5`, `multiply`
- **Expected Output**: `The result of 4.0 multiply 5.0 is equal to 20.0`

### Use Case 4: Division
- **Input**: `20`, `4`, `divide`
- **Expected Output**: `The result of 20.0 divide 4.0 is equal to 5.0`

### Use Case 5: Division by Zero
- **Input**: `1`, `0`, `divide`
- **Expected Output**: `An error occurred: Cannot divide by zero`

### Use Case 6: Invalid Operation
- **Input**: `9`, `3`, `unknown`
- **Expected Output**: `Unknown operation: unknown`

### Use Case 7: Invalid Number Input
- **Input**: `a`, `3`, `add`
- **Expected Output**: `Invalid number input: a or 3 is not a valid number.`

### Use Case 8: Another Invalid Number Input
- **Input**: `5`, `b`, `subtract`
- **Expected Output**: `Invalid number input: 5 or b is not a valid number.`

## Testing
### Test Cases
The project includes test cases that cover all functional requirements using `pytest`. Each test validates the expected output against the actual output for both valid and invalid inputs. The tests utilize the Faker library to generate random numeric inputs for testing.

### Coverage
The test suite aims for high coverage across all functionalities and edge cases, ensuring reliability and correctness.

## Future Enhancements
- Implement additional mathematical functions (e.g., exponentiation, square root).
- Create a graphical user interface (GUI) for better user interaction.
- Add persistent storage for calculation history.

## Conclusion
This Python calculator project serves as a fundamental tool for basic arithmetic operations while demonstrating good programming practices, including error handling and testing. The integration of the Faker library enhances the testing process, ensuring that the calculator can handle a variety of input scenarios effectively.

