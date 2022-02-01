"""app.configuration
Module that keeps all environment stuff in a centralized
dictionary for other modules to use.
"""
import os
from distutils.util import strtobool


OPENAPI = {
    'export': strtobool(os.getenv('ENVIRONMENT_OPENAPI_EXPORT', 'false')),
    'filename': 'app/doc/openapi',
    'type_file': 'yaml' # yaml or json
}

DATABASE = {
    'driver': os.getenv('DB_DRIVER', 'postgresql+psycopg2'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'name': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'unix_socket': os.getenv('DB_UNIX_SOCKET')
}
