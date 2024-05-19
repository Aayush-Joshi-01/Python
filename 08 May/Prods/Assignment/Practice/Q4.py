# Write a program to arrange string characters such that lowercase letters should come first
# Given:str1 = pYthoNFastAPI Expected: pthoastYNFAPI

def arrange_string_characters(input_string):
    lowercase_letters = [c for c in input_string if c.islower()]
    uppercase_letters = [c for c in input_string if c.isupper()]
    other_characters = [c for c in input_string if not c.isalpha()]
    return ''.join(lowercase_letters + uppercase_letters + other_characters)

input_string = "pYthoNFastAPI"
result = arrange_string_characters(input_string)
print(result)