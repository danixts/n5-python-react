from pydantic import BaseModel, Field
from typing import Optional


class UserBase(BaseModel):
    id: Optional[int] = None
    username: str
    password: str
    email: str
    is_superuser: bool
    type: str


class UserUpdate(BaseModel):
    password: str
    email: str


class UserResponse(UserBase):
    is_superuser: bool
    is_active: bool
    type: str
    password: str = Field(..., exclude=True)


class UserModel(UserBase):
    name: Optional[str] = None
    code_officer: Optional[int] = None

    class Config:
        from_attributes = True
