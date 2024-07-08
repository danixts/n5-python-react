from datetime import datetime

from pydantic import BaseModel
from app.models.user.user_schema import UserResponse


class SignIn(BaseModel):
    email: str
    password: str


class Payload(BaseModel):
    email: str
    username: str
    type: str
    super: bool


class SignInResponse(BaseModel):
    access_token: str
    expiration: datetime
    user_info: UserResponse

