from msilib.schema import Class
from wsgiref.validate import validator
from pydantic import BaseModel
from pydantic import validator
from typing import Any
from pydantic.utils import GetterDict
from peewee import ModelSelect


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):

        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)

        return res


class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):

        if len(username) < 3 or len(username) > 50:
            raise ValueError('Username must have between 3 and 50 characters')

        return username


class UserResponseModel(ResponseModel):
    id: int
    username: str


class ReviewRequestModel(BaseModel):
    user_id: int
    movie_id: int
    review: str
    score: int

    @validator('score')
    def score_validator(cls, score):

        if score < 1 or score > 5:

            raise ValueError('Score must be a value between 1 and 5')

        return score




class ReviewResponseModel(ResponseModel):
    id: int
    movie_id: int
    review: str
    score: int
