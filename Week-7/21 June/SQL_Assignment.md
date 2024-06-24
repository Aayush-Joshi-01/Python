# Assignment SQL -Aayush Joshi 1100673

## EmployeeInfo Table

| EmpID | EmpFirstName | EmpLastName | Department | Project | Address        | DOB        | Gender |
|-------|--------------|-------------|------------|---------|----------------|------------|--------|
| 1     | Sanjay       | Mehra       | HR         | P1      | Hyderabad(HYD) | 01/12/1976 | M      |
| 2     | Ananya       | Mishra      | Admin      | P2      | Delhi(DEL)     | 02/05/1968 | F      |
| 3     | Rohan        | Diwan       | Account    | P3      | Mumbai(BOM)    | 01/01/1980 | M      |
| 4     | Sonia        | Kulkarni    | HR         | P1      | Hyderabad(HYD) | 02/05/1992 | F      |
| 5     | Ankit        | Kapoor      | Admin      | P2      | Delhi(DEL)     | 03/07/1994 | M      |


```sql
CREATE TABLE EmployeeInfo (
    EmpID INT PRIMARY KEY,
    EmpFirstName VARCHAR(50),
    EmpLastName VARCHAR(50),
    Department VARCHAR(50),
    Project VARCHAR(50),
    Address VARCHAR(100),
    DOB DATE,
    Gender CHAR(1)
);

INSERT INTO EmployeeInfo (EmpID, EmpFirstName, EmpLastName, Department, Project, Address, DOB, Gender)
VALUES
(1, 'Sanjay', 'Mehra', 'HR', 'P1', 'Hyderabad (HYD)', '1976-12-01', 'M'),
(2, 'Ananya', 'Mishra', 'Admin', 'P2', 'Delhi (DEL)', '1968-05-02', 'F'),
(3, 'Rohan', 'Diwan', 'Account', 'P3', 'Mumbai (BOM)', '1980-01-01', 'M'),
(4, 'Sonia', 'Kulkarni', 'HR', 'P1', 'Hyderabad (HYD)', '1992-05-02', 'F'),
(5, 'Ankit', 'Kapoor', 'Admin', 'P2', 'Delhi (DEL)', '1994-07-03', 'M');

```

```commandline
Query OK, 0 rows affected (0.26 sec)

Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0
```


## EmployeePosition Table

| EmpID | EmpPosition | DateOfJoining | Salary   |
|-------|-------------|---------------|----------|
| 1     | Manager     | 01/05/2022    | 500000   |
| 2     | Executive   | 02/05/2022    | 75000    |
| 3     | Manager     | 01/05/2022    | 90000    |
| 4     | Lead        | 02/05/2022    | 85000    |
| 5     | Executive   | 01/05/2022    | 300000   |

```sql
CREATE TABLE EmployeePosition (
    EmpID INT,
    EmpPosition VARCHAR(50),
    DateOfJoining DATE,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (EmpID) REFERENCES EmployeeInfo(EmpID)
);

INSERT INTO EmployeePosition (EmpID, EmpPosition, DateOfJoining, Salary)
VALUES
(1, 'Manager', '2022-05-01', 500000),
(2, 'Executive', '2022-05-02', 75000),
(3, 'Manager', '2022-05-01', 90000),
(2, 'Lead', '2022-05-02', 85000),
(1, 'Executive', '2022-05-01', 300000);

```

```commandline
Query OK, 0 rows affected (0.08 sec)

Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0
```

```sql
SELECT * FROM EmployeeInfo;
SELECT * FROM EmployeePosition;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)     | 1994-07-03 | M      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
5 rows in set (0.03 sec)

+-------+-------------+---------------+-----------+
| EmpID | EmpPosition | DateOfJoining | Salary    |
+-------+-------------+---------------+-----------+
|     1 | Manager     | 2022-05-01    | 500000.00 |
|     2 | Executive   | 2022-05-02    |  75000.00 |
|     3 | Manager     | 2022-05-01    |  90000.00 |
|     4 | Lead        | 2022-05-02    |  85000.00 |
|     5 | Executive   | 2022-05-01    | 300000.00 |
+-------+-------------+---------------+-----------+
5 rows in set (0.00 sec)
```

### Q1 Write a query to fetch the EmpFname from the EmployeeInfo table in upper case and use the ALIAS name as EmpName.

```sql
SELECT UPPER(EmpFirstName) AS EmpName FROM EmployeeInfo;
```

```commandline
+---------+
| EmpName |
+---------+
| SANJAY  |
| ANANYA  |
| ROHAN   |
| SONIA   |
| ANKIT   |
+---------+
5 rows in set (0.00 sec)
```

### Q2. Write a query to fetch the number of employees working in the department ‘HR’.

```sql
SELECT COUNT(*) FROM EmployeeInfo WHERE Department = 'HR';
```

