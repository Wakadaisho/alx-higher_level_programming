-- List all the shows in hbtn_0d_tvshows
-- Format: tv_shows.title - tv_genres.name

SELECT
s.title,
g.name
FROM
tv_show_genres s_g
RIGHT JOIN tv_shows s ON s_g.show_id = s.id
LEFT JOIN tv_genres g ON s_g.genre_id = g.id
ORDER BY s.title, g.name;
