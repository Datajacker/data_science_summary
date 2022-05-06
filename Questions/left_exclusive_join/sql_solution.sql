-- this apply when we have unique key
SELECT <column_list>
FROM TABLEA a
LEFTJOIN TABLEB b 
ON a.Key = b.Key 
WHERE b.Key IS NULL;

-- NOT EXISTS
SELECT name FROM table2 as t2
WHERE NOT EXISTS (SELECT * FROM table1 as t1 WHERE t1.name = t2.name)

--without unique key
select id, name from table1
minus
select id, name from table2