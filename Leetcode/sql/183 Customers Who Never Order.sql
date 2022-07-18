# Write your MySQL query statement below
select name as Customers
from Customers
    left join orders on customerid = Customers.id
where orders.id is null;
-- Runtime: 529 ms, faster than 52.96% of MySQL online submissions for Customers Who Never Order.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.