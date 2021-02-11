from flask import render_template, request, jsonify
from app.twitter import blueprint
from app.twitter.forms.twitterForms import CargarTweetForm
from app.twitter.action.tweepyAction import TweepyAction



# ruta de inicio de twitter
@blueprint.route('/twitter')
def init_nlp():
    return "Esta es la página de Twitter"


@blueprint.route("/cargarTweets")
def mostrar_formulario_carga():
    form = CargarTweetForm
    return render_template("cargarTweet.html", form=form)

@blueprint.route("/cargarTweetsTweepy", methods=['GET', 'POST'])
def cargar_tweets_tweepy():
    print(">>>>>>>>> dentro")
    search = request.args.get('search')
    maximo = request.args.get('maximo')    
    fecha_hasta = request.args.get('fecha_hasta')
    

    msg = "Es obligatorio que introduzca un filtro de búsqueda y un número máximo de Tweets a cargar"
    print(">>>>>>>>> buscando")
    if search is not None and maximo is not None:
        tweepy = TweepyAction()
        tweepy.cargar_tweets(search,int(maximo),fecha_hasta)
        msg ="La Carga ha sido satisfactoria"    

    return jsonify(result=msg)
