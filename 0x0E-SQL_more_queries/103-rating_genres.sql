-- List all shows by their rating
-- Format: tv_shows.title - rating sum

SELECT
g.name,
SUM(r.rate) AS rating
FROM
tv_show_genres s_g
JOIN tv_shows s on s_g.show_id = s.id
JOIN tv_genres g on s_g.genre_id = g.id
JOIN tv_show_ratings r ON s.id = r.show_id
GROUP BY g.name
ORDER BY rating DESC, g.name;
