Certainly! Let's structure the SQL queries for each operation you've listed, along with sample outputs.

### Create a New Table

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10, 2)
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);
```

```commandline
Query OK, 0 rows affected (0.13 sec)

Query OK, 0 rows affected (0.04 sec)
```

### Insert Data into Both Tables

```sql
INSERT INTO Employees (EmployeeID, EmployeeName, Department, Salary)
VALUES (1, 'Aaradhy Vijayawat', 'HR', 50000),
       (2, 'Aaradhya Korde', 'IT', 60000),
       (3, 'Shivom Munshi', 'Finance', 55000),
       (4, 'Avichal Trivedi', 'HR', 52000),
       (5, 'Rudraksh Kumrawat', 'IT', 58000),
       (6, 'Sarthak Dongare', 'Finance', 56000),
       (7, 'Aayush Joshi', 'IT', 70000),
       (8, 'Jatin Sahijwani', 'IT', 59000),
       (9, 'Anirudh Singh', 'Finance', 57000),
       (10, 'Mayank Tilwankar', 'IT', 60000);


INSERT INTO Departments (DepartmentID, DepartmentName)
VALUES (1, 'HR'),
       (2, 'IT'),
       (3, 'Finance'),
       (4, 'Marketing'),
       (5, 'Operations');

```

```commandline
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

Query OK, 5 rows affected (0.00 sec)
Records: 5  Duplicates: 0  Warnings: 0
```

### Equi Join

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
JOIN Departments d ON e.Department = d.DepartmentName;
```

```commandline
+-------------------+----------------+
| EmployeeName      | DepartmentName |
+-------------------+----------------+
| Aaradhy Vijayawat | HR             |
| Aaradhya Korde    | IT             |
| Shivom Munshi     | Finance        |
| Avichal Trivedi   | HR             |
| Rudraksh Kumrawat | IT             |
| Sarthak Dongare   | Finance        |
| Aayush Joshi      | IT             |
| Jatin Sahijwani   | IT             |
| Anirudh Singh     | Finance        |
| Mayank Tilwankar  | IT             |
+-------------------+----------------+
10 rows in set (0.00 sec)
```

### Non-Equi Join

```sql
SELECT e.EmployeeName, e.Salary
FROM Employees e
JOIN Departments d ON e.Salary > 55000;
```

```commandline
+-------------------+----------+
| EmployeeName      | Salary   |
+-------------------+----------+
| Mayank Tilwankar  | 60000.00 |
| Anirudh Singh     | 57000.00 |
| Jatin Sahijwani   | 59000.00 |
| Aayush Joshi      | 70000.00 |
| Sarthak Dongare   | 56000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Aaradhya Korde    | 60000.00 |
| Mayank Tilwankar  | 60000.00 |
| Anirudh Singh     | 57000.00 |
| Jatin Sahijwani   | 59000.00 |
| Aayush Joshi      | 70000.00 |
| Sarthak Dongare   | 56000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Aaradhya Korde    | 60000.00 |
| Mayank Tilwankar  | 60000.00 |
| Anirudh Singh     | 57000.00 |
| Jatin Sahijwani   | 59000.00 |
| Aayush Joshi      | 70000.00 |
| Sarthak Dongare   | 56000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Aaradhya Korde    | 60000.00 |
| Mayank Tilwankar  | 60000.00 |
| Anirudh Singh     | 57000.00 |
| Jatin Sahijwani   | 59000.00 |
| Aayush Joshi      | 70000.00 |
| Sarthak Dongare   | 56000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Aaradhya Korde    | 60000.00 |
| Mayank Tilwankar  | 60000.00 |
| Anirudh Singh     | 57000.00 |
| Jatin Sahijwani   | 59000.00 |
| Aayush Joshi      | 70000.00 |
| Sarthak Dongare   | 56000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Aaradhya Korde    | 60000.00 |
+-------------------+----------+
35 rows in set (0.00 sec)
```

