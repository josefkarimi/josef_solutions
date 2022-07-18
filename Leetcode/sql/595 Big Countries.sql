--  Write your MySQL query statement below
select name,
    population,
    area
from world
where area >= 30000000
    or population >= 25000000;
SELECT name,
    population,
    area
FROM World
Where (area >= 3000000)
UNION
SELECT name,
    population,
    area
FROM World
Where (population >= 25000000);
--  Runtime: 294 ms, faster than 65.84% of MySQL online submissions for Big Countries.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Big Countries.