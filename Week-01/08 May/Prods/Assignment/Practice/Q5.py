# Write a program to Count all letters, digits, and special symbols from a given string Given: str1= "P@#yn26at^&i5ve"
#
# Expected: Total counts of chars, digits, and symbols Chars = 8 Digits = 3 Symbol = 4

def count_letters_digits_symbols(input_string):
    letters = sum(1 for c in input_string if c.isalpha())
    digits = sum(1 for c in input_string if c.isdigit())
    symbols = sum(1 for c in input_string if not c.isalnum())
    return {'chars': letters, 'digits': digits, 'symbols': symbols}


input_string = "P@#yn26at^&i5ve"
result = count_letters_digits_symbols(input_string)
print(result)
