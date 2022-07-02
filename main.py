from fastapi import FastAPI

app = FastAPI(title='This project write about movies',
            description='In this project we can write about movies',
            version='1'
            )


@app.on_event('startup')
def startup():
    print ('The server is begining')


@app.on_event('shutdown')
def shutdown():
    print ('The server is ending')

@app.get('/')
async def index():
    return 'Hello world!, from a server on FastAPI'


