from fastapi import APIRouter

from .user.user_controller import router as user_router
from .auth.auth_controller import router as auth_router
from .vehicle.vehicle_controller import router as vehicle_router
from .infraction.infraction_controller import router as infraction_router

routers = APIRouter()
router_list = [auth_router, user_router, vehicle_router, infraction_router]

for router in router_list:
    routers.include_router(router)
