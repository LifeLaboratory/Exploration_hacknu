select
*
from users u
where
id != {id} and sex = any(array{sex_find})
and id not in (select distinct id_second from likes where id_first = {id}::text)
and not exists(select 1 from meetings where id_first = u.id or id_second = u.id )
order by random()
limit 5::int