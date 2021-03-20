select
    status
from likes
where id_first = {id_first}::text
and id_second = {id_second}::text
and status is True
