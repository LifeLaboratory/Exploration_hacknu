UPDATE
  users
SET
  avatar = {avatar},
  description = {description},
  name = {name},
  lastname = {lastname},
  avatarThumb = {avatarThumb},
  phone = {phone},
  latitude = {latitude}::float,
  longitude = {longitude}::float
WHERE id = {id}
RETURNING id;