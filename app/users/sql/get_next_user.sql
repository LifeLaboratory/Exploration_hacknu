select
*
from users
where
id not in (select distinct id_second from likes where id_first = {id}::text limit 1)
limit 1