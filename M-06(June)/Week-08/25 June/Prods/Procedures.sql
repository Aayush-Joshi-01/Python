-- Procedures
use employee;


-- Sample Procedure

DELIMITER //
create procedure new_proc(in a int)
begin
select a ;
end //
DELIMITER ;

-- Calling the above Procedure

call new_proc(5);

-- Procedure to Reverse the number 
DELIMITER //
create procedure reverse_num(in num int)
begin
declare remainder int;
declare reversed_num int;
set reversed_num = 0;
while num > 0
do
set remainder = num % 10 ;
set reversed_num = reversed_num * 10 + remainder ;
set num = floor( num / 10) ;
end while;
select reversed_num;
end //
DELIMITER ;

-- Procedure to view the data of two tables simultaneously
DELIMITER //
create procedure view_table()
begin
select * from employee.employeeinfo;
select * from employee.employeeposition;
end //
DELIMITER ; 

-- Droping the Procedures
drop procedure reverse_num;
drop procedure view_table;

-- Calling the Procedures

call reverse_num(1234567);

call view_table();

