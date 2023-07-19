-- List all shows that are not a Comedy
-- Format: tv_shows.title

SELECT
title
FROM 
tv_shows
WHERE title NOT IN (
	SELECT
	s.title
	FROM
	tv_show_genres s_g
	JOIN tv_shows s ON s_g.show_id = s.id
	JOIN tv_genres g ON s_g.genre_id = g.id
	WHERE g.name = "Comedy"
)
ORDER BY title;

