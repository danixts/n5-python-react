from fastapi import FastAPI, Request, responses
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import Configs
from app.models.router import routers
from app.config.container import Container
from app.commons.global_exception import HTTPException

api = FastAPI()


@api.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return responses.JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "data": False,
            "codeError": exc.cod_error,
        },
        headers=exc.headers,
    )


@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    custom_errors = []
    for error in errors:
        field = error.get("loc")[-1]
        message = error.get("msg")
        custom_errors.append({"field": field, "error": message})
    return responses.JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": custom_errors,
            "data": False,
            "codeError": "COD422",
        },
    )


@api.exception_handler(403)
async def unauthorized_exception_handler(request, exc):
    return responses.JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "data": False,
            "codeError": "COD403",
            "message": "Not authenticated"
        },
    )


origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(routers, prefix=Configs.API_V1_STR)

container = Container()
db = container.db()
db.create_database()
