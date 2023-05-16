-- Computes and filters the average of a group of records
-- in a table in the database
SELECT city, AVG(value) 'avg_temp' FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
