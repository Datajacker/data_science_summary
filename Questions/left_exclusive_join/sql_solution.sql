# this apply when we have unique key
SELECT <column_list>
FROM TABLEA a
LEFTJOIN TABLEB b 
ON a.Key = b.Key 
WHERE b.Key IS NULL;

# without unique key
select id, name from table1
minus
select id, name from table2