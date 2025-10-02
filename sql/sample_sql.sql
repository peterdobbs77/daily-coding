-------------------------------------------------------------
-- Table Name : Employees

--  ID | Name    | Department | Salary | Joining_Date
-- ----+---------+------------+--------+--------------
--  1  | Rajesh  | IT         | 50000  | 2020-01-10
--  2  | Sneha   | HR         | 45000  | 2019-04-12
--  3  | Kiran   | Finance    | 52000  | 2021-08-23
--  4  | Priya   | Marketing  | 48000  | 2018-06-15
--  5  | Arjun   | IT         | 53000  | 2022-09-19
-------------------------------------------------------------

-- Count employees in each department.
select department, count(distinct(id)) as department_headcount from employees group by department;
-- Finance|1
-- HR|1
-- IT|2
-- Marketing|1

-- Retrieve the minimum salary in the table.
select * from employees order by salary asc limit 1;
-- 2|Sneha|HR|45000|2019-04-12

-- Calculate the sum of all employees' salaries.
select sum(salary) from employees;
-- 248000

-- List employees who joined in the month of September.
select * from employees where joining_date like '____-09-%'; -- in some SQL versions: where month(joining_date) = 9
-- 5|Arjun|IT|53000|2022-09-19

-- Retrieve the last 2 entries in the Employees table
select * from employees order by id desc limit 2; -- not very efficient :(
-- 5|Arjun|IT|53000|2022-09-19
-- 4|Priya|Marketing|48000|2018-06-15

-- List employees with names ending in 'a'.
select * from employees where name like '%a';
-- 2|Sneha|HR|45000|2019-04-12
-- 4|Priya|Marketing|48000|2018-06-15

-- List employees with a salary that is a multiple of 5000.
select * from employees where salary % 5000 = 0;
-- 1|Rajesh|IT|50000|2020-01-10
-- 2|Sneha|HR|45000|2019-04-12

-- Update the salary of 'Rajesh' to 55000.
update employees set salary = 55000 where name = "Rajesh";
select * from employees where name = "Rajesh";
-- 1|Rajesh|IT|55000|2020-01-10

-- Delete an entry where the Department is 'HR'.
delete from employees where department = "HR";
select * from employees;
-- 1|Rajesh|IT|50000|2020-01-10
-- 3|Kiran|Finance|52000|2021-08-23
-- 4|Priya|Marketing|48000|2018-06-15
-- 5|Arjun|IT|53000|2022-09-19


-------------------------------------------------------------
-- Table Name : Products

--  Product_ID | Product_Name | Category    | Price | Stock
-- ------------+ -------------+-------------+-------+-------
--  1          | Laptop       | Electronics | 55000 | 15
--  2          | Mobile Phone | Electronics | 30000 | 30
--  3          | Office Chair | Furniture   | 7000  | 10
--  4          | Coffee Maker | Appliances  | 4000  | 20
--  5          | Dining Table | Furniture   | 15000 | 5
-------------------------------------------------------------

-- Retrieve all products priced above the average price.
select * from products where price > (select avg(price) from products);
-- 1|Laptop|Electronics|55000|15
-- 2|Mobile Phone|Electronics|30000|30


-- Retrieve the highest-priced product in each category.
select *, max(price) from products group by category;
-- 4|Coffee Maker|Appliances|4000|20|4000
-- 1|Laptop|Electronics|55000|15|55000
-- 5|Dining Table|Furniture|15000|5|15000

-- Display the product with the lowest stock quantity.
select *, MIN(stock) from products;
-- 5|Dining Table|Furniture|15000|5|5
SELECT * FROM Products ORDER BY Stock ASC LIMIT 1;
-- 5|Dining Table|Furniture|15000|5

-- Show all products, replacing null values in stock with 0.
select product_id, product_name, category, price, COALESCE(stock, 0) as stock from products;
-- shows all (no nulls in this case, but nice use of `COALESC` function)

-- Update the stock of "Mobile Phone" by reducing it by 5.
update products set stock = stock - 5 where product_name = "Mobile Phone";
select * from products where product_name = "Mobile Phone";

-- List the top 2 most expensive products in each category.
with ranked as
    (   select category, price,
            row_number() over
                (   partition by category order by price desc   ) as rn
        from products
    )
select category, price from ranked
where rn <= 2
order by price;
-- Appliances|4000
-- Furniture|7000
-- Furniture|15000
-- Electronics|30000
-- Electronics|55000


-- List products grouped by category and sorted by price.
-- OPTION A:
with categories_ordered_by_price as
  (   select *,
        row_number() over
          ( partition by category order by price desc ) as rn
      from products
  )
select * from categories_ordered_by_price;
-- OPTION B:
select * from products order by category, price desc;

-- Show products with prices within 20% of the maximum price.
select * from products where price >= 0.8 * (select max(price) from products);
-- 1|Laptop|Electronics|55000|15

-- Find categories with an average product price above 10000.
-- OPTION A:
select category from (select category, AVG(price) as avg_price from products group by category) where avg_price > 10000;
-- OPTION B:
select category from products group by category having AVG(price) > 10000;
-- Electronics
-- Furniture

-- List all products showing only the first 3 characters of each name.
select substr(product_name, 1, 3) from products;
-- Lap
-- Mob
-- Off
-- Cof
-- Din

-- Retrieve products ordered by stock quantity, with Electronics first.
select * from products order by case when category = "Electronics" then 0 else 1 end, stock desc;
-- 2|Mobile Phone|Electronics|30000|30
-- 1|Laptop|Electronics|55000|15
-- 4|Coffee Maker|Appliances|4000|20
-- 3|Office Chair|Furniture|7000|10
-- 5|Dining Table|Furniture|15000|5
