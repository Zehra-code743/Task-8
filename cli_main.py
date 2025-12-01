from calculator import calculate
from utils import validate_numeric_input

def main():
    print("Simple Calculator (CLI Mode)")
    while True:
        try:
            num1_input = input("Enter the first number (or 'q' to quit): ")
            if num1_input.lower() == 'q':
                break

            operation = input("Enter operation (add, subtract, multiply, divide): ")
            if operation.lower() == 'q':
                break

            num2_input = input("Enter the second number (or 'q' to quit): ")
            if num2_input.lower() == 'q':
                break

            num1 = validate_numeric_input(num1_input, "first number")
            num2 = validate_numeric_input(num2_input, "second number")

            result = calculate(num1, num2, operation)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print("\n")

if __name__ == "__main__":
    main()
