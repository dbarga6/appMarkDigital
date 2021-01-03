from flask import Flask, url_for
from importlib import import_module
from os import path





# Registro de rutas por blueprints
def register_blueprints(app):
    for module_name in ('base', 'mongodb','nlp','twitter'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

# funcion principal de creación de la app
def create_app(config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    register_blueprints(app)
    return app
