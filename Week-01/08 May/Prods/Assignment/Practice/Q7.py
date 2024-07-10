# Write a program to count occurrences of all characters within a string
# str1= "pythonpy"
# {'p':3, 'y':1, 't':1, 'h':1..etc}

def count_char_occurrences(input_string):
    count_dict = {}
    for char in input_string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


input_string = "pythonpy"
result = count_char_occurrences(input_string)
print(result)
