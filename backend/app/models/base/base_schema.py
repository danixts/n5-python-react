from typing import List

from pydantic import BaseModel, Field

from app.models.auth.auth_schema import SignInResponse
from app.models.infraction.infraction_schema import InfractionResponse, InfractionReportResponse
from app.models.user.user_schema import UserResponse
from app.models.vehicle.vehicle_schema import VehicleResponse


class ApiResponseAuth(BaseModel):
    data: SignInResponse
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseUser(BaseModel):
    data: UserResponse
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseUsers(BaseModel):
    data: List[UserResponse]
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseVehicle(BaseModel):
    data: VehicleResponse
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseVehicles(BaseModel):
    data: List[VehicleResponse]
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseInfraction(BaseModel):
    data: InfractionResponse
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseInfractions(BaseModel):
    data: List[InfractionReportResponse]
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"


class ApiResponseInfractionReport(BaseModel):
    data: List[InfractionReportResponse]
    success: bool = True
    codError: str = "COD000"
    message: str = "OK"
