CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  title VARCHAR(60),
  description VARCHAR(200),
  price FLOAT,
  CONSTRAINT posprice CHECK (price >= 0.0)
);

INSERT INTO products VALUES (DEFAULT, '5-Panel Yankees Cap', 'Needs no introduction.', 18.50);
