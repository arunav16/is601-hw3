import sys
from app.calculator import Calculator

def main(args = None):
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

    num1, num2, operation = sys.argv[1], sys.argv[2], sys.argv[3]
    result = Calculator.perform_operation(num1, num2, operation)
    print(result)

if __name__ == "__main__":
    main()
