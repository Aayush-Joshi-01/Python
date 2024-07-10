# Write a program to find the last position of a substring in a given string.
# str1 = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?" substring = "chuck"

def find_last_position_of_substring(input_string, substring):
    last_position = input_string.rfind(substring)
    return last_position


input_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
substring = "chuck"
result = find_last_position_of_substring(input_string, substring)
print(result)
