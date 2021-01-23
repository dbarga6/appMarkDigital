from flask import Flask, url_for
from importlib import import_module
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager =  LoginManager()

# Registro de Base de Datos
def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
  
"""
configure_database .- Función para la configuración de la base de datos.
Parametros de entrada - app
"""
def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

""" 
    register_blueprints.- Función que registra las rutas del blueprints
    Parametros de entrada 
     app
"""
def register_blueprints(app):
    for module_name in ('base', 'mongodb','nlp','twitter','login'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

"""
    create_app.-  Función principal para la creación de la app 
    
    Parametros de salida 
     app 
"""
def create_app(config_mode):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config_mode)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
