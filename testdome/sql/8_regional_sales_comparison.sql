select r.name as region, AVG(emp_amount) avg_emp_sales from(
  select e.id as employeeId, e.stateid, SUM(IFNULL(sa.amount,0)) as emp_amount 
  FROM employees e
  LEFT OUTER join sales sa
  on e.id = sa.employeeId
  group by e.id, e.stateid
) agg
left outer join states st on agg.stateId = st.id
left outer join regions r on st.regionId = r.id
group by r.name