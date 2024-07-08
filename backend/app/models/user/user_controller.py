from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.config.container import Container
from app.models.user.user_schema import UserModel, UserResponse, UserUpdate
from .user_service import UserService
from app.config.dependencies import get_current_super_user
from ..base.base_schema import ApiResponseUser, ApiResponseUsers

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("", response_model=ApiResponseUser)
@inject
async def create_user(
        user: UserModel, service: UserService = Depends(Provide[Container.user_service]),
        _=Depends(get_current_super_user)
):
    return service.create_user(user)


@router.get("/all", response_model=ApiResponseUsers)
@inject
async def get_all_users(service: UserService = Depends(Provide[Container.user_service]),
                                        _=Depends(get_current_super_user)
                                        ):
    return service.find_by_all()


@router.get("", response_model=ApiResponseUser)
@inject
async def get_user_by_email_or_username(
        username: str, service: UserService = Depends(Provide[Container.user_service]),
        _=Depends(get_current_super_user)
):
    return service.find_by_email_or_username(username)


@router.put("", response_model=ApiResponseUser)
@inject
async def update_user_by_id(
        id_user: int, body: UserUpdate, service: UserService = Depends(Provide[Container.user_service]),
        _=Depends(get_current_super_user)
):
    return service.update_user(id_user, body)


@router.delete("", response_model=ApiResponseUser)
@inject
async def delete_user_by_id(
        id_user: int, service: UserService = Depends(Provide[Container.user_service]),
        _=Depends(get_current_super_user)
):
    return service.delete_user(id_user)
