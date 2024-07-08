import datetime

from pydantic import BaseModel, Field


class InfractionRequest(BaseModel):
    comments: str
    state: bool
    timestamp: datetime.datetime
    vehicle_id: int
    police_id: int


class InfractionResponse(InfractionRequest): ...


class InfractionReportResponse(BaseModel):
    name: str
    car_plate: str
    model: str
    color: str
    comment: str
    date: str


class ReportModel:
    def __init__(self, name: str, car_plate: str, model: str, color: str, comment: str, date: str):
        self.name = name
        self.car_plate = car_plate
        self.model = model
        self.color = color
        self.comment = comment
        self.date = date

    def to_dict(self):
        return {
            'name': self.name,
            'car_plate': self.car_plate,
            'model': self.model,
            'color': self.color,
            'comment': self.comment,
            'date': self.date,
        }
