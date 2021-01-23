# Fichero principal para la ejecución de la aplicación.
from app import create_app,db
from os import environ
from config import config_dict
from sys import exit

get_config_mode = environ.get('DESA_CONFIG_MODE')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid DESA_CONFIG_MODE environment variable entry.')


app = create_app(config_mode)
