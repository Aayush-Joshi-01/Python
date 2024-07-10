def get_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation_input():
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Please enter an arithmetic operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")


def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Error: Division by zero is not allowed.")
        return num1 / num2


def main():
    print("Welcome to the arithmetic calculator!")

    num1 = get_number_input("Please enter the first number: ")
    num2 = get_number_input("Please enter the second number: ")
    operation = get_operation_input()

    try:
        result = perform_operation(num1, num2, operation)
    except ZeroDivisionError as e:
        print(e)
    else:
        print(f"The result of {num1} {operation} {num2} is {result}")


if __name__ == "__main__":
    main()
