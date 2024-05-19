# You are developing a program to clean and preprocess text data.
# Write a Python function to remove leading and trailing whitespaces from a given string.


def remove_whitespace(input_string):
    return input_string.strip()

# Example usage:
input_string = "   Hello, World!   "
print(remove_whitespace(input_string))