```commandline
+----------+
| COUNT(*) |
+----------+
|        2 |
+----------+
1 row in set (0.01 sec)
```

### Q3. Write a query to get the current date.

```sql
SELECT CURRENT_DATE() AS CurrentDate;
```

```commandline
+-------------+
| CurrentDate |
+-------------+
| 2024-06-21  |
+-------------+
1 row in set (0.00 sec)
```

### Q4. Write a query to retrieve the first four characters of EmpLname from the EmployeeInfo table.

```sql
SELECT EmpID, EmpFirstName, EmpLastName, LEFT(EmpLastName, 4) AS FirstFourCharsOfEmpLname FROM EmployeeInfo;
```

```commandline
+-------+--------------+-------------+--------------------------+
| EmpID | EmpFirstName | EmpLastName | FirstFourCharsOfEmpLname |
+-------+--------------+-------------+--------------------------+
|     1 | Sanjay       | Mehra       | Mehr                     |
|     2 | Ananya       | Mishra      | Mish                     |
|     3 | Rohan        | Diwan       | Diwa                     |
|     4 | Sonia        | Kulkarni    | Kulk                     |
|     5 | Ankit        | Kapoor      | Kapo                     |
+-------+--------------+-------------+--------------------------+
5 rows in set (0.01 sec)
```

### Q5. Write a query to fetch only the place name(string before brackets) from the Address column of EmployeeInfo table. Using the MID function in MySQL

```sql 
SELECT REVERSE(MID(REVERSE(Address),7)) AS PlaceName From EmployeeInfo;

SELECT SUBSTRING_INDEX(TRIM(Address), '(', 1) AS PlaceName FROM EmployeeInfo;
```

```commandline
+-----------+
| PlaceName |
+-----------+
| Hyderabad |
| Delhi     |
| Mumbai    |
| Hyderabad |
| Delhi     |
+-----------+
5 rows in set (0.01 sec)
```

### Q6. Write a query to create a new table which consists of data and structure copied from the other table.

```sql
CREATE TABLE EmployeeInformation AS
SELECT * FROM EmployeeInfo;

SELECT * FROM EmployeeInformation;

SHOW TABLES;
```

```commandline
Query OK, 5 rows affected (0.05 sec)
Records: 5  Duplicates: 0  Warnings: 0


+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)     | 1994-07-03 | M      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
5 rows in set (0.00 sec)


+---------------------+
| Tables_in_employee  |
+---------------------+
| employeeinfo        |
| employeeinformation |
| employeeposition    |
+---------------------+
3 rows in set (0.01 sec)
```

### Q7. Write a query to find all the employees whose salary is between 50000 to 100000.

```sql
SELECT * FROM EmployeeInfo ei JOIN EmployeePosition ep ON ei.EmpID = ep.EmpID WHERE Salary BETWEEN 50000 AND 100000;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+----------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender | EmpID | EmpPosition | DateOfJoining | Salary   |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+----------+
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |     2 | Executive   | 2022-05-02    | 75000.00 |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |     3 | Manager     | 2022-05-01    | 90000.00 |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |     4 | Lead        | 2022-05-02    | 85000.00 |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+----------+
3 rows in set (0.00 sec)
```

### Q8. Write a query to find the names of employees that begin with ‘S’

```sql
SELECT EmpFirstName AS FIRST_NAME, EmpLastName AS LAST_NAME FROM EmployeeInfo WHERE EmpFirstName LIKE 'S%';
```

```commandline
+------------+-----------+
| FIRST_NAME | LAST_NAME |
+------------+-----------+
| Sanjay     | Mehra     |
| Sonia      | Kulkarni  |
+------------+-----------+
2 rows in set (0.01 sec)
```

### Q9. Write a query to fetch top N records.

```sql
SELECT * FROM EmployeeInfo LIMIT 3;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
3 rows in set (0.02 sec)
```

### Q10. Write a query to retrieve the EmpFname and EmpLname in a single column as “FullName”. The first name and the last name must be separated with space.

```sql
SELECT CONCAT(EmpFirstname, ' ', EmpLastname) AS FullName FROM EmployeeInfo;
```

```commandline
+----------------+
| FullName       |
+----------------+
| Sanjay Mehra   |
| Ananya Mishra  |
| Rohan Diwan    |
| Sonia Kulkarni |
| Ankit Kapoor   |
+----------------+
5 rows in set (0.00 sec)
```

### Q11. Write a query find number of employees whose DOB is between 02/05/1970 to 31/12/1975 and are grouped according to gender

```sql
SELECT * FROM EmployeeInfo WHERE DOB BETWEEN '1970-05-02' AND '1975-12-31';
```

```commandline
Empty set (0.01 sec)
```

