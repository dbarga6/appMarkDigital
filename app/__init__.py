from flask import Flask, url_for
from importlib import import_module
from os import path



""" 
    register_blueprints.- Función que registra las rutas del blueprints
    Parametros de entrada 
     app
"""
def register_blueprints(app):
    for module_name in ('base', 'mongodb','nlp','twitter'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

"""
    create_app.-  Función principal para la creación de la app 
    
    Parametros de salida 
     app 
"""
def create_app():
    app = Flask(__name__, static_folder='base/static')
    register_blueprints(app)
    return app
