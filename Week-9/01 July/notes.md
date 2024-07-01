# NumPy

### What is NumPy?

NumPy (Numerical Python) is an open-source Python library widely used in science and engineering. It provides support for large multidimensional array data structures (ndarray) and a collection of functions to operate efficiently on these arrays.

### How to Import NumPy

After installing NumPy, import it into Python using:
```python
import numpy as np
```

### Array Basics

#### Array Creation
- **Using Python List:**
  ```python
  a = np.array([1, 2, 3, 4, 5, 6])
  ```
- **Two-dimensional Array:**
  ```python
  b = np.array([[1, 2, 3], [4, 5, 6]])
  ```

#### Accessing Elements
- **Indexing (0-indexed):**
  ```python
  a[0]  # Returns 1
  ```
- **Slicing (Returns a view):**
  ```python
  a[:3]  # Returns array([1, 2, 3])
  ```

#### Mutability
- **Arrays are mutable:**
  ```python
  a[0] = 10
  ```

#### Multi-dimensional Access
- **Accessing specific elements:**
  ```python
  b[1, 2]  # Returns 6
  ```

### Array Attributes
- **ndim:** Number of dimensions
  ```python
  a.ndim  # Returns 1
  ```
- **shape:** Tuple of array dimensions
  ```python
  b.shape  # Returns (2, 3)
  ```
- **size:** Total number of elements
  ```python
  b.size  # Returns 6
  ```
- **dtype:** Data type of elements
  ```python
  a.dtype  # Returns dtype('int64')
  ```

### Why Use NumPy?

- NumPy arrays are homogeneous and fixed-size, making them faster, more memory-efficient, and convenient for numerical operations compared to Python lists.
- Ideal for handling large datasets and performing complex mathematical operations efficiently.


## Creating Arrays

### Basic Array Creation

- **np.zeros():** Creates an array filled with zeros.
  ```python
  np.zeros(2)  # array([0., 0.])
  ```

- **np.ones():** Creates an array filled with ones.
  ```python
  np.ones(2)  # array([1., 1.])
  ```

- **np.empty():** Creates an uninitialized array.
  ```python
  np.empty(2)  # May vary: array([3.14, 42.])
  ```

- **np.arange():** Creates an array with a range of values.
  ```python
  np.arange(4)  # array([0, 1, 2, 3])
  ```

- **np.linspace():** Creates an array with evenly spaced values over a specified interval.
  ```python
  np.linspace(0, 10, num=5)  # array([ 0. ,  2.5,  5. ,  7.5, 10. ])
  ```

### Reshaping Arrays

- **reshape():** Reshapes an array without changing its data.
  ```python
  a = np.arange(6)
  b = a.reshape(3, 2)
  ```
  Result:
  ```
  array([[0, 1],
         [2, 3],
         [4, 5]])
  ```

### Adding Dimensions to Arrays

- **np.newaxis:** Adds a new axis to an array.
  ```python
  a = np.array([1, 2, 3, 4, 5, 6])
  row_vector = a[np.newaxis, :]
  col_vector = a[:, np.newaxis]
  ```
  Result:
  ```
  row_vector.shape  # (1, 6)
  col_vector.shape  # (6, 1)
  ```

- **np.expand_dims():** Expands an array by inserting a new axis at a specified position.
  ```python
  b = np.expand_dims(a, axis=1)
  c = np.expand_dims(a, axis=0)
  ```
  Result:
  ```
  b.shape  # (6, 1)
  c.shape  # (1, 6)
  ```

### Array Attributes

- **ndarray.ndim:** Number of array dimensions.
  ```python
  array_example.ndim  # 3
  ```

- **ndarray.size:** Total number of elements in the array.
  ```python
  array_example.size  # 24
  ```

- **ndarray.shape:** Tuple of integers indicating the array dimensions.
  ```python
  array_example.shape  # (3, 2, 4)
  ```

## Indexing and Slicing

### Indexing and Slicing Basics

```python
data = np.array([1, 2, 3])

data[1]         # 2
data[0:2]       # array([1, 2])
data[1:]        # array([2, 3])
data[-2:]       # array([2, 3])
```

### Conditional Indexing

```python
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a[a < 5])               # array([1, 2, 3, 4])
print(a[a >= 5])              # array([ 5,  6,  7,  8,  9, 10, 11, 12])
print(a[a % 2 == 0])          # array([ 2,  4,  6,  8, 10, 12])
print(a[(a > 2) & (a < 11)])  # array([ 3,  4,  5,  6,  7,  8,  9, 10])
```

### Using np.nonzero()

```python
b = np.nonzero(a < 5)
print(b)
# (array([0, 0, 0, 0]), array([0, 1, 2, 3]))

list_of_coordinates = list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    print(coord)
# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)

print(a[b])
# array([1, 2, 3, 4])
```

---

## Creating Arrays from Existing Data

### Slicing and Indexing

```python
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr1 = a[3:8]
# array([4, 5, 6, 7, 8])
```

### Stacking Arrays

```python
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

np.vstack((a1, a2))
# array([[1, 1],
#        [2, 2],
#        [3, 3],
#        [4, 4]])

np.hstack((a1, a2))
# array([[1, 1, 3, 3],
#        [2, 2, 4, 4]])
```

