"""Module to export openapi doc"""
import os.path
import json
import yaml

from fastapi.openapi import utils
from stackdriver_formatter import logging
from app import configuration


LOGGER = logging.getLogger(__name__)

def openapi_generate(app):
    """Function to export openapi doc"""
    try:
        with open('tempfile', 'w+') as temp_file:
            content = utils.get_openapi(
                title="Desafio API",
                version="1.0.0",
                description="Api schema",
                routes=app.routes,
            )

            if configuration.OPENAPI['type_file'] == 'json':
                temp_file.write(json.dumps(content, indent=2))
            elif configuration.OPENAPI['type_file'] == 'yaml':
                temp_file.write(yaml.dump(content))


    except Exception as ex: # pylint: disable=W0703
        LOGGER.exception(ex)
        return

    if os.path.isfile(configuration.OPENAPI['filename']):
        os.remove(configuration.OPENAPI['filename'])

    os.rename(
        'tempfile',
        f'{configuration.OPENAPI["filename"]}.{configuration.OPENAPI["type_file"]}'
    )
