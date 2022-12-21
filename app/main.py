from fastapi import FastAPI
from curses.panel import new_panel
from hashlib import new
from random import randrange
import stat
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from .routers import posts, users, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres', cursor_factory=RealDictCursor)    #RealDictCursor will cause the returned values to be a dict otherwise it would return an object (i think)
        cursor = conn.cursor()
        print("Database Connection was successful")
        break
    except Exception as error:
        print("Condnection to database failed")
        print("Error: ", error)
        time.sleep(2)


my_posts = [{"title": "title od post 1", "content": "content of post 1", "id": 1}, {"title": "title of post 2", "content": "content of post 2", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}



