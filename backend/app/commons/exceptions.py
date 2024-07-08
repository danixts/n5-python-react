from typing import Any, Dict, Optional

from fastapi import status
from app.commons.global_exception import HTTPException


class DuplicatedError(HTTPException):
    def __init__(
            self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)


class AuthError(HTTPException):
    def __init__(
            self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)


class NotFoundError(HTTPException):
    def __init__(
            self,
            detail: Any = None,
            headers: Optional[Dict[str, Any]] = None,
            cod_error: Any = "COD100",
    ) -> None:
        super().__init__(
            status.HTTP_404_NOT_FOUND, detail, headers, cod_error=cod_error
        )


class ValidationError(HTTPException):
    def __init__(
            self, detail: Any = None, headers: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(status.HTTP_422_UNPROCESSABLE_ENTITY, detail, headers)


class SuccessResponse:
    def __init__(self, data) -> None:
        self.codError = "COD000"
        self.success = True
        self.data = data
        self.message = "OK"
