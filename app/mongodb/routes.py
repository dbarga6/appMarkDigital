from flask import render_template, request,jsonify
from app.mongodb import blueprint
from app.mongodb.action.mongoAction import TweetCollection
import json
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)


# ruta de inicio de mongodb
@blueprint.route('/mongodb')
def init_mongodb():
    return "Esta es la página de MongoDB - " + current_user.username


@blueprint.route('/contarDocumentos')
def route_count():
    mongo = TweetCollection()
    user = current_user.username
    tweetCollection = mongo.getCargaInicial(user)
    resultado = mongo.countDocument(tweetCollection)
    return jsonify(result=resultado)
   