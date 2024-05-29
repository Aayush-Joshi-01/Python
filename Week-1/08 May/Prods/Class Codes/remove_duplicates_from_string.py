input_string = input("Enter the the string you want : ")
result = ''
for char in input_string:
    if char not in result:
        result = result + char
print(result)
