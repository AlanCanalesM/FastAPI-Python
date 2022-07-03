
from fastapi import FastAPI
from .routers import user_router
from .routers import reviews_router
from project.database import User
from project.database import Movie
from project.database import userReviews
from project.database import database as connection


app = FastAPI(title='This project write about movies',
              description='In this project we can write about movies',
              version='1'
              )


app.include_router(user_router)
app.include_router(reviews_router)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, userReviews])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Close')







