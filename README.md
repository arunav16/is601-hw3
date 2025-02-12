# Python OOP-Based Calculator

## Overview
This project implements a **modular, object-oriented calculator** using Python. It follows **best software engineering practices**, including encapsulation, separation of concerns, and proper error handling. The code is designed to satisfy a variety of evaluation criteria for creating a calculator application in Python.

---

## Features
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Encapsulated Design**:
  - `Operations` class handles arithmetic logic with static methods.
  - `Calculator` class manages the REPL interface for user input and error handling.
- **Error Handling**: Proper error handling for divide-by-zero and invalid inputs.
- **REPL (Read-Eval-Print Loop)**: Users can enter operations interactively. Type `'exit'` to quit.
- **Calculation History**: Tracks previous operations for user reference.

---

## Evaluation Criteria

### 1. **Basic Arithmetic Operations**
   - The calculator supports **addition**, **subtraction**, **multiplication**, and **division** as basic arithmetic operations.
   - All operations are implemented in the `Operations` class using static methods.

### 2. **Exception Handling and Divide by Zero**
   - **Error Handling**: Includes proper handling for division by zero and invalid inputs.
   - **ZeroDivisionError**: Raised when attempting division by zero.

### 3. **Static, Class, and Instance Methods**
   - **Static Methods**: The `Operations` class contains static methods for arithmetic operations (`add`, `subtract`, `multiply`, `divide`).
   - **Class Methods**: The `Calculator` class interacts with `Operations` through the `add`, `subtract`, `multiply`, and `divide` methods.
   - **Instance Methods**: The `Calculator` class has instance methods to manage user input and output results.

### 4. **Storing Operations in an Instance Property**
   - The `Calculator` class stores the operation history in an instance property, allowing the user to track previous calculations.

### 5. **Calculation History**
   - The `Calculator` class has a mechanism to store the history of calculations and output the last operation performed.
   - Users can see their previous calculations after each operation.

### 6. **Convenience Methods for History**
   - Convenience methods are provided to display, clear, and manage the calculation history.

### 7. **Parameterized Test Data**
   - The project includes parameterized tests for the arithmetic operations to ensure robustness across a variety of inputs and edge cases.
   - The `pytest` framework is used to test the operations with multiple data sets.

---
