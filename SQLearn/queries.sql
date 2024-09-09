-- Data types
- integer
- text
- real

-- Creating a table
create database celebs ( id integer, name text, age integer);

-- Insertion
insert into celebs (id, name age) values (2, 'Justin Bieber', 33);

-- Alter
alter table celebs add column twitter_handle text;

-- Update
update celebs set twitter_handle='@taylorswift13' where id = 4;

-- Delete
delete from celebs where twitter_handle is null;

-- Constraints

CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);

-- note : If default is specified then no need to pass the column name in insert command

-- Select
select name, age from people;

-- distinct - unique values
select distinct country from films

-- count
select count(distinct birthdate) from people;

-- all entries who have a birthdate data, then distinct and then count

-- filtering
select title, release_year from films where release_year > '2000' AND release_year < '2010';
select title, release_year from films where release_year > '2000' OR release_year < '2010';

SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');

-- options :: =, <>, >, <, >=, <=

-- IN
select title,language from films where language in ('English','Spanish','French');

-- SELECT COUNT(*) FROM people WHERE birthdate IS NULL;

-- Like
NULL - it represents a missing or unknown value
SELECT name FROM companies WHERE name LIKE 'Data%';

-- The _ wildcard will match a single character
SELECT name FROM companies WHERE name LIKE 'DataC_mp';

-- Aggregate

SELECT AVG(budget) FROM films;
SELECT MAX(budget) FROM films;
SELECT MIN(budget) FROM films;
SELECT SUM(budget) FROM films;

-- AS - Aliasing
SELECT (10 / 3) as result;
-- o/p 3

select title, gross - budget as net_profit from films;
-- net_profit = gross - budget 

-- Ordering
-- By default ORDER BY will sort in ascending order. 
-- If you want to sort the results in descending order, you can use the DESC keyword. For example,

SELECT title FROM films ORDER BY release_year DESC;

-- Sorting by multiple columns
select birthdate, name from people order by birthdate, name;

-- Grouping
SELECT sex, count(*)
FROM employees
GROUP BY sex;

-- o/p
-- sex	   count
-- male 	15
-- female	19

-- Having
select release_year, avg (budget) as avg_budget ,avg(gross) as avg_gross from films 
where release_year > 1990 GROUP BY release_year HAVING avg(budget) > 60000000;

-- limit
select country, avg(budget) as avg_budget, avg(gross) as avg_gross
from films
group by country
having count(*) > 10
order by country
-- desc // for descending order
limit 5;

-- join (inner)
select * from customers
join employees
on customers.id = employees.id

select col1, col2 as col3 from customers
join employees
on customers.id = employees.id