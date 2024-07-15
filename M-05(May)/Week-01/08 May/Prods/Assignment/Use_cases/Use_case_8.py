# You are building a program to process text data. Write a Python
# function to find the longest substring of consecutive vowels in a given
# string.

def longest_vowel_substring(s):
    vowels = set('aeiou')
    longest = ''
    current = ''
    for char in s:
        if char.lower() in vowels:
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ''
    if len(current) > len(longest):
        longest = current
    return longest


if __name__ == '__main__':
    s = input("Enter a string: ")
    print(longest_vowel_substring(s))