### Inner Join

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.Department = d.DepartmentName;
```

```commandline
+-------------------+----------------+
| EmployeeName      | DepartmentName |
+-------------------+----------------+
| Aaradhy Vijayawat | HR             |
| Aaradhya Korde    | IT             |
| Shivom Munshi     | Finance        |
| Avichal Trivedi   | HR             |
| Rudraksh Kumrawat | IT             |
| Sarthak Dongare   | Finance        |
| Aayush Joshi      | IT             |
| Jatin Sahijwani   | IT             |
| Anirudh Singh     | Finance        |
| Mayank Tilwankar  | IT             |
+-------------------+----------------+
10 rows in set (0.00 sec)
```

### Left Outer Join

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.Department = d.DepartmentName;
```

```commandline
+-------------------+----------------+
| EmployeeName      | DepartmentName |
+-------------------+----------------+
| Aaradhy Vijayawat | HR             |
| Aaradhya Korde    | IT             |
| Shivom Munshi     | Finance        |
| Avichal Trivedi   | HR             |
| Rudraksh Kumrawat | IT             |
| Sarthak Dongare   | Finance        |
| Aayush Joshi      | IT             |
| Jatin Sahijwani   | IT             |
| Anirudh Singh     | Finance        |
| Mayank Tilwankar  | IT             |
+-------------------+----------------+
10 rows in set (0.00 sec)
```

### Right Outer Join

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d ON e.Department = d.DepartmentName;
```

```commandline
-- Output
+-------------------+----------------+
| EmployeeName      | DepartmentName |
+-------------------+----------------+
| Avichal Trivedi   | HR             |
| Aaradhy Vijayawat | HR             |
| Mayank Tilwankar  | IT             |
| Jatin Sahijwani   | IT             |
| Aayush Joshi      | IT             |
| Rudraksh Kumrawat | IT             |
| Aaradhya Korde    | IT             |
| Anirudh Singh     | Finance        |
| Sarthak Dongare   | Finance        |
| Shivom Munshi     | Finance        |
| NULL              | Marketing      |
| NULL              | Operations     |
+-------------------+----------------+
12 rows in set (0.00 sec)
```

### Full Outer Join

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.Department = d.DepartmentName
UNION
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d ON e.Department = d.DepartmentName
WHERE e.Department IS NULL;
```

```commandline
+-------------------+----------------+
| EmployeeName      | DepartmentName |
+-------------------+----------------+
| Aaradhy Vijayawat | HR             |
| Aaradhya Korde    | IT             |
| Shivom Munshi     | Finance        |
| Avichal Trivedi   | HR             |
| Rudraksh Kumrawat | IT             |
| Sarthak Dongare   | Finance        |
| Aayush Joshi      | IT             |
| Jatin Sahijwani   | IT             |
| Anirudh Singh     | Finance        |
| Mayank Tilwankar  | IT             |
| NULL              | Marketing      |
| NULL              | Operations     |
+-------------------+----------------+
12 rows in set (0.00 sec)
```

