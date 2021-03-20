select
*
from users u
where
id != {id}
order by random()
limit 5::int