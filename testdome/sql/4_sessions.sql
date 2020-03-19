--TABLE sessions
--  id INTEGER PRIMARY KEY,
--  userId INTEGER NOT NULL,
--  duration DECIMAL NOT NULL


select userId, avg_dur from (
  select userId, AVG(duration) as avg_dur, COUNT(id) as num 
  from sessions
  group by userId
) calc
where num>1
