insert into meetings
(
    id_first,
    id_second,
    id_place,
    datetime
)
values
(
    {id_first},
    {id_second},
    {id_place},
    now()
)
returning *
