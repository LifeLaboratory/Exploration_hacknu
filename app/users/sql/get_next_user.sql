select
*
from users
where id = {id}
and id not in (select distinct id_second from likes where id_first = {id})