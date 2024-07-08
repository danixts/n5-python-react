from fastapi import HTTPException as StarletteHTTPException
from typing import Any, Dict


class HTTPException(StarletteHTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Dict[str, str] | None = None,
        cod_error: Dict[str, Any] | None = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        self.cod_error = cod_error

    def __str__(self) -> str:
        return f"{self.status_code}: {self.detail} - Extra: {self.cod_error}"

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r}, cod_error={self.cod_error!r})"