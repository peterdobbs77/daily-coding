--TABLE sellers
--  id INTEGER PRIMARY KEY,
--  name VARCHAR(30) NOT NULL,
--  rating INTEGER NOT NULL
--
--TABLE items
--  id INTEGER PRIMARY KEY,
--  name VARCHAR(30) NOT NULL,
--  sellerId INTEGER REFERENCES sellers(id)


select i.name,good_sellers.name from (
  select * from sellers where rating>4
) good_sellers
join (select * from items) i
on i.sellerId = good_sellers.id
