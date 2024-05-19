# Tuple

## Introduction
A tuple in Python is an immutable collection of elements, similar to lists but with the key distinction of immutability. Here are some key points about tuples:

- **Immutable Nature**: Tuples are immutable, meaning once created, their elements cannot be changed. This immutability makes iterating over tuples faster compared to lists.
- **Static Character**: Tuples ensure the integrity of data, as their contents cannot be altered after creation.
- **Ordered and Unchangeable**: Like lists, tuples maintain the order of elements, but unlike lists, they cannot be modified once created.
- **Usage in Dictionaries**: Tuples with immutable keys can be used as keys in dictionaries, providing a unique and unchangeable identifier.

## Sets

### Introduction
Sets in Python are collections of unique elements with no specific order. Here are some important characteristics of sets:

- **Unique Values**: Sets store only unique elements, eliminating duplicates automatically.
- **Support for Logical Operations**: Sets support operations like union, intersection, and difference, making them useful for set theory operations.
- **Mutable**: Unlike tuples, sets are mutable, meaning their elements can be added or removed after creation.
- **Support for Hashing**: Sets support hashing, which allows for efficient membership testing.
- **No Slicing or Indexing**: Sets do not support slicing or indexing because they are unordered collections.

### Example
```python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # Output: {'cherry', 'banana', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # Output: {'banana', 'papaya', 'mango', 'apple', 'pineapple', 'cherry'}
```

## Frozen Sets

### Introduction
Frozen sets in Python are similar to sets, but they are immutable. Once created, the elements of a frozen set cannot be changed. Here are some key points about frozen sets:

- **Immutable**: Frozen sets, like tuples, are immutable collections, making them suitable for situations where immutability is desired.
- **Hashable Objects**: Frozen sets support hashable objects, enabling their use as elements in other sets or as keys in dictionaries.
- **Unordered**: Frozen sets, like sets, do not maintain a specific order of elements.
- **Similar to Mathematical Sets**: Frozen sets mirror mathematical sets, allowing for set operations like union, intersection, and difference.

## Dictionary

### Introduction
A dictionary in Python is an unordered collection of key-value pairs. Here are some key aspects of dictionaries:

- **Ordered**: Dictionaries maintain the order of insertion, preserving the sequence of key-value pairs.
- **Key-Value Pairs**: Each element in a dictionary consists of a key and its corresponding value.
- **Accessing by Keys**: Elements in a dictionary are accessed using their keys rather than numerical indices.
- **Mutable and Indexed**: Dictionaries are mutable, allowing for the addition, removal, and modification of key-value pairs.
- **Key Immunity**: Keys in dictionaries must be immutable types, such as strings, integers, or tuples.