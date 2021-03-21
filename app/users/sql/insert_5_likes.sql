insert into likes
(
    id_first,
    id_second,
    datetime
)
select

unnest(
array{ids}
)
,unnest (
array{ids_likes}
)
, now()