-- Retrieves all genres from the hbtn_0d_tvshows database with the count of linked shows.
-- Excludes genres with no linked shows.
-- Records are ordered by the number of linked shows in descending order.

SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS t
       ON g.`id` = t.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
 
