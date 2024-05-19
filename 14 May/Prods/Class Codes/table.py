
def print_table_of_a_number(argument):
    for num in range(2, argument+1):
        if num % 2 == 0:
            for iterator in range(1, 11):
                # if iterator % 2 == 0:
                    print(f"{num}" + " X " + f"{iterator} = {num * iterator}")
        print()

if __name__ == '__main__':
    number = int(input("Enter the number for which you want to print the table: "))
    print_table_of_a_number(number)