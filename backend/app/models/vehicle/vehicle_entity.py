from typing import List

from app.models.base.base_model import BaseModel
from app.models.infraction.infraction_entity import InfractionEntity
from app.models.user.user_entity import UserEntity

from sqlmodel import Field, Relationship


class VehicleEntity(BaseModel, table=True):
    __tablename__ = "vehicle"
    car_plate: str = Field(unique=True, index=True)
    model: str = Field()
    color: str = Field()
    user_id: int = Field(foreign_key="user.id")
    is_active: bool = Field(default=True)
    user: UserEntity = Relationship(back_populates="vehicles")
    # infractions: List["InfractionEntity"] = Relationship(back_populates="infraction")
