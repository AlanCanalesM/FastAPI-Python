from fastapi import FastAPI
from database import database as connection


app = FastAPI(title='This project write about movies',
              description='In this project we can write about movies',
              version='1'
              )


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

        print('Connecting...')


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        print('Close')


@app.get('/')
async def index():
    return 'Hello world!, from a server on FastAPI'
