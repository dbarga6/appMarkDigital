from flask import render_template, request
from app.mongodb import blueprint



# ruta de inicio de mongodb
@blueprint.route('/mongodb')
def init_mongodb():
    return "Esta es la página de MongoDB"