from flask import render_template, request
from app.base import blueprint



# ruta de inicio de twitter
@blueprint.route('/')
def init():
    return render_template("home.html")