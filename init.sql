CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  title VARCHAR(60),
  description VARCHAR(200),
  imageurl VARCHAR(200),
  price FLOAT,
  CONSTRAINT posprice CHECK (price >= 0.0)
);

INSERT INTO products VALUES (DEFAULT, '5-Panel Yankees Cap', 'Needs no introduction', 'https://raw.githubusercontent.com/Sam-JR-Milburn/productapi/refs/heads/main/images/yankees.jpg', 18.50);
INSERT INTO products VALUES (DEFAULT, 'Brown Sunglasses', 'For that 70s oil crisis look.', 'https://raw.githubusercontent.com/Sam-JR-Milburn/productapi/refs/heads/main/images/brownglasses.jpg', 32.00);
INSERT INTO products VALUES (DEFAULT, 'The Great Gatsby', 'The Great American Novel', 'https://raw.githubusercontent.com/Sam-JR-Milburn/productapi/refs/heads/main/images/greatgatsby.jpg', 25.00);
INSERT INTO products VALUES (DEFAULT, 'Homer''s Iliad', 'Kleos Aphthiton.', 'https://raw.githubusercontent.com/Sam-JR-Milburn/productapi/refs/heads/main/images/homer-theiliad.jpg', 45.00);
INSERT INTO products VALUES (DEFAULT, 'Triple Cheeseburger', 'Why not?', 'https://raw.githubusercontent.com/Sam-JR-Milburn/productapi/refs/heads/main/images/triplecheese.jpg', 10.40);
