import time
time.sleep(3) # Wait for Postgres Server to start.

# Python ORM.
import sqlalchemy
from sqlalchemy import create_engine, insert, text
from sqlalchemy import Table, Column, Integer, String, Float, MetaData

from fastapi import FastAPI # Uvicorn ASGI WebServer
import sys

# Requires psycopg2 driver, postgresql driver.
CONNECTION_STR: str = "postgresql+psycopg2://postgres:postgres@postgres_db:5432/commerce"
def get_connection() -> sqlalchemy.engine.Connection:
    engine = create_engine(CONNECTION_STR)
    return engine.connect()

connection: sqlalchemy.engine.Connection = None
try:
    connection = get_connection()
except:
    print("Failed to get DB connection.")
    #sys.exit()


meta = MetaData()
# products table
products = Table(
    'products', meta,
    Column('id', Integer, primary_key = True),
    Column('title', String),
    Column('description', String),
    Column('price', Float)
)




application = FastAPI()
'''
@application.get("/")
async def root():
    return {"Hi": "There"}
'''

@application.get("/products")
async def get_products():
    return {"productlist": ["product1", "product2"]}

@application.get("/products/{productid}")
async def read_item(productid):
    return {"productid": productid}
