from flask import render_template, request
from app.nlp import blueprint



# ruta de inicio de nlp
@blueprint.route('/nlp')
def init_nlp():
    return "Esta es la página de NLP"