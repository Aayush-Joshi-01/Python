# SQL
## Codd's 12 Rules:
**Rule 1:** The Information Rule
All information, whether it is user information or metadata, that is stored in a database must be entered as a value in a cell of a table. It is said that everything within the database is organized in a table layout.

**Rule 2:** The Guaranteed Access Rule
Each data element is guaranteed to be accessible logically with a combination of the table name, primary key (row value), and attribute name (column value). 

**Rule 3:** Systematic Treatment of NULL Values
Every Null value in a database must be given a systematic and uniform treatment. 

**Rule 4:** Active Online Catalog Rule
The database catalog, which contains metadata about the database, must be stored and accessed using the same relational database management system.

**Rule 5:** The Comprehensive Data Sub language Rule
A crucial component of any efficient database system is its ability to offer an easily understandable data manipulation language (DML) that facilitates defining, querying, and modifying information within the database.

**Rule 6:** The View Updating Rule
All views that are theoretically updatable must also be updatable by the system.

**Rule 7:** High-level Insert, Update, and Delete
A successful database system must possess the feature of facilitating high-level insertions, updates, and deletions that can grant users the ability to conduct these operations with ease through a single query.

**Rule 8:** Physical Data Independence
Application programs and activities should remain unaffected when changes are made to the physical storage structures or methods.

**Rule 9:** Logical Data Independence 
Application programs and activities should remain unaffected when changes are made to the logical structure of the data, such as adding or modifying tables.

**Rule 10:** Integrity Independence
Integrity constraints should be specified separately from application programs and stored in the catalog. They should be automatically enforced by the database system.

**Rule 11:** Distribution Independence
The distribution of data across multiple locations should be invisible to users, and the database system should handle the distribution transparently.

**Rule 12:** Non-Subversion Rule
If the interface of the system is providing access to low-level records, then the interface must not be able to damage the system and bypass security and integrity constraints.

## These SQL commands are mainly categorized into five categories: 

1. DDL – Data Definition Language (CREATE, ALTER, TRUNCATE, DROP, RENAME)
2. DQL – Data Query Language (SELECT)
3. DML – Data Manipulation Language (INSERT, UPDATE, DELETE)
4. DCL – Data Control Language (GRANT, REVOKE)
5. TCL – Transaction Control Language (ROLLBACK, COMMIT, SAVEPOINT)

Example of Update:
```shell
Table name = emp_table

mysql>> update emp_table set name = 'aayush' where dept = 'java' and empid = 102;
```


## 15 examples of Relational Database Management Systems (RDBMS):

1. **MySQL**: One of the most popular open-source RDBMS developed by Oracle.
   
2. **PostgreSQL**: Another powerful open-source RDBMS known for its advanced features and SQL compliance.
   
3. **Oracle Database**: A commercial RDBMS developed by Oracle Corporation, widely used in enterprise environments.
   
4. **SQL Server**: Developed by Microsoft, SQL Server is a robust RDBMS with strong integration with Microsoft products.
   
5. **SQLite**: A self-contained, serverless, zero-configuration SQL database engine, often used in embedded systems and mobile apps.
   
6. **IBM Db2**: A family of data management products, including a relational database server, developed by IBM.
   
7. **MariaDB**: An open-source fork of MySQL, designed to be a drop-in replacement with enhanced features.
   
8. **Amazon RDS (Relational Database Service)**: A cloud-based service by Amazon Web Services (AWS) offering managed RDBMS solutions like MySQL, PostgreSQL, SQL Server, Oracle, and others.
   
9. **Microsoft Access**: A desktop relational database management system often used by small teams and individuals.
   
10. **Teradata**: A data warehousing and analytics RDBMS known for its parallel processing capabilities.
    
11. **SAP HANA**: An in-memory database management system designed by SAP, optimized for real-time analytics and applications.
    
12. **Firebird**: An open-source RDBMS offering high performance and concurrency, suitable for both embedded and server applications.
    
13. **IBM Informix**: A flexible RDBMS known for its low administration requirements and high availability.
    
14. **InterSystems Caché**: A multi-model DBMS supporting relational, object, and hierarchical data models, often used in healthcare and finance.
    
