select

json_build_object(
    'user', json_build_object(
                    'id', coalesce(u1.id, u2.id),
                    'avatar', coalesce(u1.avatar, u2.avatar),
                    'description', coalesce(u1.description, u2.description),
                    'name', coalesce(u1.name, u2.name),
                    'lastname', coalesce(u1.lastname, u2.lastname),
                    'avatarThumb', coalesce(u1."avatarThumb", u1."avatarThumb"),
                    'phone', coalesce(u1.phone, u2.phone)
    ),
    'place', json_build_object(
                    'id_place', p.id_place,
                    'link', p.link,
                    'latitude', p.latitude,
                    'longitude', p.longitude
    ),
    'datetime', m.datetime
) meeting_info

from

meetings m
left join places p on p.id_place = m.id_place
left join users u1 on u1.id = m.id_first and u1.id != {id}::text
left join users u2 on u2.id = m.id_second and u2.id != {id}::text
where m.id_second = {id}::text or m.id_first = {id}::text
