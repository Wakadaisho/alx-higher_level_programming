-- Lists all the cities from hbtn_0d_usa
-- Format: cities.id - cities.name - states.name

SELECT
c.id,
c.name,
s.name
FROM
cities c
JOIN states s ON c.state_id = s.id
ORDER BY c.id;
