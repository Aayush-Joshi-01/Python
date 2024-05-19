# Write a program to String characters balance Test Strings str1 and str2 are balanced if all the characters in the str1 are present in str2. Given: s1 = "Fo" s2 = "PythonFastAPI"
#
# Expected: True

def string_characters_balance_test(s1, s2):
    for char in s1:
        if char not in s2:
            return False
    return True
s1 = "Fo"
s2 = "PythonFastAPI"
result = string_characters_balance_test(s1, s2)
print(result)