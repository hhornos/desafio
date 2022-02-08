# pylint:disable=unused-argument
"""app.main
Module with a init method that gives our configured FastAPI application.
"""
from http import HTTPStatus
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from stackdriver_formatter import logging
from app.open_api_generate import openapi_generate
from app.insight import main as insight_main
from app import configuration
from app import exceptions as app_exceptions


LOGGER = logging.getLogger(__name__)

APP = FastAPI()

origins = ['*']


@APP.exception_handler(Exception)
async def http_exception_handler(request, exc):
    """Handler to normalize exception error responses"""
    LOGGER.info('Internal server error')
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={'detail': [{'msg': "Internal server error"}]}
    )


@APP.exception_handler(app_exceptions.NotFound)
async def not_fount_exception_handler(request, exc):
    """Handler to normalize exception error responses"""
    LOGGER.info('Entity not found')
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={'detail': [{'msg': "Entity not found"}]}
    )


@APP.exception_handler(app_exceptions.AlreadyExists)
async def not_fount_exception_handler(request, exc):
    """Handler to normalize exception error responses"""
    LOGGER.info('Entity not found')
    return JSONResponse(
        status_code=HTTPStatus.CONFLICT,
        content={'detail': [{'msg': "Entity already exists"}]}
    )

@APP.exception_handler(RequestValidationError)
def request_validation_exception_handler(request, exc: RequestValidationError):
    """Handler to normalize validation error responses"""
    LOGGER.info('UNPROCESSABLE ENTITY')

    errors = exc.errors()
    normalized_errors = []

    for error in errors:
        msg = {"msg": f"{error['loc'][-1]}: {error['msg']}"}
        normalized_errors.append(msg)

    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={'detail': normalized_errors}
    )


@APP.exception_handler(app_exceptions.ListEntityNotFound)
def request_validation_exception_handler(request, exc: app_exceptions.ListEntityNotFound):
    """Handler to normalize validation error responses"""
    LOGGER.info('UNPROCESSABLE ENTITY')

    errors = exc.errors()
    normalized_errors = []

    for error in errors:
        msg = {"msg": f"{error['loc'][-1]}: {error['msg']}"}
        normalized_errors.append(msg)

    return JSONResponse(
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
        content={'detail': normalized_errors}
    )

def build_api():
    """ ADD CORS SETTINGS """
    APP.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    """Build API routers."""
    APP.include_router(insight_main.ROUTER)

    if configuration.OPENAPI['export']:
        openapi_generate(APP)

    return APP