### Splitting Arrays

```python
x = np.arange(1, 25).reshape(2, 12)
np.hsplit(x, 3)
# [array([[ 1,  2,  3,  4],
#         [13, 14, 15, 16]]),
#  array([[ 5,  6,  7,  8],
#         [17, 18, 19, 20]]),
#  array([[ 9, 10, 11, 12],
#         [21, 22, 23, 24]])]
```

---

## Basic Array Operations

### Basic Operations

```python
data = np.array([1, 2])
ones = np.ones(2, dtype=int)

data + ones      # array([2, 3])
data - ones      # array([0, 1])
data * data      # array([1, 4])
data / data      # array([1., 1.])
```

### Aggregation Functions

```python
a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

a.sum()          # 4.8595784
a.min()          # 0.05093587
a.min(axis=0)    # array([0.12697628, 0.05093587, 0.26590556, 0.5510652 ])
```

### Broadcasting

```python
data = np.array([1.0, 2.0])
data * 1.6       # array([1.6, 3.2])
```


### Creating Matrices

You can create a 2D array (matrix) in NumPy by passing a list of lists to `np.array()`:

```python

# Creating a 2D array (matrix)
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)
```

Output:
```
array([[1, 2],
       [3, 4],
       [5, 6]])
```

### Indexing and Slicing Matrices

Indexing and slicing operations in matrices are similar to those in arrays:

```python
# Indexing
print(data[0, 1])  # Accessing element at row 0, column 1 (prints 2)

# Slicing
print(data[1:3])   # Slicing rows 1 to 2 (prints [[3, 4], [5, 6]])
print(data[0:2, 0]) # Slicing rows 0 to 1 and column 0 (prints [1, 3])
```

### Aggregating Matrices

You can aggregate matrices similarly to vectors using aggregation functions:

```python
# Aggregating
print(data.max())  # Maximum value in the entire matrix (prints 6)
print(data.min())  # Minimum value in the entire matrix (prints 1)
print(data.sum())  # Sum of all elements in the matrix (prints 21)

# Aggregating across columns or rows
print(data.max(axis=0))  # Maximum value in each column (prints [5, 6])
print(data.max(axis=1))  # Maximum value in each row (prints [2, 4, 6])
```

### Arithmetic Operations on Matrices

You can perform arithmetic operations on matrices if they are of the same size or if one of them has only one row or column (broadcasting):

```python
# Arithmetic operations
ones = np.array([[1, 1], [1, 1]])
print(data + ones)  # Element-wise addition (prints [[2, 3], [4, 5]])

# Broadcasting with different sizes
ones_row = np.array([[1, 1]])
print(data + ones_row)  # Broadcasting across rows (prints [[2, 3], [4, 5], [6, 7]])
```

### Transposing and Reshaping Matrices

You can transpose or reshape matrices using `.T` and `.reshape()` respectively:

```python
# Transposing
print(data.T)  # Transpose of the matrix (prints [[1, 3, 5], [2, 4, 6]])

# Reshaping
print(data.reshape(2, 3))  # Reshape the matrix to 2 rows, 3 columns
```

### Reversing Matrices

You can reverse the contents of matrices along rows, columns, or both using `np.flip()`:

```python
# Reversing rows
print(np.flip(data, axis=0))  # Reverses rows (prints [[5, 6], [3, 4], [1, 2]])

# Reversing columns
print(np.flip(data, axis=1))  # Reverses columns (prints [[2, 1], [4, 3], [6, 5]])
```

### Generating Random Numbers

You can generate random numbers to initialize matrices using `np.random`:

```python
# Generating random numbers
rng = np.random.default_rng()
random_matrix = rng.random((3, 2))  # Generates a 3x2 matrix of random numbers
print(random_matrix)
```


Here's a concise explanation and example code on how to use `.flatten()` and `.ravel()` in NumPy:

### Using `.flatten()` and `.ravel()` in NumPy

#### 1. `flatten()`

The `flatten()` method in NumPy returns a **copy** of the array collapsed into one dimension. It creates a new array, and modifications to the result do not affect the original array.

```python
import numpy as np

# Example array
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Flatten the array
a1 = x.flatten()

# Modify the flattened array
a1[0] = 99

# Original array remains unchanged
print(x)
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Flattened array is modified
print(a1)
# Output:
# [99  2  3  4  5  6  7  8  9 10 11 12]
```

#### 2. `ravel()`

The `ravel()` method returns a **view** of the original array whenever possible. It is a reference to the parent array, so modifying it will affect the original array.

```python
import numpy as np

# Example array
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Ravel the array
a2 = x.ravel()

# Modify the raveled array
a2[0] = 98

# Original array is modified
print(x)
# Output:
# [[98  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Raveled array is modified
print(a2)
# Output:
# [98  2  3  4  5  6  7  8  9 10 11 12]
```

### Key Differences:

- **Memory Efficiency**: `ravel()` does not create a copy, so it saves memory especially with large arrays.
- **Original Array Impact**: Changes to `ravel()` affect the original array because it shares the same data, while `flatten()` creates a separate copy.
- **View vs. Copy**: `ravel()` returns a view of the original array, while `flatten()` returns a copy.
