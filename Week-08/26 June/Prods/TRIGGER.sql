-- To Make a trigger that works on Saturday and Sunday

DELIMITER //

-- For Insert------------------------------------------------------------------------------------------

create trigger trigg1
before insert on employee.employeeinfo
for each row
begin
if (DAYOFWEEK(CURDATE()) = 7 or DAYOFWEEK(CURDATE()) = 1) then
signal sqlstate '45000' SET MESSAGE_TEXT = 'You cannot perform this on saturday and sunday';
end if ;
end //

-- For Update------------------------------------------------------------------------------------------

create trigger trigg1
before insert on employee.employeeinfo
for each row
begin
if (DAYOFWEEK(CURDATE()) = 7 or DAYOFWEEK(CURDATE()) = 1) then
signal sqlstate '45000' SET MESSAGE_TEXT = 'You cannot perform this on saturday and sunday';
end if ;
end //

-- For Delete------------------------------------------------------------------------------------------

create trigger trigg1
before insert on employee.employeeinfo
for each row
begin
if (DAYOFWEEK(CURDATE()) = 7 or DAYOFWEEK(CURDATE()) = 1) then
signal sqlstate '45000' SET MESSAGE_TEXT = 'You cannot perform this on saturday and sunday';
end if ;
end //

DELIMITER ;