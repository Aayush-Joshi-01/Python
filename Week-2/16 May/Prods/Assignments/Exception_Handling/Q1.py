def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def divide_numbers():
    print("Welcome to the division calculator!")

    numerator = get_integer_input("Please enter the numerator (an integer): ")
    denominator = get_integer_input("Please enter the denominator (an integer): ")

    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The result of {numerator} divided by {denominator} is {result}")


if __name__ == "__main__":
    divide_numbers()
