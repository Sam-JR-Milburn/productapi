from sqlalchemy import create_engine, insert, text
import time

time.sleep(4) # Wait for Postgres backend to start.

# --
print("Attempting to create dbms python engine...")
engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres_db:5432/commerce")
conn = engine.connect()
print("Connected.")
# --
query = text("INSERT INTO product VALUES (DEFAULT, {title}, {description}, {price});".format(title=''))
conn.execute(query)
conn.commit()
print("Committed.")
