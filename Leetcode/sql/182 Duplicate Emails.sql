# Write your MySQL query statement below
select one.email as Email
from person one
    join person two on one.email = two.email
where one.id != two.id
Group by email;
-- Runtime: 401 ms, faster than 53.57% of MySQL online submissions for Duplicate Emails.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.