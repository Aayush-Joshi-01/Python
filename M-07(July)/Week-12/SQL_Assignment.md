### Project 1: Supply Chain Analysis with Advanced SQL Techniques
 
**File: supply_chain_analysis.sql**
```sql
-- Step 1: Create a comprehensive view of the supply chain network
CREATE VIEW supply_chain_view AS
SELECT 
    p.productCode, p.productName, pl.productLine, s.supplierName, i.quantityInStock, i.buyPrice
FROM
    products p
JOIN
    productlines pl ON p.productLine = pl.productLine
JOIN
    inventory i ON p.productCode = i.productCode
JOIN
    suppliers s ON i.supplierID = s.supplierID;
 
-- Step 2: Find the best supplier for each product based on price and quantity
WITH RankedSuppliers AS (
    SELECT 
        productCode, supplierID, buyPrice, quantityInStock,
        RANK() OVER (PARTITION BY productCode ORDER BY buyPrice ASC, quantityInStock DESC) AS rank
    FROM 
        inventory
)
SELECT 
    productCode, supplierID, buyPrice, quantityInStock
FROM 
    RankedSuppliers
WHERE 
    rank = 1;
 
-- Step 3: List of employees and total amount of sales they have made
SELECT 
    e.employeeNumber, e.firstName, e.lastName, SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
    employees e
JOIN 
    customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN 
    orders o ON c.customerNumber = o.customerNumber
JOIN 
    orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY 
    e.employeeNumber, e.firstName, e.lastName
ORDER BY 
    totalSales DESC;
 
-- Step 4: Create a system-versioned table for the inventory
CREATE TABLE inventory_history (
    inventoryID INT PRIMARY KEY,
    productCode VARCHAR(15),
    supplierID INT,
    quantityInStock INT,
    buyPrice DECIMAL(10, 2),
    validFrom TIMESTAMP,
    validTo TIMESTAMP
) WITH SYSTEM VERSIONING;
```
 
### Project 2: Employee Performance and Compensation Review
 
**File: employee_performance.sql**
```sql
-- Step 1: Stored procedure to calculate total compensation
DELIMITER //
CREATE PROCEDURE calculate_total_compensation(IN empID INT, OUT totalCompensation DECIMAL(10,2))
BEGIN
    SELECT 
        (s.salary + IFNULL(b.bonus, 0)) INTO totalCompensation
    FROM 
        salaries s
    LEFT JOIN 
        bonuses b ON s.employeeID = b.employeeID
    WHERE 
        s.employeeID = empID;
END //
DELIMITER ;
 
-- Step 2: Function to calculate average sales by employee's department
DELIMITER //
CREATE FUNCTION avg_department_sales(empID INT) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE deptID INT;
    DECLARE avgSales DECIMAL(10, 2);
    
    SELECT departmentID INTO deptID FROM employees WHERE employeeID = empID;
    
    SELECT AVG(sales) INTO avgSales
    FROM (
        SELECT 
            e.departmentID, SUM(od.quantityOrdered * od.priceEach) AS sales
        FROM 
            employees e
        JOIN 
            customers c ON e.employeeNumber = c.salesRepEmployeeNumber
        JOIN 
            orders o ON c.customerNumber = o.customerNumber
        JOIN 
            orderdetails od ON o.orderNumber = od.orderNumber
        WHERE 
            e.departmentID = deptID
        GROUP BY 
            e.employeeNumber
    ) AS deptSales;
    
    RETURN avgSales;
END //
DELIMITER ;
 
-- Step 3: Query to display total compensation and average department sales for each employee
SELECT 
    e.employeeID, e.firstName, e.lastName, 
    calculate_total_compensation(e.employeeID) AS totalCompensation,
    avg_department_sales(e.employeeID) AS avgDeptSales
FROM 
    employees e;
```
 
### Project 3: Sales Trend Analysis
 
**File: sales_trend_analysis.sql**
```sql
-- Step 1: Recursive CTE to calculate cumulative sales for each month and year
WITH RECURSIVE sales_cte AS (
    SELECT 
        YEAR(orderDate) AS year, MONTH(orderDate) AS month,
        SUM(od.quantityOrdered * od.priceEach) AS monthlySales
    FROM 
        orders o
    JOIN 
        orderdetails od ON o.orderNumber = od.orderNumber
    GROUP BY 
        YEAR(orderDate), MONTH(orderDate)
    UNION ALL
    SELECT 
        year, month,
        (SELECT SUM(od.quantityOrdered * od.priceEach)
         FROM orders o
         JOIN orderdetails od ON o.orderNumber = od.orderNumber
         WHERE YEAR(orderDate) = sales_cte.year
         AND MONTH(orderDate) <= sales_cte.month) AS cumulativeSales
    FROM 
        sales_cte
    WHERE 
        month < 12
)
SELECT * FROM sales_cte;
 
-- Step 2: Create view sales_trends with monthly and yearly sales growth
CREATE VIEW sales_trends AS
SELECT 
    year, month, monthlySales,
    LAG(monthlySales, 1) OVER (ORDER BY year, month) AS previousMonthSales,
    (monthlySales - LAG(monthlySales, 1) OVER (ORDER BY year, month)) / LAG(monthlySales, 1) OVER (ORDER BY year, month) * 100 AS monthlyGrowth,
    SUM(monthlySales) OVER (PARTITION BY year ORDER BY month) AS cumulativeYearlySales,
    LAG(SUM(monthlySales) OVER (PARTITION BY year ORDER BY month), 1) OVER (ORDER BY year) AS previousYearCumulativeSales,
    (SUM(monthlySales) OVER (PARTITION BY year ORDER BY month) - LAG(SUM(monthlySales) OVER (PARTITION BY year ORDER BY month), 1) OVER (ORDER BY year)) / LAG(SUM(monthlySales) OVER (PARTITION BY year ORDER BY month), 1) OVER (ORDER BY year) * 100 AS yearlyGrowth
FROM 
    sales_cte;
 
-- Step 3: Query to display sales trends
SELECT 
    year, month, monthlySales, monthlyGrowth, cumulativeYearlySales, yearlyGrowth
FROM 
    sales_trends
ORDER BY 
    year, month;
```
 
