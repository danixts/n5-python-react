from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class VehicleResponse(BaseModel):
    id: int
    car_plate: str = Field(min_length=3, max_length=10)
    model: str
    color: str


class VehicleRequest(BaseModel):
    car_plate: str = Field(min_length=3, max_length=10)
    model: str
    color: str
