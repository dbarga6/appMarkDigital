from flask import render_template, request,jsonify
from app.nlp import blueprint
from app.mongodb.action.mongoAction import TweetCollection
import json
import plotly
import plotly.graph_objects as go
import plotly.express as px




# ruta de inicio de nlp
@blueprint.route('/nlp')
def init_nlp():
    return "Esta es la página de NLP"

@blueprint.route("/limpieza")
def route_limpieza():
    tabla_tweets = ""
    return render_template("limpiezaTweet.html",table_json=tabla_tweets)

# Conexión con mongodb para mostrar la información almacenada de los tweets    
# método llamado desde jquery

@blueprint.route('/obtenerTweets')
def route_obtener_tweets():
    
    tweets = TweetCollection()
    df_resultados = tweets.obtener_tweets()
    df_show = df_resultados.head(10)
    fig = go.Figure(data=[go.Table(header=dict(values=['Tweet','nombre','Localización','fecha','favoritos','retweet'],
                fill_color='paleturquoise',align='left'),cells=dict(values=[df_show['Tweet'],
                df_show['nombre'],df_show['localizacion'],df_show['fecha'],df_show['favoritos'],
                df_show['retweet']],fill_color='lavender',align='left'))])
    tabla_tweets = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify(table_json=tabla_tweets)