
# def greatest_number(number_1, number_2, number_3):
#     return number_1 if number_1 > number_2 and number_1 > number_3 else number_2 if number_2 > number_1 and number_2 > number_3 else number_3

def greatest_between_number(number_1, number_2, number_3):
    if number_1 > number_2 and number_1 > number_3:
        return number_1
    elif number_2 > number_1 and number_2 > number_3:
        return number_2
    else:
        return number_3

# def greater_number(number_1, number_2):
#     return number_1 if number_1 > number_2 else number_2
def get_inputs():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    number_3 = int(input("Enter the third number: "))
    return number_1, number_2, number_3

if __name__ == '__main__':
    num_1, num_2, num_3 = get_inputs()
    print(greatest_between_number(num_1, num_2, num_3))