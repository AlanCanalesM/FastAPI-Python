from ..database import User
from fastapi import Cookie, Response
from fastapi import APIRouter, HTTPException
from ..schemas import ReviewResponseModel, UserRequestModel
from typing import List
from ..schemas import ReviewResponseModel
from fastapi import Cookie
from ..schemas import UserResponseModel
from fastapi import APIRouter
from fastapi.security import HTTPBasicCredentials


router = APIRouter(prefix='/users')


@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).first():
        raise HTTPException(409, 'This username is already exists, You could try with other')

    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )

    return user

@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):

    user = User.select().where(User.username == credentials.username).first()

    if user is None:
        raise HTTPException(404, "User not found")
    
    if user.password != User.create_password(credentials.password):
        raise HTTPException(404, "Password error")

    response.set_cookie(key = 'user_id', value = user.id)

    return user

@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(None)):

    user = User.select().where(User.id == user_id).first()

    if user is None:
        raise HTTPException(404, "User not found")

    return [ user_reviews for user_reviews in user.reviews]