### Project 4: Customer Segmentation
 
**File: customer_segmentation.sql**
```sql
-- Step 1: Create view customer_orders consolidating customer details, total orders placed, and total amount spent
CREATE VIEW customer_orders AS
SELECT 
    c.customerNumber, c.customerName, c.contactLastName, c.contactFirstName,
    COUNT(o.orderNumber) AS totalOrders, SUM(od.quantityOrdered * od.priceEach) AS totalAmountSpent
FROM 
    customers c
JOIN 
    orders o ON c.customerNumber = o.customerNumber
JOIN 
    orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY 
    c.customerNumber, c.customerName, c.contactLastName, c.contactFirstName;
 
-- Step 2: Stored procedure to segment customers based on total purchase amount
DELIMITER //
CREATE PROCEDURE segment_customers()
BEGIN
    UPDATE customer_orders
    SET segment = CASE 
        WHEN totalAmountSpent > 100000 THEN 'high-value'
        WHEN totalAmountSpent BETWEEN 50000 AND 100000 THEN 'medium-value'
        ELSE 'low-value'
    END;
END //
DELIMITER ;
 
-- Step 3: Query to display list of customers along with their segment
CALL segment_customers();
 
SELECT 
    customerNumber, customerName, contactLastName, contactFirstName, totalOrders, totalAmountSpent, segment
FROM 
    customer_orders;
```
 
### Project 5: Database Performance Tuning
 
**File: database_performance_tuning.sql**
```sql
-- Step 1: Identify problematic queries using EXPLAIN and database statistics
-- Example: Analyze query performance
EXPLAIN SELECT * FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Step 2: Write efficient SQL queries for the identified problematic queries
-- Original query:
-- SELECT * FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Optimized query:
CREATE INDEX idx_orderDate ON orders(orderDate);
SELECT * FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Step 3: Compare performance using EXPLAIN
EXPLAIN SELECT * FROM orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Step 4: Document findings and justifications (this would typically be in a separate document)
-- Example documentation:
-- - Added index on orderDate to optimize query performance.
-- - Reduced full table scan by utilizing index on orderDate column.
```
 
### Project 6: Performance Optimization for an E-Commerce Database
 
**File: ecommerce_performance_optimization.sql**
```sql
-- Session 1: Performance Audit and Database Statistics
-- Step 1: Identify performance issues (typically involves stakeholder communication, not SQL)
-- Step 2: Review MySQL query logs (administrative task, not SQL)
-- Step 3: Retrieve database statistics
SELECT 
    table_name AS `Table`, 
    table_rows AS `Total Rows`, 
    data_length AS `Total Size (bytes)`, 
    update_time AS `Last Update`
FROM 
    information_schema.tables
WHERE 
    table_schema = '
 
ecommerce';
 
-- Step 4: Capture performance metrics for long-running queries (example query)
EXPLAIN ANALYZE SELECT * FROM Orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Session 2: Index Optimization and Query Performance
-- Step 1: Review current indexes (example query)
SHOW INDEX FROM Orders;
 
-- Step 2: Implement new indexes and measure performance changes
CREATE INDEX idx_orderDate ON Orders(orderDate);
 
-- Step 3: Develop index maintenance strategy (typically involves documentation and scheduled tasks)
 
-- Step 4: Ensure SQL code quality (best practices)
 
-- Session 3: Query Optimization and Performance Tuning
-- Step 1: Optimize long-running queries (example)
-- Original query:
-- SELECT * FROM Orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Optimized query:
CREATE INDEX idx_orderDate ON Orders(orderDate);
SELECT * FROM Orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Step 2: Generate and analyze execution plans (example)
EXPLAIN SELECT * FROM Orders WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- Step 3: Ensure SQL code quality (best practices)
 
-- Session 4: Monitoring and Reporting
-- Step 1: Monitor performance improvements (example)
-- Monitor using performance schema or other tools
 
-- Step 2: Prepare report (typically involves writing a document or presentation)
 
-- Step 3: Propose future plans (typically involves writing a document or presentation)
```
 