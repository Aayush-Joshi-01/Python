#  Write a program to print True if all characters in the string are digits, print
# False if not.

def check_if_all_characters_are_digits(string):
    for char in string:
        if char not in '0123456789':
            return False
    return True
if __name__ == '__main__':
    text = input("Enter the string of numbers: ")
    print(check_if_all_characters_are_digits(text))