def list_to_dict(lst):
    groups = {}
    for item in lst:
        if item in groups:
            groups[item].append(item)
        else:
            groups[item] = [item]
    return groups

test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
result = list_to_dict(test_list)
print(result)