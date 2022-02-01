# pylint: skip-file
from fastapi import FastAPI

from app.management import management_resource
from app.open_api_generate import openapi_generate


app = FastAPI()
app.include_router(management_resource.ROUTER)


openapi_generate(app)
