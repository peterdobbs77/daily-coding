--TABLE dogs
--  id INTEGER NOT NULL PRIMARY KEY,
--  name VARCHAR(50) NOT NULL
--
--TABLE cats
--  id INTEGER NOT NULL PRIMARY KEY,
--  name VARCHAR(50) NOT NULL


select distinct(name) from (
  select name from dogs union
  select name from cats
) pets
