from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.config.container import Container
from .auth_schema import SignIn
from .auth_service import AuthService
from ..base.base_schema import ApiResponseAuth


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login", response_model=ApiResponseAuth)
@inject
async def login(
        body: SignIn, service: AuthService = Depends(Provide[Container.auth_service])
):
    return service.login(body)
