-- Retrieves all shows in hbtn_0d_tvshows with at least one linked genre.
-- Records are sorted by tv_shows.title and tv_show_genres.genre_id in ascending order.

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
 
