# Write your MySQL query statement below
select Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
    LEFT JOIN Address ON Person.personId = Address.personId;
-- Runtime: 502 ms, faster than 38.18% of MySQL online submissions for Combine Two Tables.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.