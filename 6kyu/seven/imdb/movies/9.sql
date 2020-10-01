-- In 9.sql, write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.
-- Your query should output a table with a single column for the name of each person.
-- People with the same birth year may be listed in any order.
-- No need to worry about people who have no birth year listed, so long as those who do have a birth year are listed in order.
-- If a person appeared in more than one movie in 2004, they should only appear in your results once.

-- Executing 9.sql results in a table with 1 column and 18,013 rows.
SELECT people.name
from people
where people.id in (
select distinct stars.person_id
from stars join movies on stars.movie_id = movies.id
WHERE movies.year = 2004)
ORDER BY people.birth;

-- https://stackoverflow.com/questions/59664139/why-is-this-sql-query-not-working-cs50-pset7-movies
