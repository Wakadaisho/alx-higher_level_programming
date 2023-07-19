-- List all shows by their rating
-- Format: tv_shows.title - rating sum

SELECT
s.title,
SUM(r.rate) AS rating
FROM
tv_shows s
JOIN tv_show_ratings r ON s.id = r.show_id
GROUP BY s.title
ORDER BY rating DESC;
