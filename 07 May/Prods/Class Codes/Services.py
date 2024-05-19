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


def if_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def if_even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


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
        print("You have chosen Fibonacci Series Service")
        number = int(input("Enter a number for fibonacci series: "))
        print(fibonacci_series(number))
        repeat_services()
    elif service == 3:
        print("You have chosen Armstrong Series Service")
        number = int(input("Enter a number for armstrong series: "))
        if armstrong_series(number):
            print(f"{number} is an Armstrong number")
        else:
            print(f"{number} is not an Armstrong number")
        repeat_services()
    elif service == 4:
        print("You have chosen Palindrome Service")
        argument = int(input("Enter a number/string for palindrome: "))
        if check_palindrome(argument):
            print(f"{argument} is a palindrome")
        else:
            print(f"{argument} is not a palindrome")
        repeat_services()
    elif service == 5:
        print("You have chosen Leap Year Service")
        year = int(input("Enter a year for leap year: "))
        if if_leap_year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
        repeat_services()
    elif service == 6:
        print("You have chosen Even or Odd Service")
        number = int(input("Enter a number for even or odd: "))
        if if_even_odd(number):
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")
        repeat_services()
    else:
        print("Enter a Valid Service ID")


def view_menu():
    print("Welcome to the Services Menu")
    print("1. Factorial Service")
    print("2. Fibonacci Series Service")
    print("3. Armstrong Series Service")
    print("4. Palindrome Service")
    print("5. Leap Year Service")
    print("6. Even or Odd Service")

if __name__ == "__main__":
    view_menu()
    Check_Again = True
    while Check_Again:
        service = int(input("Enter the service you want to use: "))
        choose_service(service)