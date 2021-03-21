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
    {time_meeting}::timestamp
)
returning *
