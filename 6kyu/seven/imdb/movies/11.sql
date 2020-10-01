-- In 11.sql, write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
-- Your query should output a table with a single column for the title of each movie.
-- You may assume that there is only one person in the database with the name Chadwick Boseman.

-- Executing 11.sql results in a table with 1 column and 5 rows.
SELECT title FROM
(SELECT * FROM
people p JOIN stars s ON p.id = s.person_id JOIN
movies m ON s.movie_id = m.id JOIN
ratings r ON m.id = r.movie_id
WHERE name = "Chadwick Boseman")
ORDER BY rating DESC
LIMIT 5;
