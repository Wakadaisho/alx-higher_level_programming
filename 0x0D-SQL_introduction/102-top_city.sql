-- Display top 3 cities temperature
-- for June (7) and August (8)
-- Descending temperature average

SELECT
city,
AVG(value) AS 'avg_temp'
FROM
temperatures
WHERE MONTH IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
