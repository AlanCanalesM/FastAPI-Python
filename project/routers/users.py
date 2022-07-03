from ..database import User
from fastapi import APIRouter, HTTPException
from ..schemas import UserRequestModel
from ..schemas import UserResponseModel
from fastapi import APIRouter


router = APIRouter(prefix = '/api/v1/users')


@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):

    if User.select().where(User.username == user.username).first():
        return HTTPException(409, 'This username is already exists, You could try with other')

    hash_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )

    return user