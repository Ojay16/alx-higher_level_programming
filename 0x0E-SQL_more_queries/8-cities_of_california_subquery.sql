-- Retrieves all cities in California (CA) from the hbtn_0d_usa database.
-- Results are sorted by cities.id in ascending order.

SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
 