15. **MemSQL**: An in-memory distributed RDBMS designed for real-time analytics and applications, now known as SingleStore.


## Examples of Object-Oriented Database Management Systems (OODBMS):

1. **db4o**: An open-source object database for Java and .NET platforms, designed to store and retrieve objects natively.

2. **ObjectDB**: A Java-based object database management system, providing persistence for Java objects without requiring conversion to relational database structures.

3. **Versant Object Database**: A commercial OODBMS supporting complex data models and high-performance applications.

4. **Objectivity/DB**: A scalable and distributed object database management system used in applications requiring real-time data management.

5. **Zope Object Database (ZODB)**: A native object database for Python, designed to provide transparent persistence for Python objects.

6. **GemStone/S**: An OODBMS designed for high-performance and scalability, often used in mission-critical applications and enterprise systems.

7. **Perst**: An open-source object-oriented database for Java and .NET, offering embedded and client/server modes.

8. **ObjectStore**: A high-performance OODBMS providing persistence for complex data models and scalable applications.

9. **ODMG-compliant databases**: Various databases compliant with the Object Data Management Group (ODMG) standard, which defines a common API for object-oriented databases.

10. **ObjectDBX**: A lightweight object-oriented database management system with support for embedded and server modes, suitable for small to medium-scale applications.

11. **Object-oriented features in NoSQL databases**: Some NoSQL databases like MongoDB and Couchbase incorporate object-oriented concepts, although they are not purely OODBMS.

12. **VelocityDB**: A .NET-based OODBMS offering high-performance object persistence and retrieval.

13. **ObjectDB for C++**: An object-oriented database management system designed for C++ applications, providing persistence for native C++ objects.

14. **OODBMS integrated with programming languages**: Many modern programming languages have libraries or frameworks that integrate OODBMS functionality directly, such as ObjectBox for Kotlin and Java.

15. **OODBMS for embedded systems**: Some OODBMS are optimized for embedded systems and IoT applications, providing lightweight and efficient object persistence.


Comparison between RDBMS, OODBMS, and DBMS:

| Feature                 | RDBMS                                                             | OODBMS                                                            | DBMS                                                           |
|-------------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------|
| **Data Model**          | Relational (Tables, Rows, Columns)                                | Object-Oriented (Objects, Classes, Attributes)                    | Various (Hierarchical, Network, Relational, Object, etc.)      |
| **Data Storage**        | Data stored in tables and rows                                    | Objects stored as they are in memory or disk                      | Typically in files with varying structures                     |
| **Query Language**      | SQL (Structured Query Language)                                   | Often proprietary or extends SQL for object operations            | Varies widely depending on the type (SQL, proprietary, etc.)   |
| **Schema Flexibility**  | Structured schema with defined relationships                      | More flexible schema, can evolve with object model                | Can be rigid or flexible depending on implementation           |
| **Transaction Support** | ACID transactions (Atomicity, Consistency, Isolation, Durability) | ACID transactions, but with more complex object structures        | Varies; some offer transaction support, others do not          |
| **Performance**         | Generally optimized for read-heavy operations                     | Optimized for complex object retrieval and navigation             | Varies widely depending on implementation and use case         |
| **Scalability**         | Scales well for large datasets and concurrent users               | Can scale, but can be complex due to object management            | Varies; scalability depends on architecture and implementation |
| **Use Cases**           | Business applications, web applications, reporting systems        | Applications with complex data models, CAD/CAM, real-time systems | Embedded systems, file systems, simple data storage            |
| **Examples**            | MySQL, PostgreSQL, SQL Server                                     | db4o, ObjectDB, Versant Object Database                           | File systems, SQLite, early versions of MySQL                  |

