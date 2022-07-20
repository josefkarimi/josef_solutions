-- # Please write a DELETE statement and DO NOT write a SELECT statement.
-- # Write your MySQL query statement below


delete p1 from person p1, person p2 where p1.email = p2.email and  p1.id > p2.id ; 


-- Runtime: 803 ms, faster than 69.20% of MySQL online submissions for Delete Duplicate Emails.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.