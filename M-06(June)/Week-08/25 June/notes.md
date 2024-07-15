# Difference Between Functions and Procedures

1. **Function**:
   - **Purpose**: Functions are used to calculate something from a given input. They are often named after mathematical functions.
   - **Return Value**: Functions **always return a value** after executing queries.
   - **Input Parameters**: Functions can have input parameters.
   - **DML Statements**: Functions cannot contain DML (Data Manipulation Language) statements (e.g., `INSERT`, `UPDATE`, `DELETE`).
   - **Multiple Result Sets**: Functions cannot return multiple result sets.
   - **Transaction Management**: Functions do not support transaction management.
   - **Try-Catch Blocks**: Functions do not support try-catch blocks for error handling.
   - **Usage in SELECT Statement**: Functions can be used in the `SELECT` statement.
   - **Example**:
     ```sql
     CREATE FUNCTION MultiplyNumbers(@int1 AS INT, @int2 AS INT) AS
     BEGIN
         RETURN (@int1 * @int2)
     END
     ```

2. **Procedure**:
   - **Purpose**: Procedures are used to execute specific tasks or functions.
   - **Return Value**: Procedures can return a value using "IN OUT" and "OUT" arguments.
   - **Input Parameters**: Procedures can have input/output parameters.
   - **DML Statements**: Procedures can contain DML statements.
   - **Multiple Result Sets**: Procedures can return multiple result sets.
   - **Transaction Management**: Procedures allow transaction management.
   - **Try-Catch Blocks**: Procedures support try-catch blocks for error handling.
   - **Usage in SELECT Statement**: Procedures cannot be used directly in the `SELECT` statement.
   - **Example**:
     ```sql
     CREATE OR REPLACE PROCEDURE INC_SAL(eno IN NUMBER, up_sal OUT NUMBER) IS
     BEGIN
         UPDATE emp_table SET salary = salary + 1000 WHERE emp_no = eno;
         COMMIT;
         SELECT sal INTO up_sal FROM emp_table WHERE emp_no = eno;
     END
     ```
     