### Explanation:
- **Data Model**: RDBMS store data in tables with rows and columns, while OODBMS store data as objects with attributes and methods.
- **Data Storage**: RDBMS store data in a structured manner using tables, whereas OODBMS store objects directly as they are.
- **Query Language**: RDBMS use SQL for querying, while OODBMS may use a variant of SQL or proprietary languages that handle object-oriented constructs.
- **Schema Flexibility**: RDBMS have structured schemas with defined relationships, whereas OODBMS offer more flexible schemas that can evolve with object models.
- **Transaction Support**: Both RDBMS and OODBMS support ACID transactions, but OODBMS handle more complex object structures.
- **Performance**: RDBMS are generally optimized for read-heavy operations, while OODBMS are optimized for complex object retrieval and navigation.
- **Scalability**: RDBMS scale well for large datasets and concurrent users, whereas OODBMS scalability can be more complex due to managing object relationships.
- **Use Cases**: RDBMS are commonly used in business applications and reporting systems, while OODBMS are suited for applications with complex data models and real-time systems.
- **Examples**: Examples of RDBMS include MySQL, PostgreSQL, and SQL Server, while examples of OODBMS include db4o, ObjectDB, and Versant Object Database.



## Comparison Between Delete Drop and Truncate

| Parameter  | Delete                                                                                                                                          | Drop                                                                   | Truncate                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Language   | Data Manipulation Language Command (DML)                                                                                                        | Data Definition Language Command (DDL)                                 | Data Definition Language Command (DDL)                                       |
| Purpose    | Used to delete content in rows of a table.                                                                                                      | Used to delete entire content of table along with the table structure. | Used to delete entire content of table leaving the table structure.          |
| Syntax     | DELETE from;(to delete all the rows of the table) DELETE FROM table_name WHERE condition; (to delete the row of the table as per the condition) | DROP table <table_name>;                                               | TRUNCATE table <table_name>;                                                 |
| ROLLBACK   | Can be Rollback                                                                                                                                 | Cannot be Rollback                                                     | Cannot be Rollback                                                           |
| Data       | Removes specific rows depending upon condition                                                                                                  | Removes the entire data immediately.                                   | Removes all rows                                                             |
| Efficiency | Less efficient for large tables as we have to manually specify each and every condition.                                                        | Efficiency depends on the size of the object which is being dropped.   | More efficient for large tables as we are removing all the data in one step. |


# SQL Assignment

```shell
>> CREATE DATABASE Employee;
```
```commandline
Query OK, 1 row affected (0.04 sec)
```

```shell
>> USE Employee;
```
```commandline
Database changed
```

