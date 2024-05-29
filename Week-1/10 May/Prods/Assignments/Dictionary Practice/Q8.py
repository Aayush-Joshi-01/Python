def remove_duplicates_in_dict_values(dictionary):
    result = {}
    for key, value in dictionary.items():
        unique_values = list(set(value))
        if unique_values:
            result[key] = unique_values[-1] if len(unique_values) == 1 else unique_values[1:]
        else:
            result[key] = []
    return result


if __name__ == '__main__':
    input_dict = {'first': [1, 4, 5, 6], 'sec': [1, 8, 9], 'third': [10, 22, 4], 'fourth': [5, 11, 22]}
    print(remove_duplicates_in_dict_values(input_dict))