### Q12. Write a query to fetch all the records from the EmployeeInfo table ordered by EmpLname in descending order and Department in the ascending order.

```sql
SELECT * FROM EmployeeInfo ORDER BY EmpLastName DESC, Department ASC;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)     | 1994-07-03 | M      |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
5 rows in set (0.01 sec)
```

### Q13. Write a query to fetch details of employees whose EmpLname ends with an alphabet ‘A’ and contains five alphabets.

```sql
SELECT * FROM EmployeeInfo WHERE EmpLastName LIKE '%a' AND LENGTH(EmpLastName) = 5;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
1 row in set (0.01 sec)
```

### Q14. Write a query to fetch details of all employees excluding the employees with first names, “Sanjay” and “Sonia” from the EmployeeInfo table.

```sql
SELECT * FROM EmployeeInfo WHERE EmpFirstName NOT IN ('Sanjay', 'Sonia');
```

```commandline
+-------+--------------+-------------+------------+---------+--------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address      | DOB        | Gender |
+-------+--------------+-------------+------------+---------+--------------+------------+--------+
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)  | 1968-05-02 | F      |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM) | 1980-01-01 | M      |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)  | 1994-07-03 | M      |
+-------+--------------+-------------+------------+---------+--------------+------------+--------+
3 rows in set (0.01 sec)
```

### Q15. Write a query to fetch details of employees with the address as “DELHI(DEL)”.

```sql
SELECT * FROM EmployeeInfo WHERE Address = 'DELHI (DEL)';
```

```commandline
+-------+--------------+-------------+------------+---------+-------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address     | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-------------+------------+--------+
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL) | 1968-05-02 | F      |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL) | 1994-07-03 | M      |
+-------+--------------+-------------+------------+---------+-------------+------------+--------+
2 rows in set (0.00 sec)
```

### Q16. Write a query to fetch all employees who also hold the managerial position.

```sql
SELECT * FROM EmployeeInfo ei JOIN EmployeePosition ep ON ei.EmpID = ep.EmpID WHERE EmpPosition = 'Manager';
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+-----------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender | EmpID | EmpPosition | DateOfJoining | Salary    |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+-----------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |     1 | Manager     | 2022-05-01    | 500000.00 |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |     3 | Manager     | 2022-05-01    |  90000.00 |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+-----------+
2 rows in set (0.01 sec)
```

### Q17. Write a query to fetch the department-wise count of employees sorted by department’s count in ascending order.

```sql
SELECT Department, COUNT(*) AS EmployeeCount FROM EmployeeInfo GROUP BY Department ORDER BY EmployeeCount ASC;
```

```commandline
+------------+---------------+
| Department | EmployeeCount |
+------------+---------------+
| Account    |             1 |
| HR         |             2 |
| Admin      |             2 |
+------------+---------------+
3 rows in set (0.02 sec)
```

### Q18. Write a query to calculate the even and odd records from a table.

- Even Records
```sql
SELECT * FROM EmployeeInfo WHERE EmpID % 2 = 0;  
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
2 rows in set (0.01 sec)
```
- Odd Records
```sql
SELECT * FROM EmployeeInfo WHERE EmpID % 2 <> 0;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)     | 1994-07-03 | M      |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+
3 rows in set (0.00 sec)
```

### Q19. Write a SQL query to retrieve employee details from EmployeeInfo table who have a date of joining in the EmployeePosition table.

```sql
SELECT * FROM EmployeeInfo RIGHT OUTER JOIN EmployeePosition ON EmployeeInfo.EmpID = EmployeePosition.EmpID;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+-----------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender | EmpID | EmpPosition | DateOfJoining | Salary    |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+-----------+
|     1 | Sanjay       | Mehra       | HR         | P1      | Hyderabad (HYD) | 1976-12-01 | M      |     1 | Manager     | 2022-05-01    | 500000.00 |
|     2 | Ananya       | Mishra      | Admin      | P2      | Delhi (DEL)     | 1968-05-02 | F      |     2 | Executive   | 2022-05-02    |  75000.00 |
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |     3 | Manager     | 2022-05-01    |  90000.00 |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |     4 | Lead        | 2022-05-02    |  85000.00 |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)     | 1994-07-03 | M      |     5 | Executive   | 2022-05-01    | 300000.00 |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+-------+-------------+---------------+-----------+
5 rows in set (0.00 sec)
```

### Q20. Write a query to retrieve two minimum and maximum salaries from the EmployeePosition table. To retrieve two minimum salaries, you can write a query as below:

- Two Highest
```sql
SELECT EmpID, EmpPosition, DateOfJoining, Salary FROM EmployeePosition ORDER BY Salary ASC LIMIT 2;
```

