CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  title VARCHAR(60),
  description VARCHAR(200),
  imageurl VARCHAR(200),
  price FLOAT,
  CONSTRAINT posprice CHECK (price >= 0.0)
);

INSERT INTO products VALUES (DEFAULT, '5-Panel Yankees Cap', 'Needs no introduction', '', 18.50);
INSERT INTO products VALUES (DEFAULT, 'Brown Sunglasses', 'For that 70s oil crisis look.', '', 32.00);
INSERT INTO products VALUES (DEFAULT, 'The Great Gatsby', 'The Great American Novel', '', 25.00);
INSERT INTO products VALUES (DEFAULT, 'Homer''s Iliad', 'Kleos Aphthiton.', '', 45.00);
INSERT INTO products VALUES (DEFAULT, 'Triple Cheeseburger', 'Why not?', '', 10.40);
