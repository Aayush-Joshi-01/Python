# Write a program to split a given string on hyphens and display each substring. \
# text = "Violet-Indigo-Blue-Green-Yellow-Orange-Red" #['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']


def split_string_on_hyphens(input_string):
    substrings = input_string.split("-")
    return substrings
input_string = "Violet-Indigo-Blue-Green-Yellow-Orange-Red"
result = split_string_on_hyphens(input_string)
print(result)