### Cross Join

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
CROSS JOIN Departments d;
```

```commandline
+-------------------+----------------+
| EmployeeName      | DepartmentName |
+-------------------+----------------+
| Aaradhy Vijayawat | Operations     |
| Aaradhy Vijayawat | Marketing      |
| Aaradhy Vijayawat | Finance        |
| Aaradhy Vijayawat | IT             |
| Aaradhy Vijayawat | HR             |
| Aaradhya Korde    | Operations     |
| Aaradhya Korde    | Marketing      |
| Aaradhya Korde    | Finance        |
| Aaradhya Korde    | IT             |
| Aaradhya Korde    | HR             |
| Shivom Munshi     | Operations     |
| Shivom Munshi     | Marketing      |
| Shivom Munshi     | Finance        |
| Shivom Munshi     | IT             |
| Shivom Munshi     | HR             |
| Avichal Trivedi   | Operations     |
| Avichal Trivedi   | Marketing      |
| Avichal Trivedi   | Finance        |
| Avichal Trivedi   | IT             |
| Avichal Trivedi   | HR             |
| Rudraksh Kumrawat | Operations     |
| Rudraksh Kumrawat | Marketing      |
| Rudraksh Kumrawat | Finance        |
| Rudraksh Kumrawat | IT             |
| Rudraksh Kumrawat | HR             |
| Sarthak Dongare   | Operations     |
| Sarthak Dongare   | Marketing      |
| Sarthak Dongare   | Finance        |
| Sarthak Dongare   | IT             |
| Sarthak Dongare   | HR             |
| Aayush Joshi      | Operations     |
| Aayush Joshi      | Marketing      |
| Aayush Joshi      | Finance        |
| Aayush Joshi      | IT             |
| Aayush Joshi      | HR             |
| Jatin Sahijwani   | Operations     |
| Jatin Sahijwani   | Marketing      |
| Jatin Sahijwani   | Finance        |
| Jatin Sahijwani   | IT             |
| Jatin Sahijwani   | HR             |
| Anirudh Singh     | Operations     |
| Anirudh Singh     | Marketing      |
| Anirudh Singh     | Finance        |
| Anirudh Singh     | IT             |
| Anirudh Singh     | HR             |
| Mayank Tilwankar  | Operations     |
| Mayank Tilwankar  | Marketing      |
| Mayank Tilwankar  | Finance        |
| Mayank Tilwankar  | IT             |
| Mayank Tilwankar  | HR             |
+-------------------+----------------+
50 rows in set (0.00 sec)
```

### Using Aggregate Functions in SQL

#### MIN()

```sql
SELECT MIN(Salary) AS MinSalary
FROM Employees;
```

```commandline
+-----------+
| MinSalary |
+-----------+
|  50000.00 |
+-----------+
1 row in set (0.00 sec)
```

#### MAX()

```sql
SELECT MAX(Salary) AS MaxSalary
FROM Employees;
```

```commandline
+-----------+
| MaxSalary |
+-----------+
|  70000.00 |
+-----------+
1 row in set (0.00 sec)
```

#### AVG()

```sql
SELECT AVG(Salary) AS AvgSalary
FROM Employees;
```

```commandline
+--------------+
| AvgSalary    |
+--------------+
| 57700.000000 |
+--------------+
1 row in set (0.00 sec)
```

#### COUNT()

```sql
SELECT COUNT(*) AS EmployeeCount
FROM Employees;
```

```commandline
+---------------+
| EmployeeCount |
+---------------+
|            10 |
+---------------+
1 row in set (0.02 sec)
```

#### DISTINCT()

```sql
SELECT DISTINCT Department
FROM Employees;
```

```commandline
+------------+
| Department |
+------------+
| HR         |
| IT         |
| Finance    |
+------------+
3 rows in set (0.00 sec)
```

### LIKE / Wildcards

```sql
SELECT EmployeeName
FROM Employees
WHERE EmployeeName LIKE 'A%';
```

```commandline
+-------------------+
| EmployeeName      |
+-------------------+
| Aaradhy Vijayawat |
| Aaradhya Korde    |
| Avichal Trivedi   |
| Aayush Joshi      |
| Anirudh Singh     |
+-------------------+
5 rows in set (0.00 sec)
```
### IN
```sql
SELECT EmployeeName, Salary
FROM Employees
WHERE Salary BETWEEN 55000 AND 60000;
```
```commandline
+-------------------+----------+
| EmployeeName      | Salary   |
+-------------------+----------+
| Aaradhya Korde    | 60000.00 |
| Shivom Munshi     | 55000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Sarthak Dongare   | 56000.00 |
| Jatin Sahijwani   | 59000.00 |
| Anirudh Singh     | 57000.00 |
| Mayank Tilwankar  | 60000.00 |
+-------------------+----------+
7 rows in set (0.00 sec)
```
### BETWEEN
```sql
SELECT EmployeeName, Salary
FROM Employees
WHERE Salary BETWEEN 55000 AND 60000;
```
```commandline
+-------------------+----------+
| EmployeeName      | Salary   |
+-------------------+----------+
| Aaradhya Korde    | 60000.00 |
| Shivom Munshi     | 55000.00 |
| Rudraksh Kumrawat | 58000.00 |
| Sarthak Dongare   | 56000.00 |
| Jatin Sahijwani   | 59000.00 |
| Anirudh Singh     | 57000.00 |
| Mayank Tilwankar  | 60000.00 |
+-------------------+----------+
7 rows in set (0.00 sec)
```
