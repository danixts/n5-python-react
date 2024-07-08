from datetime import datetime

from sqlmodel import Column, DateTime, Field, SQLModel, func


class BaseModel(SQLModel):
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default=func.now())
    updated_at: datetime = Field(default=func.now())
