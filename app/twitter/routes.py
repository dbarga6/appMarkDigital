from flask import render_template, request
from app.twitter import blueprint



# ruta de inicio de twitter
@blueprint.route('/twitter')
def init_nlp():
    return "Esta es la página de Twitter"