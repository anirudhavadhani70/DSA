# Write your MySQL query statement below
select name from employee where id IN
 (
    select managerID from Employee Group By managerID having count(*)>=5
 );