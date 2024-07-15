# Python Lists

## Introduction

Lists are a versatile and fundamental data structure in Python used to store collections of items. They are ordered,
mutable (modifiable), and can contain elements of different data types. Lists are defined using square brackets `[ ]`
and elements are separated by commas.

## Creating Lists

```python
# Empty list
empty_list = []

# List with elements
my_list = [1, 2, 3, 4, 5]

# List with mixed data types
mixed_list = [1, 'hello', True, 3.14]
```

## Accessing Elements

Elements in a list can be accessed using indexing and slicing.

```python
my_list = [1, 2, 3, 4, 5]

# Accessing single element
print(my_list[0])  # Output: 1

# Slicing
print(my_list[1:4])  # Output: [2, 3, 4]
```

## Modifying Lists

Lists are mutable, meaning you can change their content.

```python
my_list = [1, 2, 3, 4, 5]

# Changing an element
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]
```

## List Operations

```python
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = [1] * 3
print(repeated_list)  # Output: [1, 1, 1]

# Length of a list
print(len(concatenated_list))  # Output: 6
```

## Common List Methods

- `append()`: Add an element to the end of the list.
- `extend()`: Extend the list by appending elements from another list.
- `insert()`: Insert an element at a specified position.
- `remove()`: Remove the first occurrence of a value from the list.
- `pop()`: Remove and return the element at the specified position.
- `index()`: Return the index of the first occurrence of a value.
- `count()`: Return the number of occurrences of a value.
- `sort()`: Sort the elements of the list in place.
- `reverse()`: Reverse the elements of the list in place.

## Conclusion

Lists are powerful and versatile data structures in Python, offering a wide range of operations for managing collections
of items efficiently.
