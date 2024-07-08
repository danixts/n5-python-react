from sqlmodel import Field, Relationship

from app.models.base.base_model import BaseModel
from app.models.user.user_entity import UserEntity


class PoliceEntity(BaseModel, table=True):
    __tablename__ = "police"
    name: str = Field(unique=True)
    code_officer: str = Field(unique=True)
    user_id: int = Field(foreign_key="user.id")

    class Config:
        from_attributes = True
