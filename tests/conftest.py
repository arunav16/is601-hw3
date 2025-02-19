import pytest
from faker import Faker

fake = Faker()

def generate_test_cases():
    test_cases = []
    operations = ["add", "subtract", "multiply", "divide"]
    
    for _ in range(100):  # Generate 100 test cases
        a, b = fake.random_int(1, 100), fake.random_int(1, 100)
        operation = fake.random_element(operations)
        
        if operation == "add":
            expected = a + b
        elif operation == "subtract":
            expected = a - b
        elif operation == "multiply":
            expected = a * b
        elif operation == "divide":
            expected = "An error occurred: Cannot divide by zero" if b == 0 else a / b
        
        test_cases.append((a, b, operation, expected))
    
    return test_cases

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test cases to generate")

@pytest.fixture(params=generate_test_cases())
def test_data(request):
    return request.param
