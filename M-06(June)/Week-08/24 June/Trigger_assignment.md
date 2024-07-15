# Trigger Assigment

## Requirements

**During the Time between 6pm to 10am in the morning Any user should not be allowed to Insert Update and Delete from the table**

```sql
DELIMITER // -- TO allow ';' to be used without terminating the execution 

CREATE TRIGGER insert_restrictions 
-- Creating Insert Restriction Trigger
BEFORE INSERT ON employee.employeeinfo
FOR EACH ROW
BEGIN

    IF ( (CURTIME() >= '18:00:00' AND CURTIME() <= '23:59:59') OR 

    -- Checking time between 18:00:00 (6 pm) to 11:59:59 (midnight)

         (CURTIME() >= '00:00:00' AND CURTIME() <= '10:00:00') ) THEN 

         -- Checking time between 00:00:00 (midnight) to 10:00:00 (10 am)

        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insert Operations are not allowed till 10am and after 6pm';
        
        -- Using SIGNAL SQLSTATE '45000' for Unhandled User-defined Exception /  Error
        -- and SET MESSAGE_TEXT to give a custom error message;

    END IF;
END //

CREATE TRIGGER update_restrictions -- Createing Update Restriction
BEFORE UPDATE ON employee.employeeinfo
FOR EACH ROW
BEGIN
    IF ( (CURTIME() >= '18:00:00' AND CURTIME() <= '23:59:59') OR
         (CURTIME() >= '00:00:00' AND CURTIME() <= '10:00:00') ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Operations are not allowed till 10am and after 6pm';
    END IF;
END //

CREATE TRIGGER delete_restrictions -- Creating Delete Restriction
BEFORE DELETE ON employee.employeeinfo
FOR EACH ROW
BEGIN
    IF ( (CURTIME() >= '18:00:00' AND CURTIME() <= '23:59:59') OR
         (CURTIME() >= '00:00:00' AND CURTIME() <= '10:00:00') ) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Delete Operations are not allowed till 10am and after 6pm';
    END IF;
END //

DELIMITER 
```

```commandline
14:40:41	
CREATE TRIGGER insert_restrictions BEFORE INSERT ON employee.employeeinfo FOR EACH ROW BEGIN      
IF ( (CURTIME() >= '18:00:00' AND CURTIME() <= '23:59:59') OR          
(CURTIME() >= '00:00:00' AND CURTIME() <= '10:00:00') ) THEN        
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insert Operations are not allowed till 10am and after 6pm';     
END IF; 
END	
0 row(s) affected	0.094 sec


14:41:35	
CREATE TRIGGER update_restrictions BEFORE UPDATE ON employee.employeeinfo FOR EACH ROW BEGIN      
IF ( (CURTIME() >= '18:00:00' AND CURTIME() <= '23:59:59') OR          
(CURTIME() >= '00:00:00' AND CURTIME() <= '10:00:00') ) THEN         
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Operations are not allowed till 10am and after 6pm';     
END IF; 
END	
0 row(s) affected	0.016 sec


14:41:35	
CREATE TRIGGER update_restrictions BEFORE UPDATE ON employee.employeeinfo FOR EACH ROW BEGIN      
IF ( (CURTIME() >= '18:00:00' AND CURTIME() <= '23:59:59') OR          
(CURTIME() >= '00:00:00' AND CURTIME() <= '10:00:00') ) THEN         
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Operations are not allowed till 10am and after 6pm';     
END IF; 
END	
0 row(s) affected	0.016 sec
```