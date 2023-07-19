-- Count shows by genre in hbtn_0d_tvshows
-- Format: <TV Show genre> - <Number of shows linked to this genre>

SELECT
g.name AS 'genre',
COUNT(*) AS 'number_of_shows'
FROM
tv_show_genres s_g
JOIN tv_genres g ON s_g.genre_id = g.id
GROUP BY genre
ORDER BY number_of_shows DESC;
