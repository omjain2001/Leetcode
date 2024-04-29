# Write your MySQL query statement below
SELECT customer_id, count(customer_id) as count_no_trans FROM Visits v WHERE visit_id NOT IN (SELECT visit_id FROM Transactions) GROUP BY customer_id;