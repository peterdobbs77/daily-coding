--TABLE regions
--  id INTEGER PRIMARY KEY
--  name VARCHAR(50) NOT NULL
--
--TABLE states
--  id INTEGER PRIMARY KEY
--  name VARCHAR(50) NOT NULL
--  regionId INTEGER NOT NULL REFERENCES regions(id)
--
--TABLE employees
--  id INTEGER PRIMARY KEY
--  name VARCHAR(50) NOT NULL
--  stateId INTEGER NOT NULL REFERENCES states(id)
--
--TABLE sales
--  id INTEGER PRIMARY KEY
--  amount INTEGER NOT NULL
--  employeeId INTEGER NOT NULL REFERENCES employees(id)


select r.name as region, AVG(emp_amount) as avg_emp_sales
, (MAX(AVG(emp_amount)) OVER())-AVG(emp_amount) as diff
from(
  select e.id as employeeId, e.stateid, SUM(IFNULL(sa.amount,0)) as emp_amount 
  FROM employees e
  LEFT OUTER join sales sa
  on e.id = sa.employeeId
  group by e.id, e.stateid
) agg
join states st on agg.stateId = st.id
join regions r on st.regionId = r.id
group by r.name
