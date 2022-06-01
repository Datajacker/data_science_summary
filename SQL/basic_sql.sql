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

-- 185. Department Top Three Salaries
with t as(
   select 
   name, 
   departmentId,salary,
   DENSE_RANK() over(PARTITION BY departmentId ORDER BY salary DESC) AS rnk
 from Employee
)

select a.name as Department, 
       t.name as Employee, 
       t.salary as Salary
from t
left join Department a
on t.departmentId = a.id 
where rnk < 4

-- 196. Delete Duplicate Emails
DELETE FROM Person WHERE Id NOT IN 
(SELECT * FROM(
    SELECT MIN(Id) FROM Person GROUP BY Email) as p)


-- 262. Trips and Users
# Write your MySQL query statement below
with client as (
select *
from Users
where role = 'client' and banned = 'No'),
driver as(
select *
from Users
where role = 'driver' and banned = 'No'),
trips_clean as (
select *
from Trips
where request_at between '2013-10-01' and '2013-10-03'
      and client_id in (select users_id from client)
      and driver_id in (select users_id from driver)),
trip_completed as (
select request_at as 'Day',
       count(status) as completed
from trips_clean
where status = 'completed'
group by request_at),
trip_total as (
select request_at as 'Day',
       count(status) as total
from trips_clean
group by request_at)

select trip_total.Day, ifnull(round(1-trip_completed.completed/trip_total.total, 2), 1) as 'Cancellation Rate'
from trip_total
left join trip_completed
on trip_total.Day = trip_completed.Day



-- 511. Game Play Analysis I
# Write your MySQL query statement below
with rnk as (
     select player_id,
            event_date,
            rank() over(partition by player_id order by event_date) as 'num'
     from Activity
      
      )
      
select player_id, event_date as first_login
from rnk 
where num = 1

-- 512. Game Play Analysis II
select a1.player_id, a1.device_id
from Activity a1
inner join (
  select player_id, min(event_date) as event_date
  from Activity 
  group by player_id
) a2 on a1.player_id = a2.player_id and a1.event_date = a2.event_date

select player_id, device_id
from Activity
where (player_id, event_date) in (
  select player_id, min(event_date)
  from Activity
  group by player_id
)

with cte as (
  select 
    *, 
    min(event_date) over(partition by player_id order by event_date asc) as min_event_date
  from Activity
)
select player_id, device_id
from cte
where event_date = min_event_date

-- 534. Game Play Analysis III
select player_id, event_date, 
    sum(games_played) over(partition by player_id order by event_date) as
    games_played_so_far
    from Activity

-- 550. Game Play Analysis IV
with a2 as (
SELECT player_id, MIN(event_date) as first_login
    FROM Activity
    GROUP BY player_id),
b as (
SELECT a1.player_id
FROM Activity as a1
INNER JOIN a2
    ON a1.player_id = a2.player_id AND a1.event_date - a2.first_login = 1
    )
    
SELECT
    ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id),2) as fraction
FROM Activity as a
LEFT JOIN b 
ON a.player_id = b.player_id

-- 569. Median Employee Salary
with ranked as(
select id, company, salary,
       row_number() over(partition by company order by salary) as rnk,
       COUNT(*) OVER (PARTITION BY company) AS cnt
from Employee
), -- get the rank and count
selected as (
    select company, cnt/2 as rnk  
    from ranked 
    where cnt%2 = 0
    union -- deal with even number
    select company, cnt/2 + 1 as rnk  
    from ranked 
    where cnt%2 = 0
    union -- deal with odd number of count
    select company, (cnt+1)/2 as rnk  
    from ranked 
    where (cnt+1)%2 = 0
    )
    
select id, ranked.company, salary
from ranked
inner join selected
on ranked.company = selected.company and ranked.rnk = selected.rnk

-- Alternative solution
with cte as (
    select
        *,
        count(*) over(partition by company) as cnt,
        row_number() over(partition by company order by salary asc) as rw
    from Employee
)
select id, company, salary
from cte
where 
    (cnt % 2 = 0 and rw in (cnt / 2, cnt / 2 + 1)) or
    (cnt % 2 <> 0 and rw = round(cnt / 2))


with cte as
(
select
id,
company,
salary,
rank() over(partition by company order by salary asc, id asc) as rnk,
count(id) over(partition by company) as ttl
from Employee
group by 1
)

select
id,
company,
salary
from cte
where ceiling((ttl+1)/2) = rnk
or floor((ttl+1)/2) = rnk

-- 570. Managers with at Least 5 Direct Reports
with sorted as (
select distinct managerId, 
       count(name) over(partition by managerId) as cnt
       
       from Employee)
       
       
       select Employee.name
       from Employee
       inner join sorted
       on Employee.id = sorted.managerId
       where sorted.cnt >4