import pymongo
import os

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