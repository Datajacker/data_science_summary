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
END

-- 181. Employees Earning More Than Their Managers
select t1.name as Employee
from Employee t1, Employee t2
where t1.managerId = t2.id and t1.salary > t2.salary