def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def fibonacci_series(number):
    if number <= 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    else:
        list_of_numbers = [0, 1]
        while len(list_of_numbers) < number:
            list_of_numbers.append(list_of_numbers[-1] + list_of_numbers[-2])
        return list_of_numbers


def armstrong_series(number):
    number_string = str(number)
    return sum(int(digit) ** len(number_string) for digit in number_string) == number


def check_palindrome(argument):
    argument = str(argument)
    return argument == argument[::-1]


def print_table_of_a_number(argument):
    for i in range(1, 21):
        print(f"{argument}" + " X " + f"{i} = {argument * i}")


def find_sum_of_digits(argument):
    return sum(int(digit) for digit in str(argument))


def check_perfect_number(argument):
    return sum(number for number in range(1, argument) if argument % number == 0) == argument


def repeat_services():
    yes_or_no = input("Do you Wish to Continue y / n : ")
    if yes_or_no.lower() in ['y', 'yes']:
        if input("Do you want to view menu again y / n : ") in ['y', 'yes']:
            view_menu()
            return
        return
    else:
        global Check_Again
        Check_Again = False


def choose_service(service):
    if service == 1:
        print("You have chosen Factorial Service")
        number = int(input("Enter a number for factorial: "))
        print(factorial(number))
        repeat_services()
    elif service == 2:
        print("You have chosen Table Service")
        number = int(input("Enter a number for table: "))
        print_table_of_a_number(number)
        repeat_services()
    elif service == 3:
        print("You have chosen Fibonacci Series Service")
        number = int(input("Enter a number for fibonacci series: "))
        print(fibonacci_series(number))
        repeat_services()
    elif service == 4:
        print("You have chosen Sum of Digits Service")
        argument = int(input("Enter a number for sum of digits: "))
        print(find_sum_of_digits(argument))
        repeat_services()
    elif service == 5:
        print("You have chosen Perfect Number Service")
        argument = int(input("Enter a number for perfect number: "))
        if check_perfect_number(argument):
            print(f"{argument} is a perfect number")
        else:
            print(f"{argument} is not a perfect number")
        repeat_services()
    elif service == 6:
        print("You have chosen Palindrome Service")
        argument = int(input("Enter a number/string for palindrome: "))
        if check_palindrome(argument):
            print(f"{argument} is a palindrome")
        else:
            print(f"{argument} is not a palindrome")
        repeat_services()
    elif service == 7:
        print("You have chosen Armstrong Series Service")
        number = int(input("Enter a number for armstrong series: "))
        if armstrong_series(number):
            print(f"{number} is an Armstrong number")
        else:
            print(f"{number} is not an Armstrong number")
        repeat_services()
    else:
        print("Enter a Valid Service ID")


# 1-	Write a program to Calculator Factorial of any number.
# 2-	Write a program to print table of any number.
# 3-	Write a program to print Fibonacci Series.
# 4-	Write a program to Calculator sum of digits of a number.
# 5-	Write a program to Calculator number entered  is a perfect number or not.
# 6-	Write a program that accept a three digit number from user and check whether it is palindrome or not?
# 7-	Write a program that accept a three digit number from user and check whether it is Armstrong or not?
def view_menu():
    print("------------------------------------")
    print("Welcome to the Services Menu")
    print("1. Factorial Service")
    print("2. Table Service")
    print("3. Fibonacci Series Service")
    print("4. Sum of Digits Service")
    print("5. Perfect Number Service")
    print("6. Palindrome Service")
    print("7. Sum of Digits Service")
    print("------------------------------------")


if __name__ == "__main__":
    view_menu()
    Check_Again = True
    while Check_Again:
        service = int(input("Enter the service you want to use: "))
        choose_service(service)