```shell
>>  CREATE TABLE emp_data (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2),
    PRIMARY KEY (id)
    );
```
```commandline
Query OK, 0 rows affected (0.03 sec)
```
```shell
>>  INSERT INTO emp_data (first_name, last_name, department, job_title, salary)
    -> VALUES
    -> ('Aayush', 'Joshi', 'Software Engineer', 'Machine Learning Engineer', 50000.00),
    -> ('Prankur', 'Aggarwal', 'Marketing', 'Marketing Manager', 60000.00),
    -> ('Aaditya', 'Singh', 'IT', 'Software Engineer', 70000.00),
    -> ('Ishaan', 'Mishra', 'HR', 'HR Generalist', 40000.00),
    -> ('Abhinay', 'Pandey', 'Finance', 'Financial Analyst', 55000.00),
    -> ('Kaustaubh', 'Narayan', 'Operations', 'Operations Manager', 65000.00),
    -> ('Aarav', 'Sharma', 'Research', 'Research Scientist', 75000.00);
```
```commandline
Query OK, 7 rows affected (0.02 sec)
Records: 7  Duplicates: 0  Warnings: 0
```
```shell
>> UPDATE emp_data SET salary = 100000 where first_name = 'Aayush' and last_name = 'Joshi';
```
```commandline
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```
```shell
>> SELECT * FROM emp_data;
```
```commandline
+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer |  50000.00 |
|  2 | Prankur    | Aggarwal  | Marketing  | Marketing Manager         |  60000.00 |
|  3 | Aaditya    | Singh     | IT         | Software Engineer         |  70000.00 |
|  4 | Ishaan     | Mishra    | HR         | HR Generalist             |  40000.00 |
|  5 | Abhinay    | Pandey    | Finance    | Financial Analyst         |  55000.00 |
|  6 | Kaustaubh  | Narayan   | Operations | Operations Manager        |  65000.00 |
|  7 | Aarav      | Sharma    | Research   | Research Scientist        |  75000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
7 rows in set (0.00 sec)
```
```shell
>> INSERT INTO emp_data (first_name, last_name, department, job_title, salary)
    -> Values
    -> ('Ananya', 'Arora', 'Management', 'Human Resource', 40000);
```
```commandline
Query OK, 1 row affected (0.01 sec)
```
```shell
>> SELECT * FROM emp_data;
```
```commandline
+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer | 100000.00 |
|  2 | Prankur    | Aggarwal  | Marketing  | Marketing Manager         |  60000.00 |
|  3 | Aaditya    | Singh     | IT         | Software Engineer         |  70000.00 |
|  4 | Ishaan     | Mishra    | HR         | HR Generalist             |  40000.00 |
|  5 | Abhinay    | Pandey    | Finance    | Financial Analyst         |  55000.00 |
|  6 | Kaustaubh  | Narayan   | Operations | Operations Manager        |  65000.00 |
|  7 | Aarav      | Sharma    | Research   | Research Scientist        |  75000.00 |
|  8 | Ananya     | Arora     | Management | Human Resource            |  40000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
8 rows in set (0.00 sec)
```
```shell
>> DELETE FROM emp_data where first_name = 'Ananya';
```
```commandline
Query OK, 1 row affected (0.00 sec)
```
```shell
>> SELECT * FROM emp_data
```
```commandline
+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer | 100000.00 |
|  2 | Prankur    | Aggarwal  | Marketing  | Marketing Manager         |  60000.00 |
|  3 | Aaditya    | Singh     | IT         | Software Engineer         |  70000.00 |
|  4 | Ishaan     | Mishra    | HR         | HR Generalist             |  40000.00 |
|  5 | Abhinay    | Pandey    | Finance    | Financial Analyst         |  55000.00 |
|  6 | Kaustaubh  | Narayan   | Operations | Operations Manager        |  65000.00 |
|  7 | Aarav      | Sharma    | Research   | Research Scientist        |  75000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
7 rows in set (0.00 sec)
```
```shell
-- Select all employees
>> SELECT * FROM emp_data;

-- Select employees in the 'IT' department
>> SELECT * FROM emp_data WHERE department = 'IT';

-- Select employees with a salary greater than 60000
>> SELECT * FROM emp_data WHERE salary > 60000;

-- Select the average salary of all employees
>> SELECT AVG(salary) AS average_salary FROM emp_data;
```
```commandline
+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer | 100000.00 |
|  2 | Prankur    | Aggarwal  | Marketing  | Marketing Manager         |  60000.00 |
|  3 | Aaditya    | Singh     | IT         | Software Engineer         |  70000.00 |
|  4 | Ishaan     | Mishra    | HR         | HR Generalist             |  40000.00 |
|  5 | Abhinay    | Pandey    | Finance    | Financial Analyst         |  55000.00 |
|  6 | Kaustaubh  | Narayan   | Operations | Operations Manager        |  65000.00 |
|  7 | Aarav      | Sharma    | Research   | Research Scientist        |  75000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
7 rows in set (0.00 sec)

+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer | 100000.00 |
|  3 | Aaditya    | Singh     | IT         | Software Engineer         |  70000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
2 rows in set (0.00 sec)

+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer | 100000.00 |
|  3 | Aaditya    | Singh     | IT         | Software Engineer         |  70000.00 |
|  6 | Kaustaubh  | Narayan   | Operations | Operations Manager        |  65000.00 |
|  7 | Aarav      | Sharma    | Research   | Research Scientist        |  75000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
4 rows in set (0.00 sec)

+----------------+
| average_salary |
+----------------+
|   66428.571429 |
+----------------+
1 row in set (0.00 sec)
```
```shell
-- Update an employee salary
>> UPDATE emp_data SET salary = 52000.00 WHERE id = 4;

-- Update an employee department and job title
>> UPDATE emp_data SET department = 'Finance', job_title = 'Financial Manager' WHERE id = 2;
```
```commandline
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```
```shell
-- Delete an employee
>> DELETE FROM emp_data WHERE id = 3;

-- Delete all employees in the 'HR' department
>> DELETE FROM emp_data WHERE department = 'HR';
```
```commandline
Query OK, 1 row affected (0.01 sec)

Query OK, 1 row affected (0.01 sec)
```
```shell
>> SELECT * FROM emp_data;
```
```commandline
+----+------------+-----------+------------+---------------------------+-----------+
| id | first_name | last_name | department | job_title                 | salary    |
+----+------------+-----------+------------+---------------------------+-----------+
|  1 | Aayush     | Joshi     | IT         | Machine Learning Engineer | 100000.00 |
|  2 | Prankur    | Aggarwal  | Finance    | Financial Manager         |  60000.00 |
|  5 | Abhinay    | Pandey    | Finance    | Financial Analyst         |  55000.00 |
|  6 | Kaustaubh  | Narayan   | Operations | Operations Manager        |  65000.00 |
|  7 | Aarav      | Sharma    | Research   | Research Scientist        |  75000.00 |
+----+------------+-----------+------------+---------------------------+-----------+
5 rows in set (0.00 sec)
```
```shell
-- Add a new column 'email' to the table
>> ALTER TABLE emp_data ADD COLUMN email VARCHAR(100);

-- Modify the data type of the 'salary' column
>> ALTER TABLE emp_data MODIFY COLUMN salary DECIMAL(12, 2);

-- Rename the 'department' column to 'dept'
>> ALTER TABLE emp_data RENAME COLUMN department TO dept;

-- Drop the 'job_title' column
>> ALTER TABLE emp_data DROP COLUMN job_title;
```
```commandline
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

Query OK, 5 rows affected (0.08 sec)
Records: 5  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0
```
```shell
>> SELECT * FROM emp_data;
```
```commandline
+----+------------+-----------+------------+-----------+-------+
| id | first_name | last_name | dept       | salary    | email |
+----+------------+-----------+------------+-----------+-------+
|  1 | Aayush     | Joshi     | IT         | 100000.00 | NULL  |
|  2 | Prankur    | Aggarwal  | Finance    |  60000.00 | NULL  |
|  5 | Abhinay    | Pandey    | Finance    |  55000.00 | NULL  |
|  6 | Kaustaubh  | Narayan   | Operations |  65000.00 | NULL  |
|  7 | Aarav      | Sharma    | Research   |  75000.00 | NULL  |
+----+------------+-----------+------------+-----------+-------+
5 rows in set (0.00 sec)
```
```shell
>> TRUNCATE TABLE emp_data;
```
```commandline
Query OK, 0 rows affected (0.03 sec)
```
```shell
>> SELECT * FROM emp_data;
```
```commandline
Empty set (0.00 sec)
```
```shell
>> DESC emp_data;
```
```commandline
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| id         | int           | NO   | PRI | NULL    | auto_increment |
| first_name | varchar(50)   | NO   |     | NULL    |                |
| last_name  | varchar(50)   | NO   |     | NULL    |                |
| dept       | varchar(50)   | NO   |     | NULL    |                |
| salary     | decimal(12,2) | YES  |     | NULL    |                |
| email      | varchar(100)  | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+
6 rows in set (0.03 sec)
```
```shell
>> INSERT INTO emp_data (first_name, last_name, department, salary, email)
    -> VALUES
    -> ('Aayush', 'Joshi', 'Software Engineer', 50000.00, 'aayushjoshi.dev@gmail.com'),
```
```commandline
Query OK, 1 row affected (0.01 sec)
```
```shell
>> SELECT * FROM emp_data;
```
```commondline
+----+------------+-----------+-------------------+----------+---------------------------+
| id | first_name | last_name | dept              | salary   | email                     |
+----+------------+-----------+-------------------+----------+---------------------------+
|  1 | Aayush     | Joshi     | Software Engineer | 50000.00 | aayushjoshi.dev@gmail.com |
+----+------------+-----------+-------------------+----------+---------------------------+
1 row in set (0.00 sec)
```
```shell
>> DROP TABLE emp_data;
```
```commandline
Query OK, 0 rows affected (0.02 sec)
```
```shell
>> SELECT * FROM emp_data;

>> DESC emp_data;
```
```commandline
ERROR 1146 (42S02): Table 'employee.emp_data' doesn't exist

ERROR 1146 (42S02): Table 'employee.emp_data' doesn't exist
```




