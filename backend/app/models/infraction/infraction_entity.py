from datetime import datetime
from sqlmodel import Field, Relationship

from app.models.base.base_model import BaseModel


class InfractionEntity(BaseModel, table=True):
    __tablename__ = "infraction"
    comments: str = Field()
    state: bool = Field(default=False)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    vehicle_id: int = Field(nullable=False)
    police_id: int = Field(nullable=False)

    class Config:
        from_attributes = True
