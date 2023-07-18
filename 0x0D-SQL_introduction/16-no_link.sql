-- List all records in hbtn_0c_0.second_table
-- Descending score
-- No records without name

SELECT
score, name
FROM
second_table
WHERE NAME IS NOT NULL
ORDER BY score DESC;
