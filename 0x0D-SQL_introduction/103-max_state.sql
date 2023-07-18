-- Display each state max temperature
-- Ascending state name

SELECT
state,
MAX(value) AS 'max_temp'
FROM
temperatures
GROUP BY state
ORDER BY state;
