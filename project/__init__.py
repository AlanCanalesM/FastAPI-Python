
from fastapi import FastAPI
from .routers import user_router
from .routers import reviews_router
from project.database import User
from project.database import Movie
from project.database import userReviews
from fastapi import APIRouter
from project.database import database as connection


app = FastAPI(title='This project write about movies',
              description='In this project we can write about movies',
              version='1'
              )

api_v1 = APIRouter(prefix='/api/v1')


api_v1.include_router(user_router)
api_v1.include_router(reviews_router)

app.include_router(api_v1)

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
