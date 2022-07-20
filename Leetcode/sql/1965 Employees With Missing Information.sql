-- # Write your MySQL query statement below
SELECT T.employee_id
FROM  
  (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
   UNION 
   SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS T
WHERE T.salary IS NULL OR T.name IS NULL
ORDER BY employee_id;


-- # Runtime: 1883 ms, faster than 5.02% of MySQL online submissions for Employees With Missing Information.
-- # Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees With Missing Information.






SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION 
SELECT employee_id FROM Salaries WHERE employee_id NOT IN (SELECT employee_id FROM Employees) order by 
employee_id;



-- Runtime: 540 ms, faster than 63.22% of MySQL online submissions for Employees With Missing Information.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees With Missing Information.