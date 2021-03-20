select

json_build_object(
    'user_first', json_build_object(
                    'id', u1.id,
                    'avatar', u1.avatar,
                    'description', u1.description,
                    'name', u1.name,
                    'lastname', u1.lastname,
                    'avatarThumb', u1."avatarThumb",
                    'phone', u1.phone
    ),
    'user_second', json_build_object(
                    'id', u2.id,
                    'avatar', u2.avatar,
                    'description', u2.description,
                    'name', u2.name,
                    'lastname', u2.lastname,
                    'avatarThumb', u2."avatarThumb",
                    'phone', u2.phone
    ),
    'place', json_build_object(
                    'id_place', p.id_place,
                    'link', p.link,
                    'latitude', p.latitude,
                    'longitude', p.longitude
    ),
    'datetime', m.datetime
)

from

meetings m
left join places p on p.id_place = m.id_place
left join users u1 on u1.id = m.id_first
left join users u2 on u2.id = m.id_second
where m.id_first = {id}::text or m.id_second = {id}::text
