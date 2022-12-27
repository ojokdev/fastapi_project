from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency - we are jjst going to keep calling this session every time we have a request tot he db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Not using below login anymore but we are keeping it here for our reference. Just in case we want to connecto to Postgres using the native drivers:
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)    #RealDictCursor will cause the returned values to be a dict otherwise it would return an object (i think)
#         cursor = conn.cursor()
#         print("Database Connection was successful")
#         break
#     except Exception as error:
#         print("Condnection to database failed")
#         print("Error: ", error)
#         time.sleep(2)