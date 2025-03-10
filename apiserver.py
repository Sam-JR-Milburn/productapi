import time
time.sleep(3) # Wait for Postgres Server to start.

# Python ORM.
import sqlalchemy
from sqlalchemy import create_engine, insert, text
from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from sqlalchemy.orm import Session, sessionmaker

from fastapi import FastAPI, HTTPException # Uvicorn ASGI WebServer
import sys

# Requires psycopg2 driver, postgresql driver.
CONNECTION_STR: str = "postgresql+psycopg2://postgres:postgres@postgres_db:5432/commerce"
def get_connection() -> sqlalchemy.engine.Connection:
    engine = create_engine(CONNECTION_STR)
    return engine.connect()

# Check for DB connection.
connection: sqlalchemy.engine.Connection = None
try:
    connection = get_connection()
except:
    print("Failed to get DB connection.")
    sys.exit()

# Table exists already.
Meta = MetaData()
Products = Table(
    'products', Meta,
    Column('id', Integer, primary_key = True),
    Column('title', String),
    Column('description', String),
    Column('imageurl', String),
    Column('price', Float)
)

# Build a database session to Postgres, so we can communicate back-and-forth.
Session = sessionmaker(bind = connection)
pgSession = Session()

# Start the API server.
application = FastAPI()

@application.get("/products")
async def get_products():
    results = pgSession.query(Products).all()
    # Yield an error if the products couldn't be reached.
    if not results or len(results) < 1:
        raise HTTPException(status_code = 404, detail = "products couldn't be found")
    # Go through the returned rows, add them to a list. [Doesn't need description when getting all products.]
    productlist = []
    for product in results:
        productinfo = {"productid": product.id, "title": product.title, "imageurl": product.imageurl, "price": product.price}
        productlist.append(productinfo)
    # Finally, yield the list as JSON through FastAPI.
    return productlist

@application.get("/products/{productid}")
async def read_item(productid):
    # If the productid isn't a number, raise an HTTP 400.
    if not str(productid).isnumeric():
        raise HTTPException(status_code = 400, detail = "invalid productid request - must be a number")

    results = pgSession.query(Products).filter(Products.c.id == productid).all() # '.c.': Columns
    # Yield an error if the product couldn't be reached.
    if not results or len(results) < 1:
        raise HTTPException(status_code = 404, detail = "the product couldn't be found")

    # There should only be one product, but SQL is set-theoretic.
    productinfo = None
    for product in results:
        productinfo = {"productid": product.id, "title": product.title, "description": product.description, "imageurl": product.imageurl, "price": product.price}
        break
    return productinfo
