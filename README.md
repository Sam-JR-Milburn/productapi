# productapi
This is a 'toy' Python3 + FastAPI + PostgreSQL + Docker project to demonstrate a simple HTTP (w/ JSON) RESTful API.

Build this with 'docker compose build', then run 'docker compose up -d'. 
This will deploy two docker containers: 
  Hostname **postgres_db - port 5432**
  The official Postgres container with an initialised 'products' table under a 'commerce' database.

  Hostname **apiserver - port 8000**.
  A simple Python3 application using FastAPI Uvicorn Server and the SQLAlchemy ORM library to connect to the Postgres container.
  It responds to requests under /products and /products{numericidhere} on [port 8000].

Note: When running, check that there isn't a Postgres daemon instance open on your machine, which occupies port 5432.
At the moment the project is simple, but I'll update it alongside the WebDev frontend project to include product images, simple product list catalogues vs detailed product page information, and more.
