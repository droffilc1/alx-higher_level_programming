-- A script that lists all records of the table second_table of the database hbtn_0c_0
-- Records are ordered by descending order.
SELECT `score`, `name` FROM `second_table`
WHERE `name` != "" ORDER BY `score` DESC;
