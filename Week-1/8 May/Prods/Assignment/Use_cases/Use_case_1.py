#  You're developing a Python program to handle string operations for managing user input.
#  Implement the following functionalities:
# 1. Remove duplicate characters from a string while preserving the original order.
# 2. Check if a string is a palindrome.
# 3. Count the occurrences of each character in a string and store them in a dictionary.
# 4. Reverse words in a sentence while maintaining the order of words.

def remove_duplicates(input_string):
    seen = set()
    output_string = ""
    for char in input_string:
        if char not in seen:
            seen.add(char)
            output_string += char
    return output_string

def is_palindrome(input_string):
    return input_string == input_string[::-1]

def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def reverse_words(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# Example usage:
if __name__ == '__main__':
    input_string = "hello world"
    print(remove_duplicates(input_string))
    print(is_palindrome("madam"))
    print(count_characters("hello"))
    print(reverse_words("hello world"))