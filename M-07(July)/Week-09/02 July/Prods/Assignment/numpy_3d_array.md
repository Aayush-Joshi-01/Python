# Numpy 3-D Array Practice

- Create a 3D array of shape (4, 3, 2) with all elements initialized to zero.

- Create a 3D array of shape (2, 5, 4) with all elements initialized to one.

- Create a 3D array of shape (3, 3, 3) with random integers between 10 and 20.

1. Create a 3D array of dimensions 3x3x3 with all elements initialized to zero.

   ```python
   array_3d = np.zeros((3, 3, 3), dtype=int)
   ```

   Optionally, initialize with some values for practice:

   ```python
   array_3d = np.array([[[ 1,  2,  3], [ 4,  5,  6], [ 7,  8,  9]],
                        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                        [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
   ```

   Iterate over all elements in the 3D array.

2. Create a 3D array of shape (3, 4, 5) filled with random integers between 0 and 20, and print the array.

   - Access and print the element at position (2, 3, 4) in the 3D array created above.

   - Access and print the entire first row of the second matrix (i.e., when the first-dimension index is 1).

   - Add 5 to each element in the 3D array and print the result.

   - Multiply each element in the 3D array by 2 and print the result.

   - Calculate and print the sum of all elements in the 3D array.

   - Calculate and print the mean of the elements along the second axis.

   - Create a new array containing only the elements from the original 3D array that are greater than 10.

   - Replace all elements in the 3D array that are less than 10 with the value 0 and print the modified array.
