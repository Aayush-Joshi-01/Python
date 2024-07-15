def addition(num1: int, num2: int):
    return num1 + num2


def subtraction(num1: int, num2: int):
    return num1 - num2


def multiplication(num1: int, num2: int):
    return num1 * num2


def division(num1: int, num2: int):
    return num1 / num2


def main():
    while True:
        print("Welcome to the arithmetic calculator!")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation you want to perform (+, -, *, /): ")
        if operation == '+':
            print(addition(num1, num2))
        elif operation == '-':
            print(subtraction(num1, num2))
        elif operation == '*':
            print(multiplication(num1, num2))
        elif operation == '/':
            print(division(num1, num2))
        else:
            print("Invalid operation")
            break


if __name__ == '__main__':
    main()
