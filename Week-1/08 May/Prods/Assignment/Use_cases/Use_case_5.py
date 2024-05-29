# You are working on a program to process user input for a search
# feature. Implement a Python function to extract all words from a given
# text string, excluding punctuation marks.
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


# Example usage:
text = "Hello, World! This is a test string. We're processing user input for a search feature."
print(remove_punctuation(text))
