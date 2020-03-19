--TABLE employees
--  id INTEGER NOT NULL PRIMARY KEY
--  managerId INTEGER REFERENCES employees(id)
--  name VARCHAR(30) NOT NULL


select name from (
  select * from employees 
) underlings
where not exists (
  select * from employees 
  where managerId = underlings.id
)
