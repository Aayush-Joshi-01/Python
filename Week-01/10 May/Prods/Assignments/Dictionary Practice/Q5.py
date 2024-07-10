def combine_values(item_list):
    result = {}
    for item in item_list:
        result[item['item']] = result.get(item['item'], 0) + item['amount']
    return result


if __name__ == '__main__':
    item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    print(combine_values(item_list))
