# Dictionary Practice

1: Write a Python program group Similar items to Dictionary Values List

```
Input: test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
Expected: {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
``` 

```commandline
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

>>>
{4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}

Process finished with exit code 0
```

2: Write a Python program convert List of Dictionaries to List of Lists

```
Input:  [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}] 
Expected: [['Gfg', 'best'], [123, 10], [51, 7]] 
```

```commandline
def segregate(dicts_list):
    result = []
    for d in dicts_list:
        result.extend(list(d.items()))
    return result

input_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
result = segregate(input_list)
print(result)

>>>
[('Gfg', 123), ('best', 10), ('Gfg', 51), ('best', 7)]

Process finished with exit code 0
```

3: Write a Python program to print all distinct values in a dictionary.

```
Original List:  [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]        
                                                                                    
Unique Values: {'S009', 'S002', 'S007', 'S005', 'S001'}  
```

```commandline
def print_distinct_values(dct):
    values = set()
    for d in dct:
        values.add(list(d.values())[0])
    print(values)

input_dict = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]
print_distinct_values(input_dict)

>>>
{'S007', 'S002', 'S001', 'S009', 'S005'}

Process finished with exit code 0
```

4: Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

```
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
Expected: ['b', 'e', 'c']
```

```commandline
def find_highest_values(dct, n=3):
    values = list(dct.values())
    max_values = sorted(values, reverse=True)[:n]
    keys = [k for k, v in dct.items() if v in max_values]
    return keys

my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
result = find_highest_values(my_dict)
print(result)

>>>
['b', 'c', 'e']

Process finished with exit code 0

```

5: Write a Python program to combine values in a list of dictionaries.

```
Input: item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

Expected: ({'item1': 1150, 'item2': 300})
```

```commandline
def combine_values(item_list):
    result = {}
    for item in item_list:
        result[item['item']] = result.get(item['item'], 0) + item['amount']
    return result


if __name__ == '__main__':
    item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    print(combine_values(item_list))
    
>>>
{'item1': 1150, 'item2': 300}

Process finished with exit code 0
```

6: Write a Python program to sort a list alphabetically in a dictionary.

```
Input: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
Expected: {'n1': [1, 2, 3], ‘n2’:10,'n3': [1, 2, 5], 'n3': [2, 3, 4]}, ‘n4’: 30
```

```commandline
def sort_list_in_dict(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[key] = sorted(value)
    return result


if __name__ == '__main__':
    num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    print(sort_list_in_dict(num))
```

```commandline
{'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}

Process finished with exit code 0
```

7: Write a Python program to count the number of items in a dictionary value that is a list.

```
Input: dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

Expected: 5
```

```commandline
def count_items_in_list(d):
    return sum(len(v) for v in d.values())


if __name__ == '__main__':
    dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    print(count_items_in_list(dict))
```

```commandline
5

Process finished with exit code 0
```

8: Write a Python program remove duplicate values across Dictionary Values

```
Input: {'first': [1, 4, 5, 6], 'sec': [1, 8, 9], 'third': [10, 22, 4], 'fourth': [5, 11, 22]}
Expected: {'first': [6], 'sec': [8, 9], 'third': [10], 'fourth': [11]}
```

```commandline
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
```

```commandline
{'first': [4, 5, 6], 'sec': [1, 9], 'third': [4, 22], 'fourth': [5, 22]}

Process finished with exit code 0

```

9: Write a Python program counting the frequencies in a list using dictionary in Python

```
Input:  [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
Expected:  1 : 5
           2 : 4
           3 : 3
           4 : 3
           5 : 2
```

```commandline
def count_frequencies(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict


if __name__ == '__main__':
    input_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    freq_dict = count_frequencies(input_list)
    for key, value in freq_dict.items():
        print(f"{key} : {value}")

```

```commandline
1 : 5
5 : 2
3 : 3
4 : 3
2 : 4

Process finished with exit code 0
```