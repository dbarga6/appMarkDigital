from flask import render_template, request,jsonify
from app.nlp import blueprint
from app.nlp.action.nlpAction import NLPAction
from app.nlp.action.analisisSentimientos import AnalisisSentimientos,AnalisisSentiemientosVader
from app.mongodb.action.mongoAction import TweetCollection
import pandas as pd
import json 
import os.path as path
import plotly
import plotly.graph_objects as go
import plotly.express as px




# ruta de inicio de nlp
@blueprint.route('/nlp')
def init_nlp():
    return "Esta es la página de NLP"

@blueprint.route("/mostrarTweets")
def route_mostrar_tweets():
    
    return render_template("mostrarTweets.html")

# Conexión con mongodb para mostrar la información almacenada de los tweets    
# método llamado desde jquery

@blueprint.route('/obtenerTweets')
def route_obtener_tweets():
    
    tweets = TweetCollection()
    df_resultados = tweets.obtener_tweets()
    df_show = df_resultados.head(50)
    fig = go.Figure(data=[go.Table(header=dict(values=['Tweet','nombre','Localización','fecha','favoritos','retweet'],
                fill_color='paleturquoise',align='left'),cells=dict(values=[df_show['Tweet'],
                df_show['nombre'],df_show['localizacion'],df_show['fecha'],df_show['favoritos'],
                df_show['retweet']],fill_color='lavender',align='left'))])
    tabla_tweets = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify(table_json=tabla_tweets)

@blueprint.route("/limpiezaTweet")
def route_limpiar_tweets():

    file_tweets = "app/nlp/static/docs/tweets_limpios.csv"
    if path.exists(file_tweets):
        df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])
        df_tweets = df_tweets.drop(df_tweets.columns[[0]], axis='columns')

    else:

        nlp = NLPAction("tweets_obtenidos.csv")
        df_tweets = nlp.proceso_nlp()

    df_show = df_tweets.head(50)
    fig = go.Figure(data=[go.Table(header=dict(values=['Tweet','Tweet_limpio','Longitud','Palabras'],
                fill_color='paleturquoise',align='left'),cells=dict(values=[df_show['Tweet'],
                df_show['Tweet_limpio'],df_show['Longitud'],df_show['Palabras']],fill_color='lavender',align='left'))])
    tabla_tweets_limpios = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("limpiezaTweet.html", table_limpios=tabla_tweets_limpios)

@blueprint.route("/tokenizarTweet")
def route_tokenizar_tweets():

    file_tweets = "app/nlp/static/docs/proceso_tokenizacion.csv"
    if path.exists(file_tweets):
        df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])
        df_tweets = df_tweets.drop(df_tweets.columns[[0]], axis='columns')

    else:

        nlp = NLPAction("tweets_limpios.csv")
        df_tweets = nlp.tokenizacion()

    df_show = df_tweets.head(50)
    fig = go.Figure(data=[go.Table(header=dict(values=['Tweet','Tokenizado'],
                fill_color='paleturquoise',align='left'),cells=dict(values=[df_show['Tweet'],
                df_show['Tokenizado']],fill_color='lavender',align='left'))])
    tabla_token = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("tokenizarTweet.html", table_token=tabla_token)


@blueprint.route("/analisisSentimientosTweet")
def route_analisis_sentiemientos_tweets():

    file_tweets = "app/nlp/static/docs/tweets_analisis_sentimientos.csv"
    if path.exists(file_tweets):
        df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])
        df_tweets = df_tweets.drop(df_tweets.columns[[0]], axis='columns')

    else:

        analisis = AnalisisSentimientos()
        df_tweets = analisis.polaridad()

    df_show = df_tweets.head(50)
    fig = go.Figure(data=[go.Table(header=dict(values=['Tweet','Polarity','Subjectivity','Polarity Scores'],
                fill_color='paleturquoise',align='left'),cells=dict(values=[df_show['Tweet'],
                df_show['Polarity'],df_show['Subjectivity'],df_show['Polarity Scores']],fill_color='lavender',align='left'))])
    table_analisis = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("analisisSentimientos.html", table_analisis=table_analisis)

@blueprint.route("/analisisSentimientosTweetVader")
def route_analisis_sentiemientos_vader():

    file_tweets = "app/nlp/static/docs/tweets_analisis_sentimientosVader.csv"
    if path.exists(file_tweets):
        df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])
        df_tweets = df_tweets.drop(df_tweets.columns[[0]], axis='columns')

    else:

        analisis = AnalisisSentiemientosVader()
        df_tweets = analisis.polaridad()

    df_show = df_tweets.head(50)
    fig = go.Figure(data=[go.Table(header=dict(values=['Tweet','AnalisisVader'],
                fill_color='paleturquoise',align='left'),cells=dict(values=[df_show['Tweet'],
                df_show['AnalisisVader']],fill_color='lavender',align='left'))])
    table_analisis = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("analisisSentimientosVader.html", table_analisis=table_analisis)

@blueprint.route("/topics")
def route_topics():
    return render_template("topicsTweet.html")

@blueprint.route("/wordCloud")
def route_wordCloud():
    return render_template("wordCloudTweet.html")