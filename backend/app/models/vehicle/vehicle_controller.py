from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.config.container import Container

from app.models.vehicle.vehicle_service import VehicleService
from .vehicle_schema import VehicleRequest
from ..base.base_schema import ApiResponseVehicles, ApiResponseVehicle
from ...config.dependencies import get_current_active_user

router = APIRouter(
    prefix="/vehicle",
    tags=["vehicle"],
)


@router.post("", response_model=ApiResponseVehicle)
@inject
async def register_vehicle(
        body: VehicleRequest, service: VehicleService = Depends(Provide[Container.vehicle_service]),
        user_active=Depends(get_current_active_user)
):
    return service.register_vehicle(body, user_active.data.id)


@router.get("", response_model=ApiResponseVehicles)
@inject
async def get_all_vehicles(service: VehicleService = Depends(Provide[Container.vehicle_service]),
                           user_active=Depends(get_current_active_user)
                           ):
    return service.get_vehicles(user_active.data.id)
