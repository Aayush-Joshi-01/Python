# Python that checks if a variable x is between 0 and 10, or between 20 and 30, or between 40 and 50, or between 60 and 70
def check_in_between(value):
    number = int(value)
    if 0 <= number <= 10:
        print("number is between 0 and 10")
    elif 20 <= number <= 30:
        print("number is between 20 and 30")
    elif 40 <= number <= 50:
        print("number is between 40 and 50")
    elif 60 <= number <= 70:
        print("number is between 60 and 70")
    else:
        print("number is not between 0 and 70")
# Write a program to check user name and password if both is true then print login successful either print login failure.
def check_user_name_and_password(user_name, password):
    if user_name == 'admin' and password == '123':
        print("login successful")
    else:
        print("login failure")

# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 100 and 200 (both included).
def check_divisible_by_7_and_multiple_of_5():
    for number in range(100, 201):
        if number % 35 == 0:
            print(number)
# write a program that accept a three digit  number from user and find greater digit.
def find_greater_digit(number):
    number = str(number)
    if number[0] > number[1] and number[0] > number[2]:
        print(number[0])
    elif number[1] > number[0] and number[1] > number[2]:
        print(number[1])
    else:
        print(number[2])

def take_input(service):
    if service == '1':
        value = input('Please enter the value: ')
        check_in_between(value)
    elif service == '2':
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        check_user_name_and_password(username, password)
    elif service == '3':
        check_divisible_by_7_and_multiple_of_5()
    elif service == '4':
        number = int(input('Please enter the number: '))
        if len(str(number)) == 3:
            find_greater_digit(number)
        else:
            print("Please enter a three digit number ")
            take_input(service)

def all_services():
    print("All services are as follows: ")
    print("Service 1 check_in_between()")
    print("Service 2 check_user_name_and_password()")
    print("Service 3 check_divisible_by_7_and_multiple_of_5()")
    print("Service 4 find_greater_digit()")
    service = int(input("Enter the number of service you want to use"))
    take_input(service)


if __name__ == '__main__':
    all_services()