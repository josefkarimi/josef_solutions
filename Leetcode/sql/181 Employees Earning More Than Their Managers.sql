# Write your MySQL query statement below
select e.name as Employee
from Employee e
    join Employee m on e.managerId = m.id
where m.salary < e.salary;
-- Runtime: 670 ms, faster than 26.08% of MySQL online submissions for Employees Earning More Than Their Managers.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.