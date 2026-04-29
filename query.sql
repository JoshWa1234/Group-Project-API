
UPDATE users SET user_type_id = 1 where id = '14967c56-f3e7-445d-b4b8-81b02a149568'


CREATE TABLE challenges (
  id INTEGER NOT NULL,
  title VARCHAR NOT NULL,
  description VARCHAR,
  points INTEGER NOT NULL,
  target INTEGER NOT NULL,
  frequency VARCHAR NOT NULL,
  due_date VARCHAR NOT NULL,
  assigned_to VARCHAR NOT NULL,
  status VARCHAR NOT NULL,
  progress INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
)