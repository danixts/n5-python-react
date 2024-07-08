from dependency_injector.wiring import Provide, inject
from fastapi import Depends
import jwt
from pydantic import ValidationError
from app.config.config import Configs
from app.config.container import Container
from app.commons.exceptions import AuthError
from app.commons.security import ALGORITHM, JWTBearer
from app.models.auth.auth_schema import Payload
from app.models.user.user_service import UserService


@inject
def get_current_user(
        token: str = Depends(JWTBearer()),
        service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        payload = jwt.decode(token, Configs.SECRET_KEY, algorithms=ALGORITHM)
        token_data = Payload(**payload)
    except (jwt.PyJWKError, ValidationError):
        raise AuthError(detail="Could not validate credentials")
    current_user = service.find_by_email_or_username(token_data.username)
    if not current_user:
        raise AuthError(detail="User not found")
    return current_user


def get_current_active_user(
        current_user=Depends(get_current_user),
):
    if not current_user.data.is_active:
        raise AuthError("Inactive user")
    return current_user


def get_current_super_user(
        current_user=Depends(get_current_user),
):
    if not current_user.data.is_active:
        raise AuthError("Inactive user")
    if current_user.data.is_superuser:
        return current_user
    raise AuthError("Not service active user normal")


def get_current_user_with_no_exception(
        token: str = Depends(JWTBearer()),
        service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        payload = jwt.decode(token, Configs.SECRET_KEY, algorithms=ALGORITHM)
        token_data = Payload(**payload)
    except (jwt.PyJWKError, ValidationError):
        return False
    current_user = service.find_by_email_or_username(token_data.username)
    if not current_user:
        return None
    return current_user
