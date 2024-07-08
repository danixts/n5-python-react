from contextlib import AbstractContextManager
from typing import Callable
from app.models.base.base_repository import BaseRepository
from sqlalchemy.orm import Session

from app.models.user.user_entity import UserEntity
from app.models.vehicle.vehicle_entity import VehicleEntity


class VehicleRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, VehicleEntity)

    def get_car_plate(self, car_plate: str):
        with self.session_factory() as session:
            query = session.query(self.model).filter(self.model.car_plate == car_plate).first()
        return query

    def get_vehicles_by_user_id(self, user_id: int):
        with self.session_factory() as session:
            print("filter by id remove ", user_id)
            query = session.query(self.model)
        return query
