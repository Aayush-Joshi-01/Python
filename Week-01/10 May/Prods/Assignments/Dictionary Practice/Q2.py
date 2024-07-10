def segregate(dicts_list):
    result = []
    for d in dicts_list:
        result.extend(list(d.items()))
    return result


input_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
result = segregate(input_list)
print(result)
