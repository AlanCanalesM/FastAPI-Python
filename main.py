from genericpath import exists
from fastapi import HTTPException
from typing import List
from fastapi import FastAPI
from numpy import where
from schemas import UserRequestModel
from schemas import UserResponseModel
from schemas import ReviewRequestModel
from schemas import ReviewResponseModel
from schemas import ReviewUpdateModel
from database import User
from database import Movie
from database import userReviews
from database import database as connection


app = FastAPI(title='This project write about movies',
              description='In this project we can write about movies',
              version='1'
              )


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


@app.get('/')
async def index():
    return 'Hello world!, from a server on FastAPI'


@app.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).first():
        return HTTPException(409, 'This username is already exists, You could try with other')

    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )

    return user


@app.post('/reviews', response_model=ReviewResponseModel)
async def create_review(review: ReviewRequestModel):

    if User.select().where(User.id == review.user_id).first() is None:
        raise HTTPException(404, 'User not found')

    if Movie.select().where(Movie.id == review.movie_id).first() is None:
        raise HTTPException(404, 'Movie not found')

    user_review = userReviews.create(
        user_id=review.user_id,
        movie_id=review.movie_id,
        review=review.review,
        score=review.score
    )

    return user_review


@app.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews():

    reviews = userReviews.select()  # Select * From userReviews;

    return [user_review for user_review in reviews]


@app.get('/reviews/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):

    user_review = userReviews.select().where(userReviews.id == review_id).first()

    if user_review is None:

        raise HTTPException(404, 'Review not found')

    return user_review


@app.put('/reviews/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, new_review: ReviewUpdateModel):

    user_review = userReviews.select().where(userReviews.id == review_id).first()

    if user_review is None:

        raise HTTPException(404, 'Review not found')

    user_review.review = new_review.review
    user_review.score = new_review.score

    user_review.save()

    return user_review
