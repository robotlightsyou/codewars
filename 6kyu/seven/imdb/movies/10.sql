-- In 10.sql, write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0.
-- Your query should output a table with a single column for the name of each person.

-- Executing 10.sql results in a table with 1 column and 1,841 rows.
SELECT people.name FROM
people
WHERE people.id in
(SELECT DISTINCT directors.person_id FROM
people JOIN directors ON people.id = directors.person_id JOIN
(SELECT * FROM movies join ratings ON movies.id = ratings.movie_id
WHERE rating >= 9.0) m
ON directors.movie_id = m.id);
