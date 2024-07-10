# Write a program to remove special symbols / punctuation from a string.
# str1 = "Hello!, he said, -- I have $45 & you?" #Hello he said I have 45 you
import string


def remove_punctuation(input_string):
    # Create an empty string to store the result
    result = ""
    # Iterating through each character in the input string
    for char in input_string:
        # If the character is not a punctuation, add it to the result
        if char not in string.punctuation:
            result += char
    return result


input_string = "Hello!, he said, -- I have $45 & you?"
result = remove_punctuation(input_string)
print(result)
