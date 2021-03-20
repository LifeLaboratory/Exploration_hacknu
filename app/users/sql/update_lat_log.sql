UPDATE
  users
SET
  latitude = {latitude}::float,
  longitude = {longitude}::float
WHERE id = {id}
RETURNING id;