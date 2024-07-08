from app.commons.exceptions import SuccessResponse, NotFoundError
from app.models.base.base_service import BaseService
from app.models.vehicle.vehicle_entity import VehicleEntity
from app.models.vehicle.vehicle_repository import VehicleRepository


class VehicleService(BaseService):
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository
        super().__init__(vehicle_repository)

    def register_vehicle(self, vehicle, user_id):
        _vehicle = self.vehicle_repository.get_car_plate(vehicle.car_plate)
        if not _vehicle:
            new_vehicle = VehicleEntity(user_id=user_id)
            new_vehicle.car_plate = vehicle.car_plate
            new_vehicle.model = vehicle.model
            new_vehicle.color = vehicle.color
            return SuccessResponse(self.vehicle_repository.create(new_vehicle))
        raise NotFoundError(detail="VEHICLE ERROR CREATE", cod_error="COD002")

    def get_vehicles(self, user_id):
        vehicles = self.vehicle_repository.get_vehicles_by_user_id(user_id)
        return SuccessResponse(vehicles)
