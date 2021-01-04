import pymongo
import os
import pandas as pd
import os.path as path
from datetime import datetime

"""
   MongodbAction.- Clase base que conecta con la base de datos de Mongodb y realiza las funciones de inserccion, busqueda

"""
class MongodbAction():
 
    def __init__(self):
        self.connection_url = os.environ.get('MONGO_URL')
        self.client = pymongo.MongoClient(self.connection_url)
        self.database = self.client.get_database(os.environ.get('MONGO_DB'))
       

    """
       insertOne.- Función que inserta un tweet en formato json en una colección 
       Parametros de entrada
          collection.- nombre de la colección
          tweet.- Tweet a insertar en formato json 

    """
    def insertOne(self, collection, tweet):
        collection.insert_one(tweet)
    
    """
       findAll.- Función que recupera todos los tweets de una colección
       Parametros de entrada
          collection.- nombre de la colección

       Parámetros de salida:
          result .- Cursor con todos los tweets recuperados

          
    """
    def findAll(self, collection):
        result = list(collection.find({}, {'_id': 0, 'id_str':1, 'full_text': 1, 'user.screen_name': 1,
                                           'created_at': 1, 'user.location':1,'favorite_count':1,'retweet_count':1}))
        return result
    

    """
       countDocument.- Función que dada un nombre de colección nos retorna el número de documentos que contiene
       Parametros de entrada
          collection.- nombre de la colección

       Parámetros de salida:
          result .- Número de documentos que contiene la colección
    """         
         
    def countDocument(self,collection):
        result = collection.count()
        return result


class TweetCollection(MongodbAction):

    def getUserTabla(self):
        return self.database.UserCollection

    def getAparcamientoTabla(self):
        return self.database.AparcamientoCollection
    
    def getHistoricoTabla(self):
        return self.database.HistoricoTabla

    def convertir_str_fecha(self, fechaStr):

        return datetime.strptime(fechaStr, '%a %b %d %H:%M:%S %z %Y')
    
    def convertir_fecha_str(self, fecha):
        
        return  datetime.strftime(fecha, '%d/%m/%Y %H:%M:%S') 

    def obtener_tweets(self):
       
        file_tweets = "app/nlp/static/docs/tweets_obtenidos.csv"
        df_tweets = pd.DataFrame(columns=["id_str",
                                 "Tweet", "nombre","localizacion", "fecha","favoritos","retweet"])
        
        if path.exists(file_tweets):
           
             df_tweets = pd.read_csv(file_tweets, parse_dates =["fecha"])
             df_tweets = df_tweets.drop(df_tweets.columns[[0]], axis='columns')

        else:
            
             resultweet = self.findAll(self.getAparcamientoTabla())
             # recorremos la lista recibida y la almacenamos en el dataFrame
             for tweet in resultweet:
                  fecha = self.convertir_str_fecha(tweet["created_at"])
                                   
                  resultados = [tweet["id_str"], tweet["full_text"], tweet["user"]["screen_name"],
                            tweet["user"]["location"], self.convertir_fecha_str(fecha),
                            tweet["favorite_count"], tweet["retweet_count"]]

                  df_tweets.loc[len(df_tweets)] = resultados
                  df_tweets.to_csv(file_tweets)

        return df_tweets


      