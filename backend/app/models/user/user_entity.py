from app.models.base.base_model import BaseModel
from sqlmodel import Field, Relationship
from typing import List


class UserEntity(BaseModel, table=True):
    __tablename__ = "user"
    email: str = Field(unique=True)
    password: str = Field()
    username: str = Field(unique=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    type: str = Field(default="user")  # user | policy
    vehicles: List["VehicleEntity"] = Relationship(back_populates="user")

    class Config:
        from_attributes = True
