from fastapi import FastAPI

app = FastAPI(title='This project write about movies',
            description='In this project we can write about movies',
            version='1'
            )


@app.get('/')
async def index():
    return 'Hello world!, from a server on FastAPI'

@app.get('/about')
async def about():
    return 'About Us'
