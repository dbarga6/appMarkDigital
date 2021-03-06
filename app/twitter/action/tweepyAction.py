
import tweepy
import pandas as pd
import os
import os.path as path
from app.mongodb.action.mongoAction import TweetCollection
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)


"""
   Clase que se encarga de conectar con API de Twitter a través de la libreria Tweepy

"""
class TweepyAction():
    def __init__(self):
        self.api = self.get_api()

    # función principal para la conexión con la API de Twitter
    def get_api(self):
        # Variables que contienen las credenciales para el acceso a la API de Twitter
        self.access_token = os.environ.get('ACCESS_TOKEN')
        self.access_secret = os.environ.get('ACCESS_SECRET')
        self.consumer_key = os.environ.get('CONSUMER_KEY')
        self.consumer_secret = os.environ.get('CONSUMER_SECRET')
       
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api

    """
     cargar_tweets: función que conectará con Twitter y realizará un búsqueda con un filtro recibido por parametros
                    y un número máximo de Tweets a cargar. 
                    Estos los cargara en la colección oportuna y obtendrá sus usuarios cargandolos en otra colección.

    """
    def cargar_tweets(self, filtro, maximo,fecha_hasta):
      
        mongo = TweetCollection()
        user = current_user.username
        print(">>>>>>>> usuario",user)
        tweetCollection = mongo.getCargaInicial(user)
        #tweetCollection = mongo.getAparcamientoTabla()
        userCollection = mongo.getUserTabla()
        print(">>>>>>>> estoy dentro")

        try:
            for tweet in tweepy.Cursor(self.api.search,
                                    q=filtro + ' -filter:retweets',
                                    lang='es',
                                    tweet_mode="extended",
                                    until=fecha_hasta
                                    ).items(maximo):
                                    
                mongo.insertOne(tweetCollection, tweet._json)
                mongo.insertOne(userCollection, tweet._json['user'])

        except tweepy.TweepError as e:  
                print(e.reason)
                
               
        except StopIteration: #stop iteration when last tweet is reached
                print("StopIteration")

   
