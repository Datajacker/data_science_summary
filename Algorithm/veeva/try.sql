-- root
-- t
select distinct N
from t
where P is null

--leaf
select distinct N
from t
where N is not in (
    select distinct P
    from t
)

select distinct N,
       case when P is null then 'root' as label
       case when N is not in (
          select distinct P
          from t
         ) then 'leaf' as