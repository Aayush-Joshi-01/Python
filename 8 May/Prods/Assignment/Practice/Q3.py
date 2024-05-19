# Write a program to append new string in the middle of a given string


def append_string(string):
    new_string = input("Enter the new string you want to append: ")
    new_string_length = len(new_string)
    middle_index = int(len(string) / 2)
    string = string[:middle_index] + new_string + string[middle_index:]
    print(string)

string = input("Enter the original string: ")
append_string(string)