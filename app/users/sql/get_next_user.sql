select
*
from users u
where
id not in (select distinct id_second from likes where id_first = {id}::text limit 1)
and not exists(select 1 from meetings where id_first = u.id or id_second = u.id )
order by random()
limit {limit}::int