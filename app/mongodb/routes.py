from flask import render_template, request,jsonify
from app.mongodb import blueprint
from app.mongodb.action.mongoAction import TweetCollection
import json



# ruta de inicio de mongodb
@blueprint.route('/mongodb')
def init_mongodb():
    return "Esta es la página de MongoDB"


@blueprint.route('/contarDocumentos')
def route_count():
    mongo = TweetCollection()
    tweetCollection = mongo.getAparcamientoTabla()
    resultado = mongo.countDocument(tweetCollection)
    return jsonify(result=resultado)
   