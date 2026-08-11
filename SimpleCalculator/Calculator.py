"""
Simple Calculator
------------------
A command-line calculator that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.

It takes user input, validates it, and handles errors such as
invalid numbers or division by zero using try/except.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 3 or 3.5).")


def get_operation():
    valid_ops = ("+", "-", "*", "/")
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operation! Please choose one of +, -, *, /.")


def calculate(num1, num2, op):
    try:
        if op == "+":
            return add(num1, num2)
        elif op == "-":
            return subtract(num1, num2)
        elif op == "*":
            return multiply(num1, num2)
        elif op == "/":
            return divide(num1, num2)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None


def main():
    print("=== Simple Calculator ===")
    print("Type 'q' at any time during number entry to quit.\n")

    while True:
        first_input = input("Enter first number (or 'q' to quit): ").strip()
        if first_input.lower() == "q":
            break

        try:
            num1 = float(first_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue

        op = get_operation()
        num2 = get_number("Enter second number: ")

        result = calculate(num1, num2, op)

       
        if result is not None:
            print(f"Result: {num1} {op} {num2} = {result}\n")

        
        again = input("Perform another calculation? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Thank you for using the Simple Calculator. Goodbye!")



if __name__ == "__main__":
    main()
