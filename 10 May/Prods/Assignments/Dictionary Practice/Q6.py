def sort_list_in_dict(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[key] = sorted(value)
    return result


if __name__ == '__main__':
    num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    print(sort_list_in_dict(num))