```commandline
+-------+-------------+---------------+----------+
| EmpID | EmpPosition | DateOfJoining | Salary   |
+-------+-------------+---------------+----------+
|     2 | Executive   | 2022-05-02    | 75000.00 |
|     4 | Lead        | 2022-05-02    | 85000.00 |
+-------+-------------+---------------+----------+
2 rows in set (0.00 sec)
```

-Two Lowest
```sql
SELECT EmpID, EmpPosition, DateOfJoining, Salary FROM EmployeePosition ORDER BY Salary DESC LIMIT 2;
```

```commandline
+-------+-------------+---------------+-----------+
| EmpID | EmpPosition | DateOfJoining | Salary    |
+-------+-------------+---------------+-----------+
|     1 | Manager     | 2022-05-01    | 500000.00 |
|     5 | Executive   | 2022-05-01    | 300000.00 |
+-------+-------------+---------------+-----------+
2 rows in set (0.00 sec)
```

### Q21. Write a query to find the Nth highest salary from the table without using TOP/limit keyword.

```sql
SELECT * FROM (
    SELECT EmpID, EmpPosition, DateOfJoining, Salary,
           ROW_NUMBER() OVER (ORDER BY Salary DESC) AS SalaryRank
    FROM EmployeePosition
) AS RankedSalaries
WHERE SalaryRank = 2;


SELECT * FROM (
    SELECT EmpID, EmpPosition, DateOfJoining, Salary,
           ROW_NUMBER() OVER (ORDER BY Salary DESC) AS SalaryRank
    FROM EmployeePosition
) AS RankedSalaries
WHERE SalaryRank = 3;
```

```commandline
+-------+-------------+---------------+-----------+------------+
| EmpID | EmpPosition | DateOfJoining | Salary    | SalaryRank |
+-------+-------------+---------------+-----------+------------+
|     5 | Executive   | 2022-05-01    | 300000.00 |          2 |
+-------+-------------+---------------+-----------+------------+
1 row in set (0.00 sec)


+-------+-------------+---------------+----------+------------+
| EmpID | EmpPosition | DateOfJoining | Salary   | SalaryRank |
+-------+-------------+---------------+----------+------------+
|     3 | Manager     | 2022-05-01    | 90000.00 |          3 |
+-------+-------------+---------------+----------+------------+
1 row in set (0.00 sec)
```

### Q22. Write a query to retrieve duplicate records from a table.

```sql
SELECT EmpFirstName, EmpLastName, COUNT(*) AS DuplicateCount
FROM EmployeeInfo GROUP BY EmpFirstName, EmpLastName HAVING COUNT(*) > 1;
```

```commandline
Empty set (0.00 sec)
```

### Q23. Write a query to retrieve the list of employees working in the same department.

```sql
SELECT e1.EmpID, e1.EmpFirstName, e1.EmpLastName, e1.Department FROM EmployeeInfo e1
JOIN EmployeeInfo e2 ON e1.Department = e2.Department
WHERE e1.EmpID <> e2.EmpID ORDER BY e1.Department, e1.EmpLastName, e1.EmpFirstName;
```

```commandline
+-------+--------------+-------------+------------+
| EmpID | EmpFirstName | EmpLastName | Department |
+-------+--------------+-------------+------------+
|     5 | Ankit        | Kapoor      | Admin      |
|     2 | Ananya       | Mishra      | Admin      |
|     4 | Sonia        | Kulkarni    | HR         |
|     1 | Sanjay       | Mehra       | HR         |
+-------+--------------+-------------+------------+
4 rows in set (0.01 sec)
```

### Q24. Write a query to retrieve the last 3 records from the EmployeeInfo table.

```sql
WITH ranked_rows AS (
  SELECT *, ROW_NUMBER() OVER () AS row_num
  FROM employee.employeeinfo
  ORDER BY row_num desc limit 3
)
select * from ranked_rows order by row_num;
```

```commandline
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+---------+
| EmpID | EmpFirstName | EmpLastName | Department | Project | Address         | DOB        | Gender | row_num |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+---------+
|     3 | Rohan        | Diwan       | Account    | P3      | Mumbai (BOM)    | 1980-01-01 | M      |       3 |
|     4 | Sonia        | Kulkarni    | HR         | P1      | Hyderabad (HYD) | 1992-05-02 | F      |       4 |
|     5 | Ankit        | Kapoor      | Admin      | P2      | Delhi (DEL)     | 1994-07-03 | M      |       5 |
+-------+--------------+-------------+------------+---------+-----------------+------------+--------+---------+
3 rows in set (0.03 sec)
```

### Q25. Write a query to find the third-highest salary from the EmpPosition table.

```sql
SELECT DISTINCT Salary
FROM EmployeePosition
ORDER BY Salary DESC
LIMIT 2, 1;
```

```commandline
+----------+
| Salary   |
+----------+
| 90000.00 |
+----------+
1 row in set (0.00 sec)
```
