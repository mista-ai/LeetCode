# Write your MySQL query statement below
DELETE p1 FROM Person p1, person p2
WHERE p1.email = p2.email AND p1.ID > p2.ID