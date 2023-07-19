-- List all genres not linked to the show Dexter
-- Format: tv_genres.name

SELECT
name
FROM 
tv_genres
WHERE name NOT IN (
	SELECT
	g.name
	FROM
	tv_show_genres s_g
	JOIN tv_shows s ON s_g.show_id = s.id
	JOIN tv_genres g ON s_g.genre_id = g.id
	WHERE s.title = "Dexter"
)
ORDER BY name;
