-- List all the shows in hbtn_0d_tvshows
-- Format: tv_shows.title - tv_show_genres.genre_id

SELECT
s.title,
s_g.genre_id
FROM
tv_show_genres s_g
RIGHT JOIN tv_shows s ON s_g.show_id = s.id
ORDER BY s.title, s_g.genre_id;
