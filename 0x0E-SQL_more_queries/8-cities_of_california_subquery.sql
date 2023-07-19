-- Lists all the cities of California from hbtn_0d_usa

SELECT
c.id,
c.name
FROM
cities c
JOIN states s ON c.state_id = s.id
WHERE s.name = "California";
