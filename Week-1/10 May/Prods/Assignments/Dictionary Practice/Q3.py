def print_distinct_values(dct):
    values = set()
    for d in dct:
        values.add(list(d.values())[0])
    print(values)

input_dict = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
print_distinct_values(input_dict)