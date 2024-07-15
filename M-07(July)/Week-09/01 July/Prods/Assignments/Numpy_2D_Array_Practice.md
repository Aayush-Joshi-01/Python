# 2-D Array Practice

**Array Creation and Attributes**

1. Create a 4x2 integer array and print its attributes (shape, size, dimensions).

2. Create a 5x2 integer array from a range between 100 and 200, with a difference of 10 between each element.

**Array Operations**

3. Given the 2-D array `arr = numpy.array([[34,43,73],[82,22,12],[53,94,66]])`, print the maximum value from axis 0 and the minimum value from axis 1.

4. Given `sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])` and `newColumn = numpy.array([[10,10,10]])`, delete the second column from `sampleArray` and insert `newColumn` in its place.

5. For the given NumPy array `arr = np.array([[4,8,16,20], [10,20,30,40],[20,22,23,25], [30,42,53,75],[32,33,34,35]])`, print the array of odd rows and even columns.

6. Add the NumPy arrays `arr1 = np.array([[4,5,6], [7,8,9]])` and `arr2 = np.array([[2,3,4], [5,6,7]])` and calculate the cube root of the elements in the resultant matrix.

**Handling Missing Values and Data Transformation**

* How to find if a given array has any null values?
* How to replace all missing values with 0 in a NumPy array?
* How to find the count of unique values in a NumPy array?
* How to convert a numeric array to a categorical (text) array?

**Advanced Array Manipulation**

* How to create a new column from existing columns of a NumPy array?
* How to find the most frequent value in a NumPy array?
* How to replace all values greater than a given value with a given cutoff?
* How to drop all missing values from a NumPy array
# Project: Student Grades Analysis

**Data**

We have a NumPy array `grades_data` representing student grades in different subjects over a semester. Each row represents a student, and each column represents a subject. Grades are out of 100.

grades_data = np.array([ [85, 90, 88, 72], [95, 82, 78, 88], [92, 90, 85, 88], [75, 80, 85, 90], [88, 82, 85, 92] ])



**Analysis**

* **Column-wise Calculations (axis=0):** Calculate the mean, maximum, minimum, and standard deviation of grades for each subject.
* **Row-wise Calculations (axis=1):** Calculate the mean, maximum, minimum, and standard deviation of grades for each student.
* **Total Grades:** Calculate the total grade for each student by summing their grades across all subjects.

