# Write a program to create a new string made of the first, middle, and last
# characters of each input string
# Given:
# str1 = Python
# str2 = django
# expected: Pdtjno

def first_middle_last_chars(str1, str2):
    # Check if the input strings are empty or have less than 3 characters
    if not str1 or len(str1) < 3 or not str2 or len(str2) < 3:
        return ""
    # Find the middle characters of the input strings
    middle_index1 = len(str1) // 2 -1
    middle_index2 = len(str2) // 2 -1
    # Create the new string
    new_string = str1[0] + str2[0] + str1[middle_index1] + str2[middle_index2] + str1[-1] + str2[-1]

    return new_string

# Example usage:
str1 = "Python"
str2 = "dajngo"
print(first_middle_last_chars(str1, str2))