-- Computes number of records with a score in hbtn_0c_0.second_table
-- Descending score

SELECT
score,
COUNT(score) AS 'number'
FROM
second_table
GROUP BY score
ORDER BY score DESC;
