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


select *, (MAX(avg_emp_sales) OVER())-avg_emp_sales as diff
from(
  select r.name as region, IFNULL(AVG(emp_amount),0) as avg_emp_sales
  from regions r
  LEFT OUTER join states st on st.regionId = r.id
  LEFT OUTER join (
    select e.id as employeeId, e.stateid, SUM(IFNULL(sa.amount,0)) as emp_amount 
    FROM employees e
    LEFT OUTER join sales sa
    on e.id = sa.employeeId
    group by e.id, e.stateid
  ) agg
  on agg.stateId = st.id
  group by r.name
)
