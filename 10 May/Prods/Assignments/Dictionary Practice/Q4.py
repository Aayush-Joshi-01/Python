def find_highest_values(dct, n=3):
    values = list(dct.values())
    max_values = sorted(values, reverse=True)[:n]
    keys = [k for k, v in dct.items() if v in max_values]
    return keys

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
result = find_highest_values(my_dict)
print(result)