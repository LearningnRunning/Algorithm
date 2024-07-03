# Write your MySQL query statement below
WITH consecutive_visits AS (
    SELECT id, visit_date, people,
           LAG(people, 1) OVER (ORDER BY id) AS prev_people,
           LAG(people, 2) OVER (ORDER BY id) AS prev2_people,
           LEAD(people, 1) OVER (ORDER BY id) AS next_people,
           LEAD(people, 2) OVER (ORDER BY id) AS next2_people
    FROM Stadium
)
SELECT DISTINCT s.id, s.visit_date, s.people
FROM consecutive_visits s
WHERE s.people >= 100 AND (
    (s.prev_people >= 100 AND s.prev2_people >= 100) OR
    (s.prev_people >= 100 AND s.next_people >= 100) OR
    (s.next_people >= 100 AND s.next2_people >= 100)
)
ORDER BY s.visit_date;