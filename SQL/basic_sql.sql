--176. Second Highest Salary
salary as SecondHighestSalary
from Employee
order by salary
limit 1 offset 1

select max(salary) as SecondHighestSalary
from Employee 
where salary < (select max(salary) from Employee)

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary

-- 177. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN ( with a as(
          SELECT  distinct salary, DENSE_RANK() over(order by salary desc) as 'Rank' 
          FROM Employee)
      
      select salary
      from a
      where a.Rank = N
      
  );


-- 181. Employees Earning More Than Their Managers
select t1.name as Employee
from Employee t1, Employee t2
where t1.managerId = t2.id and t1.salary > t2.salary

select E.name as Employee from Employee E
join Employee as M
on E.ManagerId = M.Id
where E.Salary > M.Salary;

-- 184. Department Highest Salary
with t as(
   select 
   name, 
   departmentId,salary,
   RANK() over(PARTITION BY departmentId ORDER BY salary DESC) AS rnk
 from Employee
)

select a.name as Department, 
       t.name as Employee, 
       t.salary as Salary
from t
left join Department a
on t.departmentId = a.id 
where rnk = 1

/*
WITH ranked AS(
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary,
        RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC) AS rnk
    FROM Employee e 
    JOIN Department d 
    ON e.departmentId = d.id) 

-- The highest salary is just those with rank = 1
SELECT 
    Department,
    Employee,
    Salary
FROM ranked
WHERE rnk = 1;
*/

SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;