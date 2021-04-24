DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  address VARCHAR(255),
  phone VARCHAR(255),
  website VARCHAR(255)
);

CREATE TABLE modules (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  stock INT,
  buying_cost INT,
  selling_price INT,
  function VARCHAR(255),
  width INT,
  depth INT,
  minus_12v INT,
  plus_12v INT,
  manufacturer_id INT REFERENCES manufacturers(id),
  image_url VARCHAR(255)
);