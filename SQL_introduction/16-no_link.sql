-- List all records of the table `second_table` of the database `hbtn_0c_0` in the MySQL server.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
