from datetime import timedelta

from app.config.config import Configs
from app.commons.exceptions import AuthError, SuccessResponse
from app.commons.security import create_access_token, get_password_hash, verify_password
from app.models.user.user_repository import UserRepository
from .auth_schema import Payload, SignIn
from app.models.base.base_service import BaseService


class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        super().__init__(user_repository)

    def login(self, body: SignIn):
        find_user = self.user_repository.get_user_by_user(body.email)
        if not find_user:
            raise AuthError(detail="USER NOT FOUND")

        if not verify_password(body.password, find_user.password):
            raise AuthError(detail="USER ERROR PASSWORD")

        payload = Payload(
            email=find_user.email,
            username=find_user.username,
            type=find_user.type,
            super=find_user.is_superuser
        )
        token_lifespan = timedelta(minutes=Configs.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token, expiration_datetime = create_access_token(payload.model_dump(), token_lifespan)
        sign_in_result = {
            "access_token": access_token,
            "expiration": expiration_datetime,
            "user_info": find_user,
        }
        return SuccessResponse(sign_in_result)
