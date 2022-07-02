from wsgiref.validate import validator
from pydantic import BaseModel
from pydantic import validator


class UserBaseModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):

        if len(username) < 3 or len(username) > 50:
            raise ValueError('Username must have between 3 and 50 characters')

        return username
