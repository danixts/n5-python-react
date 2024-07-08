from datetime import datetime, timezone, timedelta
from typing import Tuple

from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
import jwt
from app.config.config import Configs
from app.commons.exceptions import AuthError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

current_utc = datetime.now(timezone.utc)

ALGORITHM = "HS512"


def create_access_token(
        subject: dict, expires_delta: timedelta = None
) -> Tuple[str, str]:
    if expires_delta:
        expire = current_utc + expires_delta
    else:
        expire = current_utc + timedelta(minutes=Configs.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"exp": expire, **subject}
    encoded_jwt = jwt.encode(payload, Configs.SECRET_KEY, algorithm=ALGORITHM)
    expiration_datetime = expire.strftime(Configs.DATETIME_FORMAT)
    return encoded_jwt, expiration_datetime


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, Configs.SECRET_KEY, algorithms=ALGORITHM)
        return (
            decoded_token
            if decoded_token["exp"] >= int(round(current_utc.timestamp()))
            else None
        )
    except Exception as e:
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        res = {"message": "Invalid authorization code"}
        if credentials:
            if not credentials.scheme == "Bearer":
                raise AuthError(detail="Invalid authentication user")
            if not self.verify_jwt(credentials.credentials):
                raise AuthError(detail="Invalid token or expired token")
            return credentials.credentials
        else:
            raise AuthError(detail=res)

    def verify_jwt(self, jwt_token: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = decode_jwt(jwt_token)
        except Exception as e:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid
