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
  longitude = {longitude}::float,
  sex = {sex},
  sex_find = {sex_find}
WHERE id = {id}
RETURNING id;