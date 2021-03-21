insert into users(id, avatar, description, name, sex)
select unnest(array{id}), unnest(array{avatar}), unnest(array{description}), unnest(array{name}), {sex}
returning id;

