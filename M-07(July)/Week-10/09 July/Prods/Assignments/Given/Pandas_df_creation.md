### Task 1

1. **Create a Pandas DataFrame:**
   - Names: 'Amit', 'Ankit', 'Kapil', 'Sulabh'
   - Age: 28, 24, 35, 32
   - City: Indore, Pune, Indore, Mau

2. **Operations:**
   - Create the DataFrame and print it.
   - Display the first two rows.
   - Sort the DataFrame by age in descending order.
   - Select the rows where the age is greater than 30.
   - Select the 'Name' and 'City' columns.
   - Increase everyone's salary by 5%.

### Task 2

1. **Create a Pandas DataFrame:**
   - Names: 'Amit', 'Ankit', 'Kapil', 'Sulabh', 'Khushi'
   - Age: 28, 24, NaN, 32, 24
   - City: Indore, Pune, NaN, Mau, Varanasi

2. **Operations:**
   - Create the DataFrame and print it.
   - Fill missing values in 'Age' with the mean age.
   - Drop rows where any value is missing.

### Task 3

1. **Create a DataFrame from Data:**
   - Name: Amit, Ankit, Kapil, Sulabh
   - Age: 28, 22, 32, 20
   - City: Indore, Pune, Varanasi, Mau

2. **Operations:**
   - Create the DataFrame and print it.
   - Add a new column 'Country' with values ['INDIA', 'JAPAN', 'INDIA','AUSTRALIA'] to the DataFrame.
   - Select rows where the 'Age' is greater than 25.
   - Drop the 'City' column from the DataFrame.
   - Group the DataFrame by 'Country' and find the average age.

### Task 4

1. **Join two DataFrames:**
   - data1: Name ['Amit', 'Ankit', 'Sulabh'], Age [25, 30, 25]
   - data2: Name ['Amit', 'Ankit', 'Sulabh'], City ['Indore', 'Ghazipur', 'Mau']

### Task 5

1. **Create a Pandas DataFrame from a CSV file:**
   - File: employees.csv
     ```
     Name,Age,Department,Salary
     Alice,25,HR,50000
     Bob,30,Engineering,60000
     Charlie,35,Marketing,55000
     David,40,Engineering,65000
     Eve,45,HR,70000
     ```

2. **Operations:**
   - Create and manipulate the DataFrame.
   - Display the first 5 rows of the DataFrame.
   - Show columns ['Name', 'Department'].
   - Filter rows where Department is 'Engineering'.
   - Group by a column and calculate mean salary.
   - Add a new column 'Bonus * 500' in salary.
   - Save the modified DataFrame to a new CSV file.

### Task 6

1. **Download Global Land Temperatures by Country dataset:**
   - File Name: GlobalLandTemperaturesByCountry.csv

2. **Operations:**
   - Read the CSV file into a DataFrame.
   - Display the first few rows of the DataFrame.
   - Display summary statistics of the DataFrame.
   - Add a new column for the year extracted from the 'dt' column.
   - Calculate the average temperature by year for the filtered data.
   - Find all missing values.
   - Fill missing values with the mean temperature.
   - Find the country with the highest average temperature.
   